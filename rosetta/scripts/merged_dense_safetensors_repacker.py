#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path
import argparse, json, math
import numpy as np
import torch
from safetensors import safe_open
from safetensors.torch import save_file


def quant_scheme(name:str, dtype:torch.dtype, keyset:set[str]):
    if name.endswith('.weight') and str(dtype).endswith('uint32') and name[:-7]+'.scales' in keyset and name[:-7]+'.biases' in keyset:
        return 'qwen_u32_affine4'
    if name.endswith('.qweight') and str(dtype).endswith('int32') and name[:-8]+'.qzeros' in keyset and name[:-8]+'.scales' in keyset:
        return 'awq_i32_affine4'
    return None


def unpack_u32_to_u4(arr: np.ndarray) -> np.ndarray:
    arr = arr.astype(np.uint32, copy=False)
    shifts = np.arange(8, dtype=np.uint32) * np.uint32(4)
    out = ((arr[..., None] >> shifts) & np.uint32(0xF)).astype(np.float16)
    new_shape = arr.shape[:-1] + (arr.shape[-1] * 8,)
    return out.reshape(new_shape)


def unpack_i32_to_u4(arr: np.ndarray) -> np.ndarray:
    return unpack_u32_to_u4(arr.view(np.uint32))


def decode_qwen_weight(weight_u32: torch.Tensor, scales: torch.Tensor, biases: torch.Tensor) -> np.ndarray:
    w = weight_u32.cpu().numpy()
    s = scales.cpu().numpy().astype(np.float16, copy=False)
    b = biases.cpu().numpy().astype(np.float16, copy=False)
    unpacked = unpack_u32_to_u4(w)
    groups = s.shape[-1]
    group_size = unpacked.shape[-1] // groups
    if group_size * groups != unpacked.shape[-1]:
        raise ValueError(f'Qwen group mismatch: unpacked={unpacked.shape}, scales={s.shape}')
    out = np.empty_like(unpacked, dtype=np.float16)
    for g in range(groups):
        lo = g * group_size
        hi = lo + group_size
        out[..., lo:hi] = unpacked[..., lo:hi] * s[..., g:g+1] + b[..., g:g+1]
    return out


def decode_awq_qweight(qweight: torch.Tensor, qzeros: torch.Tensor, scales: torch.Tensor) -> np.ndarray:
    qw = qweight.cpu().numpy()
    qz = qzeros.cpu().numpy()
    sc = scales.cpu().numpy().astype(np.float16, copy=False)
    unpacked_w = unpack_i32_to_u4(qw)
    unpacked_z = unpack_i32_to_u4(qz)
    in_features, out_features = unpacked_w.shape
    groups = unpacked_z.shape[0]
    if sc.shape != (groups, out_features):
        raise ValueError(f'AWQ scales shape mismatch: scales={sc.shape}, expected={(groups, out_features)}')
    group_size = math.ceil(in_features / groups)
    out = np.empty((in_features, out_features), dtype=np.float16)
    for g in range(groups):
        lo = g * group_size
        hi = min((g + 1) * group_size, in_features)
        if lo >= hi:
            break
        out[lo:hi, :] = (unpacked_w[lo:hi, :] - unpacked_z[g:g+1, :]) * sc[g:g+1, :]
    return out


def repack(input_path: Path, out_path: Path, metadata_extra: dict[str,str]|None=None):
    tensors = {}
    manifest = {
        'source_file': str(input_path),
        'output_file': str(out_path),
        'decoded_quantized_tensors': 0,
        'passthrough_tensors': 0,
        'dropped_auxiliary_quant_tensors': 0,
        'quant_schemes': {},
        'tensor_count_out': 0,
    }
    scheme_counts = {}
    with safe_open(str(input_path), framework='pt', device='cpu') as f:
        keys = list(f.keys())
        keyset = set(keys)
        skip = set()
        for k in keys:
            if k in skip:
                continue
            t = f.get_tensor(k)
            scheme = quant_scheme(k, t.dtype, keyset)
            if scheme == 'qwen_u32_affine4':
                base = k[:-7]
                scales_k = base + '.scales'
                biases_k = base + '.biases'
                dense = decode_qwen_weight(t, f.get_tensor(scales_k), f.get_tensor(biases_k))
                tensors[k] = torch.from_numpy(dense)
                skip.update({scales_k, biases_k})
                manifest['decoded_quantized_tensors'] += 1
                manifest['dropped_auxiliary_quant_tensors'] += 2
                scheme_counts[scheme] = scheme_counts.get(scheme, 0) + 1
            elif scheme == 'awq_i32_affine4':
                base = k[:-8]
                qzeros_k = base + '.qzeros'
                scales_k = base + '.scales'
                dense = decode_awq_qweight(t, f.get_tensor(qzeros_k), f.get_tensor(scales_k))
                out_name = base + '.weight'
                tensors[out_name] = torch.from_numpy(dense)
                skip.update({qzeros_k, scales_k})
                manifest['decoded_quantized_tensors'] += 1
                manifest['dropped_auxiliary_quant_tensors'] += 2
                scheme_counts[scheme] = scheme_counts.get(scheme, 0) + 1
            else:
                # skip standalone aux tensors for quantized weights if their base was handled already
                if (k.endswith('.scales') or k.endswith('.biases') or k.endswith('.qzeros')):
                    base = k.rsplit('.',1)[0]
                    # keep non-quant aux only if not paired with quant family
                    if (base + '.weight' in keyset) or (base + '.qweight' in keyset):
                        if ((base + '.weight' in keyset and quant_scheme(base + '.weight', f.get_tensor(base + '.weight').dtype, keyset)) or
                            (base + '.qweight' in keyset and quant_scheme(base + '.qweight', f.get_tensor(base + '.qweight').dtype, keyset))):
                            manifest['dropped_auxiliary_quant_tensors'] += 1
                            continue
                tensors[k] = t
                manifest['passthrough_tensors'] += 1
    manifest['quant_schemes'] = scheme_counts
    manifest['tensor_count_out'] = len(tensors)
    metadata = {'source_file': str(input_path), 'repacked_by': 'merged_dense_safetensors_repacker'}
    if metadata_extra:
        metadata.update(metadata_extra)
    save_file(tensors, str(out_path), metadata=metadata)
    sidecar = out_path.with_suffix(out_path.suffix + '.manifest.json')
    sidecar.write_text(json.dumps(manifest, indent=2))
    return manifest, sidecar


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('input', type=Path)
    ap.add_argument('output', type=Path)
    args = ap.parse_args()
    repack(args.input, args.output)

if __name__ == '__main__':
    main()

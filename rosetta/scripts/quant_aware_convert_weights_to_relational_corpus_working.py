#!/usr/bin/env python3
from __future__ import annotations

import argparse, collections, datetime as dt, hashlib, json, re
from pathlib import Path
from typing import Iterable

import numpy as np
from safetensors import safe_open

LAYER_RE = re.compile(r"(?:layers?|blocks?)\.(\d+)")
ROLE_PATTERNS = [
    ("attention_qkv", [".q_proj", ".k_proj", ".v_proj", "self_attn.q", "self_attn.k", "self_attn.v"]),
    ("attention_out", [".o_proj", "self_attn.o", "attn.out"]),
    ("mlp_gate", [".gate_proj", ".gate"]),
    ("mlp_up", [".up_proj", ".fc1", ".w1"]),
    ("mlp_down", [".down_proj", ".fc2", ".w2"]),
    ("norm", [".norm", "layernorm", "ln_"]),
    ("embedding", ["embed", "embedding", "tok_embeddings"]),
    ("vision_encoder", ["vision", "visual", "patch_embed"]),
    ("audio_encoder", ["audio", "whisper"]),
]
FAMILY_PATTERNS = [
    ("attention", ["attn", "attention", "q_proj", "k_proj", "v_proj", "o_proj"]),
    ("mlp", ["mlp", "gate_proj", "up_proj", "down_proj", "fc1", "fc2"]),
    ("normalization", ["norm", "layernorm", "ln_"]),
    ("embedding", ["embed", "embedding"]),
    ("multimodal", ["vision", "visual", "audio", "whisper"]),
]
VALUES_PER_U32 = 8
QUANT_BITS = 4

def classify(name, patterns, default):
    lname = name.lower()
    for label, needles in patterns:
        if any(n in lname for n in needles):
            return label
    return default

def parse_layer_index(name):
    m = LAYER_RE.search(name)
    return int(m.group(1)) if m else None

def byte_width(dtype):
    dl = dtype.lower()
    if any(x in dl for x in ["u32", "i32", "f32"]): return 4
    if any(x in dl for x in ["f16", "bf16", "u16", "i16"]): return 2
    return 1

def iter_safetensors(paths: Iterable[Path]):
    for p in paths:
        if p.is_file() and p.suffix == ".safetensors":
            yield p
        elif p.is_dir():
            yield from p.rglob("*.safetensors")

def derive_companions(name):
    base = name[:-len(".weight")]
    return base + ".scales", base + ".biases"

def infer_quant(reader, name, storage_shape, dtype):
    if len(storage_shape) != 2 or dtype.upper() != "U32" or not name.endswith(".weight"):
        return {"kind": "none"}
    sname, bname = derive_companions(name)
    keys = set(reader.keys())
    if sname not in keys or bname not in keys:
        return {"kind": "none", "reason": "missing_companions"}
    sshape = list(reader.get_slice(sname).get_shape())
    bshape = list(reader.get_slice(bname).get_shape())
    if sshape != bshape or len(sshape) != 2:
        return {"kind": "none", "reason": "invalid_companion_shapes", "scale_shape": sshape, "bias_shape": bshape}
    rows, packed_cols = map(int, storage_shape)
    srows, groups = map(int, sshape)
    if srows != rows:
        return {"kind": "none", "reason": "row_mismatch", "scale_shape": sshape}
    logical_cols = packed_cols * VALUES_PER_U32
    if groups <= 0 or logical_cols % groups != 0:
        return {"kind": "none", "reason": "non_integral_grouping", "logical_cols": logical_cols, "groups": groups}
    return {
        "kind": "affine_nibble_u32",
        "packed_dtype": dtype,
        "packed_shape": [rows, packed_cols],
        "logical_shape": [rows, logical_cols],
        "group_size": logical_cols // groups,
        "values_per_u32": VALUES_PER_U32,
        "scale_tensor": sname,
        "bias_tensor": bname,
        "scale_shape": sshape,
        "bias_shape": bshape,
        "decode_formula": "decoded = unpack4(weight_u32_nibbles) * scale + bias",
        "confidence": 0.96,
    }

def dense_stats(reader, name, sample_max=16384):
    arr = np.asarray(reader.get_tensor(name)).reshape(-1)
    if arr.size > sample_max:
        idx = np.linspace(0, arr.size - 1, num=sample_max, dtype=np.int64)
        arr = arr[idx]
    arr = arr.astype(np.float64, copy=False)
    return {
        "sample_count": int(arr.size),
        "mean": float(np.mean(arr)),
        "std": float(np.std(arr)),
        "min": float(np.min(arr)),
        "max": float(np.max(arr)),
        "l2_norm": float(np.linalg.norm(arr)),
        "approx_zero_fraction": float(np.mean(np.isclose(arr, 0.0, atol=1e-8))),
    }

def quant_stats(reader, name, qinfo, sample_max=16384):
    weights = np.asarray(reader.get_tensor(name), dtype=np.uint32)
    scales = np.asarray(reader.get_tensor(qinfo["scale_tensor"]), dtype=np.float32)
    biases = np.asarray(reader.get_tensor(qinfo["bias_tensor"]), dtype=np.float32)
    rows, logical_cols = qinfo["logical_shape"]
    group_size = int(qinfo["group_size"])
    total = rows * logical_cols
    sample_n = min(sample_max, total)
    flat = np.linspace(0, total - 1, num=sample_n, dtype=np.int64)
    r = flat // logical_cols
    c = flat % logical_cols
    pc = c // VALUES_PER_U32
    nib = c % VALUES_PER_U32
    g = c // group_size
    packed = weights[r, pc]
    q = ((packed >> (nib * QUANT_BITS)) & 0xF).astype(np.float32)
    s = scales[r, g]
    b = biases[r, g]
    decoded = q * s + b
    return {
        "quant_aware": True,
        "sample_count": int(sample_n),
        "quant_min": float(np.min(q)),
        "quant_max": float(np.max(q)),
        "quant_mean": float(np.mean(q)),
        "decoded_mean": float(np.mean(decoded)),
        "decoded_std": float(np.std(decoded)),
        "decoded_min": float(np.min(decoded)),
        "decoded_max": float(np.max(decoded)),
        "decoded_l2_norm": float(np.linalg.norm(decoded)),
        "decoded_approx_zero_fraction": float(np.mean(np.isclose(decoded, 0.0, atol=1e-8))),
        "scale_mean": float(np.mean(s)),
        "scale_std": float(np.std(s)),
        "bias_mean": float(np.mean(b)),
        "bias_std": float(np.std(b)),
    }

def build_record(reader, source_file: Path, name, sample_max=16384):
    storage_shape = list(reader.get_slice(name).get_shape())
    dtype = str(reader.get_slice(name).get_dtype())
    numel = 1
    for d in storage_shape: numel *= int(d)
    qinfo = infer_quant(reader, name, storage_shape, dtype)
    if qinfo.get("kind") == "affine_nibble_u32":
        logical_shape = list(qinfo["logical_shape"])
        logical_numel = int(np.prod(logical_shape))
        logical_dtype = "F32(decoded_sampled)"
        stats = quant_stats(reader, name, qinfo, sample_max)
        provenance = [
            "quantization detected heuristically from packed weight + scales + biases naming pattern",
            "decoded statistics are sample-based approximate dequant values, not full dense materialization",
            "intermediate relational corpus, not a semantic proof layer",
        ]
    else:
        logical_shape = storage_shape
        logical_numel = numel
        logical_dtype = dtype
        stats = dense_stats(reader, name, sample_max)
        provenance = [
            "role_guess is heuristic only",
            "family_guess is heuristic only",
            "intermediate relational corpus, not a semantic proof layer",
        ]
    return {
        "source_file": str(source_file),
        "tensor_name": name,
        "shape": storage_shape,
        "logical_shape": logical_shape,
        "dtype": dtype,
        "logical_dtype": logical_dtype,
        "numel": numel,
        "logical_numel": logical_numel,
        "size_bytes": numel * byte_width(dtype),
        "layer_index": parse_layer_index(name),
        "role_guess": classify(name, ROLE_PATTERNS, "unknown"),
        "family_guess": classify(name, FAMILY_PATTERNS, "unknown"),
        "name_hash": hashlib.sha256(name.encode("utf-8")).hexdigest(),
        "quantization": qinfo,
        "sample_stats": stats,
        "provenance_notes": provenance,
    }

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("inputs", nargs="+")
    ap.add_argument("--out", required=True)
    ap.add_argument("--sample-max-elements", type=int, default=16384)
    args = ap.parse_args()
    inputs = [Path(x).expanduser().resolve() for x in args.inputs]
    out = Path(args.out).expanduser().resolve()
    out.mkdir(parents=True, exist_ok=True)
    files = list(iter_safetensors(inputs))
    if not files:
        raise SystemExit("No .safetensors files found")
    recs = []
    for sf in files:
        with safe_open(str(sf), framework="np") as reader:
            for name in reader.keys():
                recs.append(build_record(reader, sf, name, args.sample_max_elements))
    with (out / "tensors.jsonl").open("w", encoding="utf-8") as f:
        for r in recs:
            f.write(json.dumps(r) + "\n")
    role_hist = collections.Counter(r["role_guess"] for r in recs)
    family_hist = collections.Counter(r["family_guess"] for r in recs)
    dtype_hist = collections.Counter(r["dtype"] for r in recs)
    logical_dtype_hist = collections.Counter(r["logical_dtype"] for r in recs)
    layer_hist = collections.Counter("none" if r["layer_index"] is None else str(r["layer_index"]) for r in recs)
    quant_hist = collections.Counter(r["quantization"].get("kind", "none") for r in recs)
    (out / "families.json").write_text(json.dumps({
        "by_role": dict(role_hist),
        "by_family": dict(family_hist),
        "by_dtype": dict(dtype_hist),
        "by_logical_dtype": dict(logical_dtype_hist),
        "by_layer": dict(layer_hist),
        "by_quantization": dict(quant_hist),
    }, indent=2), encoding="utf-8")
    quantized = [r for r in recs if r["quantization"].get("kind") != "none"]
    (out / "stats.json").write_text(json.dumps({
        "tensor_count": len(recs),
        "quantized_tensor_count": len(quantized),
        "total_size_bytes_est": sum(r["size_bytes"] for r in recs),
        "total_logical_numel_est": sum(r["logical_numel"] for r in recs),
        "timestamp_utc": dt.datetime.now(dt.UTC).isoformat(),
    }, indent=2), encoding="utf-8")
    (out / "manifest.json").write_text(json.dumps({
        "source_files": [str(p) for p in files],
        "notes": [
            "Quant-aware extension over packaged relational converter.",
            "Heuristic classifications are provisional.",
            "Quant-aware decode currently supports affine nibble-packed U32 weights with matching scales and biases.",
            "Decoded statistics are sampled approximate values, not full dense reconstruction."
        ]
    }, indent=2), encoding="utf-8")
    print(str(out))

if __name__ == "__main__":
    main()

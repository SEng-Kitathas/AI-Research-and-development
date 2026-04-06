# Full Dequant Overlay Export Report

Status: completed for both uploaded raw safetensors files.

## Outputs

### Qwen
- overlay dir: `/mnt/data/qwen_full_dequant_overlay`
- decoded tensors: 169
- passthrough tensors: 459
- on-disk size: ~943 MiB
- quant law: `qwen_u32_affine4`
- inferred group size: 64

### H2O
- overlay dir: `/mnt/data/h2o_full_dequant_overlay`
- decoded tensors: 112
- passthrough tensors: 259
- on-disk size: ~793 MiB
- quant law: `awq_i32_affine4`
- inferred group size: 128

## What was exported
This pass exported **fully decoded float16 overlay tensors** for every quantized tensor:
- Qwen: every `*.weight` tensor that had paired `*.scales` and `*.biases`
- H2O: every `*.qweight` tensor that had paired `*.qzeros` and `*.scales`

Non-quantized tensors were left as passthrough references in the overlay manifest instead of being redundantly recopied.

## Practical meaning
These overlays are the first point where the Rosetta lane stops being only:
- provenance
- family topology
- sampled quant-aware stats

and becomes a real **full decoded tensor export** for the quantized portions of both models.

## Limits
- Output is an overlay directory of `.npy` tensors plus manifest, not a single merged safetensors model.
- H2O AWQ path uses the standard unpack/dezero/scale affine decode assumption already inferred from the file layout.
- This proves full decode/export; it does not yet prove downstream model-quality equivalence against a reference runtime.

## Next best move
Build a **merged dense overlay packer** that:
1. copies/passes through native fp16 tensors
2. inserts the decoded overlay tensors
3. emits a single dense `.safetensors` shard set or merged archive

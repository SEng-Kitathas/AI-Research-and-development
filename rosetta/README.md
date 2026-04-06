# Rosetta — Weight Extraction Pipeline

## Purpose
Rosetta extracts quantized weights from SOTA models, decodes them to full precision, and prepares them for downstream ternary projection (the "Slime Protocol" first stage).

## Completed Extractions

### Qwen (~509M logical params)
- **Tensors:** 628 total, 169 quantized
- **Quantization scheme:** `affine_nibble_u32` (4-bit nibble-packed in U32)
- **Group size:** 64
- **Decode formula:** `decoded = unpack4(weight_u32_nibbles) * scale + bias`

### H2O
- **Tensors:** 371 total, 112 quantized
- **Quantization scheme:** `awq_i32_affine4`
- **Group size:** 128

## Directory Structure
```
rosetta/
├── scripts/
│   ├── quant_aware_convert_weights_to_relational_corpus_working.py
│   └── merged_dense_safetensors_repacker.py
├── manifests/
│   ├── h2o_overlay_manifest.json
│   ├── qwen_overlay_manifest.json
│   ├── h2o_dense_merged.safetensors.manifest.json
│   └── qwen_dense_merged.safetensors.manifest.json
├── docs/
│   ├── FULL_DEQUANT_OVERLAY_EXPORT_REPORT.md
│   └── README_REJOIN.txt
├── families.json          # Tensor classification by role/family
├── stats.json             # Extraction statistics
├── manifest.json          # Source provenance
└── tensors.jsonl          # Full relational corpus (628 records)
```

## Tensor Classification

By role:
- embedding: 3
- norm: 49
- mlp_down: 72
- mlp_gate: 72
- mlp_up: 72
- attention_qkv: 288
- attention_out: 72

By quantization:
- none (F16 passthrough): 459
- affine_nibble_u32: 169

## Usage

### Extract relational corpus from safetensors
```bash
python scripts/quant_aware_convert_weights_to_relational_corpus_working.py \
    /path/to/model.safetensors \
    --out /path/to/output/
```

Outputs:
- `tensors.jsonl` — per-tensor records with stats, quantization info, provenance
- `families.json` — classification histograms
- `stats.json` — summary statistics
- `manifest.json` — source file provenance

### tensors.jsonl record schema
```json
{
  "source_file": "...",
  "tensor_name": "model.layers.0.mlp.down_proj.weight",
  "shape": [896, 608],
  "logical_shape": [896, 4864],
  "dtype": "U32",
  "logical_dtype": "F32(decoded_sampled)",
  "layer_index": 0,
  "role_guess": "mlp_down",
  "family_guess": "mlp",
  "quantization": {
    "kind": "affine_nibble_u32",
    "group_size": 64,
    "decode_formula": "decoded = unpack4(...) * scale + bias"
  },
  "sample_stats": {
    "decoded_mean": -0.0001,
    "decoded_std": 0.015,
    "decoded_l2_norm": 1.99
  }
}
```

## Next Step
Build projection from decoded weights to TQ2 3×3 ternary representation. The research question: does this projection preserve useful structure?

## Provenance
- Extraction date: 2026-04-05
- Source models: Qwen (quantized safetensors), H2O (AWQ quantized)
- Status: Full dequant overlay export complete for both

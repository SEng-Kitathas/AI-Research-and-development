# AI Research and Development — Current State
**Date:** 2026-04-06
**Status:** Active research phase

---

## Active Research Frontier: TQ2 / Tesseract Quaternion

### Core Invention
TQ2 replaces scalar multiply-accumulate with **discrete geometric rotation** on 9-state ternary (x,y) weight coordinates.

Each weight is a coordinate `(x,y)` on a 3×3 grid where x, y ∈ {-1, 0, +1} → 9 discrete states.

Inference is rotation, not arithmetic:
```
(x,y) → (-y,x)   for 90°
(x,y) → (-x,-y)  for 180°
(x,y) → (y,-x)   for 270°
```

### Current Empirical Results
- **Best architecture (A1):** 79.42% accuracy across sigma v2/v3/v4 surfaces
- **Policy search:** 1,296 configurations evaluated
- **Warning surface (sigma v5):** 72.92% — async advantage is conditional on resolver/sync law

### Working Conclusion
> The next build pressure should focus on controlled replay, explicit resolver/sync ablations, and report-stable reruns rather than broadening the architecture surface.

---

## Rosetta Pipeline — Weight Consumption

### Purpose
Extract quantized weights from SOTA models, decode to full precision, prepare for ternary projection.

### Completed
- **Qwen extraction:** 628 tensors, 169 quantized (affine_nibble_u32), ~509M logical params
- **H2O extraction:** 371 tensors, 112 quantized (awq_i32_affine4)
- **Full dequant overlay export:** Complete float16 decoded tensors for all quantized weights
- **Relational corpus:** `tensors.jsonl` with per-tensor provenance, statistics, quantization metadata

### Next Step
**Connect rosetta → TQ2 kernel** — feed actual dequantized tensor chunks to the kernel, not synthetic sigma surfaces.

---

## Repository Structure

```
ai_research_repo/
├── tq2_kernel/              # TQ2 reference implementation
│   ├── src/                 # Core semantics modules
│   ├── harness/             # Experiment runners
│   ├── results/             # JSON result archives
│   ├── docs/                # Technical documentation
│   └── reports/             # Canonical summary reports
├── rosetta/                 # Weight extraction pipeline
│   ├── scripts/             # Quant-aware converters
│   ├── manifests/           # Dequant overlay manifests
│   ├── docs/                # Pipeline documentation
│   └── *.json/jsonl         # Corpus outputs
├── evaluations/             # Model evaluations
│   └── minilm_attention/    # MiniLM attention branch analysis
├── experiments/             # Raw experiment archives
├── audits/                  # CIL audit trails
├── payload/                 # Historical thread artifacts
└── thread_artifacts/        # Incremental research outputs
```

---

## Evolutionary Lineage

| Gen | Name | Bits/Weight | States | Math Operation | Status |
|-----|------|-------------|--------|----------------|--------|
| 0 | 2-bit | 2 | 3 | add/sub/skip | Ancestral |
| 1 | TQ1 | 1.58 | 3 | add/sub/skip | Seed Crystal |
| 2 | **TQ2** | 4-bit nibble XY | **9** | **Geometric rotation** | **CANONICAL** |
| 3 | TQ4 | 8-bit quaternion | 72+ | Full quaternion rotation | Future (OD-60) |

---

## Research Questions (Priority Order)

1. **Can TQ2 usefully digest real model weights?**
   - Is there a projection from extracted weight topology to 3×3 ternary that preserves useful structure?

2. **Why is async advantage conditional on resolver/sync law?**
   - Sigma v5 ablations needed

3. **What downstream task can the kernel learn?**
   - Tensor family classification from statistics?
   - Attention vs MLP discrimination?

---

## Methodology Notes

- **Law 0:** Discourse/spec refinement is NOT implementation. Iterate freely.
- **Law 1:** When we build — no stubs/TODOs/MVPs. Full production-grade only.
- **Law Ω:** Every artifact at theoretical maximum quality. Platonic ideal in bytes.
- **Ω Methodology:** Audit first → Catalog issues → Fix with per-fix verification → Final lint

---

## Session Provenance
This state document synthesizes:
- TQ2 canonical harness tree (2026-04-04)
- Rosetta full dequant overlay export (2026-04-05)
- Geometric inference thread artifacts (2026-03-29 through 2026-04-04)
- ChatGPT evaluation of ternary weight thesis

# TQ2/CIL Research — Current State
_Version: 2026-04-03 · Recovered from cached session_

## Active baseline
- **Canonical substrate**: TQ2 geometric weight encoding
- **Integrated runtime candidate**: RB-2R_v3 (with metadata-aware mode gating)
- **Async architecture winner**: A1 (direct_delta + family_contrast + veto resolver, parallel_join)
- **CIL**: exact-memory / evidence-traceability core
- **K2**: live fast lane — route-structure accumulation over time
- **K3**: meta/checkpoint/cold-state only, NOT live control

## Experimental state (as of 2026-03-30)

### Policy search (eb): 1296 policies searched
Best: m2 / blend=0.58 / agreement_bonus=0.18 / mirror_pen=0.3
→ mean_acc=78.59 | mirror=14 | rr=5 | composite=67.393
Surface: v2=88.89 / v3=71.88 / v4=75.00

### Async architecture search (ec): 1944 architectures
Best: direct_delta + family_contrast + veto + parallel_join / conf_gate=0.35
→ mean_acc=79.42 | mirror=13 | rr=5 | composite=68.635
Surface: v2=88.89 / v3=71.88 / v4=77.50

### A1 vs M2* comparison (ed)
A1 leads M2* by +0.83 accuracy, -1 mirror error on v4 specifically

### Sigma v5 stress test (eg) — architecture-sensitive surface
Both M2* and A1T: acc=70.83
M2*: mirror=7 rr=1 | A1T: mirror=8 rr=3
→ A1T loses edge on v5 stress surface

### Unified sync+async (eh): 3240 total
Best overall: async (direct_delta + family_contrast + sum resolver + shape_priority)
→ acc=72.92 | mirror=7 | rr=2 | composite=69.570

### A1 local refinement on v5 (ei): 729 variants
Best refined: right_bias=0.08 / blend=0.5 / conf_gate=0.25 / shape_priority / sum / veto=0.0
→ acc=72.92 | mirror=7 | rr=2 | composite=69.570

## Priority next experiments
- P0: Route-aware dual-head readout (TQ2-11: forge metadata for RB-2R_v3)
- P0: OOD + recurrence combined probe (TQ2-10)
- P0: Criticality map
- P1: Stepwise latent dissection
- P1: Bridge / hot-cold memory evaluation

## Reference implementations
- `payload/tq2_reference_semantics_v3_2026-03-29f.py` — RB-2R_v3 metadata-aware mode gating
- `payload/tq2_reference_semantics_v2_2026-03-29e.py` — RB-2R_v2 baseline
- `payload/tq2_reference_semantics_2026-03-29d.py` — original

## White paper lineage
v0.1 → v0.2 → v0.4 → v0.5 → v0.6 → v0.7 → v0.8 → v0.9 → **v1.0** (canonical)
Current best candidates: TQ2 (substrate), RB-2R_v3 (runtime), RegimeCache (inspiration note)

## Handoff note
This corpus was recovered from browser-cached session state after a sync corruption event.
The TQ2/CIL research track is intact. KarnOS/GODSPEC/FASM is classified as ancestral/reference material.

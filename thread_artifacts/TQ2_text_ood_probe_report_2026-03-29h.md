# TQ2 text OOD / catch-all probe
_Version: 2026-03-29h_

This extends the z80-inspired text classification probe with an explicit `UNKNOWN` class.

## Why this matters
The next pressure seam after intent classification is robustness:
- can the substrate avoid forcing everything into a known bucket?
- can a cheap runtime support abstention / catch-all behavior?

## Results

| model        |   accuracy_pct |   macro_f1_pct |   n_examples |
|:-------------|---------------:|---------------:|-------------:|
| BASE-0       |          46.67 |          45.81 |           45 |
| RB-2A        |          51.11 |          48.06 |           45 |
| RB-2B        |          31.11 |          29.39 |           45 |
| RB-2R_v2     |          46.67 |          42.47 |           45 |
| RB-2R_v3     |          46.67 |          42.47 |           45 |
| RB-2R_v4_OOD |          51.11 |          46.69 |           45 |

## Load-bearing findings

- `RB-2R_v4_OOD` reaches **51.11%** accuracy.
- `RB-2R_v3` reaches **46.67%**.
- `RB-2A` reaches **51.11%**.
- `RB-2B` reaches **31.11%**.

## Interpretation

This is the first probe where **OOD-aware abstention** becomes explicit.
If `RB-2R_v4_OOD` beats `RB-2R_v3`, then simple confidence-thresholded UNKNOWN handling is probably worth keeping as an optional runtime policy.

This does not mean the substrate "understands unknowns."
It means the runtime can be taught not to overcommit.

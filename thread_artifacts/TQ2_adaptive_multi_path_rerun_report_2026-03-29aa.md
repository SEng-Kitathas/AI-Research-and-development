# TQ2 adaptive multi-path rerun
_Version: 2026-03-29aa_

This reruns the synthetic multi-path latent benchmark with the adaptive K2 branch added.

## Results

| metric                  |   accuracy_pct |   macro_f1_pct |   n_examples |
|:------------------------|---------------:|---------------:|-------------:|
| PER_STEP_FAMILY         |          52.08 |          52.29 |          288 |
| K2_FAMILY               |          32.99 |          34.63 |          288 |
| ADAPTIVE_K2_FAMILY      |          32.99 |          34.63 |          288 |
| PER_STEP_ROUTE_PROBE    |          41.32 |          40.26 |          288 |
| K2_ROUTE_PROBE          |          24.31 |          25.07 |          288 |
| ADAPTIVE_K2_ROUTE_PROBE |          24.31 |          25.07 |          288 |

## Interpretation
The key comparison is:
- `K2_ROUTE_PROBE`
vs
- `ADAPTIVE_K2_ROUTE_PROBE`

If adaptive K2 remains low, then route diversity collapse is not mainly caused by fixed collapse timing.

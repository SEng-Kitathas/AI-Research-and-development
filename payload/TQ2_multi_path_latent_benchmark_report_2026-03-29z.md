# TQ2 multi-path latent benchmark
_Version: 2026-03-29z_

This is the first direct test of whether the latent family machinery preserves multiple valid internal routes.

## Metrics
- `PER_STEP_FAMILY`: family accuracy under per-step decode
- `K2_FAMILY`: family accuracy under K2 latent reuse
- `PER_STEP_ROUTE_PROBE`: route distinguishability under per-step family latent
- `K2_ROUTE_PROBE`: route distinguishability under K2 latent reuse

## Results

| metric               |   accuracy_pct |   macro_f1_pct |   n_examples |
|:---------------------|---------------:|---------------:|-------------:|
| PER_STEP_FAMILY      |          52.08 |          52.29 |          288 |
| K2_FAMILY            |          30.9  |          32.18 |          288 |
| PER_STEP_ROUTE_PROBE |          41.32 |          40.26 |          288 |
| K2_ROUTE_PROBE       |          24.31 |          25.07 |          288 |

## Interpretation
If family accuracy stays high while route-probe accuracy collapses, the system is likely collapsing route diversity into a shared family groove.
If route-probe accuracy remains strong, then the latent state is preserving more internal path information.

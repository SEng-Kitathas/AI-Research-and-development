# TQ2 dimension-selective readout
_Version: 2026-03-29aj_

This is the first head-specific latent weighting pass after the z_MAYBE gate/drop result.

## Full-range results

| variant                     |   family_accuracy_pct |   family_macro_f1_pct |   route_accuracy_pct |   route_macro_f1_pct |   route_delta_vs_baseline |
|:----------------------------|----------------------:|----------------------:|---------------------:|---------------------:|--------------------------:|
| BASELINE_UNWEIGHTED         |                 46.53 |                 41.06 |                26.74 |                20.19 |                    0      |
| ASYM_DROP_MAYBE_FAMILY      |                 47.92 |                 43.36 |                28.12 |                22.24 |                    0.0139 |
| ASYM_FAMILY_CRIT_ROUTE_KEEP |                 47.57 |                 43.03 |                27.78 |                22.01 |                    0.0104 |
| ASYM_SOFT_MAYBE_FAMILY      |                 48.96 |                 44.19 |                28.12 |                22.25 |                    0.0139 |
| ROUTE_ONLY_LATE_CRIT        |                 46.53 |                 41.06 |                27.08 |                20.5  |                    0.0035 |

## Late-step results (step >= 3)

| variant                     |   family_accuracy_step3plus_pct |   family_macro_f1_step3plus_pct |   route_accuracy_step3plus_pct |   route_macro_f1_step3plus_pct |   route_delta_vs_baseline_step3plus |
|:----------------------------|--------------------------------:|--------------------------------:|-------------------------------:|-------------------------------:|------------------------------------:|
| BASELINE_UNWEIGHTED         |                           77.78 |                           32.64 |                          50    |                          17.14 |                              0      |
| ASYM_DROP_MAYBE_FAMILY      |                           77.78 |                           33.78 |                          50    |                          16.67 |                              0      |
| ASYM_FAMILY_CRIT_ROUTE_KEEP |                           77.78 |                           33.78 |                          50    |                          16.67 |                              0      |
| ASYM_SOFT_MAYBE_FAMILY      |                           77.78 |                           33.78 |                          50    |                          16.67 |                              0      |
| ROUTE_ONLY_LATE_CRIT        |                           77.78 |                           32.64 |                          50.93 |                          17.33 |                              0.0093 |

## Interpretation
Positive route deltas indicate that asymmetric family-vs-route latent use is helping.
If a family-suppressed / route-retained z_MAYBE regime wins, then the next readout layer should stop using a single pooled latent policy.

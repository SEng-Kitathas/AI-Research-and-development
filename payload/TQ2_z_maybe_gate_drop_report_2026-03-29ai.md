# TQ2 z_MAYBE gate/drop experiment
_Version: 2026-03-29ai_

This tests whether dropping or gating z_MAYBE improves readout in the K2 multi-path regime.

## Full-range results

| variant                  |   family_accuracy_pct |   family_macro_f1_pct |   route_accuracy_pct |   route_macro_f1_pct |   route_delta_vs_baseline |
|:-------------------------|----------------------:|----------------------:|---------------------:|---------------------:|--------------------------:|
| BASELINE_ALL_DIMS        |                 46.53 |                 41.06 |                26.74 |                20.19 |                    0      |
| GLOBAL_DROP_Z_MAYBE      |                 48.96 |                 44.04 |                27.08 |                20.76 |                    0.0035 |
| FAMILY_DROP_ONLY         |                 48.96 |                 44.04 |                28.12 |                22.37 |                    0.0139 |
| ROUTE_DROP_ONLY          |                 46.53 |                 41.06 |                25.69 |                18.71 |                   -0.0104 |
| LATE_ROUTE_DROP_ONLY     |                 46.53 |                 41.06 |                25    |                18.66 |                   -0.0174 |
| LATE_GLOBAL_DROP_Z_MAYBE |                 48.96 |                 44.04 |                26.39 |                20.73 |                   -0.0035 |

## Late-step results (step >= 3)

| variant                  |   family_accuracy_step3plus_pct |   family_macro_f1_step3plus_pct |   route_accuracy_step3plus_pct |   route_macro_f1_step3plus_pct |   route_delta_vs_baseline_step3plus |
|:-------------------------|--------------------------------:|--------------------------------:|-------------------------------:|-------------------------------:|------------------------------------:|
| BASELINE_ALL_DIMS        |                           77.78 |                           32.64 |                          50    |                          17.14 |                              0      |
| GLOBAL_DROP_Z_MAYBE      |                           77.78 |                           33.31 |                          45.37 |                          15.22 |                             -0.0463 |
| FAMILY_DROP_ONLY         |                           77.78 |                           33.31 |                          50    |                          17.29 |                              0      |
| ROUTE_DROP_ONLY          |                           77.78 |                           32.64 |                          45.37 |                          14.98 |                             -0.0463 |
| LATE_ROUTE_DROP_ONLY     |                           77.78 |                           32.64 |                          45.37 |                          14.98 |                             -0.0463 |
| LATE_GLOBAL_DROP_Z_MAYBE |                           77.78 |                           33.31 |                          45.37 |                          15.22 |                             -0.0463 |

## Interpretation
Positive route deltas mean that dropping or gating z_MAYBE helps route readout.
If a late-step variant helps most, that suggests z_MAYBE is specifically harmful when route structure has already formed.

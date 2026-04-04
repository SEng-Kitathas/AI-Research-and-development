# TQ2 interaction-aware route head
_Version: 2026-03-29ak_

This is the first pairwise-interaction readout pass after the dimension-selective weighting result.

## Full-range results

| variant                     |   family_accuracy_pct |   family_macro_f1_pct |   route_accuracy_pct |   route_macro_f1_pct |   route_delta_vs_baseline |
|:----------------------------|----------------------:|----------------------:|---------------------:|---------------------:|--------------------------:|
| BASELINE_ASYM_FAMILY        |                 47.92 |                 43.36 |                27.78 |                21.82 |                    0      |
| INTERACTION_ROUTE_HEAD      |                 47.92 |                 43.36 |                26.74 |                22.81 |                   -0.0104 |
| INTERACTION_ROUTE_HEAD_WIDE |                 47.92 |                 43.36 |                29.17 |                24.67 |                    0.0139 |
| INTERACTION_BOTH_HEADS      |                 22.22 |                 18.14 |                11.81 |                 8.7  |                   -0.1597 |

## Late-step results (step >= 3)

| variant                     |   family_accuracy_step3plus_pct |   family_macro_f1_step3plus_pct |   route_accuracy_step3plus_pct |   route_macro_f1_step3plus_pct |   route_delta_vs_baseline_step3plus |
|:----------------------------|--------------------------------:|--------------------------------:|-------------------------------:|-------------------------------:|------------------------------------:|
| BASELINE_ASYM_FAMILY        |                           77.78 |                           33.78 |                          49.07 |                          16.58 |                              0      |
| INTERACTION_ROUTE_HEAD      |                           77.78 |                           33.78 |                          46.3  |                          19.57 |                             -0.0278 |
| INTERACTION_ROUTE_HEAD_WIDE |                           77.78 |                           33.78 |                          52.78 |                          22.42 |                              0.037  |
| INTERACTION_BOTH_HEADS      |                           32.41 |                           12.09 |                          17.59 |                           6.38 |                             -0.3148 |

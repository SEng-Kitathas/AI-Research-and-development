# TQ2 recursive validation pass
_Version: 2026-03-29al_

This pass applies the newest findings back onto earlier tests.

## Larger-N latent-final rerun

| variant                        |   family_accuracy_pct |   family_macro_f1_pct |   n_sequences |
|:-------------------------------|----------------------:|----------------------:|--------------:|
| FINAL_ONLY_BASELINE            |                    96 |                 95.96 |           100 |
| FINAL_ONLY_CONSERVATIVE_FAMILY |                    96 |                 95.99 |           100 |
| LAST_STEP_BASELINE             |                    94 |                 94.12 |           100 |
| LAST_STEP_CONSERVATIVE_FAMILY  |                    81 |                 81.64 |           100 |

## Recursive validation matrix

| variant                             |   full_family_acc_pct |   full_route_acc_pct |   late_route_acc_pct |   n_examples |
|:------------------------------------|----------------------:|---------------------:|---------------------:|-------------:|
| BASELINE_POOLED                     |                 45.83 |                28.33 |                48.33 |          480 |
| CONSERVATIVE_SCALAR_ROUTE           |                 48.12 |                29.79 |                50    |          480 |
| CONSERVATIVE_WIDE_INTERACTION_ROUTE |                 48.12 |                30    |                50.56 |          480 |

## Phase behavior under recursive validation

| variant                             |   early_route_behavior_pct |   mid_route_behavior_pct |   late_route_behavior_pct |
|:------------------------------------|---------------------------:|-------------------------:|--------------------------:|
| BASELINE_POOLED                     |                      16.33 |                    47.86 |                        50 |
| CONSERVATIVE_SCALAR_ROUTE           |                      17.67 |                    50    |                        50 |
| CONSERVATIVE_WIDE_INTERACTION_ROUTE |                      17.67 |                    50.71 |                        50 |

## Interpretation
- If `FINAL_ONLY_CONSERVATIVE_FAMILY` beats the old final-only baseline, the family-head update is real beyond one toy pass.
- If `CONSERVATIVE_WIDE_INTERACTION_ROUTE` stays best in the recursive matrix, the interaction-aware route head survives recursion instead of being a one-off win.

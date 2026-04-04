# TQ2 stepwise multi-path separability
_Version: 2026-03-29ah_

This is the first direct stepwise read of the multi-path regime itself.

## Stepwise summary

| mode        |   step |   family_behavior_acc_pct |   route_behavior_acc_pct |   family_probe_acc_pct |   route_probe_acc_pct |   mean_family_margin |   mean_family_entropy |   mean_route_margin |
|:------------|-------:|--------------------------:|-------------------------:|-----------------------:|----------------------:|---------------------:|----------------------:|--------------------:|
| per_step    |      0 |                     30    |                    15    |                  66.67 |                 33.33 |                0.575 |                 1.18  |               0     |
| per_step    |      1 |                     36.67 |                    26.67 |                  70    |                 70    |                1.112 |                 0.813 |               2.036 |
| per_step    |      2 |                     46.67 |                    38.33 |                  75    |                 80    |                1.331 |                 0.763 |               1.346 |
| per_step    |      3 |                     94.44 |                    80.56 |                  94.44 |                 61.11 |                2.203 |                 0.592 |               0.693 |
| per_step    |      4 |                    100    |                    75    |                 100    |                 75    |                1.83  |                 0.732 |               1     |
| per_step    |      5 |                     75    |                    75    |                 100    |                 79.17 |                1.958 |                 0.719 |               1.289 |
| per_step    |      6 |                     50    |                    50    |                 100    |                 83.33 |                0.82  |                 1.104 |               1.655 |
| per_step    |      7 |                      0    |                     0    |                 100    |                100    |                1.407 |                 0.682 |               2     |
| k2          |      0 |                     30    |                    15    |                  66.67 |                 33.33 |                0.575 |                 1.18  |               0     |
| k2          |      1 |                     36.67 |                    26.67 |                  55    |                 40    |                2.177 |                 0.359 |               1.926 |
| k2          |      2 |                     45    |                    36.67 |                  65    |                 48.33 |                4.075 |                 0.211 |               1.343 |
| k2          |      3 |                     44.44 |                    30.56 |                  83.33 |                 63.89 |               12.355 |                 0.056 |               0.443 |
| k2          |      4 |                     25    |                    25    |                 100    |                 87.5  |               12.665 |                 0.015 |               0.914 |
| k2          |      5 |                     25    |                    25    |                 100    |                 87.5  |               10.329 |                 0.014 |               0.664 |
| k2          |      6 |                      0    |                     0    |                 100    |                100    |                8.538 |                 0.034 |               0.578 |
| k2          |      7 |                      0    |                     0    |                 100    |                100    |               15.145 |                 0.023 |               1.655 |
| adaptive_k2 |      0 |                     30    |                    15    |                  66.67 |                 33.33 |                0.575 |                 1.18  |               0     |
| adaptive_k2 |      1 |                     36.67 |                    26.67 |                  55    |                 40    |                2.177 |                 0.359 |               1.926 |
| adaptive_k2 |      2 |                     45    |                    36.67 |                  65    |                 48.33 |                4.075 |                 0.211 |               1.343 |
| adaptive_k2 |      3 |                     44.44 |                    30.56 |                  83.33 |                 63.89 |               12.355 |                 0.056 |               0.443 |
| adaptive_k2 |      4 |                     25    |                    25    |                 100    |                 87.5  |               12.665 |                 0.015 |               0.914 |
| adaptive_k2 |      5 |                     25    |                    25    |                 100    |                 87.5  |               10.329 |                 0.014 |               0.664 |
| adaptive_k2 |      6 |                      0    |                     0    |                 100    |                100    |                8.538 |                 0.034 |               0.578 |
| adaptive_k2 |      7 |                      0    |                     0    |                 100    |                100    |               15.145 |                 0.023 |               1.655 |

## Phase summary

| mode        |   early_route_probe_pct |   mid_route_probe_pct |   late_route_probe_pct | pattern            |
|:------------|------------------------:|----------------------:|-----------------------:|:-------------------|
| per_step    |                   61.11 |                 71.76 |                  91.67 | emerges_then_holds |
| k2          |                   40.56 |                 79.63 |                 100    | emerges_then_holds |
| adaptive_k2 |                   40.56 |                 79.63 |                 100    | emerges_then_holds |

## Interpretation
- `family_behavior_acc_pct` and `route_behavior_acc_pct` show what the current readout is doing.
- `family_probe_acc_pct` and `route_probe_acc_pct` show what the latent vectors still contain.
- if route probe rises while route behavior stays weak, readout is the main suspect.
- if both stay weak, representation itself is the main suspect.

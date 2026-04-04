# TQ2 K3 route-diversity preserver
_Version: 2026-03-29am_

This is the first narrow K3 test after recursive validation.

## Full-range results

| variant                    |   family_accuracy_pct |   family_macro_f1_pct |   route_accuracy_pct |   route_macro_f1_pct |   route_delta_vs_best |
|:---------------------------|----------------------:|----------------------:|---------------------:|---------------------:|----------------------:|
| BEST_CURRENT_STACK         |                 48.12 |                 43.38 |                30    |                27.28 |                0      |
| K3_ROUTE_SUMMARY_SMALL     |                 48.12 |                 43.38 |                30    |                27.28 |                0      |
| K3_ROUTE_SUMMARY_MED       |                 48.12 |                 43.38 |                30    |                27.28 |                0      |
| K3_ROUTE_SUMMARY_LATE_ONLY |                 48.12 |                 43.38 |                29.79 |                26.7  |               -0.0021 |

## Late-step results (step >= 3)

| variant                    |   family_accuracy_step3plus_pct |   family_macro_f1_step3plus_pct |   route_accuracy_step3plus_pct |   route_macro_f1_step3plus_pct |   route_delta_vs_best_step3plus |
|:---------------------------|--------------------------------:|--------------------------------:|-------------------------------:|-------------------------------:|--------------------------------:|
| BEST_CURRENT_STACK         |                           78.89 |                           33.66 |                          50.56 |                          21.04 |                          0      |
| K3_ROUTE_SUMMARY_SMALL     |                           78.89 |                           33.66 |                          50.56 |                          21.04 |                          0      |
| K3_ROUTE_SUMMARY_MED       |                           78.89 |                           33.66 |                          50.56 |                          21.04 |                          0      |
| K3_ROUTE_SUMMARY_LATE_ONLY |                           78.89 |                           33.66 |                          50    |                          18.34 |                         -0.0056 |

## Interpretation
Positive route deltas indicate that K3 adds value as a narrow route-diversity preserver without contaminating the fast loop.

# TQ2 K2→K3 macro/micro track test
_Version: 2026-03-29an_

This is the first direct test of the user's CFAR-style K2→K3 hypothesis.

## Results

| variant                 |   family_accuracy_pct |   family_macro_f1_pct |   route_accuracy_pct |   route_macro_f1_pct |   route_accuracy_step3plus_pct |   route_delta_vs_best |   route_delta_vs_best_step3plus |
|:------------------------|----------------------:|----------------------:|---------------------:|---------------------:|-------------------------------:|----------------------:|--------------------------------:|
| BEST_CURRENT_STACK      |                 48.12 |                 43.38 |                29.79 |                25.89 |                          50    |                0      |                          0      |
| PERIODIC_K3_ALWAYS_LATE |                 48.12 |                 43.38 |                30    |                27.28 |                          50.56 |                0.0021 |                          0.0056 |
| EVENT_K3_TRACK_LATE     |                 48.12 |                 43.38 |                30    |                27.28 |                          50.56 |                0.0021 |                          0.0056 |
| CFAR_K3_LATE_IF_CFAR    |                 48.12 |                 43.38 |                30    |                27.28 |                          50.56 |                0.0021 |                          0.0056 |
| CFAR_K3_FINAL_INTERP    |                 48.12 |                 43.38 |                29.79 |                26.7  |                          50    |                0      |                          0      |

## Interpretation
- `PERIODIC_K3_ALWAYS_LATE` is the boring decimation baseline.
- `EVENT_K3_TRACK_LATE` uses simple event-driven K2 aggregation.
- `CFAR_K3_LATE_IF_CFAR` uses neighborhood-relative salience before allowing K3 into route readout.
- `CFAR_K3_FINAL_INTERP` only lets K3 participate in final convergence.

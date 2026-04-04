# TQ2 text transform-family ablation
_Version: 2026-03-29ao_

This tests transform families over the current synthetic text regime using the current best head stack.

## Results

| transform_mode   |   family_accuracy_pct |   family_macro_f1_pct |   route_accuracy_pct |   route_macro_f1_pct |   route_accuracy_step3plus_pct |   route_macro_f1_step3plus_pct |
|:-----------------|----------------------:|----------------------:|---------------------:|---------------------:|-------------------------------:|-------------------------------:|
| NO_TRANSFORM     |                 53.33 |                 50.25 |                36.46 |                33.49 |                          60    |                          24.21 |
| WHOLE_ONLY       |                 51.46 |                 47.25 |                35    |                30.84 |                          61.67 |                          24.29 |
| BLOCK_ONLY       |                 45.42 |                 38.87 |                28.12 |                23.2  |                          52.78 |                          21.56 |
| ALL_TRANSFORMS   |                 45    |                 38.72 |                27.29 |                23.44 |                          50    |                          20.13 |

## Interpretation
The best transform family for future text-side work should be the one that most consistently improves family accuracy, route accuracy, and late-step route accuracy under the current stack.

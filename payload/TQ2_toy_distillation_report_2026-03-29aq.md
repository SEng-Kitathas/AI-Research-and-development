# TQ2 toy teacher → student distillation
_Version: 2026-03-29aq_

This is the first explicit Project A feasibility result.

## Distillation results

| task                            | model                     | feature_map            |   accuracy_pct |   macro_f1_pct |
|:--------------------------------|:--------------------------|:-----------------------|---------------:|---------------:|
| T2 Block composition invariance | Teacher MLP               | raw_9                  |           54.6 |          54.72 |
| T2 Block composition invariance | Student linear distilled  | raw_9                  |           27.6 |          25.31 |
| T2 Block composition invariance | Student ternary distilled | raw_9                  |           26.2 |          21.64 |
| T2 Block composition invariance | Student linear distilled  | raw_9_plus_pairwise_45 |           56.6 |          55.54 |
| T2 Block composition invariance | Student ternary distilled | raw_9_plus_pairwise_45 |           52.6 |          52.92 |
| T4 Mixed global+local motifs    | Teacher MLP               | raw_9                  |           22.4 |          21.89 |
| T4 Mixed global+local motifs    | Student linear distilled  | raw_9                  |            9.8 |           9    |
| T4 Mixed global+local motifs    | Student ternary distilled | raw_9                  |            9.6 |           9.37 |
| T4 Mixed global+local motifs    | Student linear distilled  | raw_9_plus_pairwise_45 |           13.4 |          12.67 |
| T4 Mixed global+local motifs    | Student ternary distilled | raw_9_plus_pairwise_45 |           11.2 |          10.84 |

## Quantized student details

| task                            | feature_map            |    best_q |   alpha_w |   alpha_b |   test_accuracy_pct |   test_macro_f1_pct |   weight_zero_fraction_pct |
|:--------------------------------|:-----------------------|----------:|----------:|----------:|--------------------:|--------------------:|---------------------------:|
| T2 Block composition invariance | raw_9                  | 0.0550303 | 0.0587527 | 0.0557539 |                26.2 |               21.64 |                      88.89 |
| T2 Block composition invariance | raw_9_plus_pairwise_45 | 0.181656  | 0.354459  | 0.38569   |                52.6 |               52.92 |                      80    |
| T4 Mixed global+local motifs    | raw_9                  | 0.0850951 | 0.182389  | 0.165143  |                 9.6 |                9.37 |                      37.5  |
| T4 Mixed global+local motifs    | raw_9_plus_pairwise_45 | 0.05      | 0.135788  | 0.163758  |                11.2 |               10.84 |                      36.39 |

## Accuracy pivot (%)

| task                            | feature_map            |   Student linear distilled |   Student ternary distilled |   Teacher MLP |
|:--------------------------------|:-----------------------|---------------------------:|----------------------------:|--------------:|
| T2 Block composition invariance | raw_9                  |                       27.6 |                        26.2 |          54.6 |
| T2 Block composition invariance | raw_9_plus_pairwise_45 |                       56.6 |                        52.6 |         nan   |
| T4 Mixed global+local motifs    | raw_9                  |                        9.8 |                         9.6 |          22.4 |
| T4 Mixed global+local motifs    | raw_9_plus_pairwise_45 |                       13.4 |                        11.2 |         nan   |

## Interpretation
The useful question here is not whether the ternary student beats the teacher.
It is whether a quantized/distilled discrete student can recover a nontrivial fraction of the teacher's behavior on the task family at all.

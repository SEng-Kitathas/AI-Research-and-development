# TQ2 tiny MLP baseline on T1–T4
_Version: 2026-03-29ap_

This is the SOP external-calibration pass.

## Tiny MLP results (20 seeds)

| task                            |   mean_accuracy_pct |   std_accuracy_pct |   mean_macro_f1_pct |   std_macro_f1_pct |   n_seeds |
|:--------------------------------|--------------------:|-------------------:|--------------------:|-------------------:|----------:|
| T1 Whole-plane motif invariance |               98.86 |               0.54 |               98.86 |               0.54 |        20 |
| T2 Block composition invariance |               52.81 |               3.06 |               52.26 |               2.81 |        20 |
| T3 Majority-sign sanity         |              100    |               0    |              100    |               0    |        20 |
| T4 Mixed global+local motifs    |               17.32 |               1.79 |               16.46 |               1.78 |        20 |

## Comparison against existing branch report
Using: **RB-2R_v3 mixed-task wave**

### Accuracy (%)

| task                            |   BASE-0 |   RB-2A |   RB-2B |   RB-2R_v3 |   Tiny MLP |
|:--------------------------------|---------:|--------:|--------:|-----------:|-----------:|
| T1 Whole-plane motif invariance |    61.56 |   97.12 |   47.12 |      97.12 |      98.86 |
| T2 Block composition invariance |    76.75 |   80.19 |  100    |     100    |      52.81 |
| T3 Majority-sign sanity         |    82.94 |   82.94 |   40.44 |     100    |     100    |
| T4 Mixed global+local motifs    |    35.75 |   53.12 |   36.75 |      53.5  |      17.32 |

### Macro-F1 (%)

| task                            |   BASE-0 |   RB-2A |   RB-2B |   RB-2R_v3 |   Tiny MLP |
|:--------------------------------|---------:|--------:|--------:|-----------:|-----------:|
| T1 Whole-plane motif invariance |    58.88 |   97.06 |   42.79 |      97.06 |      98.86 |
| T2 Block composition invariance |    72.83 |   77.65 |  100    |     100    |      52.26 |
| T3 Majority-sign sanity         |    60.85 |   60.85 |   19.14 |     100    |     100    |
| T4 Mixed global+local motifs    |    32.96 |   44.94 |   24.17 |      45.65 |      16.46 |

## Interpretation
This baseline is meant to answer whether the current task family rewards a small generic learner strongly enough that our substrate results need to be interpreted more cautiously.

Because this is a reconstructed T1–T4 family benchmark rather than the exact earlier harness implementation, the comparison is directional, not strict apples-to-apples.
The useful signal is whether the tiny learned baseline is generally strong, weak, or mixed across the same task families.

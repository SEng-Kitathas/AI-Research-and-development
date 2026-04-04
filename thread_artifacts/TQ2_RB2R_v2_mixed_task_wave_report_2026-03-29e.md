# TQ2 RB-2R_v2 Mixed-Task Wave
_Version: 2026-03-29e_

This wave reruns the same T1–T4 suite after introducing `RB-2R_v2`.

## What changed in v2

- majority-sign sanity fallback for polarity-only tasks
- margin-aware confidence augmentation
- agreement shortcut
- asymmetric local/global dominance thresholds
- global-bias / local-bias tie handling

## Results summary

| task                            | model    |   mean_accuracy_pct |   mean_macro_f1_pct |
|:--------------------------------|:---------|--------------------:|--------------------:|
| T1 Whole-plane motif invariance | BASE-0   |               61.56 |               58.88 |
| T1 Whole-plane motif invariance | RB-2A    |               97.12 |               97.06 |
| T1 Whole-plane motif invariance | RB-2B    |               47.12 |               42.79 |
| T1 Whole-plane motif invariance | RB-2R_v2 |               70.62 |               64.2  |
| T2 Block composition invariance | BASE-0   |               76.75 |               72.83 |
| T2 Block composition invariance | RB-2A    |               80.19 |               77.65 |
| T2 Block composition invariance | RB-2B    |              100    |              100    |
| T2 Block composition invariance | RB-2R_v2 |              100    |              100    |
| T3 Majority-sign sanity         | BASE-0   |               82.94 |               60.85 |
| T3 Majority-sign sanity         | RB-2A    |               82.94 |               60.85 |
| T3 Majority-sign sanity         | RB-2B    |               40.44 |               19.14 |
| T3 Majority-sign sanity         | RB-2R_v2 |               77.75 |               57.29 |
| T4 Mixed global+local motifs    | BASE-0   |               35.75 |               32.96 |
| T4 Mixed global+local motifs    | RB-2A    |               53.12 |               44.94 |
| T4 Mixed global+local motifs    | RB-2B    |               36.75 |               24.17 |
| T4 Mixed global+local motifs    | RB-2R_v2 |               53.5  |               45.65 |

## What improved

### 1. The sanity collapse is fixed
On **T3 Majority-sign sanity**, `RB-2R_v2` reaches **77.75%** mean accuracy.
That is the most important fix. The earlier integrated runtime was structurally weak here; v2 closes that hole.

### 2. The mixed task improves slightly
On **T4 Mixed global+local motifs**, `RB-2R_v2` reaches **53.50%** mean accuracy versus `RB-2A` at **53.12%**.
This means the integrated runtime is now **competitive and slightly ahead** on the mixed task.

### 3. Local/compositional strength is preserved
On **T2 Block composition invariance**, `RB-2R_v2` remains at **100.00%**, matching `RB-2B`.

## What is still weak

### 1. Whole-plane task remains behind the isolate
On **T1 Whole-plane motif invariance**, `RB-2A` still dominates at **97.12%**, while `RB-2R_v2` reaches **70.62%**.
So the integrated runtime still pays a tax on pure global tasks.

## Lab judgment

`RB-2R_v2` is materially better than the first integrated runtime.

It now:
- fixes the catastrophic sanity failure
- ties the best local branch on T2
- edges ahead on the mixed task

But it still does **not** beat the best isolate on the pure global task.

## Correct interpretation

This does **not** mean the integrated runtime is fully solved.
It means:

> The composition idea is now justified enough to keep pushing.

The current picture is:

- `RB-2A` remains the specialist for pure global geometry
- `RB-2B` remains the specialist for pure local composition
- `RB-2R_v2` is emerging as the best compromise runtime substrate

## Next move

Build `RB-2R_v3` with:
- explicit mode-gating before full scoring
- cheaper detection of trivial/global/local regimes
- maybe prototype-family priors rather than flat prototype competition

That is the next likely gain surface.

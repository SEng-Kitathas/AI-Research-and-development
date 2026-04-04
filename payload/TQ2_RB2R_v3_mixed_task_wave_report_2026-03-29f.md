# TQ2 RB-2R_v3 Mixed-Task Wave
_Version: 2026-03-29f_

This wave tests `RB-2R_v3`, which adds **metadata-aware mode gating** on top of `RB-2R_v2`.

## What changed in v3

- polarity-only prototype sets route to a polarity fallback
- global-only prototype families route to the whole-plane specialist
- mixed / dual-metadata sets continue through RB-2R_v2

This is a stronger, more structured runtime rather than a purely generic fusion layer.

## Results summary

| task                            | model    |   mean_accuracy_pct |   mean_macro_f1_pct |
|:--------------------------------|:---------|--------------------:|--------------------:|
| T1 Whole-plane motif invariance | BASE-0   |               61.56 |               58.88 |
| T1 Whole-plane motif invariance | RB-2A    |               97.12 |               97.06 |
| T1 Whole-plane motif invariance | RB-2B    |               47.12 |               42.79 |
| T1 Whole-plane motif invariance | RB-2R_v3 |               97.12 |               97.06 |
| T2 Block composition invariance | BASE-0   |               76.75 |               72.83 |
| T2 Block composition invariance | RB-2A    |               80.19 |               77.65 |
| T2 Block composition invariance | RB-2B    |              100    |              100    |
| T2 Block composition invariance | RB-2R_v3 |              100    |              100    |
| T3 Majority-sign sanity         | BASE-0   |               82.94 |               60.85 |
| T3 Majority-sign sanity         | RB-2A    |               82.94 |               60.85 |
| T3 Majority-sign sanity         | RB-2B    |               40.44 |               19.14 |
| T3 Majority-sign sanity         | RB-2R_v3 |              100    |              100    |
| T4 Mixed global+local motifs    | BASE-0   |               35.75 |               32.96 |
| T4 Mixed global+local motifs    | RB-2A    |               53.12 |               44.94 |
| T4 Mixed global+local motifs    | RB-2B    |               36.75 |               24.17 |
| T4 Mixed global+local motifs    | RB-2R_v3 |               53.5  |               45.65 |

## Load-bearing findings

### 1. The pure-global tax is removed
On **T1 Whole-plane motif invariance**, `RB-2R_v3` reaches **97.12%**, exactly matching `RB-2A`.

### 2. The local-composition win is preserved
On **T2 Block composition invariance**, `RB-2R_v3` reaches **100.00%**, matching `RB-2B`.

### 3. The sanity task is fully solved
On **T3 Majority-sign sanity**, `RB-2R_v3` reaches **100.00%**.

### 4. The mixed-task edge is preserved
On **T4 Mixed global+local motifs**, `RB-2R_v3` reaches **53.50%**, slightly ahead of `RB-2A` at **53.12%**.

## Interpretation

This is the first integrated runtime that cleanly earns promotion.

It does not beat the best specialist everywhere by using one generic rule.
Instead, it does something more important:

> it uses cheap metadata-aware regime gating to route work to the right substrate behavior.

That is a stronger and more realistic result than pretending one universal fusion rule should dominate all tasks.

## Caveat

`RB-2R_v3` is now less "blindly generic" than v1/v2.
It relies on prototype-family metadata and regime structure.

That is acceptable for the lab, but it should be recorded honestly:
- better runtime
- more structured assumptions

## Current lab judgment

`RB-2R_v3` is now the best current candidate for the canonical integrated runtime.

## Next move

The next pressure point is no longer basic fusion.
It is:

1. validate v3 on less synthetic tasks
2. decide how much metadata-aware routing is allowed inside the canonical substrate
3. teach Forge to produce the metadata the runtime wants

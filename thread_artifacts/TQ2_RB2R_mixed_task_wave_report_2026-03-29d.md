# TQ2 RB-2R Mixed-Task Wave
_Version: 2026-03-29d_

This is the first benchmark wave that connects the slow reference semantics to the benchmark harness.

## Conditions

- Tasks: T1–T4 synthetic wave
- Seeds per task: 20
- Samples per seed: 80
- Comparators:
  - `BASE-0`
  - `RB-2A` whole-plane isolate
  - `RB-2B` blockwise isolate
  - `RB-2R` integrated runtime composition

## Results summary

| task                            | model   |   mean_accuracy_pct |   mean_macro_f1_pct |
|:--------------------------------|:--------|--------------------:|--------------------:|
| T1 Whole-plane motif invariance | BASE-0  |               61.56 |               58.88 |
| T1 Whole-plane motif invariance | RB-2A   |               97.12 |               97.06 |
| T1 Whole-plane motif invariance | RB-2B   |               47.12 |               42.79 |
| T1 Whole-plane motif invariance | RB-2R   |               70.69 |               63.86 |
| T2 Block composition invariance | BASE-0  |               76.75 |               72.83 |
| T2 Block composition invariance | RB-2A   |               80.19 |               77.65 |
| T2 Block composition invariance | RB-2B   |              100    |              100    |
| T2 Block composition invariance | RB-2R   |               99.94 |               99.94 |
| T3 Majority-sign sanity         | BASE-0  |               82.94 |               60.85 |
| T3 Majority-sign sanity         | RB-2A   |               82.94 |               60.85 |
| T3 Majority-sign sanity         | RB-2B   |               40.44 |               19.14 |
| T3 Majority-sign sanity         | RB-2R   |               40.44 |               19.14 |
| T4 Mixed global+local motifs    | BASE-0  |               35.75 |               32.96 |
| T4 Mixed global+local motifs    | RB-2A   |               53.12 |               44.94 |
| T4 Mixed global+local motifs    | RB-2B   |               36.75 |               24.17 |
| T4 Mixed global+local motifs    | RB-2R   |               48.25 |               39.09 |

## Load-bearing findings

### 1. RB-2A dominates the whole-plane task
On **T1 Whole-plane motif invariance**, `RB-2A` is best at **97.12%** mean accuracy.
This confirms the expected global/geometric upside.

### 2. RB-2B dominates the block composition task
On **T2 Block composition invariance**, `RB-2B` is best at **100.00%** mean accuracy.
`RB-2R` is effectively tied, which is good news for runtime composition.

### 3. RB-2R currently fails the sanity task
On **T3 Majority-sign sanity**, `RB-2R` collapses to **40.44%** mean accuracy, while `BASE-0` and `RB-2A` both reach **82.94%**.
This is a real failure mode, not a cosmetic dip.

### 4. T4 mixed-task does NOT yet justify the integrated runtime
On **T4 Mixed global+local motifs**, `RB-2A` is currently best at **53.12%**, while `RB-2R` reaches **48.25%**.
That means the current reconciliation policy has **not yet earned its complexity**.

## Interpretation

This wave is useful because it is honest.

It says:

- the branches are real
- the runtime composition idea is plausible
- but the **current RB-2R reconciliation policy is not yet good enough**

The main issue is not the substrate itself.
The issue is the **fusion logic**.

## New pressure points

1. **Confidence-aware reconciliation must be improved**
   - current equal-weight fusion is too blunt
   - it underperforms on both the sanity task and the mixed task

2. **A cheap polarity/majority micro-branch may be needed**
   - T3 exposes a real blind spot
   - this could be either:
     - a baseline fallback
     - or a built-in sanity gate before reconciliation

3. **RB-2R must beat or tie the best isolate on T4 before promotion**
   - until then, integrated runtime remains plausible but unproven

## Recommended next move

Build `RB-2R_v2` with:
- mode gating before fusion
- optional sanity fallback for trivial polarity tasks
- confidence-weighted rather than flat reconciliation

Then rerun the same wave.

## Notes

This wave should be treated as:
- benchmark-valid
- reference-semantics-backed
- still synthetic
- and intentionally harsh

That is what a clean-room lab is for.

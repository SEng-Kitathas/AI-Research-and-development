# TQ2 OOD + recurrence + refresh/reuse family-routing probe
_Version: 2026-03-29m_

This is the first probe that combines all three active seams:

- OOD / UNKNOWN handling
- recurrent carry sequence state
- refresh-vs-reuse scheduling

## Task

At each generation step, the system routes the current prompt+prefix+carry state to a response family:
- `HI`
- `YES`
- `MAYBE`
- `NO`
- `UNKNOWN`

This is not next-character prediction.
It is a family-routing probe over a recurrent sequence state.

## Strategies

- `FULL_FAM`: full recompute every step
- `FULL_FAM_OOD`: full recompute every step + UNKNOWN threshold
- `RR2_TOP2_FAM`: refresh every 2 steps, reuse top-2 family shortlist
- `RR2_TOP2_FAM_OOD`: same as above + UNKNOWN threshold

## Results

| strategy         |   accuracy_pct |   macro_f1_pct |   unknown_overcommit_pct |   relative_scoring_cost |
|:-----------------|---------------:|---------------:|-------------------------:|------------------------:|
| FULL_FAM         |          57.87 |          54.96 |                    45.83 |                     1   |
| FULL_FAM_OOD     |          50    |          35.36 |                    11.11 |                     1   |
| RR2_TOP2_FAM     |          57.87 |          54.96 |                    45.83 |                     0.7 |
| RR2_TOP2_FAM_OOD |          46.3  |          32.78 |                    22.22 |                     0.7 |

## Load-bearing findings

1. If the OOD-aware variants cut UNKNOWN overcommit without gutting accuracy, abstention is earning its place.
2. If refresh/reuse remains close to full recompute under OOD pressure, native RegimeCache remains viable under robustness constraints.
3. If reuse plus OOD collapses, then refresh logic and abstention interact badly and need redesign.

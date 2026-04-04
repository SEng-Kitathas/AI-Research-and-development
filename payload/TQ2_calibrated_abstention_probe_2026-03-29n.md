# TQ2 calibrated abstention probe under OOD + recurrence + refresh/reuse
_Version: 2026-03-29n_

This tightens the weak seam from the previous probe.

Instead of using a blunt fixed OOD margin threshold, this probe calibrates the abstention threshold on a held-out calibration split, then evaluates on separate prompts.

## Calibrated thresholds

- Full recompute threshold: **2.30**
- Refresh/reuse threshold: **2.30**

Calibration objective favored:
- lower UNKNOWN overcommit
- without destroying macro-F1

## Results on held-out prompts

| strategy         |   accuracy_pct |   macro_f1_pct |   unknown_overcommit_pct |   relative_scoring_cost |
|:-----------------|---------------:|---------------:|-------------------------:|------------------------:|
| FULL_FAM         |          60    |          58.33 |                       50 |                     1   |
| FULL_FAM_CAL_OOD |          48.33 |          33.03 |                        0 |                     1   |
| RR2_TOP2_FAM     |          60    |          58.33 |                       50 |                     0.7 |
| RR2_TOP2_CAL_OOD |          48.33 |          32.33 |                        0 |                     0.7 |

## Load-bearing findings

1. If calibrated abstention reduces UNKNOWN overcommit with less damage than the blunt threshold, then abstention is becoming more surgical.
2. If refresh/reuse plus calibrated abstention stays near full recompute, RegimeCache survives robustness pressure better than before.
3. If the calibrated thresholds collapse anyway, the problem is not just threshold choice.
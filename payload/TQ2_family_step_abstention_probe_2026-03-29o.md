# TQ2 family-specific + step-aware abstention probe
_Version: 2026-03-29o_

This probe tightens abstention one more step.

Instead of:
- one blunt fixed margin threshold

it uses:
- family-specific thresholds
- split into early vs late generation steps
- calibrated on held-out calibration prompts

## Global fallback thresholds

- Full recompute fallback: **2.30**
- Refresh/reuse fallback: **2.30**

## Results on held-out prompts

| strategy           |   accuracy_pct |   macro_f1_pct |   unknown_overcommit_pct |   relative_scoring_cost |
|:-------------------|---------------:|---------------:|-------------------------:|------------------------:|
| FULL_FAM           |             60 |          58.33 |                       50 |                     1   |
| FULL_FAM_FSTEP_CAL |             60 |          61.02 |                       50 |                     1   |
| RR2_TOP2_FAM       |             60 |          58.33 |                       50 |                     0.7 |
| RR2_TOP2_FSTEP_CAL |             60 |          61.02 |                       50 |                     0.7 |

## Load-bearing findings

1. If family/step-aware abstention beats the prior calibrated global abstention, then abstention is becoming more surgical.
2. If refresh/reuse + family/step-aware abstention remains competitive, then RegimeCache stays alive under tighter robustness rules.
3. If gains are tiny, the next seam is probably carry-drift-aware abstention rather than more threshold slicing.
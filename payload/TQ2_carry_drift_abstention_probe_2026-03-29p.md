# TQ2 carry-drift-aware abstention probe
_Version: 2026-03-29p_

This probes the next seam after family/step thresholds failed.

Abstention rule:
- abstain only when **margin is low**
- and **carry drift is high**

This turns abstention into a two-factor state-aware decision rather than a single confidence cutoff.

## Calibrated parameters

- Full recompute:
  - margin threshold = **2.30**
  - drift threshold = **0**
- Refresh/reuse:
  - margin threshold = **2.30**
  - drift threshold = **0**

## Results on held-out prompts

| strategy           |   accuracy_pct |   macro_f1_pct |   unknown_overcommit_pct |   relative_scoring_cost |
|:-------------------|---------------:|---------------:|-------------------------:|------------------------:|
| FULL_FAM           |          60    |          58.33 |                       50 |                     1   |
| FULL_FAM_DRIFT_CAL |          48.33 |          33.03 |                        0 |                     1   |
| RR2_TOP2_FAM       |          60    |          58.33 |                       50 |                     0.7 |
| RR2_TOP2_DRIFT_CAL |          48.33 |          32.33 |                        0 |                     0.7 |

## Load-bearing findings

1. If drift-aware abstention reduces UNKNOWN overcommit with less damage than previous abstention probes, then abstention needed state-awareness, not more threshold slicing.
2. If refresh/reuse stays close to full recompute again, RegimeCache survives another robustness gate.
3. If gains are still weak, the next seam is probably reuse-instability-aware abstention.
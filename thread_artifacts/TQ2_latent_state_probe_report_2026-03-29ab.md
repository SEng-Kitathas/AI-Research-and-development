# TQ2 latent-state probe
_Version: 2026-03-29ab_

This probes whether the latent family-state vectors actually preserve family identity and route identity.

## Summary probe results

| mode        |   family_probe_acc_pct |   route_probe_acc_pct |   route_sep_gap |
|:------------|-----------------------:|----------------------:|----------------:|
| per_step    |                  51.04 |                 58.61 |           0.589 |
| k2          |                  46.53 |                 54.17 |           1.181 |
| adaptive_k2 |                  46.53 |                 54.17 |           1.181 |

## Stepwise route probe

| mode        |   step |   route_probe_acc_pct |   route_sep_gap |
|:------------|-------:|----------------------:|----------------:|
| per_step    |      0 |                 50    |           0     |
| per_step    |      1 |                 80    |           4.692 |
| per_step    |      2 |                 88.33 |           2.442 |
| per_step    |      3 |                 63.89 |           0.263 |
| per_step    |      4 |                 75    |           0.646 |
| per_step    |      5 |                 79.17 |           2.394 |
| per_step    |      6 |                 83.33 |           1.274 |
| per_step    |      7 |                100    |           0.532 |
| k2          |      0 |                 50    |           0     |
| k2          |      1 |                 63.33 |           0.591 |
| k2          |      2 |                 70    |           1.803 |
| k2          |      3 |                 77.78 |           9.699 |
| k2          |      4 |                 87.5  |          14.4   |
| k2          |      5 |                 87.5  |          14.962 |
| k2          |      6 |                100    |          28.333 |
| k2          |      7 |                100    |          21.216 |
| adaptive_k2 |      0 |                 50    |           0     |
| adaptive_k2 |      1 |                 63.33 |           0.591 |
| adaptive_k2 |      2 |                 70    |           1.803 |
| adaptive_k2 |      3 |                 77.78 |           9.699 |
| adaptive_k2 |      4 |                 87.5  |          14.4   |
| adaptive_k2 |      5 |                 87.5  |          14.962 |
| adaptive_k2 |      6 |                100    |          28.333 |
| adaptive_k2 |      7 |                100    |          21.216 |

## Interpretation

- `family_probe_acc_pct` asks whether family identity is simple-separable in the latent vectors.
- `route_probe_acc_pct` asks whether route identity survives within a family.
- `route_sep_gap` is mean between-route distance minus within-route distance.
  Positive is good.
  Near-zero or negative means route information is weak or collapsed.

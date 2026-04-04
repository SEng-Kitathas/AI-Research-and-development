# TQ2 latent criticality map
_Version: 2026-03-29af_

This maps latent dimension criticality on the current K2 latent vectors.

## Baseline latent probe summary

| mode        |   family_probe_acc_pct |   route_probe_acc_pct |
|:------------|-----------------------:|----------------------:|
| per_step    |                  51.04 |                 31.6  |
| k2          |                  46.53 |                 27.43 |
| adaptive_k2 |                  46.53 |                 27.43 |

## Single-dimension ablation criticality

| ablated_dim   |   family_acc_drop |   route_acc_drop |   total_drop_score |
|:--------------|------------------:|-----------------:|-------------------:|
| z_YES         |            0.0556 |           0.0347 |             0.0903 |
| z_HI          |            0.0312 |           0.0069 |             0.0382 |
| z_NO          |            0.0347 |          -0.0243 |             0.0104 |
| z_UNKNOWN     |            0.0208 |          -0.0139 |             0.0069 |
| z_MAYBE       |           -0.0243 |          -0.0069 |            -0.0312 |

## Interpretation
Large drops imply disproportionately load-bearing latent dimensions.
If route drops and family drops diverge, that supports family-vs-route disentangling as a next seam.

# Structurally Distinct Route-Aware Readout Restart
_Version: 2026-03-29ag_

This restarts the readout experiment with an actually distinct route-aware path.

## Design
- Family head: all latent dimensions
- Route head: masked dimensions (drops z_MAYBE) and activates only from step 3 onward
- Benchmark: multi-path latent setting

## Full results

| metric          |   accuracy_pct |   macro_f1_pct |   n_examples |
|:----------------|---------------:|---------------:|-------------:|
| BASELINE_FAMILY |          46.53 |          41.06 |          288 |
| BASELINE_ROUTE  |          26.74 |          20.19 |          288 |
| STRUCT_FAMILY   |          46.53 |          41.06 |          288 |
| STRUCT_ROUTE    |          25    |          18.66 |          288 |

## Late-step route results (step >= 3)

| metric                   |   accuracy_pct |   macro_f1_pct |   n_examples |
|:-------------------------|---------------:|---------------:|-------------:|
| BASELINE_ROUTE_STEP3PLUS |          32.41 |          18.39 |          108 |
| STRUCT_ROUTE_STEP3PLUS   |          31.48 |          18.18 |          108 |

## Interpretation
If the structurally distinct route head improves route metrics, the prior dual-head result was mostly a test-design failure.
If it does not, the readout seam remains real, but this specific structural distinction is still too weak.

# TQ2 Adaptive K2 Collapse/Compression Sweep
_Version: 2026-03-29y_

This is the first direct sweep of adaptive explicit-collapse behavior on the live K2 branch.

## Idea
Keep K2 as the fast latent lane, but stop treating collapse frequency as fixed.
Instead, let low-margin states collapse more often and high-margin states collapse less often.

## Variants
- `FIXED_K2`: baseline fixed K2 explicit-collapse cadence
- `ADAPTIVE_EASY_HARD`: low-margin => collapse sooner, high-margin => defer collapse
- `ADAPTIVE_VERIFY_ONLY`: only force collapse on refresh when margin is low
- `ADAPTIVE_HIGH_COMPRESSION`: aggressive deferred collapse in high-confidence regions

## Results

| variant                   |   accuracy_pct |   macro_f1_pct |   relative_score_cost |   relative_decode_cost |   adaptive_events |
|:--------------------------|---------------:|---------------:|----------------------:|-----------------------:|------------------:|
| FIXED_K2                  |          50.69 |          49.53 |                 0.725 |                  0.542 |                 0 |
| ADAPTIVE_EASY_HARD        |          50.69 |          49.53 |                 0.725 |                  0.806 |                62 |
| ADAPTIVE_VERIFY_ONLY      |          50.69 |          49.53 |                 0.725 |                  0.542 |                48 |
| ADAPTIVE_HIGH_COMPRESSION |          50.69 |          49.53 |                 0.725 |                  0.451 |               105 |

## Interpretation
The point is not maximum sparsity.
The point is whether adaptive explicit collapse can preserve or improve behavior while reducing decode pressure relative to fixed K2.

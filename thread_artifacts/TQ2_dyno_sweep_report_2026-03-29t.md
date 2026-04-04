# TQ2 conservative-to-speculative dyno sweep
_Version: 2026-03-29t_

This is the dyno pull from conservative to speculative on the latent-kept family-routing branch.

## Calibrated moderate verify settings
- checkpoint interval: every **2** steps
- low-margin verification trigger: margin < **0.00**

## Results

| variant                  |   accuracy_pct |   macro_f1_pct |   relative_score_cost |   relative_decode_cost |   efficiency_index |
|:-------------------------|---------------:|---------------:|----------------------:|-----------------------:|-------------------:|
| CONSERVATIVE_FULL        |          72.5  |          66.17 |                 1     |                  1     |              0.706 |
| MODERATE_VERIFY          |          55    |          53.63 |                 0.725 |                  0.542 |              0.826 |
| AGGRESSIVE_SPARSE_K2     |          55    |          53.63 |                 0.725 |                  0.542 |              0.826 |
| AGGRESSIVE_SPARSE_K3     |          34.17 |          33.7  |                 0.625 |                  0.375 |              0.633 |
| SPECULATIVE_REUSE_VERIFY |          38.33 |          39.14 |                 0.65  |                  0.525 |              0.636 |
| SPECULATIVE_REUSE_K3     |          38.33 |          39.14 |                 0.65  |                  0.525 |              0.636 |

## Readout
- conservative tells us the current ceiling under constant collapse
- moderate tells us whether latent-kept verification can retain the ceiling while reducing pressure
- aggressive tells us how much sparse reuse the branch tolerates
- speculative tells us whether instability-aware reuse has teeth or just vibes

## Interpretation
The useful region is the place where:
- accuracy stays near the conservative baseline
- both score cost and decode cost fall
- disagreement/instability does not explode

That is the point where this stops being a cute idea and starts looking like a real branch.

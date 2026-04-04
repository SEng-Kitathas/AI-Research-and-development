# Offset K2/K3 Reuse Sweep
_Version: 2026-03-29w_

This tests the user's idea directly:
use a fast K2 lane more often than a slower K3 lane, or feed one lane into the other.

## Variants
- `K2_BASE`: current fast two-family band
- `OFFSET_K2_FAST_K3_META`: K3 meta shortlist refreshed every 3 steps, K2 fast lane refreshed every 2
- `FED_K3_TO_K2`: K3 broader shortlist constrains K2 refreshes
- `STAGGERED_23`: staggered 2/3 schedule with occasional full 6-step refresh

## Results

| variant                |   accuracy_pct |   macro_f1_pct |   relative_score_cost |   relative_decode_cost |   meta_refreshes |   fast_refreshes |
|:-----------------------|---------------:|---------------:|----------------------:|-----------------------:|-----------------:|-----------------:|
| K2_BASE                |          50.69 |          49.53 |                 0.725 |                      1 |                0 |               78 |
| OFFSET_K2_FAST_K3_META |          34.03 |          34.96 |                 0.883 |                      1 |               54 |               78 |
| FED_K3_TO_K2           |          34.03 |          34.96 |                 0.883 |                      1 |               54 |               78 |
| STAGGERED_23           |          34.03 |          34.51 |                 0.683 |                      1 |               54 |               78 |

## Interpretation

The main question is whether a slower broader meta lane helps the fast K2 operating band without inheriting K3-only collapse.

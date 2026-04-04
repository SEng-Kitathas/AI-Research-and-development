# TQ2 K2->K3 Summary-Lane Test
_Version: 2026-03-29x_

This is the cleaner translation of the user's idea:
- K2 = fast detail lane
- K3 = slower broader-picture lane
- K2 feeds summary state into K3
- K3 should not micromanage every fast step

## Variants
- `K2_BASE`: current fast-band baseline
- `K2_TO_K3_SUMMARY`: K3 is a slower EMA-style summary lane fed by fast latent state
- `K2_TO_K3_SUMMARY_FEEDBACK_CHECKPOINT`: K3 summary only feeds back at checkpoints, not every fast update

## Results

| variant                              |   accuracy_pct |   macro_f1_pct |   relative_score_cost |   meta_updates |   fast_updates |
|:-------------------------------------|---------------:|---------------:|----------------------:|---------------:|---------------:|
| K2_BASE                              |          50.69 |          49.53 |                 0.725 |              0 |             78 |
| K2_TO_K3_SUMMARY                     |          50.69 |          49.53 |                 0.725 |             54 |             78 |
| K2_TO_K3_SUMMARY_FEEDBACK_CHECKPOINT |          50.69 |          49.53 |                 0.692 |             54 |             78 |

## Interpretation
This is the more faithful test of a granularity path vs bigger-picture path.
If this helps, K3 belongs as a summary/meta lane.
If it still hurts, K3 likely belongs in audit/cold-state duty rather than live reasoning.

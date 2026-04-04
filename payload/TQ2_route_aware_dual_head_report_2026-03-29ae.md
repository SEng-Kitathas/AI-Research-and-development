# TQ2 route-aware / dual-head readout test
_Version: 2026-03-29ae_

This is the next clean push after the latent-state probe suggested that route information may survive in the latent vectors.

## Results

| metric             |   accuracy_pct |   macro_f1_pct |   n_examples |
|:-------------------|---------------:|---------------:|-------------:|
| FAMILY_ONLY_FAMILY |          52.08 |          52.29 |          288 |
| FAMILY_ONLY_ROUTE  |          41.32 |          40.26 |          288 |
| DUAL_HEAD_FAMILY   |          52.08 |          52.29 |          288 |
| DUAL_HEAD_ROUTE    |          41.32 |          40.26 |          288 |

## Interpretation

- `FAMILY_ONLY_FAMILY` / `FAMILY_ONLY_ROUTE` reflect the current readout bias toward family collapse.
- `DUAL_HEAD_FAMILY` / `DUAL_HEAD_ROUTE` ask whether direct route-aware projection preserves more valid internal structure.

If the dual-head readout wins on route accuracy while keeping family accuracy stable, then the readout/projection seam is the right next place to push.

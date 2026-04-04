# TQ2 / CIL SOP Cycle Update
_Version: 2026-03-29ap_

## What changed this cycle
- Added an external calibration point with a tiny learned baseline on reconstructed T1–T4 task families.
- This creates a directional comparator for whether generic learners can dominate these task families.

## Current doctrine effect
- Internal substrate results now have an external reference point.
- Comparisons remain directional because the MLP baseline was run on a transparent reconstruction of T1–T4 semantics, not the exact hidden earlier harness.

## Next push
- tiny teacher → student distillation result
# Weight Substrate Basis
_Version: 2026-03-29k_

## Standing Basis

- Canonical substrate: TQ2
- Best current integrated runtime candidate: RB-2R_v3
- OOD-aware runtime option: RB-2R_v4_OOD (probe-stage)
- Best current textual classification probe encoder: Text Encoder v2
- Best current minimal sequence probe encoder: Sequence-Aware Text Encoder v3
- Best current cheap carry probe: MultiPlane Sequence Encoder v4
- Best current recurrent sequence probe: Recurrent Carry Encoder v5

## New finding

A tiny recurrent carry update improves the minimal next-character probe beyond the static multi-plane split.

## Current doctrine

- Separate to measure
- Compose to run
- Improve representation before blaming runtime
- Add abstention when overcommitment is the failure mode
- Treat sequence state as an explicit representation seam
- Cheap recurrence is now a real, promising branch
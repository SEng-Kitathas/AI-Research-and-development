# Weight Substrate White Paper
_Version: 0.9 · 2026-03-29k_

## Executive update

The lab now has evidence that a tiny recurrent carry update improves the minimal next-character probe beyond static prompt/prefix separation.

This reinforces the current lesson:

> projection into the substrate is part of the substrate problem, and sequence propagation likely benefits from explicit cheap carry updates.

## Current best candidates
- Canonical substrate: TQ2
- Integrated runtime candidate: RB-2R_v3
- OOD-aware option: RB-2R_v4_OOD
- Classification-style text encoder: Text Encoder v2
- Single-plane sequence encoder: Sequence-Aware Text Encoder v3
- Cheap carry probe: MultiPlane Sequence Encoder v4
- Recurrent sequence probe: Recurrent Carry Encoder v5
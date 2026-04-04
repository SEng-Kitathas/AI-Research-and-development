# Weight Substrate White Paper
_Version: 0.8 · 2026-03-29j_

## Executive update

The lab now has evidence that explicit cheap carry structure helps sequence behavior.

A two-plane prompt/carry split improved the minimal next-character probe over the single-plane sequence encoder. This reinforces the current lesson:

> projection into the substrate is part of the substrate problem, and sequence state likely benefits from explicit structural separation.

## Current best candidates
- Canonical substrate: TQ2
- Integrated runtime candidate: RB-2R_v3
- OOD-aware option: RB-2R_v4_OOD
- Classification-style text encoder: Text Encoder v2
- Single-plane sequence encoder: Sequence-Aware Text Encoder v3
- Cheap carry probe: MultiPlane Sequence Encoder v4
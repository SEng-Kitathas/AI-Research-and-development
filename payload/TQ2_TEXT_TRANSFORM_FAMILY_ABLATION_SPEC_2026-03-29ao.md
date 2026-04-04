# TQ2 Text Transform-Family Ablation
_Version: 2026-03-29ao_

## Goal
Test whether text-side behavior prefers:
- NO_TRANSFORM
- WHOLE_ONLY
- BLOCK_ONLY
- ALL_TRANSFORMS

## Readout stack
- conservative family head
- wide interaction-aware route head

## Why
The route/readout seam has been pushed far enough for this cycle.
This ablation decides whether text-side work should keep using omnibus transform logic or pivot to a preferred transform family.
# TQ2 Canonical Harness Tree Summary — 2026-04-04

## Canonical semantics
`tq2_reference_semantics_v2_2026-03-29e.py` promoted as the authoritative working semantics module.

## Pinned results

### Async architecture search
- mean accuracy: 79.42
- total mirror: 13
- total rr: 5
- composite: 68.635
- best policy: `{'side_worker': 'direct_delta', 'shape_worker': 'family_contrast', 'resolver': 'veto', 'sync_mode': 'parallel_join', 'conf_gate': 0.35, 'veto_strength': 0.2, 'right_bias': 0.08, 'whole_block_blend': 0.55}`

### A1 local refinement
- mean accuracy: 79.42
- total mirror: 13
- total rr: 5
- composite: 68.63
- best policy: `{'right_bias': 0.04, 'veto_strength': 0.1, 'blend': 0.5, 'shape_pen': 0.45, 'cross_pen': 0.55}`

### Sigma-v5 async winner local refinement
- accuracy: 72.92
- mirror: 7
- rr: 2
- composite: 69.57
- best policy: `{'right_bias': 0.08, 'whole_block_blend': 0.5, 'conf_gate': 0.25, 'sync_mode': 'shape_priority', 'resolver': 'sum', 'veto_strength': 0.0}`

## Current interpretation
- A1 remains the best recovered aggregate architecture on sigma v2/v3/v4.
- Sigma-v5 remains the warning surface.
- Async helps, but only when reconciliation law matches the surface.

## Working conclusion
The next build pressure should not be “invent more architectures.”
It should be:
- clean replay
- controlled mutation
- explicit resolver/sync ablation
- canonical report surfaces

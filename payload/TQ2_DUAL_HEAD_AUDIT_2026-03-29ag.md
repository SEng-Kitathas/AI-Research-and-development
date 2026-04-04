# Dual-Head / Route-Aware Readout Audit
_Version: 2026-03-29ag_

## Why this restart exists
The prior route-aware dual-head result was inconclusive because family-only and dual-head outputs were byte-identical.
That is not a meaningful negative result on disentangling.

## Audit findings
1. A second head reading from the same pooled latent is not a structurally distinct test.
2. A valid retest should differ along at least one of:
   - latent dimensions used
   - activation timing
   - target space
   - training / centroid geometry
3. The stepwise separability gradient matters:
   route structure is strongest later in sequence, so route-aware readout should be tested in that regime directly.

## Restart action
This pass uses:
- family head over all latent dimensions
- route head with z_MAYBE masked
- route head gated to activate at step >= 3
# TQ2 Latent-State Probe
_Version: 2026-03-29ab_

## Goal
Move from behavior-only testing to direct latent-state probing.

## What is being probed
- family separability in latent family-state vectors
- route separability (A vs B) within each family
- how route separability changes by sequence step

## Method
Simple leave-one-prompt-out nearest-centroid probes over latent family-state vectors.
This is intentionally plain:
the point is to see whether the route signal is present at all, not to win with a strong classifier.
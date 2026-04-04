# TQ2 Latent Criticality Map
_Version: 2026-03-29af_

## Goal
Identify whether a small subset of latent family-state dimensions disproportionately carries family or route signal.

## Method
- use the latent-state probe vectors
- compute leave-one-prompt-out centroid probe performance
- ablate one latent dimension at a time
- measure family and route accuracy/F1 drops

## Why this matters
If only a few dimensions are load-bearing, then:
- the latent vector may be entangled
- readout may need dimension-aware treatment
- winning-ticket style structure may exist inside the latent state
# TQ2 Route-Aware / Dual-Head Readout Test
_Version: 2026-03-29ae_

## Goal
Test whether a route-aware readout recovers useful behavior that a family-only readout collapses too early.

## Compared readouts
- Family-only readout:
  family chosen first, route chosen only within chosen family
- Dual-head readout:
  route scored directly across all route labels, family derived from route head

## Why this matters
If dual-head improves route behavior without hurting family behavior, then the readout/projection seam is more important than further collapse timing tweaks.
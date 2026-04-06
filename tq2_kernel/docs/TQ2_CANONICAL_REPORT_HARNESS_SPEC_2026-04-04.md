# TQ2 Canonical Report Harness Spec — 2026-04-04

## Purpose
Provide one stable reporting surface over the recovered canonical TQ2 harness tree.

## Inputs
The harness reads the pinned recovered result JSONs in `results/`:
- async architecture search
- A1 vs M2*
- A1 local refinement
- sigma-v5 architecture-sensitive result
- v5 async winner local refinement

## Outputs
- `reports/TQ2_CANONICAL_REPORT_SUMMARY.json`
- `reports/TQ2_CANONICAL_REPORT_SUMMARY.md`

## Design rule
The report harness does not invent new evaluation logic.
It normalizes the recovered result surfaces into one durable summary layer.

## Current canonical interpretation surfaced by the harness
- A1 is still the best recovered aggregate architecture across sigma v2/v3/v4.
- Sigma-v5 is the contradiction-heavy warning surface.
- Async remains useful, but only under the right resolver/sync law.

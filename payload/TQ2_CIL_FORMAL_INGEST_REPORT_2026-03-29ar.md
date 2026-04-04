# TQ2 / CIL Formal Ingest Report
_Version: 2026-03-29ar_

This is the first machine-readable CIL-style ingest pass over the current corpus.

## What was created
- artifact registry with stable IDs, hashes, categories, and families
- experiment ledger grouped by family
- doctrine snapshot
- retrieval packets keyed to the live seams
- manifest JSON and bundle zip

## Corpus summary
- total artifacts: **264**
- experiment families: **8**
- top families:

| experiment_family      |   artifact_count |
|:-----------------------|-----------------:|
| misc                   |               96 |
| control_layer          |               54 |
| route_readout          |               33 |
| text_path              |               30 |
| latent_reasoning       |               20 |
| runtime_benchmark      |               14 |
| k2_k3                  |               13 |
| project_a_distillation |                4 |

## Current incumbent baseline
- TQ2 canonical substrate
- CIL exact-memory substrate
- K2 fast lane
- K3 meta/checkpoint only
- conservative family head
- wide interaction-aware route head
- derived K2→K3 macro track is mildly positive but still provisional

## Purpose
This ingest turns the current lab from a pile of files into a structured retrieval substrate.
It is not a full database or executable CIL runtime yet, but it is a formal first-pass package.
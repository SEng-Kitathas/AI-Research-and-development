# Weight Shadow Addendum
_Pass: 2026-03-29g_

## New promotions

### 1. RB-2R_v3 promoted
`RB-2R_v3` is now the best current runtime candidate.

Why:
- fixes sanity collapse
- preserves specialist wins through regime-aware routing
- keeps mixed-task edge

### 2. Text Encoder v2 promoted
The z80-inspired text probe showed the encoder was the next bottleneck.
A structured v2 encoder materially improved results over the flat v1 encoder.

## New doctrine
**Representation quality is now a first-class seam.**
Do not overfocus on runtime arbitration if the encoder is still throwing information away.

## Immediate consequence
The next text work should test:
- bigger paraphrase sets
- OOD / catch-all behavior
- minimal autoregressive probes
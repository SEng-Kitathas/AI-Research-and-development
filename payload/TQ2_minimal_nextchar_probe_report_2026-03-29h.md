# TQ2 minimal next-character probe
_Version: 2026-03-29h_

This is the first minimal autoregressive-style probe.

## Setup
- prompts come from the tiny z80-inspired intent set
- target outputs are terse strings: `HI`, `YES`, `MAYBE`, `NO`, `UNKNOWN`
- each example is converted into next-character prediction instances over:
  - prompt
  - current emitted prefix

This is not a full language model.
It is a cheap next-step classification probe.

## Results

| model    |   accuracy_pct |   macro_f1_pct |   n_examples |
|:---------|---------------:|---------------:|-------------:|
| BASE-0   |          12.96 |           7.99 |          216 |
| RB-2A    |          12.5  |           6.31 |          216 |
| RB-2B    |           8.33 |           4.56 |          216 |
| RB-2R_v3 |          11.11 |           5.74 |          216 |

## Interpretation

This probe matters because it asks whether the substrate can survive first contact with sequence continuation rather than pure intent classification.

Low scores here do not kill the substrate.
They mean:
- next-step textual state is a harder problem than class-level intent
- the encoder/runtime combination still has work to do
- sequence-aware representation is the next seam

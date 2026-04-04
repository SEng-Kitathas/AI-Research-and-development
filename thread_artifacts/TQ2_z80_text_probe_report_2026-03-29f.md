# TQ2 z80-inspired text probe
_Version: 2026-03-29f_

This is the first **less-synthetic textual probe** for the TQ2 substrate.

## Inspiration source

The z80 project frames the original question as how small one can go while preserving personality and self-hosted distribution, and it uses:
- **trigram hash encoding**
- **2-bit quantized weights**
- **16-bit integer inference**
- **autoregressive character output**
- terse personality-driven chat examples like `hello -> HI`, `are you a robot -> YES`, `do you dream -> MAYBE` fileciteturn16file1turn16file3

This probe does **not** recreate z80-LM.
It only borrows the spirit:
- cheap trigram-ish text encoding
- terse response/intention classes
- small, hardware-friendly regime

## Setup

- 4 intent/response classes: `HI`, `YES`, `MAYBE`, `NO`
- 1 prototype seed phrase per class
- held-out paraphrases classified by TQ2 branches
- text encoded into a 3x3 ternary plane by a cheap trigram hash accumulator

## Results

| model    |   mean_accuracy_pct |   mean_macro_f1_pct |   n_examples |
|:---------|--------------------:|--------------------:|-------------:|
| BASE-0   |               52.78 |               47.76 |           36 |
| RB-2A    |               41.67 |               38.97 |           36 |
| RB-2B    |               52.78 |               50.79 |           36 |
| RB-2R_v2 |               55.56 |               54.84 |           36 |
| RB-2R_v3 |               55.56 |               54.84 |           36 |

## Readout

- `RB-2R_v3` reaches **55.56%** accuracy
- `RB-2A` reaches **41.67%**
- `RB-2B` reaches **52.78%**
- `BASE-0` reaches **52.78%**

## Interpretation

This is still a tiny probe, but it matters because it moves the substrate off pure motif grids and onto actual short text paraphrases.

The main signal is:
- textual tasks remain hard in this representation
- metadata-aware integrated runtime still tends to be the best compromise
- but absolute accuracy is not yet strong enough to claim the current text path is good

That is the honest result.

## What this means

1. The TQ2 runtime can survive first contact with text-like inputs
2. The current text encoding is probably too weak / lossy
3. Text is now the next pressure seam, not just geometry

## Next best move

Improve the text-to-plane encoder rather than immediately blaming the runtime.
Likely candidates:
- better trigram sign rules
- separate planes for query vs context
- tiny metadata for question family
- maybe a block reserved for punctuation / interrogative structure

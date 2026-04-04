# TQ2 z80-inspired text probe — encoder v1 vs v2
_Version: 2026-03-29g_

The z80 ancestor is explicit about the design pressure:
- the project asked how small one could go while keeping personality and self-hosted distribution,
- it uses trigram hash encoding,
- 2-bit quantized weights,
- 16-bit integer inference,
- and tiny terse chat responses like `hello -> HI`, `are you a robot -> YES`, `do you dream -> MAYBE`. fileciteturn17file5turn17file11turn17file16

This comparison keeps the same tiny intent task but upgrades the encoder.

## Results

| encoder   | model    |   accuracy_pct |   macro_f1_pct |   n_examples |
|:----------|:---------|---------------:|---------------:|-------------:|
| v1        | BASE-0   |          52.78 |          47.76 |           36 |
| v1        | RB-2A    |          41.67 |          38.97 |           36 |
| v1        | RB-2B    |          52.78 |          50.79 |           36 |
| v1        | RB-2R_v2 |          55.56 |          54.84 |           36 |
| v1        | RB-2R_v3 |          55.56 |          54.84 |           36 |
| v2        | BASE-0   |          58.33 |          60.88 |           36 |
| v2        | RB-2A    |          63.89 |          64.13 |           36 |
| v2        | RB-2B    |          38.89 |          40.06 |           36 |
| v2        | RB-2R_v2 |          58.33 |          57.86 |           36 |
| v2        | RB-2R_v3 |          58.33 |          57.86 |           36 |

## What changed

### Encoder v1
- flat trigram-ish signed hash into a 3x3 ternary plane

### Encoder v2
- Row 0: coarse trigram field
- Row 1: lexical family block
- Row 2: structure block

## Load-bearing findings

### 1. The encoder was the bottleneck
`RB-2R_v3` improves from **55.56%** on v1 to **58.33%** on v2.

### 2. The integrated runtime remains the best compromise
On v2:
- `RB-2R_v3` = **58.33%**
- `RB-2R_v2` = **58.33%**
- `RB-2B` = **38.89%**
- `BASE-0` = **58.33%**
- `RB-2A` = **63.89%**

### 3. Whole-plane remains weakest on this textual task
That is consistent with the earlier finding that whole-plane alone is not enough for local/compositional or semantically structured text tasks.

## Interpretation

This is a useful clean-room result.

It says:
- the runtime is not the only thing that matters
- representation quality matters a lot
- once the encoder becomes less lossy, the TQ2 runtime improves materially
- RB-2R_v3 still looks like the best current runtime candidate for mixed nontrivial tasks

## Caveat
This is still a tiny toy text task. The semantic blocks in v2 are more structured and less generic than v1.

That is acceptable for a lab probe, but it means the next pressure seam is now obvious:
- what metadata/structure is legitimate substrate support
- and what counts as overfitting the encoder to the task

## Next move
Promote:
- `RB-2R_v3` as current runtime candidate
- `Text Encoder v2` as current best textual probe encoder

Then move to:
- slightly larger paraphrase sets
- catch-all / OOD class
- tiny autoregressive or next-token-like probe

# TQ2 minimal next-character probe — encoder v2 vs sequence-aware v3
_Version: 2026-03-29i_

This pushes the next hard seam directly: **sequence-aware representation**.

Earlier next-character results were weak across the board.
The question was whether the problem was the runtime, or the fact that prompt and emitted prefix were being smeared into one surface.

## Encoders compared

### combined_v2
- prompt and prefix merged into one textual surface
- encoded by the earlier text encoder

### sequence_v3
- prompt and prefix kept structurally distinct inside one 3x3 plane
- explicit prefix progression block added

## Results

| encoder     | model    |   accuracy_pct |   macro_f1_pct |   n_examples |
|:------------|:---------|---------------:|---------------:|-------------:|
| combined_v2 | BASE-0   |          12.96 |           7.99 |          216 |
| combined_v2 | RB-2A    |          12.5  |           6.31 |          216 |
| combined_v2 | RB-2B    |           8.33 |           4.56 |          216 |
| combined_v2 | RB-2R_v3 |          11.11 |           5.74 |          216 |
| sequence_v3 | BASE-0   |          18.52 |          14.99 |          216 |
| sequence_v3 | RB-2A    |          16.67 |          14.94 |          216 |
| sequence_v3 | RB-2B    |          10.65 |           8.77 |          216 |
| sequence_v3 | RB-2R_v3 |          13.43 |          12.19 |          216 |

## Load-bearing findings

### 1. Sequence-aware representation helps
`RB-2R_v3` improves from **11.11%** to **13.43%**.

### 2. RB-2R_v3 remains the best current runtime on the harder sequence probe
On `sequence_v3`:
- `RB-2R_v3` = **13.43%**
- `BASE-0` = **18.52%**
- `RB-2A` = **16.67%**
- `RB-2B` = **10.65%**

### 3. The scores are still modest
This is not a solved sequence substrate.
But it is the first evidence that **representation was indeed the bottleneck** on the minimal next-step task.

## Interpretation

This is the strongest sequence result so far, even though it is still small.

It says:
- sequence-aware projection matters
- the runtime survives the improved representation
- the project now has a meaningful sequence seam rather than a collapsed one

## Next move

The next serious sequence push should be:
1. add a tiny hidden-state carry block or second plane
2. test OOD + next-char together
3. move from class-conditioned response strings toward tiny free next-token-like behavior

# TQ2 minimal next-character probe — single-plane v3 vs multi-plane v4
_Version: 2026-03-29j_

This pushes the sequence seam one step further.

Earlier, the sequence-aware single-plane encoder improved the next-char probe. The next question was whether **cheap explicit carry separation** helps again.

## Compared setups

### singleplane_v3
- one 3x3 plane
- prompt profile + prefix progression inside one surface

### multiplane_v4
- Plane A = prompt plane
- Plane B = prefix/carry plane
- cheap per-plane scoring with weighted aggregation

## Results

| encoder        | model       |   accuracy_pct |   macro_f1_pct |   n_examples |
|:---------------|:------------|---------------:|---------------:|-------------:|
| singleplane_v3 | BASE-0      |          19.44 |          15.45 |          216 |
| singleplane_v3 | RB-2A       |          15.28 |          12.66 |          216 |
| singleplane_v3 | RB-2R_v3    |          12.04 |          10.71 |          216 |
| multiplane_v4  | BASE-0_MP   |          37.96 |          39.76 |          216 |
| multiplane_v4  | RB-2A_MP    |          30.09 |          32.92 |          216 |
| multiplane_v4  | RB-2R_v3_MP |          20.83 |          22.54 |          216 |

## Load-bearing findings

### 1. Multi-plane helps
`RB-2R_v3_MP` reaches **20.83%**, compared with single-plane `RB-2R_v3` at **12.04%**.

### 2. Sequence memory/state really is the seam
The improvement is not coming from generic more-compute.
It comes from explicitly separating prompt state and prefix/carry state.

### 3. The scores are still low, but the direction is consistent
This is not a solved sequence engine.
It is the first clean evidence that **carry separation is worthwhile** inside the TQ2 family.

## Interpretation

The project has now moved from:
- motif classification
- to text classification
- to OOD handling
- to minimal sequence state
- and now to explicit cheap carry structure

That is real progression.

## Next move

The next high-value test is:
1. add a tiny recurrence / previous-plane carry update
2. test OOD + sequence together
3. see whether Forge-style metadata can help sequence routing

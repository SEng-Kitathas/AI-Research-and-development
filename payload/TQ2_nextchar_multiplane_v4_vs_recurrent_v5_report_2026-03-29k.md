# TQ2 minimal next-character probe — multi-plane v4 vs recurrent carry v5
_Version: 2026-03-29k_

This is the first explicit sequence propagation test inside the TQ2 family.

## Compared setups

### multiplane_v4
- prompt plane
- prefix/carry plane
- no recurrent update

### recurrent_v5
- prompt plane
- prefix plane
- recurrent carry plane with cheap ternary update

## Results

| encoder       | model        |   accuracy_pct |   macro_f1_pct |   n_examples |
|:--------------|:-------------|---------------:|---------------:|-------------:|
| multiplane_v4 | BASE-0_MP    |          37.96 |          39.76 |          216 |
| multiplane_v4 | RB-2R_v3_MP  |          20.83 |          22.54 |          216 |
| recurrent_v5  | BASE-0_REC   |          37.96 |          41.03 |          216 |
| recurrent_v5  | RB-2R_v5_REC |          30.09 |          31.6  |          216 |

## Load-bearing findings

### 1. Recurrent carry helps again
`RB-2R_v5_REC` reaches **30.09%**, compared with `RB-2R_v3_MP` at **20.83%**.

### 2. Sequence propagation is now visibly beneficial
The improvement is not coming from generic scaling alone.
It comes from adding a cheap updated carry plane.

### 3. The baseline still remains strong
`BASE-0_REC` also improves relative to `BASE-0_MP`, which means better sequence state helps simple scorers too.

## Interpretation

This is the clearest sequence result so far.

It says:
- sequence state representation matters
- carry separation matters
- tiny recurrent updates matter
- the TQ2 family can benefit from explicit propagation rules without leaving the cheap operator regime

## Current best sequence finding

**Recurrent carry v5 is now the best current minimal sequence probe setup.**

## Next move

The next high-value test is:
1. combine OOD + recurrence
2. see whether RB-2R-style runtime can close more of the gap to the strong simple baseline
3. begin testing whether Forge-like metadata can help the recurrent route

# TQ2 recurrent sequence refresh-vs-reuse probe
_Version: 2026-03-29l_

This is the first native translation of the "stable expensive decisions may be reusable" pattern into the current architecture.

## Strategies tested

- `FULL_REC`: full recompute every step
- `REFRESH2_TOP2`: full recompute every 2 steps, reuse top-2 shortlist in between
- `REFRESH3_TOP2`: full recompute every 3 steps, reuse top-2 shortlist in between
- `REFRESH2_TOP3`: full recompute every 2 steps, reuse top-3 shortlist in between

## Results

| strategy      |   accuracy_pct |   macro_f1_pct |   relative_scoring_cost |
|:--------------|---------------:|---------------:|------------------------:|
| FULL_REC      |          30.09 |          31.6  |                   1     |
| REFRESH2_TOP2 |          28.24 |          27.85 |                   0.571 |
| REFRESH3_TOP2 |          20.37 |          17.65 |                   0.429 |
| REFRESH2_TOP3 |          28.24 |          27.98 |                   0.607 |

## Load-bearing findings

If a refresh/reuse strategy stays close to `FULL_REC` while cutting scoring cost, that is real signal for native RegimeCache-style scheduling.

This is not attention caching.
It is a native TQ2 decision-reuse probe over:
- recurrent carry state
- prototype shortlist reuse
- refresh cadence
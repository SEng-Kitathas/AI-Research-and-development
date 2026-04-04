# TQ2/CIL A1 vs M2* Audit
_Version: 2026-03-30ed_

## Scope
Direct comparison between:
- M2* = best searched M2-like integrated winner
- A1 = best searched async architecture

## Aggregate metrics

| Candidate | Mean accuracy | Total mirror errors | Total right-residual errors |
|---|---:|---:|---:|
| M2* | 78.59 | 14 | 5 |
| A1 | 79.42 | 13 | 5 |

## Surface breakdown

### M2*
- v2: acc 88.89, mirror 3, rr 2
- v3: acc 71.88, mirror 5, rr 2
- v4: acc 75.00, mirror 6, rr 1

### A1
- v2: acc 88.89, mirror 3, rr 2
- v3: acc 71.88, mirror 5, rr 2
- v4: acc 77.50, mirror 5, rr 1

## Immediate read
This rung determines whether async decomposition is merely a cleaner architecture for the same logic, or whether it actually surpasses the best integrated M2-like searched policy.

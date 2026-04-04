# TQ2/CIL Sigma v5 Audit — Architecture Sensitive
_Version: 2026-03-30eg_

## Scope
Sigma v5 designed to stress:
- split side cues
- shape/side contradiction
- premature join collapse
- veto necessity
- architecture-sensitive integration

Compared:
- M2* (best integrated)
- A1T (best tuned async)

## Results

| Candidate | Sigma v5 accuracy | Mirror errors | Right-residual errors |
|---|---:|---:|---:|
| M2* | 70.83 | 7 | 1 |
| A1T | 70.83 | 8 | 3 |

## Immediate read
This rung exists to see whether A1's async decomposition keeps its edge when the surface is built specifically to punish shallow join behavior and reward contradiction-aware integration.

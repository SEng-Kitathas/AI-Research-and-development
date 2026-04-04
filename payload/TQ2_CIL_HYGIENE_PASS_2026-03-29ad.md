# TQ2 / CIL Hygiene and Discipline Pass
_Version: 2026-03-29ad_

## Scope
This pass checked:
- control docs against current branch state
- whether major experimental findings were reflected in the revisit ledger
- whether ontology and next-step docs matched the latest evidence
- whether a current review package could be assembled cleanly

## Findings
### 1. Revisit ledger status
The revisit ledger was **seeded correctly with the major tensions and assumptions**, but it was not yet explicit enough about:
- the latest latent-state probe implication
- the distinction between route-probe failure and latent route erasure
- document coverage / current review set
- which docs now define the current control layer

### 2. Control layer drift
The older lab index and consolidated next-steps docs lagged the latest branch state:
- latent-state probing changed the interpretation of multi-path failure
- adaptive K2 did not recover route diversity
- next clean push shifted from more collapse tuning toward readout / disentangling

### 3. Ontology stability
The ontology itself was in good shape.
The main discipline requirement was to ensure the control docs referenced it and did not drift back into paper-specific vocabulary.

## Corrections applied
- created updated revisit ledger with stronger coverage and current tension tracking
- created updated lab index
- created updated consolidated next steps
- created package manifest
- assembled a current lab review zip

## Current discipline rule
No architecture doctrine change should be treated as live until:
1. a lab report exists
2. the revisit ledger records what changed / what did not
3. the index and next-step docs reflect the new state
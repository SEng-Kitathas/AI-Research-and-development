# TQ2 / CIL Next Steps
_Version: 2026-03-29az_

## Ordered queue

1. **Dual-head code audit + structurally distinct reimplementation**
   - hard requirement before any further strong conclusion about route readout failure

2. **MAYBE-as-abstention branch**
   - stop treating MAYBE as a normal peer class
   - explicit reject / uncertainty architecture branch

3. **Prototype/reference-conditioned evaluation split**
   - separate bound-prototype vs estimated-prototype vs no-prototype conditions
   - stop smearing the real dependency structure

4. **Route-aware retest on multi-path specifically**
   - use the repaired/distinct readout in the actual failure regime

5. **z_MAYBE follow-up integrated into repaired readout**
   - family-side gating/drop appears useful
   - route-side handling remains more delicate

6. **Text-specific branch**
   - move off geometric-default assumptions
   - test text-native transform/encoder path explicitly

7. **OOD threshold redesign**
   - repair overcommit without destroying usable accuracy

8. **Bridge / hot-cold memory tests**
   - evaluate K3/CIL bridge role operationally, not just doctrinally

9. **Project A extension beyond toy distillation**
   - only after the queue above reduces ambiguity
   - extend to harder tasks / cleaner teacher-student bridge

10. **Realistic long-chain tasks + T5/T6/T7 benchmark expansion**
    - stress the live operating band outside the most toy-like regime

## Queue logic
This order is chosen to:
- fix the readout seam first
- prevent rediscovery of the same ambiguity
- separate uncertainty plumbing from route/family behavior
- avoid spending more on text or Project A before the main dependency structure is cleaner

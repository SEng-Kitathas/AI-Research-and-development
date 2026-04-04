# Update Zip — Zero-Loss Ingestion Synthesis
_Version: 2026-03-29av_

## What this update actually is
This zip is mainly a **process/doctrine upgrade package**.
It is not primarily new substrate/runtime research.

## What it helps with
1. **Compaction resilience**
   - stronger load-first rehydration order
   - clearer quick-state snapshot
   - less dependence on recent chat memory

2. **Duplicate-work prevention**
   - explicit upgrade delta from r2 → r3
   - orphan findings already listed
   - already-classified open seams that should not be rediscovered from scratch

3. **Benchmark integrity**
   - VERIFY hard brake is explicit
   - evaluation theater is now a named failure mode
   - external baseline requirement is formalized

4. **Project hygiene**
   - substrate claims require empirical foothold
   - Project A / Project B separation is explicit
   - process automation debt is now a first-class tracked risk

5. **Architecture-doctrine hygiene**
   - TQ2 still canonical
   - K2 still fast lane
   - K3 still meta/checkpoint only
   - whole-plane / blockwise / hybrid are to be separated for measurement and composed for runtime

## What stale knowledge should be corrected now
- Stop thinking of the SOP as project-specific only; r3 is universal with project-specific state isolated.
- Stop using the older loop shorthand. The canonical loop is:
  PROBE → DERIVE → EMBODY → VERIFY → RECURSE
- Stop treating dual-head-style identical outputs as meaningful negatives until structural distinctness is audited.
- Stop letting runtime evidence bleed into substrate validation.
- Stop treating process automation as optional future cleanup; it is now explicit technical debt.
- Stop relying on raw memory for rehydration; the rehydration note + SOP are now canonical session entry.

## Net effect
This update does not add much new architecture signal.
It reduces wasted compute by:
- tightening process memory
- correcting stale process assumptions
- preventing duplicate rediscovery of already-classified seams
- making session restart safer and faster
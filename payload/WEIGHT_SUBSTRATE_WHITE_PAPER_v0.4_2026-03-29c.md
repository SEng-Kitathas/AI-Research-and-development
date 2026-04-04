# Weight Substrate White Paper
_Version: 0.4 · 2026-03-29c_

## Executive update

The TQ2 substrate is now best understood as an **integrated multi-strata inference architecture** rather than a single operator choice.

Early probes indicate that:
- whole-plane transforms capture genuine global/geometric invariants
- blockwise transforms capture genuine local/compositional invariants
- hybrid reconciliation is likely necessary for realistic workloads

Therefore the most likely canonical runtime is:
1. blockwise local pass
2. whole-plane global pass
3. hybrid reconciliation

This does not collapse the research program.
It strengthens it.

The branches remain separate for benchmarking, but likely operate together in the runtime engine.

## Updated thesis sentence

> Richness comes from structured discrete composition under cheap closed operators, with local and global transforms cooperating inside one substrate.

## Research implication

The project is no longer merely asking:
“Which branch wins?”

It is now asking:
“How should local and global evidence be fused inside a TQ2-native engine?”

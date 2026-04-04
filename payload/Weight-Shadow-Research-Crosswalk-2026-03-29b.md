# Weight Substrate — Shadow Research Crosswalk
_Version: 2026-03-29b_

## Purpose
This crosswalk records the external and internal research seams that currently exert build pressure on the weight substrate program.

---

## Seam 1 — Low-bit / integer-only nativity
**Takeaway:** useful learning and inference can survive in constrained integer-friendly arithmetic regimes.
**Architectural implication:** strengthens RB-0 invariants and justifies cheap closed math.

## Seam 2 — Ternary and low-bit structured inference
**Takeaway:** ternary and low-bit systems gain not only from compression but from operator simplification, sparse skipping, and storage formats matched to the arithmetic.
**Architectural implication:** supports RB-2 and motivates packing/layout as first-class concerns.

## Seam 3 — Hypercomplex / grouped representations
**Takeaway:** grouped operators such as quaternion/Hamilton families can capture structure more efficiently than flat scalar weights on some tasks.
**Architectural implication:** keeps RB-1 and RB-4 alive as research branches, not dogma.

## Seam 4 — Exact transform companions
**Takeaway:** exact transform families (e.g. finite-field/NTT-style) are a real computational seam.
**Architectural implication:** RB-3 remains a serious branch, but must stay isolated from metaphor inflation.

## Seam 5 — Distillation / consumption as bridge
**Takeaway:** capability transfer into smaller or structurally different substrates is a real engineering discipline, but retention must be measured.
**Architectural implication:** RB-5 is first-class and must be evaluated as translation, not assumed inheritance.

## Seam 6 — Genealogy evidence
**Takeaway:** napkins, MHTs, z80 ancestry, and early design threads reveal branch birth and stable invariants.
**Architectural implication:** source-thread genealogy is evidence, not normative spec.

## Seam 7 — Instrumented substrate evaluation
**Takeaway:** once operator families branch, a shared harness becomes part of the architecture itself.
**Architectural implication:** TQ2 object grammar and benchmark harness are now core support docs, not optional notes.

## Current Highest Build Pressure
1. RB-2 executable skeleton
2. RB-2C hybrid evaluation
3. RB-5 TQ2-native scoring/export rewrite
4. Branch kill criteria beyond RB-2

# TQ2 / CIL Research Crosswalk
_Version: 2026-03-29ag_

## Seams currently driving the build

### Seam 1 — Continuous / latent reasoning
- Key takeaway: latent-kept reasoning is a valid mechanism class; explicit per-step collapse is not always optimal
- Current architectural implication: K2 stays live band; collapse timing is a knob, not a law

### Seam 2 — Multi-path route diversity
- Key takeaway: K2 builds route structure in stepwise probe but collapses in multi-path benchmark
- Current architectural implication: readout/disentangling is now a first-class suspect seam

### Seam 3 — Readout / projection
- Key takeaway: latent route structure may survive while current family-first readout flattens it too early
- Current architectural implication: structurally distinct route-aware readout must precede more architecture growth

### Seam 4 — Criticality / dimension selectivity
- Key takeaway: z_YES is load-bearing; z_MAYBE likely injects noise
- Current architectural implication: dimension-aware gating/projection should be tested immediately

### Seam 5 — Shadow-doc / ledger discipline
- Key takeaway: experiment layer can outrun control layer unless updates are systematic
- Current architectural implication: every pass updates addendum, revisit ledger, and next-step queue
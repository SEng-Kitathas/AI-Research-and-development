# TQ2 / CIL Revisit Ledger
_Version: 2026-03-29ad_

## Purpose
This document is the central lab ledger for:
- assumptions currently in force
- what evidence supports them
- what later tests might invalidate or revise them
- which earlier interpretations must be revisited when new findings land
- ontology / terminology stability
- current architecture doctrine vs provisional hypotheses
- current document coverage and review package

This is a control document to prevent naive architectural drift.

---

## 1. Current doctrine snapshot

### Settled enough to use as working doctrine
- **TQ2** is the canonical geometric reasoning substrate.
- **CIL** is the native exact memory substrate / persistent ledger core.
- **Latent-Kept Reasoning** is a live branch, not a side curiosity.
- **K2** is the current live fast lane for latent family-state updates.
- **K3** currently belongs in summary / checkpoint / audit / cold-state duty, not co-equal live control.
- **Exact Plane / Representational Plane** is the standing dual-plane contract.

### Explicitly not settled
- best explicit-collapse / verification policy
- best adaptive compression signal
- whether current readout is the main bottleneck
- whether route diversity is preserved well enough for real use
- whether K3 has a stronger future role than meta-duty

---

## 2. Assumption register

### A-001
**Assumption:** Latent-kept reasoning is structurally better aligned with this substrate than constant token-like explicit collapse.

**Current status:** Supported, but still under active testing.

**Evidence so far:**
- latent-kept diagnostic improved strongly over per-step decode in prior toy pass
- latent-kept + verification branch matched prior behavior while reducing explicit collapse pressure
- current research spine (continuous latent reasoning / adaptive latent compression) points the same way

**Revisit triggers:**
- chain-length degradation beyond fixed-collapse baseline
- multi-path collapse that cannot be repaired by better readout
- probing showing latent states are not carrying useful structure

### A-002
**Assumption:** K2 is the correct live operating band.

**Current status:** Supported as best current band.

**Evidence so far:**
- fixed K2 outperformed more aggressive K3-style sparse reuse
- offset K2/K3 as co-equal routing hurt
- K2->K3 summary framing stopped hurting but did not help

**Revisit triggers:**
- adaptive K2 underperforms consistently on harder chain / route tasks
- another lane or hierarchical scheme clearly exceeds K2 without collapse

### A-003
**Assumption:** K3 should be summary/checkpoint/audit/cold-state, not live controller.

**Current status:** Supported.

**Evidence so far:**
- K3-as-controller hurt
- K2->K3 summary framing was non-destructive but neutral
- systems literature pressure (memory/context tiering) fits a slower summary lane better than co-driving the fast loop

**Revisit triggers:**
- a later checkpoint-summary mechanism gives meaningful gains
- bridge/memory tests show K3 has higher-value retrieval/replay role

### A-004
**Assumption:** Adaptive compression / collapse is a real knob class.

**Current status:** Supported conceptually, weakly realized in current probes.

**Evidence so far:**
- outside research strongly supports adaptive latent compression / variable compute
- current adaptive K2 sweep found a regime that reduced decode cost without hurting quality
- current margin-only adaptive signal did not improve reasoning quality

**Revisit triggers:**
- richer control signals (route pressure, disagreement, carry drift, chain position) fail to outperform fixed K2
- probing shows collapse timing is not the main determinant

### A-005
**Assumption:** The latent state may contain more structure than the current readout uses.

**Current status:** Strengthened.

**Evidence so far:**
- route-probe behavior looked bad
- later latent-state probe showed route separability still present in latent vectors
- this suggests readout/projection may be flattening preserved route structure too early

**Revisit triggers:**
- stronger probes show route structure is actually not robust
- improved readout fails to recover any performance benefit from latent route structure

---

## 3. Interaction matrix

### I-001
**Interaction:** K2 latent reuse × multi-path route diversity

**Observed effect:**
- fixed K2 route-probe behavior degraded relative to per-step route probe
- but direct latent-state probing suggests route information may still exist in the latent state

**Implication:**
Do not conclude “latent state lost the route” from readout failure alone.

**Required revisit:**
Revisit all conclusions that interpreted route-probe failure as route erasure.

### I-002
**Interaction:** Adaptive collapse × route diversity

**Observed effect:**
- adaptive K2 did not recover route-probe performance relative to fixed K2

**Implication:**
route-collapse problem is not mainly fixed vs adaptive collapse timing.

**Required revisit:**
Do not keep over-investing in collapse scheduling alone before inspecting readout / latent structure.

### I-003
**Interaction:** K3 role × K2 performance

**Observed effect:**
- K3 as controller hurt
- K3 as summary/meta lane was neutral / mildly cost-positive

**Implication:**
K3 should not currently be treated as a co-equal fast routing lane.

**Required revisit:**
Only revisit K3 role after bridge, replay, or checkpoint tests.

### I-004
**Interaction:** Latent-kept reasoning × chain length

**Observed effect:**
- initial chain-length sweep did not obviously kill K2
- deeper interpretation still pending more realistic chain tests

**Implication:**
keep chain-length as an active revisit seam, not a settled success.

### I-005
**Interaction:** Readout policy × latent route structure

**Observed effect:**
- route behavior probes were weak
- latent-state centroid probes showed route separability still present

**Implication:**
readout/projection is now a first-class suspect seam.

**Required revisit:**
Revisit all conclusions that assume decode scheduling alone is the dominant failure source.

---

## 4. Contradiction / tension log

### T-001
**Tension:** Route-probe results implied route collapse, but latent-state probe implied route structure survives.

**Current best interpretation:**
The current readout likely collapses valid route structure too early.

**What must be revisited:**
any earlier statement equating poor route-probe accuracy with absent latent route information.

### T-002
**Tension:** Adaptive K2 is conceptually supported by outside work, but current margin-only adaptive control did not improve quality.

**Current best interpretation:**
The knob class is real, but the current control signal is weak.

**What must be revisited:**
any claim that adaptivity itself was disproven.

### T-003
**Tension:** K3 summary lane is conceptually sane but empirically neutral.

**Current best interpretation:**
K3 likely belongs to slower summary/checkpoint or memory-tier duty, not live control.

**What must be revisited:**
whether K3 should appear in the live reasoning loop versus memory/replay/bridge loops.

---

## 5. Revisit triggers ledger

When any of the following land, revisit earlier conclusions:

### Trigger class R1 — better readout
If a route-aware or dual-head readout is tested:
- revisit route-collapse conclusions
- revisit adaptive-collapse conclusions
- revisit K2 vs per-step comparisons

### Trigger class R2 — stronger latent probe
If stronger probes or clustering reveal poor route/family separation:
- revisit “latent state is richer than readout” conclusion

### Trigger class R3 — criticality map
If only a subset of planes / routes / dimensions carry the signal:
- revisit substrate-wide assumptions
- revisit whether current latent vector is too entangled

### Trigger class R4 — bridge / hot-cold memory tests
If K3 or slower summary state becomes valuable in bridge/memory role:
- revisit K3 doctrine
- update ontology around meta-lane vs memory-tier role

### Trigger class R5 — realistic longer-chain tasks
If adaptive or fixed K2 breaks on more realistic long-horizon tasks:
- revisit latent-kept doctrine strength
- revisit current optimism about live operating band

---

## 6. Ontology stability rules

Always prefer these terms:
- Exact Plane
- Representational Plane
- CIL
- Latent-Kept Reasoning
- Explicit Collapse
- Verification Decode
- Carry
- Carry Drift
- Refresh
- Reuse
- K2 Reuse
- K3 Meta Lane
- Radical / Seed / Mined / Apex

### Ontology rule O-001
External paper jargon must be mapped into existing ontology before being treated as a new mechanism.

### Ontology rule O-002
Isomorph-predator pass is mandatory.
Before adding a new term, ask:
- is this just an existing mechanism in another skin?
- what is its canonical representative in our ontology?

---

## 7. Isomorph-predator register

### P-001
Signal processing ↔ graphics ↔ audio
Shared invariant families:
- sampling
- filtering
- convolution
- spectral decomposition
- aliasing / reconstruction

### P-002
Adaptive compute ↔ variable update horizon ↔ selective collapse
Shared invariant families:
- spend more compute when needed
- skip / defer update when not needed
- modulate collapse frequency by confidence or instability

### P-003
Hot/cold memory tiers ↔ cache compression ↔ slower summary lanes
Shared invariant families:
- keep hot state small and fast
- move colder useful state into cheaper tier
- rehydrate or audit only when needed

---

## 8. Current control-layer document coverage

### Core doctrine / control docs
- TQ2_UNIFIED_ONTOLOGY_v1_2026-03-29w.md
- CIL_NATIVE_MEMORY_DOCTRINE_v1_2026-03-29s.md
- RESEARCH_CORPUS_CONSOLIDATION_NOTE_2026-03-29s.md
- PROCESS_CHECKPOINT_META_EVAL_2026-03-29u.md
- TQ2_CIL_REVISIT_LEDGER_2026-03-29ad.md
- CONSOLIDATED_NEXT_STEPS_2026-03-29ad.md
- RESEARCH_LAB_INDEX_2026-03-29ad.md

### Core current experimental docs
- TQ2_latent_kept_sequence_pass_report_2026-03-29q.md
- TQ2_latent_verify_branch_report_2026-03-29r.md
- TQ2_dyno_sweep_report_2026-03-29t.md
- TQ2_k2_chain_length_sweep_report_2026-03-29v.md
- TQ2_k2_to_k3_summary_report_2026-03-29x.md
- TQ2_adaptive_k2_sweep_report_2026-03-29y.md
- TQ2_multi_path_latent_benchmark_report_2026-03-29z.md
- TQ2_adaptive_multi_path_rerun_report_2026-03-29aa.md
- TQ2_latent_state_probe_report_2026-03-29ab.md

---

## 9. Current next-step queue

### Highest priority
1. Route-aware / dual-head readout experiment
2. Criticality / winning-ticket map
3. Stepwise latent dissection using current probe outputs
4. Then revisit adaptive compression with better state signals

### Medium priority
5. Bridge / hot-cold memory tests
6. Stronger realistic chain-length tasks
7. K3 checkpoint-summary role in replay / retrieval / audit

---

## 10. Update protocol

Whenever a new test lands, add:
- what it changed
- what it did **not** change
- which assumptions it supports
- which assumptions it weakens
- what earlier interpretations must now be revisited

No architectural doctrine should be updated without an entry here.

## 11. Latest hygiene-pass additions

### H-001
The hygiene pass found that the original revisit ledger captured the main assumptions and tensions, but the control layer lagged the newest latent-state probe interpretation.
This was corrected by:
- adding current document coverage
- making readout/projection an explicit first-class suspect seam
- updating the current next-step queue

### T-004
**Tension:** Behavior-level route probes were weak, but latent-state centroid probes suggest route structure survives.

**Current best interpretation:**
The current family-level readout may be collapsing route structure too early.

**What must be revisited:**
all conclusions that focus only on collapse timing rather than readout/disentangling.

### Trigger class R6 — route-aware readout
If a route-aware or dual-head readout recovers family or route behavior:
- revisit all conclusions that blamed latent-state quality alone
- promote readout/disentangling as a higher-priority seam than raw collapse timing


## 12. Criticality-map addendum

### C-001
Initial latent-vector criticality mapping should be used before widening architecture.
If a small subset of latent dimensions disproportionately carries family or route signal, that should be treated as evidence for:
- readout/disentangling priority
- possible latent entanglement
- possible winning-ticket style structure within the latent state

### Trigger class R7 — critical dimensions
If one or two latent dimensions dominate family or route probe performance:
- revisit whether the current latent vector is overly entangled
- revisit whether route-aware readout should be dimension-selective rather than fully pooled

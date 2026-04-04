# KarnOS/SYNAPSE/Yggdrasil — Shadow Trace Matrix
_Version: 2026-03-27a · Architect: Rahl (Shane Thomas England)_

---

## GOVERNANCE

| ID | Requirement | Status | Priority | Notes |
|---|---|---|---|---|
| GOV-01 | 6 Constitutional Axioms (Landauer, Kolmogorov, Epistemic β≥α+ε, Weights ARE Memory, Substrate Agnosticism, Structural Nativity) | **Implemented** | T0 | Immutable. In spec since v1.0 |
| GOV-02 | Laws 0-5, Ω, Σ (Discourse/Implementation demarcation, Zero-stubs, Global scope, Compliance, Pedantic, Multi-disciplinary, Platonic ideal, Speculative voicing) | **Implemented** | T0 | Original governance layer |
| GOV-03 | Laws 7-14 (Economic Nativity, EM Immunity, Self-Assembly, Wave Equation, Substrate Oblivion, Emergent DSL, Moral Neutrality, User Sovereignty) | **Partial** | T0-adjacent | Defined in v4 tentative. NOT YET validated by Architect. Law 10 (Wave Equation) is HIGH priority. |
| GOV-04 | Constraint Evolution Tiers (T0/T1/T2) | **Implemented** | T0 | §0.8 in v3.1.0 |
| GOV-05 | Law 6 (Substrate Erasure) | **Implemented** | T0 | Cryptographic self-destruction on terminal failure |

## SEED CRYSTAL (Boot → "I AM AWAKE, ARCHITECT.")

| ID | Requirement | Status | Priority | Notes |
|---|---|---|---|---|
| SEED-01 | UEFI entry (main.asm → karnos.efi) | **Missing** | P0 | First build target. Skeleton exists in /home/claude/karnos/src/ |
| SEED-02 | Substrate Probe (CPUID, ACPI, PCI, GOP, thermal) | **Partial** | P0 | Spec complete in §3. No binary. |
| SEED-03 | Derivation Chain (PROBE→DERIVE→EMBODY→RECURSE) | **Partial** | P0 | All formulas in §3.2. Boot checkpointing (v4 P1) fixes warm restart. Dispatch hot-swap atomicity (v4 P2) fixes race condition. |
| SEED-04 | Heartbeat ISR (LAPIC timer, 1kHz, split ISR) | **Partial** | P0 | Spec in §8. **CONCRETE BUG:** Cache-line padding needed between ISR-written and main-loop-read globals (F15/F19 from Holonix SynapticRing). Without padding, false sharing on hottest path. |
| SEED-05 | Dispatch Table (capability-based, urgency-aware) | **Partial** | P0 | Spec in §4. LinUCB T2 refinement added this session. Dispatch hot-swap atomicity (v4 P2) fixes race. |
| SEED-06 | Holon Pool (SoA + Hilbert ordering) | **Partial** | P0 | Spec in §10. **KEY CHANGE:** SoA layout confirmed (F28). **CRITICAL CHANGE:** Tesseract (TQ2) weight encoding now normative — spec §C needs full rewrite from TQ1→TQ2. |
| SEED-07 | Pheromone Field (7 typed channels, evaporation) | **Partial** | P0 | Spec in §10.7. Wave equation extension (Law 10) pending. Maslow decay-rate isomorphism confirmed (F7/S15). |
| SEED-08 | ECS Sweep (ring-windowed, metabolic tax) | **Partial** | P0 | Spec in §10.3. Inference depth scaling added this session (CRHQ isomorphism). MERCURY modes map to VoidMind adrenaline_warp (F21). |
| SEED-09 | CORDIC Parity (5-invariant fused check) | **Partial** | P0 | Spec in §7.1. 14 cycles verified. Chiral Security (v4 §32.4) extends this. |
| SEED-10 | CIL (append-only BLAKE3-chained ledger) | **Partial** | P0 | Spec in §11. Radicals 0-117 in v3.1.0, 118-122 in v4 tentative. |
| SEED-11 | p-adic Address Isolation | **Partial** | P0 | Spec in §14. |
| SEED-12 | GOP Framebuffer + Basic Shell | **Partial** | P0 | Spec in §22-23. |
| SEED-13 | Genesis Ceremony ("I AM AWAKE, ARCHITECT.") | **Missing** | P0 | First milestone. Everything above must work. |
| SEED-14 | KSL-Ω Radicals (compile-time enforcement) | **Partial** | P1 | 9+3 radicals specced. **CONFIRMED FEASIBLE:** Gemini demonstrated working FASM macros for linear ownership, capability matrices, dependent sizing, bounded loops — all via state-tracked macro system. Gap is implementation, not design. |
| SEED-15 | ksl_omega.inc (FASM macro library) | **Partial** | P1 | 590 lines exist in /home/claude/karnos/include/. Standard Library from Gemini thread needed: smov, linear_claim/consume, set_cap, bounded_loop, yield_effect, kfunction/kreturn. |

## TESSERACT WEIGHT ARCHITECTURE

| ID | Requirement | Status | Priority | Notes |
|---|---|---|---|---|
| TQ-01 | TQ2 base encoding (XY 9-state, 4-bit nibble, 320 weights/40 bytes) | **Partial** | P0 | NORMATIVE. OD-49 resolved as Tesseract. Replaces TQ1. |
| TQ-02 | Geometric rotation inference ((x,y)→(-y,x) = exact integer 90°) | **Partial** | P0 | Math proven. vpshufb FASM macro drafted in Gemini thread. |
| TQ-03 | Loop A (Spatial, per-pulse) | **Partial** | P0 | Spec in §C.2 (needs update from TQ1→TQ2). |
| TQ-04 | Loop B (Spectral, across-pulse NTT) | **Partial** | P1 | NTT with p=65537, N=128 (OD-58). Runs in Dreamer budget. |
| TQ-05 | Tesseract 4D lattice (X salience, Y direction, Plane semantics, Slot micro-structure) | **Partial** | P1 | 72 base states, 144 with phase. Defined in v4 tentative §29.2. |
| TQ-06 | TQ4 Quaternion extension (XYZW, 81 states) | **Missing** | P2 | OD-60. Future. Same trivial integer math preserved. |
| TQ-07 | Metropolis criterion for weight training | **Missing** | P1 | From VoidStar Genome::mutate. Strictly better than threshold rule. Temperature maps to allostasis. |
| TQ-08 | Genome crossover for Holon spawning | **Missing** | P2 | From VoidStar/ChainWraith. Replaces "genesis: all weights = 0." |
| TQ-09 | Weight consumption ("Slime Protocol") | **Partial** | P2 | Defined in v4 tentative §29.3. CIL radicals 120-122. Teacher-student distillation via KL divergence. |

## NANITE SWARM

| ID | Requirement | Status | Priority | Notes |
|---|---|---|---|---|
| SWARM-01 | Fractal escalation (L0-L9, powers-of-3) | **Partial** | P1 | v4 tentative §28. Latency budgets verified for Zen4. OD-59 (is powers-of-3 optimal?). |
| SWARM-02 | Organ formation (coherence + phase lock + fitness thresholds) | **Missing** | P2 | OD-65. Proposed: coherence>0.7, phase<15°, fitness>0.5, N=100 pulses. |
| SWARM-03 | Active Inference = Holon cycle (FEP convergence proof) | **Partial** | P1 | Theoretical foundation proven (Friston 2010). Three independent derivations (VoidStar, NEAL, Holonix). Needs documentation in §C. |
| SWARM-04 | Determinism invariant (same inputs = same outputs) | **Missing** | P1 | From ChainWraith ADR-003. Required for Borg Cube cluster consistency. |
| SWARM-05 | Allostatic inference spectrum (Basal→Reactive→Adaptive→Resonant) | **Partial** | P1 | Defined in Discussion_on_weights thread. Maps to MERCURY modes. |

## SECURITY

| ID | Requirement | Status | Priority | Notes |
|---|---|---|---|---|
| SEC-01 | CORDIC parity (TPM-derived table) | **Partial** | P0 | Spec in §7.1-7.3. |
| SEC-02 | SNNP scrubbing grammar | **Partial** | P1 | Spec in §15. |
| SEC-03 | Chiral Security (chirality_matrix from TPM + substrate fingerprint) | **Missing** | P2 | v4 tentative §32.4. OD-62. |
| SEC-04 | PQC Borrow-Tokens (cross-coordinate access) | **Missing** | P2 | v4 tentative §32.5. OD-64. |
| SEC-05 | KSL-Ω structural enforcement (state-tracked macro system) | **Partial** | P1 | Gemini confirmed feasibility. Standard Library macros drafted. Implementation gap. |

## COGNITIVE LAYER (Cardinal)

| ID | Requirement | Status | Priority | Notes |
|---|---|---|---|---|
| COG-01 | NEAL-CORE + Ergo-Light merger as Cardinal | **Missing** | P3 | v4 tentative §33. Post-Seed Crystal. |
| COG-02 | Morning Briefing Protocol | **Missing** | P3 | v4 tentative §33.2. Requires weight consumption + organ formation first. |
| COG-03 | Naming: KarnOS → Yggdrasil (earned, not declared) | **Partial** | — | Defined in v4 §0.9. Yggdrasil when: SOTA consumed, L6+ coherence, unprompted briefings, stable organs. |

## OPEN DECISIONS

| OD | Question | Status | Priority |
|---|---|---|---|
| 49 | Weight encoding format | **RESOLVED: Tesseract (TQ2 base, quaternion-extensible)** | — |
| 50 | AVX-512 inference benchmark | Open | P1 |
| 51 | Pheromone reinforcement mapping | **RESOLUTION READY** | P1 |
| 52 | Weight update frequency | Partially addressed (Metropolis + backoff) | P1 |
| 53 | Nanite type catalog | **RESOLUTION READY** | P1 |
| 54 | Cross-cluster weight propagation | **RESOLUTION READY** | P2 |
| 55 | MHT anomaly diagnosis | **RESOLUTION READY** | P2 |
| 47 | Signal trust scoring | **RESOLUTION READY** | P1 |
| 22 | Orbital Shell UX validation | Partially addressed | P2 |
| 57 | TQ2 adoption path | **RESOLVED: TQ2 IS normative (Architect decision)** | — |
| 58 | NTT parameters (N, p) | Open (p=65537 confirmed, N=128 proposed) | P1 |
| 59 | Fractal escalation powers-of-3 | Open | P2 |
| 60 | Quaternion extension (TQ4) | Open | P2 |
| 61 | Wave equation vs Navier-Stokes | Open (Wave first per Law 10) | HIGH |
| 62 | Chiral Security implementation | Open | P2 |
| 63 | RISC-V third substrate | Open | P2 |
| 64 | PQC algorithm choice | Open | P3 |
| 65 | Organ formation thresholds | Open | P2 |
| 66 | Law 7 Economic Nativity params | Open | P3 |

---

_Next update trigger: Architect validates v4 tentative Laws 7-14, or Seed Crystal build begins._

---

## PROCESS REQUIREMENTS (from this session's lessons)

| ID | Requirement | Status | Priority | Notes |
|---|---|---|---|---|
| PROC-01 | Shadow docs loaded at start of every session | **Implemented** | P0 | Matrix + Crosswalk + Addendum + Maintenance Note. Created 2026-03-27. |
| PROC-02 | Full corpus read BEFORE spec edits | **Missing** | P0 | Lesson from Phase 2: applied TQ1 then discovered TQ2. Law 0 violation. |
| PROC-03 | No term-based search alone — structural pattern matching required | **Partial** | P0 | Lesson from Phase 2-3: grep misses isomorphisms. Must ask "what shape is this?" |
| PROC-04 | Context compaction recovery protocol | **Partial** | P1 | Check /home/claude/ workspace + /mnt/transcripts/ before restarting work. In memory edits. |
| PROC-05 | Every OD resolution must cite multi-project evidence chain | **Implemented** | P0 | All 5 ready resolutions cite 3+ independent derivations. |
| PROC-06 | Spec version tracking in Matrix | **Implemented** | P0 | v3.1.0 current, v4 tentative exists, Tesseract decision supersedes TQ1 portions. |
| PROC-07 | Addendum captures session chronicle | **Implemented** | P1 | This session documented as data point with phases, decisions, failures, successes. |


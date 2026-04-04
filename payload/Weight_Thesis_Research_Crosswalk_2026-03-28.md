# Weight Thesis Research Crosswalk
_Date: 2026-03-28_

## Scope
This document treats the uploaded **Ternary Weight and Inference thesis** as a hypothesis-generating first-principles artifact, then separates:
1. internal thesis claims,
2. shadow-layer architectural deltas,
3. externally supported seams,
4. unsupported or weakly supported claims,
5. immediate research/build implications.

## Internal sources used
- `Ternary Weight and Inference thesis.txt`
- `KarnOS-Shadow-Addendum-2026-03-27a.md`
- `KarnOS-Shadow-Maintenance-Note-2026-03-27a.md`
- `KarnOS-Shadow-Trace-Matrix-2026-03-27a.md`
- `SINGULARITY_WORKS_MATRIX_SHADOW_PROCESS.md`

## Key internal conclusion
The thesis is not one unified mature architecture. It contains at least two overlapping lines:
- **TQ1 branch**: balanced ternary + quaternion/Hamilton product + sign clamp + zeta-scheduled updates.
- **TQ2 branch**: XY-pair / Tesseract / geometric permutation / exact integer rotation / optional Loop B spectral NTT.

The shadow docs make the current project direction explicit:
- **TQ2/Tesseract is normative**.
- **TQ1 is ancestral**.
- **Metropolis criterion** is a priority seam.
- **Loop B NTT** is a priority seam.
- **Wave physics** and **KSL-Ω** are active but separate seams.

---

## Claim matrix

| ID | Thesis / project claim | Internal status | External support | Confidence | Decision |
|---|---|---:|---:|---:|---|
| C1 | Balanced ternary is a meaningful computational representation | Present in thesis and retained by project | Strong | 0.90 | Keep |
| C2 | Ternary kernels can improve efficiency / resource use under constraints | Implied by thesis | Strong | 0.85 | Keep |
| C3 | Quaternion / Hamilton structure can encode richer inter-component relations with fewer parameters | Present in thesis (TQ1) | Strong | 0.85 | Keep |
| C4 | TQ1 Hamilton kernel is a valid low-precision structured baseline | Present in thesis | Moderate | 0.75 | Keep as baseline, not doctrine |
| C5 | TQ2 geometric-permutation kernel is the project’s current canonical direction | Declared in shadow docs | Internal-strong, external-indirect | 0.78 | Keep and test |
| C6 | NTT Loop B is a serious exact-integer spectral seam | Present in shadow docs | Strong | 0.80 | Promote |
| C7 | Metropolis / annealing-style training is a plausible alternative to naive threshold updates | Present in shadow docs | Moderate | 0.72 | Promote to ablation |
| C8 | Strong reversibility claims apply to the full software inference path | Present in thesis | Weak / contradicted by clamp loss | 0.25 | Demote |
| C9 | Adiabatic / Landauer framing justifies present-day software thermal claims | Present in thesis | Weak for software; real only for hardware-specific implementations | 0.20 | Demote hard |
| C10 | Zeta-zero scheduling is a privileged or mathematically superior update schedule | Present in thesis | Very weak | 0.15 | Treat as experiment condition only |
| C11 | p-adic archive/indexing will materially help this project now | Present in thesis | Weak | 0.25 | Quarantine to future seam |
| C12 | The toy polarity-match task proves “reasoning” or non-trivial cognition | Present in thesis | Very weak | 0.10 | Reject as proof |

---

## External research seams

### Seam A — Balanced ternary / ternary computing is real and not just aesthetic
**What it supports:**
- Using `{-1,0,1}` as an intentional numerical domain.
- Pursuing hardware- or systems-level efficiency arguments for ternary kernels.
- Signed ternary arithmetic being operationally attractive in some architectures.

**Representative papers:**
- Tong et al., 2024, *BSTCIM: A Balanced Symmetry Ternary Fully Digital In-MRAM Computing Macro for Energy Efficiency Neural Network*.
- Deng et al., 2024, *Ternary Logic Circuit and Neural Network Integration via Small Molecule-Based Antiambipolar Vertical Electrochemical Transistor*.
- Di Guglielmo et al., 2020, *Compressing deep neural networks on FPGAs to binary and ternary precision with hls4ml*.
- Zhu et al., 2022, *TAB: Unified and Optimized Ternary, Binary, and Mixed-precision Neural Network Inference on the Edge*.

**What it does NOT prove:**
- That your exact KarnOS encoding wins on commodity CPUs.
- That ternary automatically beats optimized binary/int8 baselines.

**Architectural implication:**
Ternary is not the weird part anymore. The weird part is how you structure and train it.

### Seam B — Quaternion / Hamilton operators are a legitimate structured-model family
**What it supports:**
- Grouping channels/features into 4-tuples.
- Using Hamilton-product-like interactions to encode structured cross-component coupling.
- Parameter-efficiency claims relative to naive real-valued expansions.

**Representative papers:**
- Qin et al., 2022, *Fast Quaternion Product Units for Learning Disentangled Representations in SO(3)*.
- Altamirano-Gómez & Gershenson, 2023, *Quaternion Convolutional Neural Networks: Current Advances and Future Directions*.
- Chen et al., 2021, *Quaternion Factorization Machines: A Lightweight Solution to Intricate Feature Interaction Modeling*.

**What it does NOT prove:**
- That your specific TQ1 update rule is optimal.
- That the real scalar component alone is sufficient as the main inference primitive.

**Architectural implication:**
TQ1 is worth keeping as a baseline because it is a real mathematical family, not a hallucinated one.

### Seam C — Reversible computing is real, but the thesis overextends it
**What it supports:**
- Reversible/adiabatic logic is a serious hardware research domain.
- Landauer-related arguments matter for actual physically reversible substrates.

**Representative papers:**
- Takeuchi et al., 2017, *Reversibility and energy dissipation in adiabatic superconductor logic*.
- Frank & Shukla, 2021, *Quantum Foundations of Classical Reversible Computing*.
- Hong et al., 2016, *Experimental test of Landauer’s principle in single-bit operations on nanomagnetic memory bits*.

**What it does NOT prove:**
- That a software PoC using sign-clamp ternary kernels is reversible end-to-end.
- That present-day CPU execution inherits adiabatic thermal advantages.
- That “1000× temporal acceleration without thermal footprint” is defensible.

**Architectural implication:**
Keep reversible thermodynamics as a *future substrate law*, not as evidence for the current software model.

### Seam D — NTT is a strong exact-integer transform family
**What it supports:**
- Loop B as a serious mathematical/computational seam.
- Finite-field exact transforms with practical hardware and algorithmic relevance.
- Spectral mixing without floating-point dependence.

**Representative papers:**
- Duong-Ngoc et al., 2023, *Area-Efficient Number Theoretic Transform Architecture for Homomorphic Encryption*.
- Li et al., 2022, *MeNTT: A Compact and Efficient Processing-in-Memory Number Theoretic Transform Accelerator*.
- Waris et al., 2025, *Area-time efficient pipelined number theoretic transform for CRYSTALS-Kyber*.

**What it does NOT prove:**
- That Loop B improves your tasks specifically.
- That the chosen modulus / size is already optimal for KarnOS.

**Architectural implication:**
Loop B deserves real experiment budget before zeta scheduling does.

### Seam E — Annealing / Metropolis-style search is plausible for discrete constrained training
**What it supports:**
- Discrete, non-gradient, compressed-structure optimization being viable in some settings.
- Simulated annealing / related heuristics as legitimate alternatives or adjuncts in constrained search spaces.

**Representative papers:**
- Kuo et al., 2022, *Neural Network Structure Optimization by Simulated Annealing*.
- Polowczyk et al., 2025, *Heuristic optimization in classification atoms in molecules using GCN via uniform simulated annealing*.

**What it does NOT prove:**
- That Metropolis will beat gradient or straight-through methods for your kernel.
- That your specific temperature / allostasis mapping is right.

**Architectural implication:**
Metropolis belongs in the ablation plan, especially because your domain is small, discrete, and strongly constrained.

---

## Contradictions / pressure points inside the thesis

### 1. TQ1 and TQ2 are mixed together
This is the largest contamination source. The thesis speaks as if one operator family exists, but the shadow docs say the architecture has already pivoted from TQ1 to TQ2.

**Fix:** split evaluation into explicit branches.

### 2. “Reversible” is used across non-reversible steps
Once sign-clamp collapse is introduced, information is generally lost. That means the full path is not strongly reversible.

**Fix:** distinguish:
- algebraic invertibility of a pre-clamp operator,
- recoverability under restricted conditions,
- true end-to-end reversibility.

### 3. Zeta scheduling is presented as justified, but no evidence chain supports it
There is no comparable external research seam supporting zeta-zero update timing as a privileged training/inference schedule.

**Fix:** demote to experiment condition.

### 4. Toy tasks are promoted into proof language
The 3-sample polarity-match test is a smoke test, not evidence of broad capability.

**Fix:** promote only as sanity-check harness.

---

## Practical direction informed by the research

## Direction 1 — The project should become a discrete structured-kernel research program
Not “a mystical new substrate” yet.

### Branch A — TQ1 baseline
- Ternary `{-1,0,1}`.
- Grouped 4-vector weights.
- Full Hamilton product vs reduced `y0`-only variant.
- Clamp activation.
- Compare naive phase-shift update vs Metropolis.

### Branch B — TQ2 canonical line
- XY pair encoding.
- Exact integer permutation/rotation operator.
- Compact packed storage.
- Optional Loop B NTT spectral pass.
- Compare plain TQ2 vs TQ2+Loop B.

### Branch C — Plain ternary control baseline
- Same parameter budget.
- Simple signed ternary dot product.
- Same tasks and schedules.

This gives a real ladder instead of one self-flattering proof.

## Direction 2 — Zeta scheduling should move from doctrine to ablation
Test these update schedules:
1. every-step,
2. fixed periodic,
3. prime-derived,
4. zeta-derived.

If zeta does not outperform simpler deterministic schedules, kill it.

## Direction 3 — Reversibility should be formalized narrowly
Track three separate quantities:
- pre-clamp operator invertibility,
- post-clamp reconstruction error,
- audit trace sufficiency.

This prevents the thesis from claiming a physics miracle where it only has a traceability property.

## Direction 4 — NTT should be treated as the strongest “non-obvious” seam
If Loop B works, it gives you a distinctive exact-integer global mixing mechanism with real mathematical pedigree.
That is much more valuable than defending zeta symbolism.

---

## Immediate experiment matrix

| Experiment | Why it matters | Priority |
|---|---|---|
| E1: TQ1 full Hamilton vs TQ1 `y0` only | Determine whether the project is really using quaternion structure or just a signed dot product in costume | P0 |
| E2: TQ2 permutation kernel vs plain ternary baseline | Test whether the normative pivot actually buys anything | P0 |
| E3: naive phase-shift vs Metropolis | Evaluate the shadow-doc training seam | P0 |
| E4: no Loop B vs Loop B NTT | Test exact-integer spectral benefit | P1 |
| E5: fixed periodic vs prime vs zeta schedule | Decide whether zeta stays alive | P1 |
| E6: reversibility audit metrics | Quantify information loss after clamp | P1 |

## Suggested task ladder
1. Polarity match / ternary parity toy.
2. Ternary XOR-style compositional tasks.
3. Small noisy associative recall.
4. Tiny finite-state / sequence tasks.
5. Small symbol-manipulation tasks under strict parameter budget.

---

## What the research changed in direction

### Strengthened
- Balanced ternary as a serious representation choice.
- Low-precision ternary inference as a real efficiency seam.
- Quaternion/Hamilton structure as a real structured-operator family.
- NTT as a serious exact transform seam.
- Metropolis / annealing as a plausible discrete optimization seam.

### Weakened
- Blanket reversibility language.
- Adiabatic/thermal claims for software PoC.
- Zeta-zero timing as a privileged law.
- p-adic archive as near-term justification.

### Net result
The project’s strongest shape is:
**a deterministic, low-precision, structured discrete inference research program with TQ2 as canonical line, TQ1 as baseline, Loop B as high-value differentiator, and zeta/reversibility claims demoted until experimentally earned.**

---

## Recommended next artifact
Create a **Weight Thesis Trace Matrix** with rows for:
- kernel branch,
- encoding,
- update rule,
- schedule,
- task family,
- audit metric,
- implementation status,
- evidence status.

That would turn this from conceptual pressure into build pressure.

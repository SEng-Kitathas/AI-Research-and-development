# Toward a Discrete Geometric Weight Substrate
_White Paper Thesis v0.1 · 2026-03-28a_

## Abstract
This paper proposes a research program for a discrete geometric weight substrate in which model expressivity comes primarily from structured composition and cheap closed operators rather than scalar precision. The project does not assume a single already-proven weight format. Instead, it defines a shared substrate and evaluates multiple research branches over that substrate, including grouped Hamilton-style algebra, plane-block geometric permutation, spectral companion layers, 4D mutagenic lifts, and native distillation from standard models.

## 1. Problem
Modern weight fields are usually treated as large scalar arrays optimized through multiply-accumulate heavy arithmetic. This project asks whether a different regime is possible:

- lower bit depth
- more discrete structure
- richer local composition
- cheaper arithmetic
- stronger auditability
- better hardware sympathy

The core question is not whether low-bit weights can exist; that is already established in the literature. The question is whether a structured discrete substrate can achieve useful expressivity through composition and legal transforms while preserving cheap arithmetic and auditability.

## 2. Core Thesis
> Richness comes from structured discrete composition under cheap closed operators, not from scalar precision.

This yields the following thesis:
1. local weight objects should be structured, not merely scalar
2. legal transforms should remain cheap and closed
3. higher expressivity should arise from combinatory state space and grouped relations
4. higher-order lifts should preserve the same algebraic family
5. all concrete formats should be treated as research branches unless proven out

## 3. Shared Substrate
The shared substrate assumes:
- discrete low-bit or ternary-friendly nativity
- structured local objects (blocks, planes, grouped objects)
- cheap closed operations (shift, permutation, add/subtract, clamp, lookup)
- deterministic auditability
- hardware-friendly compact packing
- the ability to act on an object as a whole or on its constituent blocks

## 4. Research Branches

### RB-1 — TQ1 / grouped Hamilton branch
A grouped algebra branch that preserves the intuition that weight objects can encode richer inter-component relations than flat scalar arrays.

### RB-2 — TQ2 / plane-block geometric permutation branch
The current build-favored branch. This branch treats blocks and planes as the primitive structured objects and emphasizes permutation, reindexing, block composition, and cheap local transforms.

### RB-3 — Spectral companion branch
Adds a transform-domain or exact-integer spectral lift if it can remain a lift of the same base substrate.

### RB-4 — 4D mutagenic lift
Tests whether the same low-cost local algebra can be lifted into a 4D geometric space for mutation/evolution/search without abandoning closure.

### RB-5 — Native distillation / weight consumption
Consumes standard models or learned content and distills them into the native substrate.

### RB-6 — Control-layer coupling
Couples the weight substrate to the holon/nanite/salience-routing control layer.

### RB-7 — Scheduler/update ablations
Tests update laws, acceptance criteria, and schedules.

## 5. Research Context
Directional research support exists for:
- ternary and low-bit inference/hardware
- integer-only training/inference
- sparse additive ternary arithmetic
- quaternion/hypercomplex grouped representations
- exact integer spectral transforms such as NTT
- distillation into smaller/native students

The literature does **not** currently justify treating zeta scheduling as privileged or treating strong end-to-end software reversibility claims as established.

## 6. Genealogy
The project lineage contains at least three convergent streams:

### 6.1 Control lineage
salience → sparsity → stigmergic/mycelial routing → heartbeat → holon/nanite isomorphism

### 6.2 Weight lineage
ternary planes → block decomposition → radical assignment → geometric permutation → spectral intuition → Tesseract / 4D lift

### 6.3 Bridge lineage
consume standard weights → distill content → native low-bit substrate

The existence of these convergent streams is one reason the project should be treated as a branch program rather than a single frozen proposal.

## 7. Evaluation Criteria
All branches should be evaluated on:
- expressivity
- cost
- closure
- auditability
- hardware sympathy
- update/training viability
- degeneracy risk
- branch-specific kill criteria

## 8. Current Position
The current position is:
- the substrate is canonical
- the branches are experimental
- TQ2 is the current build-favored branch
- TQ1 remains a baseline
- spectral, 4D, and distillation branches stay alive unless falsified
- scheduler and reversibility claims remain bounded and test-driven

## 9. Immediate Next Steps
1. formalize RB-2 object grammar: block, plane, radical, transform set
2. write kill criteria for all branches
3. implement minimal RB-2 skeleton
4. implement RB-1 baseline comparator
5. define baseline task family and metric suite
6. run schedule/update ablations before doctrinal claims harden

## References / Research seams
- Tong et al. 2024 — balanced symmetry ternary CIM hardware
- Zhu et al. 2022 — TAB ternary/binary/mixed-precision inference
- Di Guglielmo et al. 2020 — binary/ternary FPGA deployment
- Wang et al. 2020 — NITI integer-only arithmetic
- Qin et al. 2022 — quaternion product units
- Altamirano-Gómez & Gershenson 2023 — quaternion CNN review
- Duong-Ngoc et al. 2023 — NTT architecture
- Cantini et al. 2024 — distillation for low-resource deployment
- Friston et al. 2022 — sparse coupling / self-organization under FEP
- Raja et al. 2021 — critique of overextended FEP claims

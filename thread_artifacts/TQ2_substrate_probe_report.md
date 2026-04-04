# TQ2 / block-plane substrate probe

This is a **toy-but-honest sandbox probe** of the user's concept.

## What was tested

Three lightweight model families were compared on synthetic 3x3 ternary-plane tasks:

1. **Baseline**
   - Plain ternary class prototype
   - No transforms
   - Acts like a cheap reference model

2. **WholeTransform**
   - Ternary plane treated as a whole object
   - Uses cheap whole-plane transforms (rotation / reflection family)
   - Classifies by best alignment under transform set

3. **Blockwise**
   - Plane decomposed into row-blocks
   - Each block scored under a cheap cyclic shift family
   - Whole score is sum of block-local best matches

## Tasks

1. **Whole-plane invariant motif**
   - Label depends on a hidden motif family under plane-wide transforms
   - Good test for whole-object geometry

2. **Block-composition invariant**
   - Label depends on block-level composition under local shifts
   - Good test for block grammar

3. **Majority-sign baseline**
   - Label depends on overall ternary polarity
   - Good sanity-check task

## Mean accuracy over 20 random splits

| task                        | model          |   mean_accuracy_pct |   std_pct |
|:----------------------------|:---------------|--------------------:|----------:|
| Whole-plane invariant motif | Baseline       |               49.58 |      3.07 |
| Whole-plane invariant motif | WholeTransform |               94.22 |      3.88 |
| Whole-plane invariant motif | Blockwise      |               48.39 |      6.77 |
| Block-composition invariant | Baseline       |               93.64 |      1.39 |
| Block-composition invariant | WholeTransform |               77.72 |      8.53 |
| Block-composition invariant | Blockwise      |               93.64 |      1.39 |
| Majority-sign baseline      | Baseline       |               92.08 |      3.78 |
| Majority-sign baseline      | WholeTransform |               75.53 |      9.05 |
| Majority-sign baseline      | Blockwise      |               93.89 |      5.52 |

## Readout

- **WholeTransform dominates the whole-plane motif task**
  - ~94.22% mean accuracy
  - Baseline and Blockwise sit near chance
  - This is the clearest positive signal for the "treat the weight object as a geometric whole" branch

- **Blockwise ties the baseline on the block-composition task**
  - ~93.64% mean accuracy
  - WholeTransform underperforms badly here
  - This says local combinatory structure matters and whole-plane-only logic is not enough

- **WholeTransform is weak on the plain majority-sign task**
  - ~75.53% mean accuracy
  - This is expected: structure-aware geometry should not be assumed to beat a simpler substrate everywhere

## Interpretation

The sandbox result is **not** "TQ2 is proven."
It *does* support a narrower claim:

> Different cheap operator families win on different structured tasks, which is exactly what a real research-branch substrate should show.

The strongest signal is:

- **whole-object transform logic** appears to buy real value when the task's invariants are geometric
- **blockwise local transforms** remain competitive or superior when the task's invariants are local/compositional
- there is **no evidence here for a single universal operator family**

## What this suggests next

The best next experiment is:

1. formalize the **TQ2 object grammar**
2. keep **whole-plane** and **blockwise** as sibling branches
3. add a fourth branch for **dual-band / multi-plane** scoring
4. replace these synthetic tasks with:
   - motif recall
   - small symbolic sequence tasks
   - compressed teacher-distillation tasks
   - maybe a tiny z80-style character model with TQ2-native operators

## Caveats

- Synthetic data only
- Prototype-level fitting, not full training
- No Forge ingestion
- No quaternion / dual-band lift yet
- No real benchmark against transformer or MLP baselines

This should be read as a **substrate probe**, not a proof of end-state capability.

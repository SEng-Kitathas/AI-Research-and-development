# Weight Shadow Trace Matrix
_Version: 2026-03-29c_

## TQ2 INFERENCE CORE

| ID | Requirement | Status | Priority | Notes |
|---|---|---:|---:|---|
| TQ2-01 | TQ2 canonical substrate (ternary plane/block object model) | Implemented (spec) | P0 | Canonical basis |
| TQ2-02 | Cheap closed operator family | Implemented (spec) | P0 | Shift / permutation / sign flip / add-sub / clamp |
| TQ2-03 | RB-2A whole-plane isolate | Partial | P0 | Probe exists; slow reference semantics still needed |
| TQ2-04 | RB-2B blockwise isolate | Partial | P0 | Probe exists; slow reference semantics still needed |
| TQ2-05 | RB-2C hybrid isolate | Partial | P0 | Defined in grammar/harness; not fully exercised |
| TQ2-06 | RB-2R integrated runtime composition | Partial | P0 | New canonical runtime model: blockwise -> whole-plane -> hybrid reconciliation |
| TQ2-07 | Confidence-aware reconciliation policy | Missing | P0 | Need exact fusion and veto rules |
| TQ2-08 | Explanatory decomposition output | Missing | P1 | Preserve local/global evidence in final result |
| TQ2-09 | Mixed-task benchmark wave | Partial | P0 | Initial substrate probe done; formal mixed wave pending |
| TQ2-10 | Forge translation targets local+global compatibility | Missing | P1 | Scientist/Engineer rewrite pressure |

## RESEARCH BRANCH GOVERNANCE

| ID | Requirement | Status | Priority | Notes |
|---|---|---:|---:|---|
| GOV-RB-01 | Keep branches separable in benchmarking | Implemented (policy) | P0 | Needed for attribution |
| GOV-RB-02 | Compose branches in runtime when justified | Implemented (policy) | P0 | New 2026-03-29c decision |
| GOV-RB-03 | Branch kill criteria recorded | Partial | P1 | Needs per-branch thresholds |
| GOV-RB-04 | Runtime composition evaluated against isolates | Missing | P0 | Must prove integrated stack earns complexity |

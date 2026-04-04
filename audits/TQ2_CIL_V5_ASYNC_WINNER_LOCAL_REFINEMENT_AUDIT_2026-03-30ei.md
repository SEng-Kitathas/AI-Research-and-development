# TQ2/CIL V5 Async Winner Local Refinement Audit
_Version: 2026-03-30ei_

## Scope
Local refinement around the unified Sigma v5 async winner architecture.

Fixed core:
- side worker = direct_delta
- shape worker = family_contrast

Searched:
- right_bias
- whole_block_blend
- conf_gate
- sync_mode
- resolver
- veto_strength

Total variants searched: **729**

## Best refined async V5 policy
```json
{
  "right_bias": 0.08,
  "whole_block_blend": 0.5,
  "conf_gate": 0.25,
  "sync_mode": "shape_priority",
  "resolver": "sum",
  "veto_strength": 0.0
}
```

- Accuracy: **72.92**
- Mirror errors: **7**
- Right-residual errors: **2**
- Composite: **69.570**

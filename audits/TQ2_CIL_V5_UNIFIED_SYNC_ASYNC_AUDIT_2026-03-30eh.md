# TQ2/CIL V5 Unified Sync+Async Search Audit
_Version: 2026-03-30eh_

## Scope
Unified all-combinations pass on Sigma v5 across:
- sync / integrated policy family
- async worker / resolver architecture family

## Search sizes
- Sync search space: **1296**
- Async search space: **1944**
- Unified total: **3240**

## Best policy overall
```json
{
  "side_worker": "direct_delta",
  "shape_worker": "family_contrast",
  "resolver": "sum",
  "sync_mode": "shape_priority",
  "conf_gate": 0.35,
  "veto_strength": 0.0,
  "right_bias": 0.08,
  "whole_block_blend": 0.55
}
```

- Family: **async**
- Accuracy: **72.92**
- Mirror errors: **7**
- Right-residual errors: **2**
- Composite: **69.570**

## Immediate read
This rung gives one ranked board on the architecture-sensitive Sigma v5 surface, so sync and async are compared under the same pressure and scoring.

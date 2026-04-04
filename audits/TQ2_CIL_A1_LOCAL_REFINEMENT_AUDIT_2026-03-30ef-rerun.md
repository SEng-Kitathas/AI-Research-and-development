# TQ2/CIL A1 Local Refinement Audit
_Version: 2026-03-30ef-rerun_

## Scope
Local refinement sweep around A1's winning async architecture class.

Total local variants searched: **243**

## Best local A1 policy
```json
{
  "right_bias": 0.04,
  "veto_strength": 0.1,
  "blend": 0.5,
  "shape_pen": 0.45,
  "cross_pen": 0.55
}
```

## Metrics
- Mean accuracy: **79.42**
- Stddev: **7.08**
- Total mirror errors: **13**
- Total right-residual errors: **5**
- Composite: **68.630**

### Surface breakdown
- Sigma v2: acc **88.89**, mirror **3**, rr **2**
- Sigma v3: acc **71.88**, mirror **5**, rr **2**
- Sigma v4: acc **77.50**, mirror **5**, rr **1**

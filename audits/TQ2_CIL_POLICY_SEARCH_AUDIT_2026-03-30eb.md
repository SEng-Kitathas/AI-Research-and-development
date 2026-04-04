# TQ2/CIL Policy Search Audit
_Version: 2026-03-30eb_

## Scope
Bounded policy search across a discretized wound-specific grammar.

Search space:
- side mode: m2 / axis_seq / dialectic
- global blend
- agreement bonus
- mirror penalty
- side strength
- shape strength
- right boost
- right penalty extra

Total policies searched: **1296**

## Best policy
```json
{
  "side_mode": "m2",
  "blend_global": 0.58,
  "agreement_bonus": 0.18,
  "mirror_pen": 0.3,
  "side_strength": 0.14,
  "shape_strength": 0.26,
  "right_boost": 0.12,
  "right_pen_extra": 0.0
}
```

### Best policy metrics
- Mean accuracy across sigma v2/v3/v4: **78.59**
- Stddev across surfaces: **7.39**
- Total mirror errors: **14**
- Total right-residual errors: **5**
- Composite score: **67.393**

### Surface breakdown
- Sigma v2: acc **88.89**, mirror **3**, rr **2**
- Sigma v3: acc **71.88**, mirror **5**, rr **2**
- Sigma v4: acc **75.00**, mirror **6**, rr **1**

## Top 10 policies

### Policy 82
- policy: `{"side_mode":"m2","blend_global":0.58,"agreement_bonus":0.18,"mirror_pen":0.3,"side_strength":0.14,"shape_strength":0.26,"right_boost":0.12,"right_pen_extra":0.0}`
- mean acc: **78.59**
- std: **7.39**
- total mirror: **14**
- total rr: **5**
- composite: **67.393**
- v2/v3/v4: **88.89 / 71.88 / 75.00**

### Policy 226
- policy: `{"side_mode":"m2","blend_global":0.66,"agreement_bonus":0.18,"mirror_pen":0.3,"side_strength":0.14,"shape_strength":0.26,"right_boost":0.12,"right_pen_extra":0.0}`
- mean acc: **78.59**
- std: **7.39**
- total mirror: **14**
- total rr: **5**
- composite: **67.393**
- v2/v3/v4: **88.89 / 71.88 / 75.00**

### Policy 370
- policy: `{"side_mode":"m2","blend_global":0.72,"agreement_bonus":0.18,"mirror_pen":0.3,"side_strength":0.14,"shape_strength":0.26,"right_boost":0.12,"right_pen_extra":0.0}`
- mean acc: **78.59**
- std: **7.39**
- total mirror: **14**
- total rr: **5**
- composite: **67.393**
- v2/v3/v4: **88.89 / 71.88 / 75.00**

### Policy 11
- policy: `{"side_mode":"m2","blend_global":0.58,"agreement_bonus":0.1,"mirror_pen":0.3,"side_strength":0.14,"shape_strength":0.26,"right_boost":0.12,"right_pen_extra":0.06}`
- mean acc: **78.47**
- std: **9.67**
- total mirror: **14**
- total rr: **5**
- composite: **66.136**
- v2/v3/v4: **91.67 / 68.75 / 75.00**

### Policy 23
- policy: `{"side_mode":"m2","blend_global":0.58,"agreement_bonus":0.1,"mirror_pen":0.3,"side_strength":0.2,"shape_strength":0.26,"right_boost":0.12,"right_pen_extra":0.06}`
- mean acc: **78.47**
- std: **9.67**
- total mirror: **14**
- total rr: **5**
- composite: **66.136**
- v2/v3/v4: **91.67 / 68.75 / 75.00**

### Policy 34
- policy: `{"side_mode":"m2","blend_global":0.58,"agreement_bonus":0.1,"mirror_pen":0.4,"side_strength":0.14,"shape_strength":0.26,"right_boost":0.12,"right_pen_extra":0.0}`
- mean acc: **78.47**
- std: **9.67**
- total mirror: **14**
- total rr: **5**
- composite: **66.136**
- v2/v3/v4: **91.67 / 68.75 / 75.00**

### Policy 46
- policy: `{"side_mode":"m2","blend_global":0.58,"agreement_bonus":0.1,"mirror_pen":0.4,"side_strength":0.2,"shape_strength":0.26,"right_boost":0.12,"right_pen_extra":0.0}`
- mean acc: **78.47**
- std: **9.67**
- total mirror: **14**
- total rr: **5**
- composite: **66.136**
- v2/v3/v4: **91.67 / 68.75 / 75.00**

### Policy 155
- policy: `{"side_mode":"m2","blend_global":0.66,"agreement_bonus":0.1,"mirror_pen":0.3,"side_strength":0.14,"shape_strength":0.26,"right_boost":0.12,"right_pen_extra":0.06}`
- mean acc: **78.47**
- std: **9.67**
- total mirror: **14**
- total rr: **5**
- composite: **66.136**
- v2/v3/v4: **91.67 / 68.75 / 75.00**

### Policy 167
- policy: `{"side_mode":"m2","blend_global":0.66,"agreement_bonus":0.1,"mirror_pen":0.3,"side_strength":0.2,"shape_strength":0.26,"right_boost":0.12,"right_pen_extra":0.06}`
- mean acc: **78.47**
- std: **9.67**
- total mirror: **14**
- total rr: **5**
- composite: **66.136**
- v2/v3/v4: **91.67 / 68.75 / 75.00**

### Policy 178
- policy: `{"side_mode":"m2","blend_global":0.66,"agreement_bonus":0.1,"mirror_pen":0.4,"side_strength":0.14,"shape_strength":0.26,"right_boost":0.12,"right_pen_extra":0.0}`
- mean acc: **78.47**
- std: **9.67**
- total mirror: **14**
- total rr: **5**
- composite: **66.136**
- v2/v3/v4: **91.67 / 68.75 / 75.00**

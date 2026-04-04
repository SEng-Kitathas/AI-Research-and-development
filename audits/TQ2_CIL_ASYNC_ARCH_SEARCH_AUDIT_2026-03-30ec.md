# TQ2/CIL Async Architecture Search Audit
_Version: 2026-03-30ec_

## Scope
Bounded async-architecture search across:
- left/right hypothesis workers
- cross/L shape workers
- resolver worker
- sync/join mode

Total architectures searched: **1944**

## Best architecture
```json
{
  "side_worker": "direct_delta",
  "shape_worker": "family_contrast",
  "resolver": "veto",
  "sync_mode": "parallel_join",
  "conf_gate": 0.35,
  "veto_strength": 0.2,
  "right_bias": 0.08,
  "whole_block_blend": 0.55
}
```

### Best architecture metrics
- Mean accuracy across sigma v2/v3/v4: **79.42**
- Stddev across surfaces: **7.08**
- Total mirror errors: **13**
- Total right-residual errors: **5**
- Composite score: **68.635**

### Surface breakdown
- Sigma v2: acc **88.89**, mirror **3**, rr **2**
- Sigma v3: acc **71.88**, mirror **5**, rr **2**
- Sigma v4: acc **77.50**, mirror **5**, rr **1**

## Top 10 architectures

### Architecture 294
- policy: `{"side_worker":"direct_delta","shape_worker":"family_contrast","resolver":"veto","sync_mode":"parallel_join","conf_gate":0.35,"veto_strength":0.2,"right_bias":0.08,"whole_block_blend":0.55}`
- mean acc: **79.42**
- std: **7.08**
- total mirror: **13**
- total rr: **5**
- composite: **68.635**
- v2/v3/v4: **88.89 / 71.88 / 77.50**

### Architecture 295
- policy: `{"side_worker":"direct_delta","shape_worker":"family_contrast","resolver":"veto","sync_mode":"parallel_join","conf_gate":0.35,"veto_strength":0.2,"right_bias":0.08,"whole_block_blend":0.65}`
- mean acc: **79.42**
- std: **7.08**
- total mirror: **13**
- total rr: **5**
- composite: **68.635**
- v2/v3/v4: **88.89 / 71.88 / 77.50**

### Architecture 298
- policy: `{"side_worker":"direct_delta","shape_worker":"family_contrast","resolver":"veto","sync_mode":"parallel_join","conf_gate":0.35,"veto_strength":0.4,"right_bias":0.08,"whole_block_blend":0.55}`
- mean acc: **79.42**
- std: **7.08**
- total mirror: **13**
- total rr: **5**
- composite: **68.635**
- v2/v3/v4: **88.89 / 71.88 / 77.50**

### Architecture 299
- policy: `{"side_worker":"direct_delta","shape_worker":"family_contrast","resolver":"veto","sync_mode":"parallel_join","conf_gate":0.35,"veto_strength":0.4,"right_bias":0.08,"whole_block_blend":0.65}`
- mean acc: **79.42**
- std: **7.08**
- total mirror: **13**
- total rr: **5**
- composite: **68.635**
- v2/v3/v4: **88.89 / 71.88 / 77.50**

### Architecture 306
- policy: `{"side_worker":"direct_delta","shape_worker":"family_contrast","resolver":"veto","sync_mode":"parallel_join","conf_gate":0.55,"veto_strength":0.2,"right_bias":0.08,"whole_block_blend":0.55}`
- mean acc: **79.42**
- std: **7.08**
- total mirror: **13**
- total rr: **5**
- composite: **68.635**
- v2/v3/v4: **88.89 / 71.88 / 77.50**

### Architecture 307
- policy: `{"side_worker":"direct_delta","shape_worker":"family_contrast","resolver":"veto","sync_mode":"parallel_join","conf_gate":0.55,"veto_strength":0.2,"right_bias":0.08,"whole_block_blend":0.65}`
- mean acc: **79.42**
- std: **7.08**
- total mirror: **13**
- total rr: **5**
- composite: **68.635**
- v2/v3/v4: **88.89 / 71.88 / 77.50**

### Architecture 310
- policy: `{"side_worker":"direct_delta","shape_worker":"family_contrast","resolver":"veto","sync_mode":"parallel_join","conf_gate":0.55,"veto_strength":0.4,"right_bias":0.08,"whole_block_blend":0.55}`
- mean acc: **79.42**
- std: **7.08**
- total mirror: **13**
- total rr: **5**
- composite: **68.635**
- v2/v3/v4: **88.89 / 71.88 / 77.50**

### Architecture 311
- policy: `{"side_worker":"direct_delta","shape_worker":"family_contrast","resolver":"veto","sync_mode":"parallel_join","conf_gate":0.55,"veto_strength":0.4,"right_bias":0.08,"whole_block_blend":0.65}`
- mean acc: **79.42**
- std: **7.08**
- total mirror: **13**
- total rr: **5**
- composite: **68.635**
- v2/v3/v4: **88.89 / 71.88 / 77.50**

### Architecture 342
- policy: `{"side_worker":"direct_delta","shape_worker":"family_contrast","resolver":"veto","sync_mode":"shape_priority","conf_gate":0.35,"veto_strength":0.2,"right_bias":0.08,"whole_block_blend":0.55}`
- mean acc: **79.42**
- std: **7.08**
- total mirror: **13**
- total rr: **5**
- composite: **68.635**
- v2/v3/v4: **88.89 / 71.88 / 77.50**

### Architecture 343
- policy: `{"side_worker":"direct_delta","shape_worker":"family_contrast","resolver":"veto","sync_mode":"shape_priority","conf_gate":0.35,"veto_strength":0.2,"right_bias":0.08,"whole_block_blend":0.65}`
- mean acc: **79.42**
- std: **7.08**
- total mirror: **13**
- total rr: **5**
- composite: **68.635**
- v2/v3/v4: **88.89 / 71.88 / 77.50**

from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
import importlib.util
import itertools
import json
import numpy as np
import sys

BASE = Path("/mnt/data")

def _load_module(path: Path, module_name: str):
    spec = importlib.util.spec_from_file_location(module_name, str(path))
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Unable to load module from {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)  # type: ignore[attr-defined]
    return module

e = _load_module(BASE / "tq2_reference_semantics_v2_2026-03-29e.py", "tq2_sem_e_ei2")

@dataclass
class Sample:
    label: str
    perturbation: str
    array: np.ndarray

def _np(a):
    return np.array(a, dtype=int)

BASE_TEMPLATES = {
    "cross_left":  _np([[0, 1, 0],[1, 1, 1],[1, 0,-1]]),
    "cross_right": _np([[0, 1, 0],[1, 1, 1],[-1,0, 1]]),
    "L_left":      _np([[1, 0, 0],[1, 0, 0],[1, 1,-1]]),
    "L_right":     _np([[0, 0, 1],[0, 0, 1],[-1,1, 1]]),
}

def sigma_v5_perturbations(label, a):
    out = []
    if label == "cross_right":
        defs = {
            "xr_split_side_cues": lambda x: (x.__setitem__((0,2), 0), x.__setitem__((2,2), 1), x.__setitem__((0,0), 1)),
            "xr_shape_side_conflict": lambda x: (x.__setitem__((1,0), 1), x.__setitem__((1,2), 0), x.__setitem__((0,1), 1)),
            "xr_dual_contradiction": lambda x: (x.__setitem__((0,0), 1), x.__setitem__((2,0), 1), x.__setitem__((2,2), 0)),
            "xr_occluded_right_then_recover": lambda x: (x.__setitem__((0,2), 0), x.__setitem__((1,2), 0), x.__setitem__((2,2), 1)),
            "xr_crossbar_vs_anchor": lambda x: (x.__setitem__((1,0), 1), x.__setitem__((0,2), 1), x.__setitem__((2,2), 0)),
            "xr_left_pull_bottom_bridge": lambda x: (x.__setitem__((2,1), 1), x.__setitem__((2,0), 1), x.__setitem__((1,2), 0)),
            "xr_sign_noise_recover": lambda x: (x.__setitem__((2,2), -1), x.__setitem__((0,2), 1), x.__setitem__((2,0), 0)),
            "xr_all_workers_needed": lambda x: (x.__setitem__((0,0), 1), x.__setitem__((1,0), 1), x.__setitem__((0,2), 0), x.__setitem__((2,2), 1)),
            "xr_edge_inversion": lambda x: (x.__setitem__((0,2), -1), x.__setitem__((2,0), 1)),
            "xr_join_trap": lambda x: (x.__setitem__((1,0), 1), x.__setitem__((0,2), 0), x.__setitem__((2,2), 1), x.__setitem__((2,0), 0)),
            "xr_veto_needed": lambda x: (x.__setitem__((0,0), 1), x.__setitem__((1,0), 1), x.__setitem__((2,2), 1)),
            "xr_parallel_advantage": lambda x: (x.__setitem__((0,2), 0), x.__setitem__((1,2), 1), x.__setitem__((2,0), 1), x.__setitem__((2,2), 1)),
        }
    elif label == "L_right":
        defs = {
            "lr_split_side_cues": lambda x: (x.__setitem__((0,2), 0), x.__setitem__((2,2), 1), x.__setitem__((0,0), 1)),
            "lr_shape_side_conflict": lambda x: (x.__setitem__((0,1), 1), x.__setitem__((1,0), 1), x.__setitem__((1,2), 0)),
            "lr_dual_contradiction": lambda x: (x.__setitem__((0,0), 1), x.__setitem__((2,0), 1), x.__setitem__((1,2), 0)),
            "lr_occluded_right_then_recover": lambda x: (x.__setitem__((0,2), 0), x.__setitem__((1,2), 0), x.__setitem__((2,2), 1)),
            "lr_crossbar_vs_anchor": lambda x: (x.__setitem__((1,0), 1), x.__setitem__((0,1), 1), x.__setitem__((0,2), 0)),
            "lr_left_pull_bottom_bridge": lambda x: (x.__setitem__((2,1), 1), x.__setitem__((2,0), 1), x.__setitem__((1,2), 0)),
            "lr_sign_noise_recover": lambda x: (x.__setitem__((2,2), -1), x.__setitem__((0,2), 1), x.__setitem__((1,0), 0)),
            "lr_all_workers_needed": lambda x: (x.__setitem__((0,0), 1), x.__setitem__((1,0), 1), x.__setitem__((0,2), 0), x.__setitem__((2,2), 1)),
            "lr_edge_inversion": lambda x: (x.__setitem__((0,2), -1), x.__setitem__((2,0), 1)),
            "lr_join_trap": lambda x: (x.__setitem__((1,0), 1), x.__setitem__((0,2), 0), x.__setitem__((2,2), 1), x.__setitem__((1,2), 0)),
            "lr_veto_needed": lambda x: (x.__setitem__((0,0), 1), x.__setitem__((1,0), 1), x.__setitem__((2,2), 1)),
            "lr_parallel_advantage": lambda x: (x.__setitem__((0,2), 0), x.__setitem__((1,2), 1), x.__setitem__((2,0), 1), x.__setitem__((2,2), 1)),
        }
    elif label == "cross_left":
        defs = {
            "xl_split_side_cues": lambda x: (x.__setitem__((0,0), 0), x.__setitem__((2,0), 1), x.__setitem__((0,2), 1)),
            "xl_shape_side_conflict": lambda x: (x.__setitem__((1,2), 1), x.__setitem__((1,0), 0), x.__setitem__((0,1), 1)),
            "xl_dual_contradiction": lambda x: (x.__setitem__((0,2), 1), x.__setitem__((2,2), 1), x.__setitem__((2,0), 0)),
            "xl_occluded_left_then_recover": lambda x: (x.__setitem__((0,0), 0), x.__setitem__((1,0), 0), x.__setitem__((2,0), 1)),
            "xl_crossbar_vs_anchor": lambda x: (x.__setitem__((1,2), 1), x.__setitem__((0,0), 1), x.__setitem__((2,0), 0)),
            "xl_right_pull_bottom_bridge": lambda x: (x.__setitem__((2,1), 1), x.__setitem__((2,2), 1), x.__setitem__((1,0), 0)),
            "xl_sign_noise_recover": lambda x: (x.__setitem__((2,0), -1), x.__setitem__((0,0), 1), x.__setitem__((2,2), 0)),
            "xl_all_workers_needed": lambda x: (x.__setitem__((0,2), 1), x.__setitem__((1,2), 1), x.__setitem__((0,0), 0), x.__setitem__((2,0), 1)),
            "xl_edge_inversion": lambda x: (x.__setitem__((0,0), -1), x.__setitem__((2,2), 1)),
            "xl_join_trap": lambda x: (x.__setitem__((1,2), 1), x.__setitem__((0,0), 0), x.__setitem__((2,0), 1), x.__setitem__((2,2), 0)),
            "xl_veto_needed": lambda x: (x.__setitem__((0,2), 1), x.__setitem__((1,2), 1), x.__setitem__((2,0), 1)),
            "xl_parallel_advantage": lambda x: (x.__setitem__((0,0), 0), x.__setitem__((1,0), 1), x.__setitem__((2,2), 1), x.__setitem__((2,0), 1)),
        }
    else:
        defs = {
            "ll_split_side_cues": lambda x: (x.__setitem__((0,0), 0), x.__setitem__((2,0), 1), x.__setitem__((0,2), 1)),
            "ll_shape_side_conflict": lambda x: (x.__setitem__((0,1), 1), x.__setitem__((1,2), 1), x.__setitem__((1,0), 0)),
            "ll_dual_contradiction": lambda x: (x.__setitem__((0,2), 1), x.__setitem__((2,2), 1), x.__setitem__((1,0), 0)),
            "ll_occluded_left_then_recover": lambda x: (x.__setitem__((0,0), 0), x.__setitem__((1,0), 0), x.__setitem__((2,0), 1)),
            "ll_crossbar_vs_anchor": lambda x: (x.__setitem__((1,2), 1), x.__setitem__((0,1), 1), x.__setitem__((0,0), 0)),
            "ll_right_pull_bottom_bridge": lambda x: (x.__setitem__((2,1), 1), x.__setitem__((2,2), 1), x.__setitem__((1,0), 0)),
            "ll_sign_noise_recover": lambda x: (x.__setitem__((2,0), -1), x.__setitem__((0,0), 1), x.__setitem__((1,2), 0)),
            "ll_all_workers_needed": lambda x: (x.__setitem__((0,2), 1), x.__setitem__((1,2), 1), x.__setitem__((0,0), 0), x.__setitem__((2,0), 1)),
            "ll_edge_inversion": lambda x: (x.__setitem__((0,0), -1), x.__setitem__((2,2), 1)),
            "ll_join_trap": lambda x: (x.__setitem__((1,2), 1), x.__setitem__((0,0), 0), x.__setitem__((2,0), 1), x.__setitem__((1,0), 0)),
            "ll_veto_needed": lambda x: (x.__setitem__((0,2), 1), x.__setitem__((1,2), 1), x.__setitem__((2,0), 1)),
            "ll_parallel_advantage": lambda x: (x.__setitem__((0,0), 0), x.__setitem__((1,0), 1), x.__setitem__((2,2), 1), x.__setitem__((2,0), 1)),
        }
    for name, fn in defs.items():
        x = a.copy(); fn(x); out.append((name, x))
    return out

def generate_samples():
    out = []
    for label, arr in BASE_TEMPLATES.items():
        for name, x in sigma_v5_perturbations(label, arr):
            out.append(Sample(label, name, x.copy()))
    return out

PROTOS = [
    e.Prototype("cross_left",  e.plane_from_array(np.array([[0,1,0],[1,1,1],[1,0,0]]), label="cross_left"),  {"kind": "mixed"}),
    e.Prototype("cross_right", e.plane_from_array(np.array([[0,1,0],[1,1,1],[0,0,1]]), label="cross_right"), {"kind": "mixed"}),
    e.Prototype("L_left",      e.plane_from_array(np.array([[1,0,0],[1,0,0],[1,1,1]]), label="L_left"),      {"kind": "mixed"}),
    e.Prototype("L_right",     e.plane_from_array(np.array([[0,0,1],[0,0,1],[1,1,1]]), label="L_right"),     {"kind": "mixed"}),
]
LABELS = ["cross_left","cross_right","L_left","L_right"]

PRE = []
for s in generate_samples():
    plane = e.plane_from_array(s.array, label=s.label)
    whole = e.score_wholeplane(plane, PROTOS)
    block = e.score_blockwise(plane, PROTOS, axis="row")
    arr = plane.data
    cell = lambda r,c: float(arr[r][c])
    feat = {}
    feat["left_anchor"] = cell(0,0) + cell(2,0) + 0.5*cell(1,0)
    feat["right_anchor"] = cell(0,2) + cell(2,2) + 0.5*cell(1,2)
    feat["bottom_left"] = cell(2,0) + 0.5*cell(2,1)
    feat["bottom_right"] = cell(2,2) + 0.5*cell(2,1)
    feat["directional_margin"] = feat["left_anchor"] - feat["right_anchor"]
    feat["crossness"] = cell(0,1)+cell(1,0)+cell(1,2)+0.5*cell(1,1)
    feat["l_leftness"] = (cell(0,0)+cell(1,0)+cell(2,0)) + feat["bottom_left"] - cell(0,1) - cell(1,2)
    feat["l_rightness"] = (cell(0,2)+cell(1,2)+cell(2,2)) + feat["bottom_right"] - cell(0,1) - cell(1,0)
    whole_best = {}
    for rec in whole["all"]:
        if rec["proto"] not in whole_best or rec["score"] > whole_best[rec["proto"]]["score"]:
            whole_best[rec["proto"]] = rec
    block_best = {}
    for rec in block["all"]:
        if rec["proto"] not in block_best or rec["score"] > block_best[rec["proto"]]["score"]:
            block_best[rec["proto"]] = rec
    PRE.append({
        "label": s.label,
        "feat": feat,
        "whole_best": {k: {"confidence": float(v["confidence"])} for k,v in whole_best.items()},
        "block_best": {k: {"confidence": float(v["confidence"])} for k,v in block_best.items()},
    })

RIGHT_BIAS = [0.04, 0.08, 0.12]
WHOLE_BLOCK_BLEND = [0.50, 0.55, 0.60]
CONF_GATE = [0.25, 0.35, 0.45]
SYNC_MODE = ["parallel_join", "shape_priority", "side_priority"]
RESOLVER = ["sum", "veto", "tension_gated"]
VETO_STRENGTH = [0.0, 0.1, 0.2]

def predict(pre, pol):
    f = pre["feat"]; wb = pre["whole_best"]; bb = pre["block_best"]
    blend = pol["whole_block_blend"]
    proto_base = {}
    for proto in LABELS:
        g = wb.get(proto, {"confidence": -99.0})["confidence"]
        b = bb.get(proto, {"confidence": -99.0})["confidence"]
        proto_base[proto] = blend*g + (1.0-blend)*b + 0.08*(g*b)

    left = max(0.0, f["left_anchor"] - f["right_anchor"]) + 0.5*max(0.0, f["bottom_left"] - f["bottom_right"])
    right = max(0.0, f["right_anchor"] - f["left_anchor"]) + 0.5*max(0.0, f["bottom_right"] - f["bottom_left"]) + pol["right_bias"]

    shape_left_cross = f["crossness"] - 0.6*max(0.0, f["l_leftness"])
    shape_left_L = f["l_leftness"] - 0.5*max(0.0, f["crossness"])
    shape_right_cross = f["crossness"] - 0.6*max(0.0, f["l_rightness"])
    shape_right_L = f["l_rightness"] - 0.5*max(0.0, f["crossness"])

    hyp = {
        "cross_left": proto_base["cross_left"] + left + shape_left_cross,
        "L_left": proto_base["L_left"] + left + shape_left_L,
        "cross_right": proto_base["cross_right"] + right + shape_right_cross,
        "L_right": proto_base["L_right"] + right + shape_right_L,
    }

    if pol["sync_mode"] == "side_priority":
        side_gap = abs(left-right)
        if side_gap >= pol["conf_gate"]:
            if left >= right:
                hyp["cross_right"] -= 0.5; hyp["L_right"] -= 0.5
            else:
                hyp["cross_left"] -= 0.5; hyp["L_left"] -= 0.5
    elif pol["sync_mode"] == "shape_priority":
        lshape = max(shape_left_cross, shape_left_L)
        rshape = max(shape_right_cross, shape_right_L)
        gap = abs(lshape-rshape)
        if gap >= pol["conf_gate"]:
            if lshape >= rshape:
                hyp["cross_right"] -= 0.35; hyp["L_right"] -= 0.35
            else:
                hyp["cross_left"] -= 0.35; hyp["L_left"] -= 0.35

    if pol["resolver"] == "veto":
        dm = f["directional_margin"]
        if dm < 0:
            hyp["cross_left"] -= pol["veto_strength"] + 0.10*abs(dm)
            hyp["L_left"] -= pol["veto_strength"] + 0.10*abs(dm)
        elif dm > 0:
            hyp["cross_right"] -= pol["veto_strength"] + 0.10*abs(dm)
            hyp["L_right"] -= pol["veto_strength"] + 0.10*abs(dm)
    elif pol["resolver"] == "tension_gated":
        tension = abs(left-right)
        if tension < pol["conf_gate"]:
            hyp["cross_left"] -= 0.2*max(0.0, f["right_anchor"] - f["left_anchor"])
            hyp["L_left"] -= 0.2*max(0.0, f["right_anchor"] - f["left_anchor"])
            hyp["cross_right"] -= 0.2*max(0.0, f["left_anchor"] - f["right_anchor"])
            hyp["L_right"] -= 0.2*max(0.0, f["left_anchor"] - f["right_anchor"])

    return max(hyp.items(), key=lambda kv: kv[1])[0]

results = []
for idx, vals in enumerate(itertools.product(RIGHT_BIAS, WHOLE_BLOCK_BLEND, CONF_GATE, SYNC_MODE, RESOLVER, VETO_STRENGTH)):
    pol = {
        "right_bias": vals[0],
        "whole_block_blend": vals[1],
        "conf_gate": vals[2],
        "sync_mode": vals[3],
        "resolver": vals[4],
        "veto_strength": vals[5],
    }
    ok = mir = rr = 0
    for x in PRE:
        pred = predict(x, pol)
        if pred == x["label"]: ok += 1
        if (x["label"], pred) in {("cross_left","cross_right"),("cross_right","cross_left"),("L_left","L_right"),("L_right","L_left")}:
            mir += 1
        if (x["label"], pred) in {("cross_right","cross_left"),("L_right","cross_left")}:
            rr += 1
    acc = round(100.0*ok/len(PRE), 2)
    composite = round(acc - 0.8*rr - 0.25*mir, 3)
    results.append({
        "policy_id": idx,
        "policy": pol,
        "acc": acc,
        "mirror": mir,
        "rr": rr,
        "composite": composite,
    })

results.sort(key=lambda r: (-r["composite"], -r["acc"], r["rr"], r["mirror"]))
out = {"search_space_size": len(results), "best_policy": results[0], "top_20": results[:20]}
out_path = BASE / "tq2_v5_async_winner_local_refine_results_2026-03-30ei.json"
out_path.write_text(json.dumps(out, indent=2), encoding="utf-8")
print(out_path)

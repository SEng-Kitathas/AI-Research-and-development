from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List
import importlib.util
import itertools
import json
import math
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

e = _load_module(BASE / "tq2_reference_semantics_v2_2026-03-29e.py", "tq2_sem_e_async")

@dataclass
class Sample:
    surface: str
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

def sigma_v2_perturbations(a: np.ndarray):
    out = [("id", a.copy())]
    b = a.copy(); b[1,1] *= -1; out.append(("center_invert", b))
    c = a.copy(); c[0,0] = 0; c[0,2] = 0; out.append(("top_anchor_dropout", c))
    d = a.copy(); d[2,0] = 0; d[2,2] = 0; out.append(("bottom_anchor_dropout", d))
    e1 = a.copy(); e1[0,2] = -e1[0,2] if e1[0,2] != 0 else 1; out.append(("right_bias_flip", e1))
    f = a.copy(); f[0,0] = -f[0,0] if f[0,0] != 0 else 1; out.append(("left_bias_flip", f))
    g = np.rot90(a, 1).copy(); g[2,1] = a[2,1]; out.append(("rot_preserve_tail", g))
    h = a.copy(); h[1,0], h[1,2] = h[1,2], h[1,0]; out.append(("midrow_swap", h))
    i = a.copy(); i[0,1] = 0; i[2,1] = 0; out.append(("vertical_cue_dropout", i))
    return out

def sigma_v3_perturbations(label: str, a: np.ndarray):
    out = []
    if label == "cross_right":
        defs = {
            "xr_righttail_drop_leftdecoy": lambda x: (x.__setitem__((2,2), 0), x.__setitem__((2,0), 1)),
            "xr_midright_drop_midleft_decoy": lambda x: (x.__setitem__((1,2), 0), x.__setitem__((1,0), 1)),
            "xr_topright_drop_topleft_decoy": lambda x: (x.__setitem__((0,2), 0), x.__setitem__((0,0), 1)),
            "xr_bridge_left_pull": lambda x: (x.__setitem__((2,2), 0), x.__setitem__((0,1), 1), x.__setitem__((1,0), 1)),
            "xr_signconflict_leftfoot": lambda x: (x.__setitem__((2,2), -1), x.__setitem__((2,0), 1)),
            "xr_rightweak_bottombridge": lambda x: (x.__setitem__((1,2), 0), x.__setitem__((2,1), 1)),
            "xr_columncollapse_leftfoot": lambda x: (x.__setitem__((0,2), 0), x.__setitem__((1,2), 0), x.__setitem__((2,0), 1)),
            "xr_midrow_swap": lambda x: x.__setitem__((1, slice(None)), np.array([1,1,0])),
        }
    elif label == "L_right":
        defs = {
            "lr_spinedrop_crossleftdecoy": lambda x: (x.__setitem__((1,2), 0), x.__setitem__((1,0), 1)),
            "lr_footdrop_leftfootdecoy": lambda x: (x.__setitem__((2,2), 0), x.__setitem__((2,0), 1)),
            "lr_topdrop_topleftdecoy": lambda x: (x.__setitem__((0,2), 0), x.__setitem__((0,0), 1)),
            "lr_crosslike_leftpull": lambda x: (x.__setitem__((0,1), 1), x.__setitem__((1,0), 1)),
            "lr_signconflict_crosspull": lambda x: (x.__setitem__((2,2), -1), x.__setitem__((1,0), 1)),
            "lr_rightweak_bottombridge": lambda x: (x.__setitem__((1,2), 0), x.__setitem__((2,1), 1)),
            "lr_columncollapse_leftfoot": lambda x: (x.__setitem__((0,2), 0), x.__setitem__((1,2), 0), x.__setitem__((2,0), 1)),
            "lr_leftcolumn_decoy": lambda x: (x.__setitem__((0,0), 1), x.__setitem__((1,0), 1)),
        }
    elif label == "cross_left":
        defs = {
            "xl_lefttail_drop_rightdecoy": lambda x: (x.__setitem__((2,0), 0), x.__setitem__((2,2), 1)),
            "xl_midleft_drop_midright_decoy": lambda x: (x.__setitem__((1,0), 0), x.__setitem__((1,2), 1)),
            "xl_topleft_drop_topright_decoy": lambda x: (x.__setitem__((0,0), 0), x.__setitem__((0,2), 1)),
            "xl_bridge_right_pull": lambda x: (x.__setitem__((2,0), 0), x.__setitem__((0,1), 1), x.__setitem__((1,2), 1)),
            "xl_signconflict_rightfoot": lambda x: (x.__setitem__((2,0), -1), x.__setitem__((2,2), 1)),
            "xl_leftweak_bottombridge": lambda x: (x.__setitem__((1,0), 0), x.__setitem__((2,1), 1)),
            "xl_columncollapse_rightfoot": lambda x: (x.__setitem__((0,0), 0), x.__setitem__((1,0), 0), x.__setitem__((2,2), 1)),
            "xl_midrow_swap": lambda x: x.__setitem__((1, slice(None)), np.array([0,1,1])),
        }
    else:
        defs = {
            "ll_spinedrop_crossrightdecoy": lambda x: (x.__setitem__((1,0), 0), x.__setitem__((1,2), 1)),
            "ll_footdrop_rightfootdecoy": lambda x: (x.__setitem__((2,0), 0), x.__setitem__((2,2), 1)),
            "ll_topdrop_toprightdecoy": lambda x: (x.__setitem__((0,0), 0), x.__setitem__((0,2), 1)),
            "ll_crosslike_rightpull": lambda x: (x.__setitem__((0,1), 1), x.__setitem__((1,2), 1)),
            "ll_signconflict_crosspull": lambda x: (x.__setitem__((2,0), -1), x.__setitem__((1,2), 1)),
            "ll_leftweak_bottombridge": lambda x: (x.__setitem__((1,0), 0), x.__setitem__((2,1), 1)),
            "ll_columncollapse_rightfoot": lambda x: (x.__setitem__((0,0), 0), x.__setitem__((1,0), 0), x.__setitem__((2,2), 1)),
            "ll_rightcolumn_decoy": lambda x: (x.__setitem__((0,2), 1), x.__setitem__((1,2), 1)),
        }
    for name, fn in defs.items():
        x = a.copy()
        fn(x)
        out.append((name, x))
    return out

def sigma_v4_perturbations(label: str, a: np.ndarray):
    out = []
    if label == "cross_right":
        defs = {
            "xr_dual_anchor_conflict": lambda x: (x.__setitem__((0,0), 1), x.__setitem__((2,2), 0)),
            "xr_right_spine_and_tail_drop": lambda x: (x.__setitem__((1,2), 0), x.__setitem__((2,2), 0)),
            "xr_cross_to_L_tension": lambda x: (x.__setitem__((0,2), 0), x.__setitem__((2,0), 1)),
            "xr_left_column_decoy": lambda x: (x.__setitem__((1,0), 1), x.__setitem__((0,0), 1)),
            "xr_topcenter_preserve_right_decay": lambda x: (x.__setitem__((0,2), 0), x.__setitem__((1,2), 0)),
            "xr_bottom_bridge_left_pull": lambda x: (x.__setitem__((2,1), 1), x.__setitem__((2,0), 1)),
            "xr_sign_inversion_with_left_foot": lambda x: (x.__setitem__((2,2), -1), x.__setitem__((2,0), 1)),
            "xr_full_midrow_swap": lambda x: x.__setitem__((1, slice(None)), np.array([1,1,0])),
            "xr_hollow_right_corner": lambda x: (x.__setitem__((0,2), 0), x.__setitem__((2,2), 0)),
            "xr_rightness_under_occlusion": lambda x: (x.__setitem__((0,2), 0), x.__setitem__((1,2), 0), x.__setitem__((2,2), 1)),
        }
    elif label == "L_right":
        defs = {
            "lr_cross_decoy_topcenter_midleft": lambda x: (x.__setitem__((0,1), 1), x.__setitem__((1,0), 1)),
            "lr_right_spine_drop_left_foot": lambda x: (x.__setitem__((1,2), 0), x.__setitem__((2,0), 1)),
            "lr_right_top_drop_left_top": lambda x: (x.__setitem__((0,2), 0), x.__setitem__((0,0), 1)),
            "lr_crossbar_pull": lambda x: (x.__setitem__((1,0), 1), x.__setitem__((1,1), 1)),
            "lr_sign_inversion_cross_pull": lambda x: (x.__setitem__((2,2), -1), x.__setitem__((1,0), 1)),
            "lr_column_collapse_left_decoy": lambda x: (x.__setitem__((0,2), 0), x.__setitem__((1,2), 0), x.__setitem__((2,0), 1)),
            "lr_upper_right_occlusion": lambda x: (x.__setitem__((0,2), 0), x.__setitem__((1,2), 1)),
            "lr_footdrop_bridgebias": lambda x: (x.__setitem__((2,2), 0), x.__setitem__((2,1), 1)),
            "lr_dual_side_pull": lambda x: (x.__setitem__((0,0), 1), x.__setitem__((1,0), 1)),
            "lr_midrow_swap": lambda x: x.__setitem__((1, slice(None)), np.array([1,0,0])),
        }
    elif label == "cross_left":
        defs = {
            "xl_dual_anchor_conflict": lambda x: (x.__setitem__((0,2), 1), x.__setitem__((2,0), 0)),
            "xl_left_spine_and_tail_drop": lambda x: (x.__setitem__((1,0), 0), x.__setitem__((2,0), 0)),
            "xl_cross_to_L_tension": lambda x: (x.__setitem__((0,0), 0), x.__setitem__((2,2), 1)),
            "xl_right_column_decoy": lambda x: (x.__setitem__((1,2), 1), x.__setitem__((0,2), 1)),
            "xl_topcenter_preserve_left_decay": lambda x: (x.__setitem__((0,0), 0), x.__setitem__((1,0), 0)),
            "xl_bottom_bridge_right_pull": lambda x: (x.__setitem__((2,1), 1), x.__setitem__((2,2), 1)),
            "xl_sign_inversion_with_right_foot": lambda x: (x.__setitem__((2,0), -1), x.__setitem__((2,2), 1)),
            "xl_full_midrow_swap": lambda x: x.__setitem__((1, slice(None)), np.array([0,1,1])),
            "xl_hollow_left_corner": lambda x: (x.__setitem__((0,0), 0), x.__setitem__((2,0), 0)),
            "xl_leftness_under_occlusion": lambda x: (x.__setitem__((0,0), 0), x.__setitem__((1,0), 0), x.__setitem__((2,0), 1)),
        }
    else:
        defs = {
            "ll_cross_decoy_topcenter_midright": lambda x: (x.__setitem__((0,1), 1), x.__setitem__((1,2), 1)),
            "ll_left_spine_drop_right_foot": lambda x: (x.__setitem__((1,0), 0), x.__setitem__((2,2), 1)),
            "ll_left_top_drop_right_top": lambda x: (x.__setitem__((0,0), 0), x.__setitem__((0,2), 1)),
            "ll_crossbar_pull": lambda x: (x.__setitem__((1,2), 1), x.__setitem__((1,1), 1)),
            "ll_sign_inversion_cross_pull": lambda x: (x.__setitem__((2,0), -1), x.__setitem__((1,2), 1)),
            "ll_column_collapse_right_decoy": lambda x: (x.__setitem__((0,0), 0), x.__setitem__((1,0), 0), x.__setitem__((2,2), 1)),
            "ll_upper_left_occlusion": lambda x: (x.__setitem__((0,0), 0), x.__setitem__((1,0), 1)),
            "ll_footdrop_bridgebias": lambda x: (x.__setitem__((2,0), 0), x.__setitem__((2,1), 1)),
            "ll_dual_side_pull": lambda x: (x.__setitem__((0,2), 1), x.__setitem__((1,2), 1)),
            "ll_midrow_swap": lambda x: x.__setitem__((1, slice(None)), np.array([0,0,1])),
        }
    for name, fn in defs.items():
        x = a.copy()
        fn(x)
        out.append((name, x))
    return out

def generate_samples():
    out = []
    for label, arr in BASE_TEMPLATES.items():
        for name, x in sigma_v2_perturbations(arr):
            out.append(Sample("sigma_v2", label, name, x.copy()))
        for name, x in sigma_v3_perturbations(label, arr):
            out.append(Sample("sigma_v3", label, name, x.copy()))
        for name, x in sigma_v4_perturbations(label, arr):
            out.append(Sample("sigma_v4", label, name, x.copy()))
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
    feat["top_center"] = cell(0,1)
    feat["mid_left"] = cell(1,0)
    feat["mid_right"] = cell(1,2)
    feat["left_column_strength"] = cell(0,0)+cell(1,0)+cell(2,0)
    feat["right_column_strength"] = cell(0,2)+cell(1,2)+cell(2,2)
    feat["crossness"] = feat["top_center"] + feat["mid_left"] + feat["mid_right"] + 0.5*cell(1,1)
    feat["l_leftness"] = feat["left_column_strength"] + feat["bottom_left"] - feat["top_center"] - feat["mid_right"]
    feat["l_rightness"] = feat["right_column_strength"] + feat["bottom_right"] - feat["top_center"] - feat["mid_left"]
    whole_best = {}
    for rec in whole["all"]:
        if rec["proto"] not in whole_best or rec["score"] > whole_best[rec["proto"]]["score"]:
            whole_best[rec["proto"]] = rec
    block_best = {}
    for rec in block["all"]:
        if rec["proto"] not in block_best or rec["score"] > block_best[rec["proto"]]["score"]:
            block_best[rec["proto"]] = rec
    PRE.append({
        "surface": s.surface,
        "label": s.label,
        "perturbation": s.perturbation,
        "feat": feat,
        "whole_top": whole["all"][0]["proto"],
        "block_top": block["all"][0]["proto"],
        "whole_best": {k: {"confidence": float(v["confidence"])} for k,v in whole_best.items()},
        "block_best": {k: {"confidence": float(v["confidence"])} for k,v in block_best.items()},
    })

# Async architecture knobs
SIDE_WORKER_MODE = ["direct_delta", "thesis_antithesis", "column_bias"]
SHAPE_WORKER_MODE = ["crossness_vs_L", "family_contrast", "side_conditioned"]
RESOLVER_MODE = ["sum", "veto", "tension_gated"]
SYNC_MODE = ["parallel_join", "side_priority", "shape_priority"]
CONF_GATE = [0.35, 0.55]
VETO_STRENGTH = [0.0, 0.2, 0.4]
RIGHT_BIAS = [0.0, 0.08]
WHOLE_BLOCK_BLEND = [0.55, 0.65]

def hypothesis_scores(pre, policy):
    f = pre["feat"]
    wb = pre["whole_best"]
    bb = pre["block_best"]
    blend = policy["whole_block_blend"]

    proto_base = {}
    for proto in LABELS:
        g = wb.get(proto, {"confidence": -99.0})["confidence"]
        b = bb.get(proto, {"confidence": -99.0})["confidence"]
        proto_base[proto] = blend*g + (1.0-blend)*b + 0.08*(g*b)

    # side workers
    if policy["side_worker"] == "direct_delta":
        left = max(0.0, f["left_anchor"] - f["right_anchor"]) + 0.5*max(0.0, f["bottom_left"] - f["bottom_right"])
        right = max(0.0, f["right_anchor"] - f["left_anchor"]) + 0.5*max(0.0, f["bottom_right"] - f["bottom_left"])
    elif policy["side_worker"] == "thesis_antithesis":
        left = 1.00*f["left_anchor"] + 0.70*f["bottom_left"] - 0.80*max(0.0, f["right_anchor"] - f["left_anchor"])
        right = 1.00*f["right_anchor"] + 0.70*f["bottom_right"] - 0.80*max(0.0, f["left_anchor"] - f["right_anchor"])
    else:  # column_bias
        left = f["left_column_strength"] + 0.4*f["bottom_left"] - 0.5*max(0.0, f["right_column_strength"] - f["left_column_strength"])
        right = f["right_column_strength"] + 0.4*f["bottom_right"] - 0.5*max(0.0, f["left_column_strength"] - f["right_column_strength"])

    right += policy["right_bias"]

    # shape workers inside each side
    if policy["shape_worker"] == "crossness_vs_L":
        shape_left_cross = f["crossness"]; shape_left_L = f["l_leftness"]
        shape_right_cross = f["crossness"]; shape_right_L = f["l_rightness"]
    elif policy["shape_worker"] == "family_contrast":
        shape_left_cross = f["crossness"] - 0.6*max(0.0, f["l_leftness"])
        shape_left_L = f["l_leftness"] - 0.5*max(0.0, f["crossness"])
        shape_right_cross = f["crossness"] - 0.6*max(0.0, f["l_rightness"])
        shape_right_L = f["l_rightness"] - 0.5*max(0.0, f["crossness"])
    else:  # side_conditioned
        shape_left_cross = f["crossness"] + 0.2*max(0.0, f["left_anchor"] - f["right_anchor"])
        shape_left_L = f["l_leftness"] + 0.2*max(0.0, f["bottom_left"] - f["bottom_right"])
        shape_right_cross = f["crossness"] + 0.2*max(0.0, f["right_anchor"] - f["left_anchor"])
        shape_right_L = f["l_rightness"] + 0.2*max(0.0, f["bottom_right"] - f["bottom_left"])

    # async worker outputs per hypothesis
    hyp = {
        "cross_left": proto_base["cross_left"] + left + shape_left_cross,
        "L_left": proto_base["L_left"] + left + shape_left_L,
        "cross_right": proto_base["cross_right"] + right + shape_right_cross,
        "L_right": proto_base["L_right"] + right + shape_right_L,
    }

    # sync mode / resolver
    if policy["sync_mode"] == "side_priority":
        side_gap = abs(left - right)
        if side_gap >= policy["conf_gate"]:
            if left >= right:
                hyp["cross_right"] -= 0.5
                hyp["L_right"] -= 0.5
            else:
                hyp["cross_left"] -= 0.5
                hyp["L_left"] -= 0.5
    elif policy["sync_mode"] == "shape_priority":
        lshape = max(shape_left_cross, shape_left_L)
        rshape = max(shape_right_cross, shape_right_L)
        shape_gap = abs(lshape - rshape)
        if shape_gap >= policy["conf_gate"]:
            if lshape >= rshape:
                hyp["cross_right"] -= 0.35
                hyp["L_right"] -= 0.35
            else:
                hyp["cross_left"] -= 0.35
                hyp["L_left"] -= 0.35

    if policy["resolver"] == "veto":
        dm = f["directional_margin"]
        if dm < 0:
            hyp["cross_left"] -= policy["veto_strength"] + 0.10*abs(dm)
            hyp["L_left"] -= policy["veto_strength"] + 0.10*abs(dm)
        elif dm > 0:
            hyp["cross_right"] -= policy["veto_strength"] + 0.10*abs(dm)
            hyp["L_right"] -= policy["veto_strength"] + 0.10*abs(dm)
    elif policy["resolver"] == "tension_gated":
        tension = abs(left - right)
        if tension < policy["conf_gate"]:
            # penalize hypotheses with larger side contradiction
            hyp["cross_left"] -= 0.2*max(0.0, f["right_anchor"] - f["left_anchor"])
            hyp["L_left"] -= 0.2*max(0.0, f["right_anchor"] - f["left_anchor"])
            hyp["cross_right"] -= 0.2*max(0.0, f["left_anchor"] - f["right_anchor"])
            hyp["L_right"] -= 0.2*max(0.0, f["left_anchor"] - f["right_anchor"])

    return hyp

POLICIES = []
for vals in itertools.product(SIDE_WORKER_MODE, SHAPE_WORKER_MODE, RESOLVER_MODE, SYNC_MODE, CONF_GATE, VETO_STRENGTH, RIGHT_BIAS, WHOLE_BLOCK_BLEND):
    POLICIES.append({
        "side_worker": vals[0],
        "shape_worker": vals[1],
        "resolver": vals[2],
        "sync_mode": vals[3],
        "conf_gate": vals[4],
        "veto_strength": vals[5],
        "right_bias": vals[6],
        "whole_block_blend": vals[7],
    })

results = []
for idx, pol in enumerate(POLICIES):
    surf_stats = {}
    total_ok = 0
    total_n = 0
    total_mirror = 0
    total_rr = 0
    for surf in ["sigma_v2","sigma_v3","sigma_v4"]:
        sub = [x for x in PRE if x["surface"] == surf]
        ok = 0; mir = 0; rr = 0
        for x in sub:
            hyp = hypothesis_scores(x, pol)
            pred = max(hyp.items(), key=lambda kv: kv[1])[0]
            if pred == x["label"]:
                ok += 1
            if (x["label"], pred) in {
                ("cross_left","cross_right"),
                ("cross_right","cross_left"),
                ("L_left","L_right"),
                ("L_right","L_left"),
            }:
                mir += 1
            if (x["label"], pred) in {
                ("cross_right","cross_left"),
                ("L_right","cross_left"),
            }:
                rr += 1
        n = len(sub)
        surf_stats[surf] = {"acc": round(100.0*ok/n,2), "mirror": mir, "rr": rr}
        total_ok += ok; total_n += n; total_mirror += mir; total_rr += rr
    mean_acc = sum(v["acc"] for v in surf_stats.values()) / 3.0
    std_acc = (sum((v["acc"]-mean_acc)**2 for v in surf_stats.values())/3.0) ** 0.5
    composite = mean_acc - 0.8*total_rr - 0.25*total_mirror - 0.5*std_acc
    results.append({
        "policy_id": idx,
        "policy": pol,
        "surfaces": surf_stats,
        "mean_acc": round(mean_acc, 2),
        "std_acc": round(std_acc, 2),
        "total_mirror": total_mirror,
        "total_rr": total_rr,
        "composite": round(composite, 3),
    })

results.sort(key=lambda r: (-r["composite"], -r["mean_acc"], r["total_rr"], r["total_mirror"], r["std_acc"]))

out = {
    "search_space_size": len(POLICIES),
    "top_20": results[:20],
    "best_policy": results[0],
}
out_path = BASE / "tq2_async_arch_search_results_2026-03-30ec.json"
out_path.write_text(json.dumps(out, indent=2), encoding="utf-8")
print(out_path)


"""
TQ2 slow reference semantics — RB-2R_v2
Version: 2026-03-29e

This version adds:
- majority-sign sanity fallback for trivial polarity tasks
- margin-aware confidence gating
- asymmetric local/global arbitration
- agreement shortcut

It remains a transparent lab reference, not an optimized kernel.
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Dict, List, Tuple, Callable, Any
import numpy as np

T_VALUES = (-1, 0, 1)


@dataclass(frozen=True)
class Block:
    values: Tuple[int, ...]
    axis: str = "row"
    index: int = 0

    def __post_init__(self):
        if any(v not in T_VALUES for v in self.values):
            raise ValueError("Block values must lie in {-1, 0, 1}")


@dataclass(frozen=True)
class Plane:
    data: Tuple[Tuple[int, int, int], Tuple[int, int, int], Tuple[int, int, int]]
    label: str = ""

    def __post_init__(self):
        if len(self.data) != 3 or any(len(row) != 3 for row in self.data):
            raise ValueError("Plane must be 3x3")
        if any(v not in T_VALUES for row in self.data for v in row):
            raise ValueError("Plane values must lie in {-1, 0, 1}")

    def array(self) -> np.ndarray:
        return np.array(self.data, dtype=int)


def plane_from_array(a: np.ndarray, label: str = "") -> Plane:
    a = np.asarray(a, dtype=int)
    return Plane(tuple(tuple(int(x) for x in row) for row in a), label=label)


# ----------------------------
# Cheap closed transform family
# ----------------------------

def identity(a: np.ndarray) -> np.ndarray:
    return np.asarray(a).copy()

def rot90(a: np.ndarray) -> np.ndarray:
    return np.rot90(a, k=1)

def rot180(a: np.ndarray) -> np.ndarray:
    return np.rot90(a, k=2)

def rot270(a: np.ndarray) -> np.ndarray:
    return np.rot90(a, k=3)

def refl_h(a: np.ndarray) -> np.ndarray:
    return np.flipud(a)

def refl_v(a: np.ndarray) -> np.ndarray:
    return np.fliplr(a)

def refl_diag(a: np.ndarray) -> np.ndarray:
    return np.asarray(a).T

def refl_anti(a: np.ndarray) -> np.ndarray:
    return np.fliplr(np.flipud(a)).T


WHOLE_PLANE_TRANSFORMS: Dict[str, Callable[[np.ndarray], np.ndarray]] = {
    "I": identity,
    "R90": rot90,
    "R180": rot180,
    "R270": rot270,
    "FH": refl_h,
    "FV": refl_v,
    "FD": refl_diag,
    "FAD": refl_anti,
}


def similarity(a: np.ndarray, b: np.ndarray) -> int:
    return int(np.sum(np.asarray(a, dtype=int) * np.asarray(b, dtype=int)))


@dataclass
class Prototype:
    name: str
    plane: Plane
    metadata: Dict[str, Any]


def default_prototypes() -> List[Prototype]:
    return [
        Prototype(
            "cross",
            plane_from_array(np.array([[0, 1, 0],
                                      [1, 1, 1],
                                      [0, 1, 0]]), label="cross"),
            {"kind": "global_geometric"},
        ),
        Prototype(
            "diag",
            plane_from_array(np.array([[1, 0, 0],
                                      [0, 1, 0],
                                      [0, 0, 1]]), label="diag"),
            {"kind": "global_geometric"},
        ),
        Prototype(
            "bars",
            plane_from_array(np.array([[1, 1, 1],
                                      [0, 0, 0],
                                      [-1, -1, -1]]), label="bars"),
            {"kind": "global_polarity"},
        ),
        Prototype(
            "checker",
            plane_from_array(np.array([[1, 0, -1],
                                      [0, 1, 0],
                                      [-1, 0, 1]]), label="checker"),
            {"kind": "local_compositional"},
        ),
        Prototype(
            "L",
            plane_from_array(np.array([[1, 0, 0],
                                      [1, 0, 0],
                                      [1, 1, 1]]), label="L"),
            {"kind": "global_shape"},
        ),
    ]


def score_blockwise(plane: Plane, prototypes: List[Prototype], axis: str = "row") -> Dict[str, Any]:
    arr = plane.array()
    best = None
    records = []

    for proto in prototypes:
        p = proto.plane.array()
        total_score = 0
        block_records = []

        for i in range(3):
            block = arr[i, :] if axis == "row" else arr[:, i]
            proto_block = p[i, :] if axis == "row" else p[:, i]

            best_block = None
            for shift in (-1, 0, 1):
                for sign in (-1, 1):
                    candidate = sign * np.roll(proto_block, shift)
                    raw = int(np.sum(block * candidate))
                    rec = {
                        "block_index": i,
                        "shift": shift,
                        "sign": sign,
                        "score": raw,
                    }
                    if best_block is None or raw > best_block["score"]:
                        best_block = rec

            total_score += best_block["score"]
            block_records.append(best_block)

        confidence = total_score / 9.0
        rec = {
            "proto": proto.name,
            "score": total_score,
            "confidence": confidence,
            "axis": axis,
            "blocks": block_records,
        }
        records.append(rec)
        if best is None or rec["score"] > best["score"]:
            best = rec

    return {"best": best, "all": sorted(records, key=lambda x: x["score"], reverse=True)}


def score_wholeplane(plane: Plane, prototypes: List[Prototype]) -> Dict[str, Any]:
    arr = plane.array()
    best = None
    records = []

    for proto in prototypes:
        p = proto.plane.array()
        for t_name, t_fn in WHOLE_PLANE_TRANSFORMS.items():
            transformed = t_fn(p)
            raw = similarity(arr, transformed)
            confidence = raw / 9.0
            rec = {
                "proto": proto.name,
                "transform": t_name,
                "score": raw,
                "confidence": confidence,
            }
            records.append(rec)
            if best is None or rec["score"] > best["score"]:
                best = rec

    return {"best": best, "all": sorted(records, key=lambda x: x["score"], reverse=True)}


def majority_sign_fallback(plane: Plane) -> str:
    s = int(plane.array().sum())
    return "pos" if s > 0 else "neg" if s < 0 else "neu"


def reconcile_scores_v2(
    local_result: Dict[str, Any],
    global_result: Dict[str, Any],
    polarity_fallback: str | None = None,
    local_dom_threshold: float = 0.35,
    global_dom_threshold: float = 0.20,
) -> Dict[str, Any]:
    local_all = local_result["all"]
    global_all = global_result["all"]
    local_best = local_all[0]
    global_best = global_all[0]

    local_margin = local_all[0]["score"] - local_all[1]["score"] if len(local_all) > 1 else local_all[0]["score"]
    global_margin = global_all[0]["score"] - global_all[1]["score"] if len(global_all) > 1 else global_all[0]["score"]

    local_conf = local_best["confidence"] + 0.08 * local_margin
    global_conf = global_best["confidence"] + 0.05 * global_margin

    agreement = local_best["proto"] == global_best["proto"]

    if agreement:
        mode = "agreement-shortcut"
        chosen = local_best["proto"]
    elif local_conf - global_conf > local_dom_threshold:
        mode = "local-first"
        chosen = local_best["proto"]
    elif global_conf - local_conf > global_dom_threshold:
        mode = "global-first"
        chosen = global_best["proto"]
    elif polarity_fallback is not None:
        mode = "polarity-fallback"
        chosen = polarity_fallback
    elif global_best["confidence"] >= 0.55 and local_margin <= 1:
        mode = "global-bias"
        chosen = global_best["proto"]
    else:
        mode = "local-bias"
        chosen = local_best["proto"]

    fused_conf = max(local_conf, global_conf) if not agreement else (local_conf + global_conf) / 2.0

    return {
        "mode": mode,
        "proto": chosen,
        "fused_confidence": round(float(fused_conf), 4),
        "agreement": agreement,
        "local": local_best,
        "global": global_best,
        "local_margin": local_margin,
        "global_margin": global_margin,
        "local_aug_conf": round(float(local_conf), 4),
        "global_aug_conf": round(float(global_conf), 4),
    }


def score_hybrid_v2(
    plane: Plane,
    prototypes: List[Prototype],
    axis: str = "row",
) -> Dict[str, Any]:
    local_result = score_blockwise(plane, prototypes, axis=axis)
    global_result = score_wholeplane(plane, prototypes)

    labelset = {p.name for p in prototypes}
    polarity_fallback = None
    if labelset == {"pos", "neg", "neu"}:
        polarity_fallback = majority_sign_fallback(plane)

    reconciled = reconcile_scores_v2(
        local_result=local_result,
        global_result=global_result,
        polarity_fallback=polarity_fallback,
    )

    return {
        "local_result": local_result,
        "global_result": global_result,
        "reconciled": reconciled,
    }


def project_output_v2(result: Dict[str, Any]) -> Dict[str, Any]:
    rec = result["reconciled"]
    return {
        "predicted_label": rec["proto"],
        "mode": rec["mode"],
        "confidence": rec["fused_confidence"],
        "support": {
            "local_proto": rec["local"]["proto"],
            "local_conf": rec["local"]["confidence"],
            "global_proto": rec["global"]["proto"],
            "global_conf": rec["global"]["confidence"],
            "agreement": rec["agreement"],
            "local_margin": rec["local_margin"],
            "global_margin": rec["global_margin"],
        },
    }


def integrated_infer_v2(
    plane: Plane,
    prototypes: List[Prototype] | None = None,
    axis: str = "row",
) -> Dict[str, Any]:
    if prototypes is None:
        prototypes = default_prototypes()
    hybrid = score_hybrid_v2(plane, prototypes, axis=axis)
    projection = project_output_v2(hybrid)
    return {
        "input_plane": plane.data,
        "hybrid": hybrid,
        "projection": projection,
    }

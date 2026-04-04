
"""
TQ2 slow reference semantics
Version: 2026-03-29d

Purpose:
- provide executable reference semantics for the integrated TQ2 runtime
- keep everything inside the cheap closed operator family
- make whole-plane, blockwise, and hybrid reconciliation explicit

This is intentionally slow and transparent. It is a lab reference, not an optimized kernel.
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Dict, List, Tuple, Callable, Any
import numpy as np

T_VALUES = (-1, 0, 1)


def clamp_ternary(x: int) -> int:
    return max(-1, min(1, int(x)))


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

    def row_block(self, idx: int) -> Block:
        return Block(tuple(int(x) for x in self.data[idx]), axis="row", index=idx)

    def col_block(self, idx: int) -> Block:
        arr = self.array()
        return Block(tuple(int(x) for x in arr[:, idx]), axis="col", index=idx)


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


def shift_block(values: Tuple[int, ...], k: int) -> Tuple[int, ...]:
    arr = np.asarray(values, dtype=int)
    return tuple(int(x) for x in np.roll(arr, k))


def signed_shift_block(values: Tuple[int, ...], k: int = 0, sign: int = 1) -> Tuple[int, ...]:
    shifted = np.roll(np.asarray(values, dtype=int), k)
    return tuple(int(sign * x) for x in shifted)


def similarity(a: np.ndarray, b: np.ndarray) -> int:
    return int(np.sum(np.asarray(a, dtype=int) * np.asarray(b, dtype=int)))


# ----------------------------
# Prototype / radical carrier
# ----------------------------

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


# ----------------------------
# Reference semantics
# ----------------------------

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


def reconcile_scores(
    local_result: Dict[str, Any],
    global_result: Dict[str, Any],
    alpha: float = 0.5,
    beta: float = 0.5,
    contradiction_penalty: float = 0.15,
    mode_threshold: float = 0.18,
) -> Dict[str, Any]:
    local_best = local_result["best"]
    global_best = global_result["best"]

    local_conf = local_best["confidence"]
    global_conf = global_best["confidence"]
    same_proto = local_best["proto"] == global_best["proto"]

    contradiction = 0.0
    if not same_proto:
        contradiction = contradiction_penalty * (
            abs(local_conf - global_conf) + min(local_conf, global_conf)
        )

    fused_conf = alpha * local_conf + beta * global_conf - contradiction

    if local_conf - global_conf > mode_threshold:
        mode = "local-first"
        chosen_proto = local_best["proto"]
    elif global_conf - local_conf > mode_threshold:
        mode = "global-first"
        chosen_proto = global_best["proto"]
    else:
        mode = "mixed"
        if same_proto:
            chosen_proto = local_best["proto"]
        else:
            chosen_proto = local_best["proto"] if local_conf >= global_conf else global_best["proto"]

    return {
        "mode": mode,
        "proto": chosen_proto,
        "fused_confidence": round(float(fused_conf), 4),
        "local": local_best,
        "global": global_best,
        "agreement": same_proto,
        "contradiction_penalty": round(float(contradiction), 4),
    }


def score_hybrid(
    plane: Plane,
    prototypes: List[Prototype],
    axis: str = "row",
    alpha: float = 0.5,
    beta: float = 0.5,
) -> Dict[str, Any]:
    local_result = score_blockwise(plane, prototypes, axis=axis)
    global_result = score_wholeplane(plane, prototypes)
    reconciled = reconcile_scores(local_result, global_result, alpha=alpha, beta=beta)
    return {
        "local_result": local_result,
        "global_result": global_result,
        "reconciled": reconciled,
    }


def project_output(result: Dict[str, Any]) -> Dict[str, Any]:
    rec = result["reconciled"]
    mode = rec["mode"]

    if mode == "local-first":
        rationale = "local/compositional evidence dominated"
    elif mode == "global-first":
        rationale = "global/geometric evidence dominated"
    else:
        rationale = "local and global evidence were fused"

    return {
        "predicted_label": rec["proto"],
        "mode": mode,
        "confidence": rec["fused_confidence"],
        "rationale": rationale,
        "support": {
            "local_proto": rec["local"]["proto"],
            "local_conf": rec["local"]["confidence"],
            "global_proto": rec["global"]["proto"],
            "global_conf": rec["global"]["confidence"],
            "agreement": rec["agreement"],
        },
    }


def integrated_infer(
    plane: Plane,
    prototypes: List[Prototype] | None = None,
    axis: str = "row",
    alpha: float = 0.5,
    beta: float = 0.5,
) -> Dict[str, Any]:
    if prototypes is None:
        prototypes = default_prototypes()
    hybrid = score_hybrid(plane, prototypes, axis=axis, alpha=alpha, beta=beta)
    projection = project_output(hybrid)
    return {
        "input_plane": plane.data,
        "hybrid": hybrid,
        "projection": projection,
    }

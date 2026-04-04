
"""
TQ2 slow reference semantics — RB-2R_v3
Version: 2026-03-29f

This version introduces metadata-aware mode gating on top of RB-2R_v2.

Idea:
- if the prototype family is clearly polarity-only, use polarity fallback
- if the prototype family is global-only, route to the whole-plane specialist
- otherwise defer to the stronger compromise runtime (RB-2R_v2)

This remains a transparent lab reference.
"""

from __future__ import annotations


def prototype_profile(prototypes):
    names = {p.name for p in prototypes}
    all_have_dual = all(
        ("global" in getattr(p, "metadata", {}) and "local" in getattr(p, "metadata", {}))
        for p in prototypes
    )
    kinds = {getattr(p, "metadata", {}).get("kind", "") for p in prototypes}
    all_globalish = all(k.startswith("global") or k == "" for k in kinds)
    polarity_set = names == {"pos", "neg", "neu"}

    return {
        "polarity_set": polarity_set,
        "all_have_dual": all_have_dual,
        "all_globalish": all_globalish,
        "kinds": kinds,
        "names": names,
    }


def integrated_infer_v3_meta(
    plane,
    prototypes,
    majority_sign_fallback,
    score_wholeplane,
    integrated_infer_v2,
):
    prof = prototype_profile(prototypes)

    if prof["polarity_set"]:
        pred = majority_sign_fallback(plane)
        return {
            "projection": {
                "predicted_label": pred,
                "mode": "meta-polarity-fallback",
                "confidence": 1.0,
            }
        }

    if prof["all_globalish"] and not prof["all_have_dual"]:
        best = score_wholeplane(plane, prototypes)["best"]
        return {
            "projection": {
                "predicted_label": best["proto"],
                "mode": "meta-global-gate",
                "confidence": best["confidence"],
            }
        }

    inner = integrated_infer_v2(plane, prototypes)
    inner["projection"]["mode"] = "meta->" + inner["projection"]["mode"]
    return inner

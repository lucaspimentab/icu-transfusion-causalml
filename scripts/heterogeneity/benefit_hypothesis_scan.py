from __future__ import annotations

import argparse
import json
import sys
from itertools import product
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scripts.common.target_trial_utils import (  # noqa: E402
    bootstrap_ci,
    load_trial_config,
    output_root,
    read_json,
    rule_mask,
    rule_to_text,
    save_table,
    write_json,
)


def _available(df: pd.DataFrame, cols: list[str]) -> list[str]:
    return [c for c in cols if c in df.columns and pd.api.types.is_numeric_dtype(df[c])]


def _thresholds(df: pd.DataFrame, col: str, qs: list[float]) -> list[float]:
    x = pd.to_numeric(df[col], errors="coerce").dropna()
    if x.nunique() < 4:
        return []
    return sorted({float(x.quantile(q)) for q in qs if np.isfinite(float(x.quantile(q)))})


def _cond(feature: str, op: str, threshold: float) -> dict[str, Any]:
    return {"feature": feature, "op": op, "threshold": float(threshold)}


def build_benefit_hypothesis_rules(discovery: pd.DataFrame) -> list[list[dict[str, Any]]]:
    anemia = _available(
        discovery,
        [
            "hemoglobin_last",
            "hemoglobin_median",
            "hemoglobin_min",
            "hemoglobin_mean",
            "hemoglobin_slope",
            "hemoglobin_delta",
        ],
    )
    lower_severity = _available(discovery, ["sofa_mean", "sofa_median", "sofa_max", "lactate_mean", "lactate_max", "creatinine_mean", "creatinine_max"])
    preserved_perfusion = _available(discovery, ["mbp_mean", "mbp_median", "mbp_min", "mbp_last", "spo2_min", "spo2_mean", "spo2_last"])
    stable_oxygen = _available(discovery, ["spo2_std", "spo2_slope"])
    lower_support = _available(discovery, ["any_vasopressor_mean", "any_vasopressor_max", "ventilation_on_mean", "ventilation_on_max"])

    anemia_rules: list[dict[str, Any]] = []
    for col in anemia:
        if col in {"hemoglobin_slope", "hemoglobin_delta"}:
            for thr in _thresholds(discovery, col, [0.25, 0.50]):
                anemia_rules.append(_cond(col, "<=", thr))
        else:
            for thr in _thresholds(discovery, col, [0.25, 0.50]):
                anemia_rules.append(_cond(col, "<=", thr))

    lower_severity_rules: list[dict[str, Any]] = []
    for col in lower_severity:
        for thr in _thresholds(discovery, col, [0.50, 0.75]):
            lower_severity_rules.append(_cond(col, "<=", thr))

    perfusion_rules: list[dict[str, Any]] = []
    for col in preserved_perfusion:
        for thr in _thresholds(discovery, col, [0.25, 0.50]):
            perfusion_rules.append(_cond(col, ">", thr))

    stability_rules: list[dict[str, Any]] = []
    for col in stable_oxygen:
        op = "<=" if col.endswith("_std") else ">"
        for thr in _thresholds(discovery, col, [0.50, 0.75]):
            stability_rules.append(_cond(col, op, thr))

    support_rules: list[dict[str, Any]] = []
    for col in lower_support:
        for thr in _thresholds(discovery, col, [0.50, 0.75]):
            support_rules.append(_cond(col, "<=", thr))

    rules: list[list[dict[str, Any]]] = []
    for a, b in product(anemia_rules, lower_severity_rules + perfusion_rules + stability_rules + support_rules):
        if a["feature"] != b["feature"]:
            rules.append([a, b])
    for a, b, c in product(anemia_rules, lower_severity_rules, perfusion_rules + stability_rules + support_rules):
        features = {a["feature"], b["feature"], c["feature"]}
        if len(features) == 3:
            rules.append([a, b, c])
    for a, b in product(lower_severity_rules, perfusion_rules + stability_rules):
        if a["feature"] != b["feature"]:
            rules.append([a, b])

    unique: dict[str, list[dict[str, Any]]] = {}
    for rule in rules:
        key = json.dumps(rule, sort_keys=True)
        unique[key] = rule
    return list(unique.values())


def evaluate_rule(df: pd.DataFrame, rule: list[dict[str, Any]], seed: int, n_boot: int) -> dict[str, Any]:
    sub = df[rule_mask(df, rule)].copy()
    values = sub["aipw_score_ate"].astype(float).to_numpy()
    ci_low, ci_high = bootstrap_ci(values, seed, n_boot)
    return {
        "rule_text": rule_to_text(rule),
        "rule_json": json.dumps(rule, sort_keys=True),
        "n": int(len(sub)),
        "n_treated": int(sub["transfused"].sum()) if "transfused" in sub else 0,
        "n_control": int((1 - sub["transfused"].astype(int)).sum()) if "transfused" in sub and len(sub) else 0,
        "effect_aipw": float(np.nanmean(values)) if len(values) else np.nan,
        "ci95_low": ci_low,
        "ci95_high": ci_high,
    }


def run_benefit_scan(config_dir: str) -> None:
    config = load_trial_config(config_dir)
    out_root = output_root(config)
    proc = out_root / "processed"
    caus = out_root / "causal"
    het = out_root / "heterogeneity"
    metadata = read_json(proc / "target_trial_metadata.json")
    df = pd.read_parquet(proc / "trial_dataset.parquet")
    nuis = pd.read_parquet(caus / "nuisance_predictions.parquet")
    analysis = df.merge(nuis[["stay_id", "aipw_score_ate", "propensity_score"]], on="stay_id", how="left")
    discovery = analysis[analysis["analysis_split"] == "discovery"].copy()
    validation = analysis[analysis["analysis_split"] == "validation"].copy()

    scan = config.get("honest_scan", {})
    seed = int(config["target_trial"].get("seed", 42))
    min_n = int(scan.get("benefit_min_n", scan.get("min_n", 150)))
    min_t = int(scan.get("benefit_min_treated", max(25, int(scan.get("min_treated", 40) * 0.6))))
    min_c = int(scan.get("benefit_min_control", max(50, int(scan.get("min_control", 40)))))
    n_boot = int(scan.get("bootstrap", 200))
    max_rules = int(scan.get("benefit_max_rules", 80))

    rows = []
    for rule in build_benefit_hypothesis_rules(discovery):
        row = evaluate_rule(discovery, rule, seed, n_boot)
        if row["n"] < min_n or row["n_treated"] < min_t or row["n_control"] < min_c:
            continue
        row["discovery_direction"] = "benefit_apparent" if row["effect_aipw"] < 0 else "harm_apparent" if row["effect_aipw"] > 0 else "neutral_apparent"
        rows.append(row)

    all_rules = pd.DataFrame(rows)
    if all_rules.empty:
        save_table(pd.DataFrame(), het / "benefit_hypothesis_scan_all.csv")
        save_table(pd.DataFrame(), het / "benefit_hypothesis_scan_validation.csv")
        print("benefit_hypothesis_scan_complete rules=0")
        return

    all_rules = all_rules.sort_values("effect_aipw", ascending=True).reset_index(drop=True)
    all_rules["rank_benefit"] = np.arange(1, len(all_rules) + 1)
    selected = all_rules[all_rules["effect_aipw"] < 0].head(max_rules).copy()

    val_rows = []
    for _, item in selected.iterrows():
        rule = json.loads(item["rule_json"])
        row = evaluate_rule(validation, rule, seed, n_boot)
        row.update(
            {
                "effect_aipw_discovery": item["effect_aipw"],
                "n_discovery": item["n"],
                "n_treated_discovery": item["n_treated"],
                "n_control_discovery": item["n_control"],
                "discovery_direction": item["discovery_direction"],
                "validation_direction": "benefit_apparent" if row["effect_aipw"] < 0 else "harm_apparent" if row["effect_aipw"] > 0 else "neutral_apparent",
                "validated_same_sign": np.sign(row["effect_aipw"]) == np.sign(float(item["effect_aipw"])),
                "validation_ci_excludes_zero": bool(row["ci95_high"] < 0 or row["ci95_low"] > 0),
            }
        )
        val_rows.append(row)

    validation_out = pd.DataFrame(val_rows)
    save_table(all_rules, het / "benefit_hypothesis_scan_all.csv")
    save_table(selected, het / "benefit_hypothesis_scan_selected.csv")
    save_table(validation_out, het / "benefit_hypothesis_scan_validation.csv")
    write_json(
        het / "benefit_hypothesis_scan_metadata.json",
        {
            "primary_outcome": metadata.get("primary_outcome"),
            "interpretation": "Benefit-focused, clinically constrained discovery; validation split remains the priority.",
            "min_n": min_n,
            "min_treated": min_t,
            "min_control": min_c,
            "selected_rules": int(len(selected)),
        },
    )
    print(f"benefit_hypothesis_scan_complete rules={len(selected)}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Clinically constrained honest scan for candidate benefit subgroups.")
    parser.add_argument("--config-dir", default="configs")
    args = parser.parse_args()
    run_benefit_scan(args.config_dir)


if __name__ == "__main__":
    main()

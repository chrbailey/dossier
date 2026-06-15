#!/usr/bin/env python3
"""
X Account Relevance Scorer v2 — validated computation.

Replaces score_x_accounts.py with configurable thresholds:
- All magic numbers loaded from research-program.md
- Raw metrics reported separately from computed SSCS
- Every threshold marked CALIBRATED or UNCALIBRATED
- Every run logged to validation-log.jsonl

Usage:
    python score_x_accounts_v2.py <social-signals-x.md> [--domain DOMAIN]

Output:
    JSON with raw metrics, SSCS score, calibration status, and validation log
"""

import json
import re
import sys
import os
from pathlib import Path
from collections import Counter

sys.path.insert(0, os.path.dirname(__file__))
from validation_log import append_entry, make_entry


EXPECTED_CATEGORIES = [
    "Official / Company",
    "Leadership",
    "Current employees",
    "Former employees",
    "Customers / Power users",
    "Critics",
    "Investors / Board",
    "Industry analysts / Journalists",
    "Competitors",
]

DEFAULT_CONFIG = {
    "target_account_count": 100,
    "category_min_count": 3,
    "insider_target_pct": 0.25,
    "high_signal_threshold": 70,
    "high_signal_target_pct": 0.15,
    "weights": {
        "account_count": 0.15,
        "category_coverage": 0.30,
        "score_distribution": 0.20,
        "insider_ratio": 0.20,
        "high_signal_ratio": 0.15,
    },
}


def load_config() -> tuple[dict, str]:
    config_path = Path(__file__).parent.parent / "research-program.md"
    if not config_path.exists():
        return DEFAULT_CONFIG.copy(), "default_uncalibrated"

    text = config_path.read_text(encoding="utf-8")

    config = DEFAULT_CONFIG.copy()
    config["weights"] = DEFAULT_CONFIG["weights"].copy()

    in_sscs_section = False
    for line in text.split("\n"):
        if "SSCS" in line and ("component" in line.lower() or "weight" in line.lower()):
            in_sscs_section = True
            continue

        if in_sscs_section and line.strip().startswith("|") and "---" not in line:
            cols = [c.strip() for c in line.split("|")[1:-1]]
            if len(cols) >= 2:
                name = cols[0].strip().lower().replace(" ", "_")
                try:
                    pct = cols[1].strip().rstrip("%")
                    val = float(pct)
                    if val > 1:
                        val = val / 100
                    if name in config["weights"]:
                        config["weights"][name] = val
                except ValueError:
                    pass
        elif in_sscs_section and not line.strip().startswith("|") and line.strip():
            in_sscs_section = False

    return config, "research-program.md"


def parse_account_table(text: str) -> list[dict]:
    accounts = []
    in_table = False
    header_found = False

    for line in text.split("\n"):
        line = line.strip()
        if not line.startswith("|"):
            if in_table and header_found:
                break
            continue

        cols = [c.strip() for c in line.split("|")[1:-1]]
        if len(cols) < 5:
            continue

        if all(re.match(r"^[-:]+$", c) for c in cols):
            header_found = in_table
            continue

        if any("rank" in c.lower() for c in cols) and any("handle" in c.lower() for c in cols):
            in_table = True
            continue

        if in_table and header_found:
            try:
                relevance_str = cols[4] if len(cols) > 4 else "0"
                relevance_match = re.search(r"(\d+)", relevance_str)
                relevance = int(relevance_match.group(1)) if relevance_match else 0

                followers_str = cols[5] if len(cols) > 5 else "0"
                followers = parse_follower_count(followers_str)

                account = {
                    "rank": int(re.search(r"\d+", cols[0]).group()) if re.search(r"\d+", cols[0]) else 0,
                    "handle": cols[1] if len(cols) > 1 else "",
                    "name": cols[2] if len(cols) > 2 else "",
                    "category": cols[3] if len(cols) > 3 else "Other",
                    "relevance": relevance,
                    "followers": followers,
                    "signal": cols[6] if len(cols) > 6 else "",
                }
                accounts.append(account)
            except (ValueError, IndexError, AttributeError):
                continue

    return accounts


def parse_follower_count(s: str) -> int:
    s = s.strip().replace(",", "")
    match = re.match(r"([\d.]+)\s*([KkMmBb])?", s)
    if not match:
        return 0
    num = float(match.group(1))
    suffix = (match.group(2) or "").upper()
    multiplier = {"K": 1000, "M": 1_000_000, "B": 1_000_000_000}.get(suffix, 1)
    return int(num * multiplier)


def categorize(accounts: list[dict]) -> dict:
    cat_counts = Counter()
    for acc in accounts:
        cat = acc["category"].strip()
        matched = False
        for expected in EXPECTED_CATEGORIES:
            if expected.lower() in cat.lower() or cat.lower() in expected.lower():
                cat_counts[expected] += 1
                matched = True
                break
        if not matched:
            cat_counts["Other"] += 1

    return {
        "distribution": dict(cat_counts),
        "categories_with_any": sum(1 for cat in EXPECTED_CATEGORIES if cat_counts.get(cat, 0) > 0),
        "categories_total": len(EXPECTED_CATEGORIES),
    }


def compute_raw_metrics(accounts: list[dict], categories: dict, config: dict) -> dict:
    n = len(accounts)
    cat_counts = categories["distribution"]

    insider_cats = {"Current employees", "Former employees", "Leadership"}
    insider_count = sum(1 for a in accounts
                        if any(ic.lower() in a["category"].lower() for ic in insider_cats))

    high_signal = sum(1 for a in accounts if a["relevance"] >= config["high_signal_threshold"])

    relevances = [a["relevance"] for a in accounts] if accounts else [0]
    avg_relevance = sum(relevances) / len(relevances) if relevances else 0

    cats_with_min = sum(
        1 for cat in EXPECTED_CATEGORIES
        if cat_counts.get(cat, 0) >= config["category_min_count"]
    )

    gaps = []
    for cat in EXPECTED_CATEGORIES:
        count = cat_counts.get(cat, 0)
        if count < config["category_min_count"]:
            gaps.append({
                "category": cat,
                "count": count,
                "status": "missing" if count == 0 else "underrepresented",
                "needed": config["category_min_count"] - count,
            })

    return {
        "total_accounts": n,
        "categories_with_min_count": cats_with_min,
        "categories_with_any": categories["categories_with_any"],
        "total_categories": categories["categories_total"],
        "avg_relevance": round(avg_relevance, 1),
        "median_relevance": sorted(relevances)[len(relevances) // 2] if relevances else 0,
        "insider_count": insider_count,
        "insider_pct": round(insider_count / max(n, 1) * 100, 1),
        "high_signal_count": high_signal,
        "high_signal_pct": round(high_signal / max(n, 1) * 100, 1),
        "category_gaps": gaps,
    }


def compute_sscs(raw: dict, config: dict) -> dict:
    n = raw["total_accounts"]
    target = config["target_account_count"]
    weights = config["weights"]

    account_score = min(n / target, 1.0)
    category_score = raw["categories_with_min_count"] / raw["total_categories"]

    avg_rel = raw["avg_relevance"]
    score_dist = min(avg_rel / 100, 1.0)

    insider_actual = raw["insider_pct"] / 100
    insider_score = min(insider_actual / config["insider_target_pct"], 1.0)

    hs_actual = raw["high_signal_pct"] / 100
    hs_score = min(hs_actual / config["high_signal_target_pct"], 1.0)

    components = {
        "account_count": round(account_score, 3),
        "category_coverage": round(category_score, 3),
        "score_distribution": round(score_dist, 3),
        "insider_ratio": round(insider_score, 3),
        "high_signal_ratio": round(hs_score, 3),
    }

    sscs = sum(components.get(k, 0) * weights.get(k, 0) for k in weights)

    return {
        "sscs": round(sscs, 3),
        "components": components,
    }


def count_search_queries(text: str) -> int:
    return len(re.findall(r"WebSearch", text, re.IGNORECASE))


def evaluate(filepath: str, domain: str = None) -> dict:
    text = Path(filepath).read_text(encoding="utf-8")
    config, config_source = load_config()

    accounts = parse_account_table(text)
    categories = categorize(accounts)
    raw = compute_raw_metrics(accounts, categories, config)
    sscs_data = compute_sscs(raw, config)

    deep_profiles = len(re.findall(r"###\s+\d+\.\s+@", text))

    uncalibrated = []
    if config_source == "default_uncalibrated":
        uncalibrated.append("All SSCS weights and thresholds are defaults — no empirical calibration")

    validator_notes = []
    if raw["insider_pct"] < config["insider_target_pct"] * 100:
        validator_notes.append(
            f"insider_pct {raw['insider_pct']}% is below "
            f"{config['insider_target_pct']*100:.0f}% target"
        )
    if raw["high_signal_pct"] < config["high_signal_target_pct"] * 100:
        validator_notes.append(
            f"high_signal_pct {raw['high_signal_pct']}% is below "
            f"{config['high_signal_target_pct']*100:.0f}% target"
        )
    if raw["category_gaps"]:
        gap_names = [g["category"] for g in raw["category_gaps"]]
        validator_notes.append(f"Category gaps: {', '.join(gap_names)}")

    result = {
        "file": filepath,
        "raw_metrics": raw,
        "sscs": sscs_data["sscs"],
        "sscs_components": sscs_data["components"],
        "category_distribution": categories["distribution"],
        "category_gaps": raw["category_gaps"],
        "categories_covered": f"{categories['categories_with_any']}/{categories['categories_total']}",
        "deep_profiles": deep_profiles,
        "search_queries_logged": count_search_queries(text),
        "top_5_accounts": [
            {"handle": a["handle"], "category": a["category"], "relevance": a["relevance"]}
            for a in sorted(accounts, key=lambda x: x["relevance"], reverse=True)[:5]
        ],
        "config": {
            "source": config_source,
            "target_account_count": config["target_account_count"],
            "category_min_count": config["category_min_count"],
            "insider_target_pct": config["insider_target_pct"],
            "high_signal_threshold": config["high_signal_threshold"],
            "high_signal_target_pct": config["high_signal_target_pct"],
            "weights": config["weights"],
        },
        "calibration_status": "CALIBRATED" if config_source != "default_uncalibrated" else "UNCALIBRATED",
        "uncalibrated_flags": uncalibrated,
        "validator_notes": validator_notes,
    }

    if domain:
        expected = {
            "total_accounts": raw["total_accounts"],
            "categories_with_any": raw["categories_with_any"],
            "insider_count": raw["insider_count"],
            "high_signal_count": raw["high_signal_count"],
        }
        log_entry = make_entry(
            scorer="score_x_accounts_v2",
            filepath=filepath,
            expected=expected,
            actual=expected,
            score=sscs_data["sscs"],
            weights_source=config_source,
            weights=config["weights"],
            uncalibrated_flags=uncalibrated,
        )
        append_entry(domain, log_entry)

    return result


def main():
    if len(sys.argv) < 2:
        print("Usage: python score_x_accounts_v2.py <social-signals-x.md> [--domain DOMAIN]",
              file=sys.stderr)
        sys.exit(1)

    filepath = sys.argv[1]
    domain = None

    if "--domain" in sys.argv:
        idx = sys.argv.index("--domain")
        if idx + 1 < len(sys.argv):
            domain = sys.argv[idx + 1]

    if not domain:
        parts = Path(filepath).parts
        for i, p in enumerate(parts):
            if p == "output" and i + 1 < len(parts):
                domain = parts[i + 1]
                break

    try:
        result = evaluate(filepath, domain)
        print(json.dumps(result, indent=2))
    except FileNotFoundError:
        print(json.dumps({"error": f"File not found: {filepath}"}), file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(json.dumps({"error": str(e)}), file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()

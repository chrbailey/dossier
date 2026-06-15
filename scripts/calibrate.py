#!/usr/bin/env python3
"""
Calibration runner for Dossier scoring systems.

Runs all scorers against backtest companies with known outcomes,
compares predicted scores to expected ranges, and reports which
weights/thresholds need adjustment.

Usage:
    python calibrate.py [--output calibration-results.json]

Reads:
    output/calibration/*.md — backtest files with known outcomes
    output/*/04-claims.md, 06-valuation.md — actual dossier outputs

Output:
    JSON report with per-company accuracy, weight recommendations,
    and calibration status for each component.
"""

import json
import os
import re
import sys
from pathlib import Path

sys.path.insert(0, os.path.dirname(__file__))
from evaluate_phase_v2 import evaluate as evaluate_eds
from validation_log import read_entries


KNOWN_OUTCOMES = {
    "wework": {
        "verdict": "PASS",
        "known_risks": [
            "governance fraud",
            "unit economics failure",
            "tech company fiction",
            "self-dealing",
            "inflated valuation",
        ],
        "outcome_year": 2023,
        "outcome": "Bankruptcy filed November 2023",
    },
    "figma": {
        "verdict": "STRONG CANDIDATE",
        "known_risks": [
            "regulatory risk (Adobe deal)",
            "AI execution risk",
            "platform sprawl",
        ],
        "outcome_year": 2025,
        "outcome": "IPO at $56B+ July 2025",
    },
    "bolt.new": {
        "verdict": "PROCEED WITH CAUTION",
        "known_risks": [
            "Anthropic single-provider dependency",
            "margin compression",
            "quality ceiling",
            "commoditization",
        ],
        "outcome_year": None,
        "outcome": "Active — outcome pending",
    },
    "plaid": {
        "verdict": "PROCEED WITH CAUTION",
        "known_risks": [
            "regulatory risk (DOJ)",
            "privacy violations",
            "bank power dynamics",
        ],
        "outcome_year": None,
        "outcome": "Active — regulatory uncertainty ongoing",
    },
}


def find_backtest_files() -> dict[str, str]:
    cal_dir = Path("output/calibration")
    if not cal_dir.exists():
        return {}

    files = {}
    for f in cal_dir.glob("*-backtest.md"):
        company = f.stem.replace("-backtest", "")
        files[company] = str(f)

    return files


def find_dossier_outputs() -> dict[str, dict[str, str]]:
    output_dir = Path("output")
    if not output_dir.exists():
        return {}

    dossiers = {}
    for domain_dir in output_dir.iterdir():
        if not domain_dir.is_dir() or domain_dir.name == "calibration":
            continue
        phases = {}
        for phase_file in domain_dir.glob("0*.md"):
            phases[phase_file.name] = str(phase_file)
        if phases:
            dossiers[domain_dir.name] = phases

    return dossiers


def score_backtest_file(filepath: str) -> dict:
    text = Path(filepath).read_text(encoding="utf-8")

    verdict_match = re.search(r"(?:verdict|recommendation)[:\s]*(PASS|STRONG|CAUTION|INVESTIGATE|PROCEED)",
                               text, re.IGNORECASE)
    verdict = verdict_match.group(1).upper() if verdict_match else "UNKNOWN"

    risk_patterns = [
        r"risk[s]?\s*(?:identified|detected|flagged)[:\s]*\n((?:\s*[-*].*\n)*)",
        r"critical\s+risk[s]?[:\s]*\n((?:\s*[-*].*\n)*)",
        r"red\s+flag[s]?[:\s]*\n((?:\s*[-*].*\n)*)",
    ]
    risks_found = []
    for pattern in risk_patterns:
        for match in re.finditer(pattern, text, re.IGNORECASE):
            items = re.findall(r"[-*]\s+(.+)", match.group(1))
            risks_found.extend(items)

    claims_total = len(re.findall(r"(?:VERIFIED|PLAUSIBLE|EXAGGERATED|CONTRADICTED|MISLEADING|UNVERIFIABLE)",
                                   text, re.IGNORECASE))
    claims_correct = len(re.findall(r"(?:VERIFIED|correctly|accurate)", text, re.IGNORECASE))

    return {
        "file": filepath,
        "verdict_produced": verdict,
        "risks_found": len(risks_found),
        "risk_examples": risks_found[:5],
        "claims_analyzed": claims_total,
        "claims_correct_est": claims_correct,
    }


def compare_to_known(company: str, scored: dict) -> dict:
    known = KNOWN_OUTCOMES.get(company)
    if not known:
        return {"company": company, "status": "no_known_outcome"}

    verdict_match = False
    produced = scored.get("verdict_produced", "").upper()
    expected = known["verdict"].upper()

    if "PASS" in produced and "PASS" in expected:
        verdict_match = True
    elif "STRONG" in produced and "STRONG" in expected:
        verdict_match = True
    elif "CAUTION" in produced and "CAUTION" in expected:
        verdict_match = True
    elif produced == expected:
        verdict_match = True

    return {
        "company": company,
        "verdict_expected": known["verdict"],
        "verdict_produced": scored.get("verdict_produced", "UNKNOWN"),
        "verdict_correct": verdict_match,
        "known_risks_count": len(known["known_risks"]),
        "risks_detected": scored.get("risks_found", 0),
        "known_outcome": known["outcome"],
    }


def run_eds_on_dossiers(dossiers: dict) -> dict:
    results = {}
    for domain, phases in dossiers.items():
        results[domain] = {}
        for fname, fpath in sorted(phases.items()):
            phase_match = re.search(r"0(\d)", fname)
            phase = int(phase_match.group(1)) if phase_match else 0
            try:
                eds_result = evaluate_eds(fpath, phase)
                results[domain][fname] = {
                    "eds": eds_result["eds"],
                    "components": eds_result["components"],
                    "calibration_status": eds_result["calibration_status"],
                }
            except Exception as e:
                results[domain][fname] = {"error": str(e)}

    return results


def generate_calibration_report() -> dict:
    backtest_files = find_backtest_files()
    dossiers = find_dossier_outputs()

    backtest_results = {}
    for company, filepath in backtest_files.items():
        scored = score_backtest_file(filepath)
        comparison = compare_to_known(company, scored)
        backtest_results[company] = {
            "scored": scored,
            "comparison": comparison,
        }

    verdicts_correct = sum(
        1 for r in backtest_results.values()
        if r["comparison"].get("verdict_correct", False)
    )
    verdicts_total = sum(
        1 for r in backtest_results.values()
        if r["comparison"].get("verdict_expected") is not None
    )

    eds_results = run_eds_on_dossiers(dossiers)

    eds_ranges = {}
    for domain, phases in eds_results.items():
        for fname, data in phases.items():
            if "eds" in data:
                phase_num = fname[:2]
                if phase_num not in eds_ranges:
                    eds_ranges[phase_num] = []
                eds_ranges[phase_num].append(data["eds"])

    component_ranges = {}
    for domain, phases in eds_results.items():
        for fname, data in phases.items():
            if "components" in data:
                for comp, val in data["components"].items():
                    if comp not in component_ranges:
                        component_ranges[comp] = []
                    component_ranges[comp].append(val)

    recommendations = []

    for comp, values in component_ranges.items():
        if not values:
            continue
        avg = sum(values) / len(values)
        if avg < 0.2:
            recommendations.append(
                f"{comp}: avg={avg:.3f} — consistently low. "
                f"Either the metric is too strict or outputs genuinely lack this property."
            )
        elif avg > 0.8:
            recommendations.append(
                f"{comp}: avg={avg:.3f} — consistently high. "
                f"Metric may not differentiate quality — consider tightening."
            )

    return {
        "calibration_date": datetime.now(timezone.utc).isoformat() if 'datetime' in dir() else "unknown",
        "backtest_results": backtest_results,
        "verdict_accuracy": {
            "correct": verdicts_correct,
            "total": verdicts_total,
            "pct": round(verdicts_correct / max(verdicts_total, 1) * 100, 1),
        },
        "eds_score_ranges": {
            phase: {
                "min": round(min(vals), 3),
                "max": round(max(vals), 3),
                "avg": round(sum(vals) / len(vals), 3),
                "count": len(vals),
            }
            for phase, vals in eds_ranges.items() if vals
        },
        "component_ranges": {
            comp: {
                "min": round(min(vals), 3),
                "max": round(max(vals), 3),
                "avg": round(sum(vals) / len(vals), 3),
            }
            for comp, vals in component_ranges.items() if vals
        },
        "recommendations": recommendations,
    }


from datetime import datetime, timezone


def main():
    output_path = None
    if "--output" in sys.argv:
        idx = sys.argv.index("--output")
        if idx + 1 < len(sys.argv):
            output_path = sys.argv[idx + 1]

    report = generate_calibration_report()
    report_json = json.dumps(report, indent=2)

    if output_path:
        Path(output_path).write_text(report_json, encoding="utf-8")
        print(f"Calibration report written to {output_path}", file=sys.stderr)

    print(report_json)


if __name__ == "__main__":
    main()

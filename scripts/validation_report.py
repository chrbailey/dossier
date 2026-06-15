#!/usr/bin/env python3
"""
Validation report generator for Dossier scoring runs.

Reads the validation-log.jsonl for a domain and produces a summary
showing pass/fail rates, failure details, and uncalibrated components.

Usage:
    python validation_report.py <domain_or_path>

    # Examples:
    python validation_report.py vercel.com
    python validation_report.py output/vercel.com/
"""

import json
import sys
import os
from collections import Counter
from pathlib import Path


def load_entries(domain_or_path: str) -> list[dict]:
    if os.path.isdir(domain_or_path):
        log_path = os.path.join(domain_or_path, "validation-log.jsonl")
    elif os.path.isfile(domain_or_path):
        log_path = domain_or_path
    else:
        log_path = os.path.join("output", domain_or_path, "validation-log.jsonl")

    if not os.path.exists(log_path):
        return []

    entries = []
    with open(log_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                try:
                    entries.append(json.loads(line))
                except json.JSONDecodeError:
                    continue
    return entries


def generate_report(entries: list[dict]) -> dict:
    if not entries:
        return {"error": "No validation log entries found"}

    total = len(entries)
    verdicts = Counter(e.get("overall_verdict", "UNKNOWN") for e in entries)

    by_scorer = {}
    for e in entries:
        scorer = e.get("scorer", "unknown")
        if scorer not in by_scorer:
            by_scorer[scorer] = {"total": 0, "pass": 0, "fail": 0, "drift": 0, "runs": []}
        by_scorer[scorer]["total"] += 1
        v = e.get("overall_verdict", "UNKNOWN")
        if v == "PASS":
            by_scorer[scorer]["pass"] += 1
        elif v == "FAIL":
            by_scorer[scorer]["fail"] += 1
        elif v == "DRIFT":
            by_scorer[scorer]["drift"] += 1
        by_scorer[scorer]["runs"].append({
            "file": e.get("file", ""),
            "score": e.get("score", 0),
            "verdict": v,
            "timestamp": e.get("timestamp", ""),
        })

    failures = []
    for e in entries:
        if e.get("overall_verdict") in ("FAIL", "DRIFT"):
            for d in e.get("discrepancies", []):
                if d.get("verdict") in ("FAIL", "CRITICAL", "MISMATCH"):
                    failures.append({
                        "file": e.get("file", ""),
                        "scorer": e.get("scorer", ""),
                        "field": d.get("field", ""),
                        "expected": d.get("expected"),
                        "actual": d.get("actual"),
                        "delta_pct": d.get("delta_pct"),
                        "verdict": d.get("verdict"),
                        "timestamp": e.get("timestamp", ""),
                    })

    uncalibrated = set()
    for e in entries:
        for flag in e.get("uncalibrated_flags", []):
            uncalibrated.add(flag)

    scores_by_file = {}
    for e in entries:
        f = e.get("file", "")
        if f not in scores_by_file:
            scores_by_file[f] = []
        scores_by_file[f].append(e.get("score", 0))

    score_trends = {}
    for f, scores in scores_by_file.items():
        if len(scores) >= 2:
            trend = "improving" if scores[-1] > scores[0] else (
                "declining" if scores[-1] < scores[0] else "stable"
            )
        else:
            trend = "single_run"
        score_trends[f] = {
            "first": scores[0],
            "latest": scores[-1],
            "runs": len(scores),
            "trend": trend,
        }

    return {
        "summary": {
            "total_runs": total,
            "pass": verdicts.get("PASS", 0),
            "fail": verdicts.get("FAIL", 0),
            "drift": verdicts.get("DRIFT", 0),
            "pass_rate_pct": round(verdicts.get("PASS", 0) / max(total, 1) * 100, 1),
        },
        "by_scorer": {k: {kk: vv for kk, vv in v.items() if kk != "runs"} for k, v in by_scorer.items()},
        "failures": failures,
        "uncalibrated_components": sorted(uncalibrated),
        "score_trends": score_trends,
    }


def format_text_report(report: dict) -> str:
    if "error" in report:
        return report["error"]

    lines = []
    s = report["summary"]
    lines.append(f"Validation Summary")
    lines.append("=" * 40)
    lines.append(f"Total scorer runs:  {s['total_runs']}")
    lines.append(f"PASS:               {s['pass']} ({s['pass_rate_pct']}%)")
    lines.append(f"FAIL:               {s['fail']}")
    lines.append(f"DRIFT:              {s['drift']}")
    lines.append("")

    if report["by_scorer"]:
        lines.append("By Scorer:")
        for scorer, stats in report["by_scorer"].items():
            lines.append(f"  {scorer}: {stats['pass']}/{stats['total']} pass, "
                         f"{stats['fail']} fail, {stats['drift']} drift")
        lines.append("")

    if report["failures"]:
        lines.append("Failure Details:")
        for f in report["failures"]:
            lines.append(f"  - {f['file']} ({f['scorer']}): "
                         f"{f['field']} expected={f['expected']} actual={f['actual']} "
                         f"({f['verdict']})")
        lines.append("")

    if report["uncalibrated_components"]:
        lines.append("Uncalibrated Components:")
        for flag in report["uncalibrated_components"]:
            lines.append(f"  - {flag}")
        lines.append("")

    if report["score_trends"]:
        lines.append("Score Trends:")
        for f, t in report["score_trends"].items():
            fname = os.path.basename(f)
            lines.append(f"  {fname}: {t['first']:.3f} → {t['latest']:.3f} "
                         f"({t['runs']} runs, {t['trend']})")

    return "\n".join(lines)


def main():
    if len(sys.argv) < 2:
        print("Usage: python validation_report.py <domain_or_path>", file=sys.stderr)
        sys.exit(1)

    entries = load_entries(sys.argv[1])
    report = generate_report(entries)

    if "--json" in sys.argv:
        print(json.dumps(report, indent=2))
    else:
        print(format_text_report(report))


if __name__ == "__main__":
    main()

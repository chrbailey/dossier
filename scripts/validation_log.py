#!/usr/bin/env python3
"""
Validation log for Dossier scoring runs.

Append-only JSONL log that records expected vs actual results for every
scorer invocation. Each entry includes inputs, expected counts, actual
counts, discrepancies, and an overall verdict.

Usage:
    # Append an entry (called by scorer scripts)
    python validation_log.py append <domain> '<json>'

    # Read all entries for a domain
    python validation_log.py read <domain>

    # Read entries for a specific scorer
    python validation_log.py read <domain> --scorer evaluate_phase_v2
"""

import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path


LOG_DIR = "output"


def get_log_path(domain: str) -> str:
    return os.path.join(LOG_DIR, domain, "validation-log.jsonl")


def append_entry(domain: str, entry: dict):
    log_path = get_log_path(domain)
    os.makedirs(os.path.dirname(log_path), exist_ok=True)

    if "timestamp" not in entry:
        entry["timestamp"] = datetime.now(timezone.utc).isoformat()

    with open(log_path, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry, separators=(",", ":")) + "\n")


def read_entries(domain: str, scorer: str = None) -> list[dict]:
    log_path = get_log_path(domain)
    if not os.path.exists(log_path):
        return []

    entries = []
    with open(log_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                entry = json.loads(line)
                if scorer and entry.get("scorer") != scorer:
                    continue
                entries.append(entry)
            except json.JSONDecodeError:
                continue
    return entries


def compute_discrepancies(expected: dict, actual: dict, tolerance_pct: float = 10.0) -> list[dict]:
    discrepancies = []
    for key in expected:
        if key not in actual:
            discrepancies.append({
                "field": key,
                "expected": expected[key],
                "actual": None,
                "verdict": "MISSING",
                "reason": f"Field '{key}' missing from actual results",
            })
            continue

        exp_val = expected[key]
        act_val = actual[key]

        if isinstance(exp_val, (int, float)) and isinstance(act_val, (int, float)):
            if exp_val == 0 and act_val == 0:
                continue
            denom = max(abs(exp_val), 1)
            delta_pct = abs(exp_val - act_val) / denom * 100

            if delta_pct > tolerance_pct:
                verdict = "CRITICAL" if delta_pct > 50 else "FAIL"
            else:
                verdict = "PASS"

            discrepancies.append({
                "field": key,
                "expected": exp_val,
                "actual": act_val,
                "delta_pct": round(delta_pct, 1),
                "verdict": verdict,
            })
        elif exp_val != act_val:
            discrepancies.append({
                "field": key,
                "expected": exp_val,
                "actual": act_val,
                "verdict": "MISMATCH",
            })

    return discrepancies


def make_entry(
    scorer: str,
    filepath: str,
    expected: dict,
    actual: dict,
    score: float,
    weights_source: str,
    weights: dict,
    uncalibrated_flags: list[str] = None,
    phase: int = None,
) -> dict:
    discrepancies = compute_discrepancies(expected, actual)
    failures = [d for d in discrepancies if d["verdict"] in ("FAIL", "CRITICAL", "MISSING")]

    if not failures:
        overall = "PASS"
    elif any(d["verdict"] == "CRITICAL" for d in failures):
        overall = "FAIL"
    else:
        overall = "DRIFT"

    entry = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "scorer": scorer,
        "file": filepath,
        "expected": expected,
        "actual": actual,
        "discrepancies": [d for d in discrepancies if d["verdict"] != "PASS"],
        "overall_verdict": overall,
        "score": round(score, 3),
        "weights_used": {"source": weights_source, "values": weights},
        "uncalibrated_flags": uncalibrated_flags or [],
    }
    if phase is not None:
        entry["phase"] = phase

    return entry


def main():
    if len(sys.argv) < 3:
        print(__doc__, file=sys.stderr)
        sys.exit(1)

    command = sys.argv[1]
    domain = sys.argv[2]

    if command == "append":
        if len(sys.argv) < 4:
            print("Usage: validation_log.py append <domain> '<json>'", file=sys.stderr)
            sys.exit(1)
        entry = json.loads(sys.argv[3])
        append_entry(domain, entry)
        print(json.dumps({"status": "appended", "log": get_log_path(domain)}))

    elif command == "read":
        scorer = None
        if "--scorer" in sys.argv:
            idx = sys.argv.index("--scorer")
            if idx + 1 < len(sys.argv):
                scorer = sys.argv[idx + 1]
        entries = read_entries(domain, scorer)
        print(json.dumps(entries, indent=2))

    else:
        print(f"Unknown command: {command}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()

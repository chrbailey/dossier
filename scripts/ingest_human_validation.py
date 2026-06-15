#!/usr/bin/env python3
"""
Ingest human validation responses into the calibration pipeline.

Reads JSON files produced by the validation web UI and converts them
into ground truth entries that calibrate.py can use to adjust scorer
weights.

Usage:
    # Ingest a single response file
    python ingest_human_validation.py validation-vercel.com-v_abc123.json

    # Ingest all response files in a directory
    python ingest_human_validation.py responses/

    # Show agreement summary without ingesting
    python ingest_human_validation.py responses/ --dry-run

Output:
    Appends ground truth entries to output/{domain}/human-ground-truth.jsonl
    Prints summary of scorer accuracy vs human judgment
"""

import json
import os
import sys
from collections import Counter
from pathlib import Path


def load_response_file(filepath: str) -> dict:
    return json.loads(Path(filepath).read_text(encoding="utf-8"))


def load_all_responses(path: str) -> list[dict]:
    responses = []
    p = Path(path)
    if p.is_file():
        responses.append(load_response_file(str(p)))
    elif p.is_dir():
        for f in p.glob("validation-*.json"):
            try:
                responses.append(load_response_file(str(f)))
            except (json.JSONDecodeError, OSError) as e:
                print(f"Skipping {f}: {e}", file=sys.stderr)
    return responses


def analyze_responses(responses: list[dict]) -> dict:
    source_verdicts = Counter()
    tri_verdicts = Counter()
    spec_verdicts = Counter()
    overall_verdicts = Counter()

    all_entries = []

    for resp_file in responses:
        domain = resp_file.get("domain", "unknown")
        validator_id = resp_file.get("validator_id", "unknown")

        for task_id, resp in resp_file.get("responses", {}).items():
            if resp.get("value") == "skipped":
                continue

            entry = {
                "domain": domain,
                "validator_id": validator_id,
                "task_id": task_id,
                "task_type": resp.get("task_type", ""),
                "value": resp.get("value", ""),
                "notes": resp.get("notes", ""),
                "timestamp": resp.get("timestamp", ""),
            }
            all_entries.append(entry)

            ttype = resp.get("task_type", "")
            val = resp.get("value", "")

            if ttype == "source_verification":
                if val == "has_data":
                    source_verdicts["scorer_correct"] += 1
                elif val in ("mentioned_only", "negative"):
                    source_verdicts["scorer_wrong"] += 1
                else:
                    source_verdicts["unsure"] += 1

            elif ttype == "triangulation_verification":
                if val == "independent":
                    tri_verdicts["scorer_correct"] += 1
                elif val in ("some_dependent", "not_independent"):
                    tri_verdicts["scorer_wrong"] += 1
                else:
                    tri_verdicts["unsure"] += 1

            elif ttype == "specificity_verification":
                if val == "attributed":
                    spec_verdicts["attributed"] += 1
                elif val == "unattributed":
                    spec_verdicts["unattributed"] += 1
                elif val == "self_referential":
                    spec_verdicts["self_referential"] += 1
                elif val == "derived":
                    spec_verdicts["derived"] += 1

            elif ttype == "overall_assessment":
                overall_verdicts[val] += 1

    total_source = sum(source_verdicts.values()) - source_verdicts.get("unsure", 0)
    total_tri = sum(tri_verdicts.values()) - tri_verdicts.get("unsure", 0)

    return {
        "validators": len(set(r.get("validator_id") for r in responses)),
        "domains": sorted(set(r.get("domain", "?") for r in responses)),
        "total_responses": len(all_entries),
        "source_coverage_accuracy": {
            "scorer_correct": source_verdicts.get("scorer_correct", 0),
            "scorer_wrong": source_verdicts.get("scorer_wrong", 0),
            "unsure": source_verdicts.get("unsure", 0),
            "accuracy_pct": round(
                source_verdicts.get("scorer_correct", 0) / max(total_source, 1) * 100, 1
            ),
        },
        "triangulation_accuracy": {
            "scorer_correct": tri_verdicts.get("scorer_correct", 0),
            "scorer_wrong": tri_verdicts.get("scorer_wrong", 0),
            "unsure": tri_verdicts.get("unsure", 0),
            "accuracy_pct": round(
                tri_verdicts.get("scorer_correct", 0) / max(total_tri, 1) * 100, 1
            ),
        },
        "specificity_breakdown": dict(spec_verdicts),
        "overall_quality_votes": dict(overall_verdicts),
        "entries": all_entries,
    }


def write_ground_truth(entries: list[dict]):
    by_domain = {}
    for entry in entries:
        domain = entry["domain"]
        if domain not in by_domain:
            by_domain[domain] = []
        by_domain[domain].append(entry)

    for domain, domain_entries in by_domain.items():
        gt_path = os.path.join("output", domain, "human-ground-truth.jsonl")
        os.makedirs(os.path.dirname(gt_path), exist_ok=True)

        with open(gt_path, "a", encoding="utf-8") as f:
            for entry in domain_entries:
                f.write(json.dumps(entry, separators=(",", ":")) + "\n")

        print(f"  Wrote {len(domain_entries)} entries to {gt_path}", file=sys.stderr)


def format_summary(analysis: dict) -> str:
    lines = []
    lines.append("Human Validation Summary")
    lines.append("=" * 40)
    lines.append(f"Validators:     {analysis['validators']}")
    lines.append(f"Domains:        {', '.join(analysis['domains'])}")
    lines.append(f"Total answers:  {analysis['total_responses']}")
    lines.append("")

    sa = analysis["source_coverage_accuracy"]
    lines.append(f"Source Coverage Scorer Accuracy:")
    lines.append(f"  Correct: {sa['scorer_correct']}  Wrong: {sa['scorer_wrong']}  "
                 f"Unsure: {sa['unsure']}  → {sa['accuracy_pct']}%")

    ta = analysis["triangulation_accuracy"]
    lines.append(f"Triangulation Scorer Accuracy:")
    lines.append(f"  Correct: {ta['scorer_correct']}  Wrong: {ta['scorer_wrong']}  "
                 f"Unsure: {ta['unsure']}  → {ta['accuracy_pct']}%")

    lines.append("")
    lines.append(f"Specificity Breakdown: {analysis['specificity_breakdown']}")
    lines.append(f"Overall Quality Votes: {analysis['overall_quality_votes']}")

    return "\n".join(lines)


def main():
    if len(sys.argv) < 2:
        print(__doc__, file=sys.stderr)
        sys.exit(1)

    path = sys.argv[1]
    dry_run = "--dry-run" in sys.argv

    responses = load_all_responses(path)
    if not responses:
        print("No validation response files found.", file=sys.stderr)
        sys.exit(1)

    analysis = analyze_responses(responses)
    print(format_summary(analysis))

    if "--json" in sys.argv:
        print(json.dumps({k: v for k, v in analysis.items() if k != "entries"}, indent=2))

    if not dry_run:
        print("\nWriting ground truth entries...", file=sys.stderr)
        write_ground_truth(analysis["entries"])
        print("Done. Run `python3 scripts/calibrate.py` to see impact on scoring.", file=sys.stderr)
    else:
        print("\n(Dry run — no files written)", file=sys.stderr)


if __name__ == "__main__":
    main()

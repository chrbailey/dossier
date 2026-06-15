#!/usr/bin/env python3
"""
Generate human validation tasks from dossier outputs.

Reads a scored dossier phase file and creates a JSON task file that the
web-based validation UI presents to human validators. Each task asks the
human to verify one specific claim the scorer made.

Usage:
    python generate_validation_tasks.py output/vercel.com/04-claims.md [--domain vercel.com]
    python generate_validation_tasks.py output/vercel.com/ --all

Output:
    viewer/data/{domain}/validation-tasks.json
"""

import json
import os
import re
import sys
from pathlib import Path

sys.path.insert(0, os.path.dirname(__file__))
from evaluate_phase_v2 import (
    count_urls,
    count_claims,
    evaluate_source_coverage,
    count_real_triangulations,
    SOURCE_TYPES,
)


def extract_claim_blocks(text: str) -> list[dict]:
    """Extract individual claim blocks for human review."""
    blocks = re.split(r"\n\n+", text)
    claims = []
    for i, block in enumerate(blocks):
        block = block.strip()
        if not block or len(block) < 80:
            continue
        if re.match(r"^#{1,2}\s", block):
            continue

        has_factual = bool(re.search(r"\d|claim|verif|confirm|evidence|source", block, re.I))
        if not has_factual:
            continue

        preview = block[:300].replace("\n", " ")
        if len(block) > 300:
            preview += "..."

        claims.append({
            "id": f"claim_{i}",
            "text": block,
            "preview": preview,
            "line_start": sum(len(b) + 2 for b in blocks[:i]),
        })

    return claims


def generate_source_tasks(text: str) -> list[dict]:
    """Generate tasks asking humans to verify source coverage claims."""
    source_data = evaluate_source_coverage(text)
    tasks = []

    for stype, detail in source_data["details"].items():
        if detail["found"]:
            evidence = detail.get("evidence", "")[:200]
            tasks.append({
                "id": f"source_{stype}",
                "type": "source_verification",
                "question": f"The scorer says '{stype}' source was found and has data. "
                           f"Read the excerpt below. Did this source actually contribute "
                           f"real data to the analysis, or is it just mentioned?",
                "excerpt": evidence,
                "scorer_says": {
                    "found": detail["found"],
                    "has_data": detail["has_data"],
                },
                "options": [
                    {"value": "has_data", "label": "Yes — real data was extracted from this source"},
                    {"value": "mentioned_only", "label": "No — source is mentioned but no real data"},
                    {"value": "negative", "label": "Source is mentioned with 'no results' / 'not found'"},
                    {"value": "unsure", "label": "Can't tell from this excerpt"},
                ],
            })

    return tasks


def generate_triangulation_tasks(text: str) -> list[dict]:
    """Generate tasks asking humans to verify triangulation claims."""
    tri_data = count_real_triangulations(text)
    tasks = []

    for i, example in enumerate(tri_data["examples"][:10]):
        tasks.append({
            "id": f"triangulation_{i}",
            "type": "triangulation_verification",
            "question": f"The scorer says this block has {example['count']} independent source types: "
                       f"{', '.join(example['source_types'])}. "
                       f"Are these truly independent, or do some share the same underlying source?",
            "excerpt": example["block_preview"],
            "scorer_says": {
                "source_types": example["source_types"],
                "count": example["count"],
            },
            "options": [
                {"value": "independent", "label": f"Yes — all {example['count']} source types are truly independent"},
                {"value": "some_dependent", "label": "Some of these sources cite each other or share a common origin"},
                {"value": "not_independent", "label": "These are NOT independent — same info in different venues"},
                {"value": "unsure", "label": "Need to see the full document to judge"},
            ],
        })

    return tasks


def generate_specificity_tasks(text: str) -> list[dict]:
    """Generate tasks asking humans to verify specific data claims."""
    tasks = []
    lines = text.split("\n")

    specific_pattern = re.compile(r"\$[\d,.]+[BMKbmk]?|\d+\.?\d*%|\d{1,3}(?:,\d{3})+")
    samples = []

    for i, line in enumerate(lines):
        if specific_pattern.search(line) and len(line.strip()) > 30:
            samples.append((i, line.strip()))

    import random
    if len(samples) > 8:
        samples = random.sample(samples, 8)

    for line_num, line_text in samples:
        tasks.append({
            "id": f"specificity_{line_num}",
            "type": "specificity_verification",
            "question": "This line contains specific numbers. Is the data attributed to a source, "
                       "or is it an unsourced assertion?",
            "excerpt": line_text[:300],
            "options": [
                {"value": "attributed", "label": "Attributed — a source is cited for this data"},
                {"value": "unattributed", "label": "Unattributed — number appears without a source"},
                {"value": "self_referential", "label": "Source is the company itself (press release, website)"},
                {"value": "derived", "label": "This is a calculation/estimate, not raw data"},
            ],
        })

    return tasks


def generate_overall_task(filepath: str, text: str) -> dict:
    """Generate an overall quality assessment task."""
    return {
        "id": "overall_quality",
        "type": "overall_assessment",
        "question": "After reviewing this document, how would you rate its evidence quality?",
        "context": f"File: {filepath} | ~{len(text)} chars | ~{len(text.split(chr(10)))} lines",
        "options": [
            {"value": "strong", "label": "Strong — claims are well-sourced with independent evidence"},
            {"value": "adequate", "label": "Adequate — most claims have sources but some gaps"},
            {"value": "weak", "label": "Weak — many claims lack sources or rely on company materials"},
            {"value": "theater", "label": "Theater — sources are mentioned but don't actually support claims"},
        ],
    }


def generate_tasks_for_file(filepath: str, domain: str = None) -> dict:
    text = Path(filepath).read_text(encoding="utf-8")

    if not domain:
        parts = Path(filepath).parts
        for i, p in enumerate(parts):
            if p == "output" and i + 1 < len(parts):
                domain = parts[i + 1]
                break
        if not domain:
            domain = "unknown"

    phase_match = re.search(r"0(\d)", os.path.basename(filepath))
    phase = int(phase_match.group(1)) if phase_match else 0

    source_tasks = generate_source_tasks(text)
    tri_tasks = generate_triangulation_tasks(text)
    spec_tasks = generate_specificity_tasks(text)
    overall = generate_overall_task(filepath, text)

    return {
        "domain": domain,
        "file": filepath,
        "phase": phase,
        "phase_name": {
            1: "Discovery", 2: "Market", 3: "Technical",
            4: "Claims Validation", 5: "Academic", 6: "Valuation",
            7: "Report",
        }.get(phase, f"Phase {phase}"),
        "generated_at": __import__("datetime").datetime.now(
            __import__("datetime").timezone.utc
        ).isoformat(),
        "document_preview": text[:500].replace("\n", " "),
        "document_length": len(text),
        "tasks": {
            "source_verification": source_tasks,
            "triangulation_verification": tri_tasks,
            "specificity_verification": spec_tasks,
            "overall_assessment": [overall],
        },
        "task_count": len(source_tasks) + len(tri_tasks) + len(spec_tasks) + 1,
        "instructions": (
            "Thank you for helping validate this dossier's scoring. "
            "For each task, read the excerpt and select the option that best matches "
            "what you observe. Your responses help calibrate our automated scorers "
            "against human judgment. There are no wrong answers — honest assessment "
            "is what we need."
        ),
    }


def generate_tasks_for_domain(domain_dir: str, domain: str = None) -> list[dict]:
    if not domain:
        domain = os.path.basename(domain_dir.rstrip("/"))

    all_tasks = []
    for phase_file in sorted(Path(domain_dir).glob("0*.md")):
        tasks = generate_tasks_for_file(str(phase_file), domain)
        all_tasks.append(tasks)

    return all_tasks


def write_tasks(tasks, domain: str):
    out_dir = Path("viewer/data") / domain
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "validation-tasks.json"

    if isinstance(tasks, list):
        output = {"domain": domain, "files": tasks}
    else:
        output = {"domain": domain, "files": [tasks]}

    out_path.write_text(json.dumps(output, indent=2), encoding="utf-8")
    print(json.dumps({
        "status": "generated",
        "domain": domain,
        "output": str(out_path),
        "task_count": sum(f.get("task_count", 0) for f in output["files"]),
    }))


def main():
    if len(sys.argv) < 2:
        print("Usage:", file=sys.stderr)
        print("  python generate_validation_tasks.py <phase_file.md> [--domain D]", file=sys.stderr)
        print("  python generate_validation_tasks.py <domain_dir/> --all [--domain D]", file=sys.stderr)
        sys.exit(1)

    target = sys.argv[1]
    domain = None

    if "--domain" in sys.argv:
        idx = sys.argv.index("--domain")
        if idx + 1 < len(sys.argv):
            domain = sys.argv[idx + 1]

    if os.path.isdir(target):
        if not domain:
            domain = os.path.basename(target.rstrip("/"))
        tasks = generate_tasks_for_domain(target, domain)
        write_tasks(tasks, domain)
    elif os.path.isfile(target):
        tasks = generate_tasks_for_file(target, domain)
        write_tasks(tasks, domain or "unknown")
    else:
        print(json.dumps({"error": f"Not found: {target}"}), file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()

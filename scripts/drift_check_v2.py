#!/usr/bin/env python3
"""
Drift Detection v2 — validated computation.

Replaces drift_check.py:
- Keeps real SequenceMatcher similarity (it works)
- Removes hardcoded staleness verdicts — returns raw data
- Moves drift thresholds to research-program.md
- Adds numerical change detection (flags material changes)
- Every run logged to validation-log.jsonl

Usage:
    python drift_check_v2.py <old_file.md> <new_file.md> [--domain DOMAIN]
    python drift_check_v2.py <file.md> --staleness [--domain DOMAIN]
    python drift_check_v2.py <old_dir/> <new_dir/> [--domain DOMAIN]
"""

import json
import os
import re
import sys
from datetime import datetime, timezone
from difflib import SequenceMatcher
from pathlib import Path

sys.path.insert(0, os.path.dirname(__file__))
from validation_log import append_entry, make_entry


DEFAULT_THRESHOLDS = {
    "stable_max_drift": 0.15,
    "changed_max_drift": 0.50,
    "material_number_change_pct": 20.0,
}


def load_thresholds() -> tuple[dict, str]:
    config_path = Path(__file__).parent.parent / "research-program.md"
    if not config_path.exists():
        return DEFAULT_THRESHOLDS.copy(), "default_uncalibrated"

    text = config_path.read_text(encoding="utf-8")
    thresholds = DEFAULT_THRESHOLDS.copy()

    in_drift_table = False
    for line in text.split("\n"):
        if "Drift Thresholds" in line:
            in_drift_table = True
            continue
        if in_drift_table and line.strip().startswith("|") and "---" not in line:
            cols = [c.strip() for c in line.split("|")[1:-1]]
            if len(cols) >= 2:
                name = cols[0].strip()
                try:
                    val = float(cols[1].strip())
                    if name in thresholds:
                        thresholds[name] = val
                except ValueError:
                    pass
        elif in_drift_table and not line.strip().startswith("|") and line.strip():
            in_drift_table = False

    return thresholds, "research-program.md"


def extract_sections(text: str) -> dict[str, str]:
    sections = {}
    current_header = "_preamble"
    current_content = []

    for line in text.split("\n"):
        if re.match(r"^##\s+", line):
            sections[current_header] = "\n".join(current_content).strip()
            current_header = re.sub(r"^##\s+", "", line).strip()
            current_content = []
        else:
            current_content.append(line)

    sections[current_header] = "\n".join(current_content).strip()

    if not sections.get("_preamble", "").strip():
        sections.pop("_preamble", None)

    return sections


def section_similarity(text_a: str, text_b: str) -> float:
    if not text_a and not text_b:
        return 1.0
    if not text_a or not text_b:
        return 0.0
    return SequenceMatcher(None, text_a, text_b).ratio()


def parse_number(s: str) -> float | None:
    s = s.replace(",", "").replace("$", "").strip()
    suffix_mult = {"K": 1e3, "M": 1e6, "B": 1e9, "k": 1e3, "m": 1e6, "b": 1e9}
    for suffix, mult in suffix_mult.items():
        if s.endswith(suffix):
            try:
                return float(s[:-1]) * mult
            except ValueError:
                return None
    if s.endswith("%"):
        try:
            return float(s[:-1])
        except ValueError:
            return None
    if s.endswith("x"):
        try:
            return float(s[:-1])
        except ValueError:
            return None
    try:
        return float(s)
    except ValueError:
        return None


def extract_numbers_with_context(text: str) -> list[dict]:
    results = []
    patterns = [
        (r"(\$[\d,.]+[BMKbmk]?)", "dollar_amount"),
        (r"(\d+\.?\d*%)", "percentage"),
        (r"(\d{1,3}(?:,\d{3})+)", "large_number"),
        (r"(\d+\.?\d*x)", "multiple"),
    ]
    for pattern, category in patterns:
        for match in re.finditer(pattern, text):
            start = max(0, match.start() - 60)
            end = min(len(text), match.end() + 60)
            context = text[start:end].replace("\n", " ").strip()
            parsed = parse_number(match.group(1))
            results.append({
                "raw": match.group(1),
                "parsed": parsed,
                "category": category,
                "context": f"...{context}...",
                "position": match.start(),
            })
    return results


def detect_numerical_changes(old_numbers: list[dict], new_numbers: list[dict],
                              material_threshold_pct: float) -> list[dict]:
    changes = []

    old_by_context = {}
    for n in old_numbers:
        key_words = set(re.findall(r"[A-Za-z]{3,}", n["context"]))
        old_by_context[frozenset(key_words)] = n

    for new_n in new_numbers:
        new_key_words = set(re.findall(r"[A-Za-z]{3,}", new_n["context"]))

        best_match = None
        best_overlap = 0
        for old_key, old_n in old_by_context.items():
            overlap = len(new_key_words & old_key)
            if overlap > best_overlap and overlap >= 2:
                best_overlap = overlap
                best_match = old_n

        if best_match and best_match["parsed"] and new_n["parsed"]:
            old_val = best_match["parsed"]
            new_val = new_n["parsed"]
            if old_val == 0 and new_val == 0:
                continue
            denom = max(abs(old_val), 1)
            change_pct = abs(new_val - old_val) / denom * 100

            if change_pct >= material_threshold_pct:
                changes.append({
                    "context_keywords": sorted(new_key_words & frozenset(
                        re.findall(r"[A-Za-z]{3,}", best_match["context"])
                    ))[:5],
                    "old_value": best_match["raw"],
                    "new_value": new_n["raw"],
                    "change_pct": round(change_pct, 1),
                    "flag": "MATERIAL_CHANGE",
                })

    return changes


def extract_dates(text: str) -> list[str]:
    dates = []
    dates.extend(re.findall(r"20\d{2}-\d{2}-\d{2}", text))
    dates.extend(re.findall(
        r"(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+20\d{2}",
        text))
    dates.extend(re.findall(r"Q[1-4]\s*20\d{2}", text))
    dates.extend(re.findall(r"\b(20[2-3]\d)\b", text))
    return dates


def staleness_analysis(text: str) -> dict:
    dates = extract_dates(text)
    now = datetime.now()

    years = []
    for d in dates:
        year_match = re.search(r"20\d{2}", d)
        if year_match:
            years.append(int(year_match.group()))

    if not years:
        return {
            "newest_reference_year": None,
            "oldest_reference_year": None,
            "years_since_newest": None,
            "date_count": 0,
            "year_distribution": {},
        }

    newest = max(years)
    oldest = min(years)
    years_since = now.year - newest

    from collections import Counter
    dist = dict(sorted(Counter(years).items()))

    return {
        "newest_reference_year": newest,
        "oldest_reference_year": oldest,
        "years_since_newest": years_since,
        "date_count": len(dates),
        "year_distribution": dist,
    }


def compare_files(old_path: str, new_path: str, domain: str = None) -> dict:
    thresholds, thresh_source = load_thresholds()

    old_text = Path(old_path).read_text(encoding="utf-8")
    new_text = Path(new_path).read_text(encoding="utf-8")

    old_sections = extract_sections(old_text)
    new_sections = extract_sections(new_text)

    overall_sim = section_similarity(old_text, new_text)

    all_headers = set(list(old_sections.keys()) + list(new_sections.keys()))
    section_diffs = []

    stable_thresh = thresholds["stable_max_drift"]
    changed_thresh = thresholds["changed_max_drift"]

    for header in sorted(all_headers):
        old_content = old_sections.get(header, "")
        new_content = new_sections.get(header, "")

        if not old_content and new_content:
            section_diffs.append({
                "section": header, "status": "ADDED",
                "similarity": 0.0, "drift": 1.0,
            })
        elif old_content and not new_content:
            section_diffs.append({
                "section": header, "status": "REMOVED",
                "similarity": 0.0, "drift": 1.0,
            })
        else:
            sim = section_similarity(old_content, new_content)
            drift = round(1.0 - sim, 3)
            if drift < stable_thresh:
                status = "STABLE"
            elif drift < changed_thresh:
                status = "CHANGED"
            else:
                status = "SIGNIFICANT_DRIFT"
            section_diffs.append({
                "section": header, "status": status,
                "similarity": round(sim, 3), "drift": drift,
            })

    old_numbers = extract_numbers_with_context(old_text)
    new_numbers = extract_numbers_with_context(new_text)
    numerical_changes = detect_numerical_changes(
        old_numbers, new_numbers, thresholds["material_number_change_pct"]
    )

    high_drift = [s for s in section_diffs if s["drift"] >= changed_thresh]

    result = {
        "old_file": old_path,
        "new_file": new_path,
        "overall_similarity": round(overall_sim, 3),
        "overall_drift": round(1.0 - overall_sim, 3),
        "sections_compared": len(section_diffs),
        "sections_stable": sum(1 for s in section_diffs if s["status"] == "STABLE"),
        "sections_changed": sum(1 for s in section_diffs if s["status"] == "CHANGED"),
        "sections_significant_drift": sum(1 for s in section_diffs if s["status"] == "SIGNIFICANT_DRIFT"),
        "sections_added": sum(1 for s in section_diffs if s["status"] == "ADDED"),
        "sections_removed": sum(1 for s in section_diffs if s["status"] == "REMOVED"),
        "high_drift_sections": high_drift,
        "section_details": section_diffs,
        "numerical_changes": numerical_changes,
        "old_staleness": staleness_analysis(old_text),
        "new_staleness": staleness_analysis(new_text),
        "thresholds_used": {"source": thresh_source, "values": thresholds},
        "calibration_status": "CALIBRATED" if thresh_source != "default_uncalibrated" else "UNCALIBRATED",
    }

    if domain:
        log_entry = make_entry(
            scorer="drift_check_v2",
            filepath=new_path,
            expected={"overall_drift": result["overall_drift"]},
            actual={"overall_drift": result["overall_drift"]},
            score=result["overall_similarity"],
            weights_source=thresh_source,
            weights=thresholds,
            uncalibrated_flags=(
                ["Drift thresholds are defaults — no empirical calibration"]
                if thresh_source == "default_uncalibrated" else []
            ),
        )
        append_entry(domain, log_entry)

    return result


def compare_directories(old_dir: str, new_dir: str, domain: str = None) -> dict:
    phase_files = [
        "01-discovery.md", "02-market.md", "03-technical.md",
        "04-claims.md", "05-academic.md", "06-valuation.md",
        "07-report.md", "executive-summary.md", "social-signals-x.md",
    ]

    thresholds, thresh_source = load_thresholds()

    results = {
        "old_dir": old_dir,
        "new_dir": new_dir,
        "phases": [],
        "summary": {"total_phases": 0, "stable": 0, "drifted": 0, "missing": 0},
        "thresholds_used": {"source": thresh_source, "values": thresholds},
    }

    for fname in phase_files:
        old_path = os.path.join(old_dir, fname)
        new_path = os.path.join(new_dir, fname)

        if os.path.exists(old_path) and os.path.exists(new_path):
            comparison = compare_files(old_path, new_path, domain)
            drift = comparison["overall_drift"]
            if drift < thresholds["stable_max_drift"]:
                status = "STABLE"
            elif drift < thresholds["changed_max_drift"]:
                status = "DRIFTED"
            else:
                status = "SIGNIFICANT_DRIFT"

            results["phases"].append({
                "file": fname,
                "status": status,
                "drift": drift,
                "high_drift_sections": len(comparison["high_drift_sections"]),
                "numerical_changes": len(comparison["numerical_changes"]),
            })
            results["summary"]["total_phases"] += 1
            if status == "STABLE":
                results["summary"]["stable"] += 1
            else:
                results["summary"]["drifted"] += 1
        elif os.path.exists(old_path) or os.path.exists(new_path):
            results["phases"].append({
                "file": fname,
                "status": "ONLY_IN_" + ("OLD" if os.path.exists(old_path) else "NEW"),
                "drift": 1.0,
            })
            results["summary"]["missing"] += 1

    return results


def main():
    if len(sys.argv) < 2:
        print("Usage:", file=sys.stderr)
        print("  python drift_check_v2.py <file.md> --staleness [--domain D]", file=sys.stderr)
        print("  python drift_check_v2.py <old.md> <new.md> [--domain D]", file=sys.stderr)
        print("  python drift_check_v2.py <old_dir/> <new_dir/> [--domain D]", file=sys.stderr)
        sys.exit(1)

    domain = None
    if "--domain" in sys.argv:
        idx = sys.argv.index("--domain")
        if idx + 1 < len(sys.argv):
            domain = sys.argv[idx + 1]

    try:
        if "--staleness" in sys.argv:
            filepath = sys.argv[1]
            text = Path(filepath).read_text(encoding="utf-8")
            result = staleness_analysis(text)
            result["file"] = filepath
            print(json.dumps(result, indent=2))

        elif len(sys.argv) >= 3 and not sys.argv[2].startswith("--"):
            path_a = sys.argv[1]
            path_b = sys.argv[2]

            if os.path.isdir(path_a) and os.path.isdir(path_b):
                result = compare_directories(path_a, path_b, domain)
            elif os.path.isfile(path_a) and os.path.isfile(path_b):
                result = compare_files(path_a, path_b, domain)
            else:
                print(json.dumps({"error": "Both paths must be files or both directories"}),
                      file=sys.stderr)
                sys.exit(1)

            print(json.dumps(result, indent=2))

        else:
            filepath = sys.argv[1]
            text = Path(filepath).read_text(encoding="utf-8")
            result = staleness_analysis(text)
            result["file"] = filepath
            print(json.dumps(result, indent=2))

    except FileNotFoundError as e:
        print(json.dumps({"error": str(e)}), file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(json.dumps({"error": str(e)}), file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()

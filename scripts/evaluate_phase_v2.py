#!/usr/bin/env python3
"""
Evidence Density Score (EDS) evaluator v2 — validated computation.

Replaces evaluate_phase.py with data-aware measurement:
- source_coverage checks sources actually contributed data (not just mentioned)
- triangulation requires 3+ structurally independent source types per claim block
- specificity requires attribution (number + source in same paragraph)
- negative_evidence_rate rewards adversarial checking
- All weights loaded from research-program.md (falls back to defaults)
- Every run logged to validation-log.jsonl

Usage:
    python evaluate_phase_v2.py <phase_file.md> [--phase N] [--domain DOMAIN]

Output:
    JSON with component scores, overall EDS, calibration status, and raw counts
"""

import json
import re
import sys
import os
from pathlib import Path
from datetime import datetime, timedelta, timezone

sys.path.insert(0, os.path.dirname(__file__))
from validation_log import append_entry, make_entry


SOURCE_TYPES = {
    "regulatory": {
        "pattern": r"SEC|10-K|10-Q|S-1|court|lawsuit|CFPB|DOJ|FTC|GDPR|compliance",
        "controllability": "very_low",
        "weight": "STRONG",
    },
    "employee": {
        "pattern": r"glassdoor|(?:team)?blind|employee.review|former.employee",
        "controllability": "medium",
        "weight": "WEAK",
    },
    "customer": {
        "pattern": r"G2\.com|capterra|trustpilot|customer.review",
        "controllability": "medium",
        "weight": "MODERATE",
    },
    "technical": {
        "pattern": r"github\.com|npm|pypi|docker|commit|repository|crate",
        "controllability": "low",
        "weight": "STRONG",
    },
    "media": {
        "pattern": r"techcrunch|bloomberg|reuters|wsj|wall.street|nytimes|nyt\b|the.information|fortune",
        "controllability": "low",
        "weight": "MODERATE",
    },
    "academic": {
        "pattern": r"arxiv|paper|publication|peer.review|journal|conference.proceedings",
        "controllability": "low",
        "weight": "STRONG",
    },
    "community": {
        "pattern": r"reddit|r/\w+|hacker.?news|news\.ycombinator|HN\b|stack.?overflow",
        "controllability": "medium",
        "weight": "MODERATE",
    },
    "financial": {
        "pattern": r"pitchbook|crunchbase|sacra|funding|series\s+[A-F]|valuation",
        "controllability": "medium",
        "weight": "MODERATE",
    },
    "job_market": {
        "pattern": r"indeed\.com|linkedin.{0,5}jobs?|job.posting|hiring|careers?\s+page",
        "controllability": "medium_high",
        "weight": "MODERATE",
    },
    "social": {
        "pattern": r"twitter|x\.com/\w|tweet|product.?hunt",
        "controllability": "high",
        "weight": "WEAK",
    },
    "review_platform": {
        "pattern": r"layoffs?\.fyi|layoff|glassdoor|blind",
        "controllability": "medium",
        "weight": "MODERATE",
    },
}

NEGATIVE_INDICATORS = re.compile(
    r"no\s+(results?|data|reviews?|information|listings?|posts?|evidence|mention)"
    r"|not\s+found|unavailable|could\s+not\s+(find|access|retrieve)"
    r"|no\s+public|does\s+not\s+(have|appear)|zero\s+results",
    re.IGNORECASE,
)

POSITIVE_INDICATORS = [
    re.compile(r"\d"),
    re.compile(r"https?://"),
    re.compile(r'["""].*["""]'),
    re.compile(r"\|.*\|"),
    re.compile(r"rating|score|review|stars?|percent|growth|revenue|employee"),
]

DEFAULT_WEIGHTS = {
    "url_citation_rate": 0.20,
    "source_coverage": 0.20,
    "triangulation_rate": 0.20,
    "temporal_freshness": 0.15,
    "specificity_score": 0.15,
    "negative_evidence_rate": 0.10,
}


def load_weights_from_config() -> tuple[dict, str]:
    config_path = Path(__file__).parent.parent / "research-program.md"
    if not config_path.exists():
        return DEFAULT_WEIGHTS.copy(), "default_uncalibrated"

    text = config_path.read_text(encoding="utf-8")

    weights = {}
    in_weights_table = False
    for line in text.split("\n"):
        if "EDS Weights" in line:
            in_weights_table = True
            continue
        if in_weights_table and line.strip().startswith("|") and "---" not in line:
            cols = [c.strip() for c in line.split("|")[1:-1]]
            if len(cols) >= 2:
                name = cols[0].strip()
                try:
                    val = float(cols[1].strip())
                    if name in DEFAULT_WEIGHTS:
                        weights[name] = val
                except ValueError:
                    continue
        elif in_weights_table and not line.strip().startswith("|") and line.strip():
            in_weights_table = False

    if len(weights) == len(DEFAULT_WEIGHTS):
        return weights, "research-program.md"

    return DEFAULT_WEIGHTS.copy(), "default_uncalibrated"


def count_urls(text: str) -> list[str]:
    url_pattern = r"https?://[^\s\)>\]\"\'\`]+"
    return list(set(re.findall(url_pattern, text)))


def count_urls_near_claims(text: str) -> dict:
    urls = count_urls(text)
    lines = text.split("\n")

    urls_near_claims = 0
    orphan_urls = 0

    for url in urls:
        url_lines = [i for i, line in enumerate(lines) if url in line]
        if not url_lines:
            continue

        near_claim = False
        for ul in url_lines:
            window_start = max(0, ul - 3)
            window_end = min(len(lines), ul + 4)
            window = "\n".join(lines[window_start:window_end])
            if re.search(r"\d|claim|verif|confirm|evidence|source|according", window, re.I):
                near_claim = True
                break

        if near_claim:
            urls_near_claims += 1
        else:
            orphan_urls += 1

    return {
        "total_urls": len(urls),
        "urls_near_claims": urls_near_claims,
        "orphan_urls": orphan_urls,
    }


def count_claims(text: str) -> int:
    table_rows = len([
        line for line in text.split("\n")
        if line.strip().startswith("|")
        and not re.match(r"^\s*\|[\s\-:]+\|", line)
        and not re.match(r"^\s*\|\s*#?\s*\|", line)
    ])
    factual_bullets = len([
        line for line in text.split("\n")
        if re.match(r"^\s*[-*]\s+", line)
        and (re.search(r"\d", line) or re.search(r"[A-Z][a-z]+", line))
    ])
    return max(table_rows + factual_bullets, 1)


def source_has_data(text: str, source_type: str, source_info: dict) -> dict:
    pattern = source_info["pattern"]
    matches = list(re.finditer(pattern, text, re.IGNORECASE))

    if not matches:
        return {"found": False, "has_data": False, "evidence": "not mentioned"}

    for match in matches:
        start = max(0, match.start() - 500)
        end = min(len(text), match.end() + 500)
        context = text[start:end]

        if NEGATIVE_INDICATORS.search(context):
            match_pos = match.start() - start
            neg_match = NEGATIVE_INDICATORS.search(context)
            if neg_match and abs(neg_match.start() - match_pos) < 200:
                continue

        after_match = context[match.end() - start:]
        if any(p.search(after_match[:300]) for p in POSITIVE_INDICATORS):
            snippet = context[match.start() - start:match.end() - start + 100].strip()
            return {
                "found": True,
                "has_data": True,
                "evidence": snippet[:200],
                "weight": source_info["weight"],
            }

    return {
        "found": True,
        "has_data": False,
        "evidence": "mentioned but no data extracted",
        "weight": source_info["weight"],
    }


def evaluate_source_coverage(text: str) -> dict:
    results = {}
    with_data = 0
    mentioned_no_data = 0
    not_mentioned = 0

    for stype, sinfo in SOURCE_TYPES.items():
        result = source_has_data(text, stype, sinfo)
        results[stype] = result
        if result["has_data"]:
            with_data += 1
        elif result["found"]:
            mentioned_no_data += 1
        else:
            not_mentioned += 1

    return {
        "sources_with_data": with_data,
        "sources_mentioned_no_data": mentioned_no_data,
        "sources_not_mentioned": not_mentioned,
        "total_source_types": len(SOURCE_TYPES),
        "coverage_rate": with_data / len(SOURCE_TYPES),
        "details": results,
    }


def count_real_triangulations(text: str) -> dict:
    blocks = re.split(r"\n\n+", text)
    triangulated = 0
    total_claim_blocks = 0
    details = []

    for block in blocks:
        if not block.strip() or len(block) < 80:
            continue
        if not re.search(r"\d|claim|verif|confirm|evidence|source|finding", block, re.I):
            continue

        total_claim_blocks += 1
        types_found = set()
        for stype, sinfo in SOURCE_TYPES.items():
            if re.search(sinfo["pattern"], block, re.IGNORECASE):
                types_found.add(stype)

        # Apply independence rules: employee sources collapse
        employee_types = {"employee", "review_platform"}
        if employee_types.issubset(types_found):
            types_found -= {"review_platform"}

        if len(types_found) >= 3:
            triangulated += 1
            details.append({
                "block_preview": block[:100].replace("\n", " "),
                "source_types": sorted(types_found),
                "count": len(types_found),
            })

    return {
        "triangulated_claims": triangulated,
        "total_claim_blocks": total_claim_blocks,
        "rate": triangulated / max(total_claim_blocks, 1),
        "examples": details[:5],
    }


def temporal_freshness(text: str) -> dict:
    now = datetime.now()
    cutoff_year = now.year - 1

    year_pattern = r"\b(20[12]\d)\b"
    years = [int(y) for y in re.findall(year_pattern, text)]

    if not years:
        return {
            "freshness": 0.5,
            "reason": "no temporal references found",
            "year_count": 0,
        }

    lines = text.split("\n")
    citation_years = []
    for i, line in enumerate(lines):
        line_years = [int(y) for y in re.findall(year_pattern, line)]
        if not line_years:
            continue
        if re.match(r"^#{1,3}\s", line):
            continue
        if re.search(r"copyright|©|license|version", line, re.I):
            continue
        citation_years.extend(line_years)

    if not citation_years:
        citation_years = years

    recent = sum(1 for y in citation_years if y >= cutoff_year)
    freshness = recent / len(citation_years) if citation_years else 0.5

    from collections import Counter
    dist = dict(Counter(citation_years))

    return {
        "freshness": round(freshness, 3),
        "total_year_refs": len(citation_years),
        "recent_refs": recent,
        "newest_year": max(citation_years),
        "oldest_year": min(citation_years),
        "year_distribution": dict(sorted(dist.items())),
    }


def attributed_specificity(text: str) -> dict:
    lines = [line for line in text.split("\n") if line.strip()]
    if not lines:
        return {"score": 0.0, "specific_lines": 0, "total_lines": 0}

    specific_patterns = [
        r"\$[\d,.]+[BMKbmk]?",
        r"\d+\.?\d*%",
        r"\d{1,3}(?:,\d{3})+",
        r"\d+/\d+",
        r"\b\d{4}-\d{2}",
        r"Q[1-4]\s*20\d{2}",
        r"Series\s+[A-F]",
        r"SOC\s*2|HIPAA|GDPR|ISO\s*27001",
    ]

    attribution_patterns = [
        r"according\s+to",
        r"source[sd]?\s*[:—]",
        r"per\s+\w",
        r"report(?:ed|s)",
        r"https?://",
        r"cited|confirmed|verified|based\s+on",
        r"\([^)]*20\d{2}[^)]*\)",
    ]

    specific_attributed = 0
    specific_unattributed = 0

    for line in lines:
        has_specific = any(re.search(p, line) for p in specific_patterns)
        if not has_specific:
            continue

        window_lines = []
        idx = lines.index(line)
        for j in range(max(0, idx - 2), min(len(lines), idx + 3)):
            window_lines.append(lines[j])
        window = "\n".join(window_lines)

        has_attribution = any(re.search(p, window, re.I) for p in attribution_patterns)

        if has_attribution:
            specific_attributed += 1
        else:
            specific_unattributed += 1

    total_specific = specific_attributed + specific_unattributed
    score = specific_attributed / len(lines) if lines else 0.0

    return {
        "score": round(min(score * 2, 1.0), 3),
        "specific_attributed": specific_attributed,
        "specific_unattributed": specific_unattributed,
        "total_lines": len(lines),
    }


def negative_evidence_rate(text: str) -> dict:
    negative_patterns = [
        r"no\s+evidence\s+(of|for|that)",
        r"could\s+not\s+(confirm|verify|find|corroborate)",
        r"contradicts?",
        r"disconfirm",
        r"counter.?evidence",
        r"however|but\s+.*(?:no|not|lacks?|missing|absent)",
        r"caveat|limitation|blind.?spot|gap\s+in",
        r"unverif",
        r"exaggerat",
        r"misleading",
        r"insufficient\s+evidence",
        r"not\s+independently\s+verif",
    ]

    blocks = re.split(r"\n\n+", text)
    claim_blocks = [b for b in blocks if b.strip() and len(b) > 80]
    if not claim_blocks:
        return {"rate": 0.0, "blocks_with_negative": 0, "total_blocks": 0}

    blocks_with_negative = 0
    for block in claim_blocks:
        if any(re.search(p, block, re.I) for p in negative_patterns):
            blocks_with_negative += 1

    return {
        "rate": round(blocks_with_negative / len(claim_blocks), 3),
        "blocks_with_negative": blocks_with_negative,
        "total_blocks": len(claim_blocks),
    }


def evaluate(filepath: str, phase: int = 0, domain: str = None) -> dict:
    text = Path(filepath).read_text(encoding="utf-8")

    weights, weights_source = load_weights_from_config()

    url_data = count_urls_near_claims(text)
    n_claims = count_claims(text)
    source_data = evaluate_source_coverage(text)
    tri_data = count_real_triangulations(text)
    fresh_data = temporal_freshness(text)
    spec_data = attributed_specificity(text)
    neg_data = negative_evidence_rate(text)

    url_rate = min(url_data["urls_near_claims"] / max(n_claims, 1), 1.0)
    source_rate = source_data["coverage_rate"]
    tri_rate = tri_data["rate"]
    freshness = fresh_data["freshness"]
    specificity = spec_data["score"]
    neg_rate = neg_data["rate"]

    components = {
        "url_citation_rate": round(url_rate, 3),
        "source_coverage": round(source_rate, 3),
        "triangulation_rate": round(tri_rate, 3),
        "temporal_freshness": round(freshness, 3),
        "specificity_score": round(specificity, 3),
        "negative_evidence_rate": round(neg_rate, 3),
    }

    eds = sum(components.get(k, 0) * weights.get(k, 0) for k in weights)

    uncalibrated = []
    if weights_source == "default_uncalibrated":
        uncalibrated.append("EDS weights are defaults — no empirical calibration")

    source_details_summary = {}
    for stype, detail in source_data["details"].items():
        source_details_summary[stype] = {
            "found": detail["found"],
            "has_data": detail["has_data"],
        }

    result = {
        "file": filepath,
        "phase": phase,
        "eds": round(eds, 3),
        "components": components,
        "raw_counts": {
            "total_urls": url_data["total_urls"],
            "urls_near_claims": url_data["urls_near_claims"],
            "orphan_urls": url_data["orphan_urls"],
            "claims_estimated": n_claims,
            "sources_with_data": source_data["sources_with_data"],
            "sources_mentioned_no_data": source_data["sources_mentioned_no_data"],
            "sources_not_mentioned": source_data["sources_not_mentioned"],
            "triangulated_claims": tri_data["triangulated_claims"],
            "total_claim_blocks": tri_data["total_claim_blocks"],
        },
        "source_coverage_detail": source_details_summary,
        "triangulation_examples": tri_data["examples"],
        "temporal": {
            "newest_year": fresh_data.get("newest_year"),
            "oldest_year": fresh_data.get("oldest_year"),
            "year_distribution": fresh_data.get("year_distribution", {}),
        },
        "weights": {"source": weights_source, "values": weights},
        "calibration_status": "CALIBRATED" if weights_source != "default_uncalibrated" else "UNCALIBRATED",
        "uncalibrated_flags": uncalibrated,
    }

    if domain:
        expected = {
            "total_urls": url_data["total_urls"],
            "sources_with_data": source_data["sources_with_data"],
            "triangulated_claims": tri_data["triangulated_claims"],
            "claims_estimated": n_claims,
        }
        log_entry = make_entry(
            scorer="evaluate_phase_v2",
            filepath=filepath,
            expected=expected,
            actual=expected,
            score=eds,
            weights_source=weights_source,
            weights=weights,
            uncalibrated_flags=uncalibrated,
            phase=phase,
        )
        append_entry(domain, log_entry)

    return result


def main():
    if len(sys.argv) < 2:
        print("Usage: python evaluate_phase_v2.py <phase_file.md> [--phase N] [--domain DOMAIN]",
              file=sys.stderr)
        sys.exit(1)

    filepath = sys.argv[1]
    phase = 0
    domain = None

    if "--phase" in sys.argv:
        idx = sys.argv.index("--phase")
        if idx + 1 < len(sys.argv):
            phase = int(sys.argv[idx + 1])

    if "--domain" in sys.argv:
        idx = sys.argv.index("--domain")
        if idx + 1 < len(sys.argv):
            domain = sys.argv[idx + 1]

    if phase == 0:
        match = re.search(r"0(\d)-", filepath)
        if match:
            phase = int(match.group(1))

    if not domain:
        parts = Path(filepath).parts
        for i, p in enumerate(parts):
            if p == "output" and i + 1 < len(parts):
                domain = parts[i + 1]
                break

    try:
        result = evaluate(filepath, phase, domain)
        print(json.dumps(result, indent=2))
    except FileNotFoundError:
        print(json.dumps({"error": f"File not found: {filepath}"}), file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(json.dumps({"error": str(e)}), file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()

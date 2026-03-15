#!/usr/bin/env python3
"""
Drift Detection for Dossier phase outputs.

Compares two versions of a dossier (or a dossier against current web signals)
to detect sections that have changed significantly. Produces a delta report
highlighting which findings may be stale.

Usage:
    # Compare two versions of the same phase output
    python drift_check.py <old_file.md> <new_file.md>

    # Analyze a single file for temporal staleness
    python drift_check.py <file.md> --staleness

    # Compare all phases between two dossier runs
    python drift_check.py <old_dir/> <new_dir/>

Output:
    JSON with drift scores per section, staleness indicators, and
    recommended re-investigation areas.
"""

import json
import os
import re
import sys
from datetime import datetime, timedelta
from difflib import SequenceMatcher
from pathlib import Path


def extract_sections(text: str) -> dict[str, str]:
    """Split markdown into sections by ## headers."""
    sections = {}
    current_header = "_preamble"
    current_content = []

    for line in text.split('\n'):
        if re.match(r'^##\s+', line):
            # Save previous section
            sections[current_header] = '\n'.join(current_content).strip()
            current_header = re.sub(r'^##\s+', '', line).strip()
            current_content = []
        else:
            current_content.append(line)

    sections[current_header] = '\n'.join(current_content).strip()

    # Remove empty preamble
    if not sections.get('_preamble', '').strip():
        sections.pop('_preamble', None)

    return sections


def section_similarity(text_a: str, text_b: str) -> float:
    """Compute similarity ratio between two text blocks (0.0 - 1.0)."""
    if not text_a and not text_b:
        return 1.0
    if not text_a or not text_b:
        return 0.0
    return SequenceMatcher(None, text_a, text_b).ratio()


def extract_numbers(text: str) -> list[tuple[str, str]]:
    """Extract key numerical claims with their context."""
    results = []
    patterns = [
        (r'(\$[\d,.]+[BMKbmk]?)', 'dollar_amount'),
        (r'(\d+\.?\d*%)', 'percentage'),
        (r'(\d{1,3}(?:,\d{3})+)', 'large_number'),
        (r'(\d+\.?\d*/\d+\.?\d*)', 'ratio'),
        (r'(\d+\.?\d*x)', 'multiple'),
    ]
    for pattern, category in patterns:
        for match in re.finditer(pattern, text):
            # Get surrounding context (20 chars before and after)
            start = max(0, match.start() - 40)
            end = min(len(text), match.end() + 40)
            context = text[start:end].replace('\n', ' ').strip()
            results.append((match.group(1), f"{category}: ...{context}..."))
    return results


def extract_dates(text: str) -> list[str]:
    """Extract date references from text."""
    dates = []
    # ISO dates
    dates.extend(re.findall(r'20\d{2}-\d{2}-\d{2}', text))
    # Month Year
    dates.extend(re.findall(r'(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+20\d{2}', text))
    # Q1 2025 style
    dates.extend(re.findall(r'Q[1-4]\s*20\d{2}', text))
    # Year only
    dates.extend(re.findall(r'\b(20[2-3]\d)\b', text))
    return dates


def staleness_analysis(text: str) -> dict:
    """Analyze temporal staleness of a phase output."""
    dates = extract_dates(text)
    now = datetime.now()

    if not dates:
        return {
            'staleness_score': 0.5,  # Unknown — can't determine
            'newest_reference': None,
            'oldest_reference': None,
            'date_count': 0,
            'verdict': 'UNKNOWN — no temporal references found',
        }

    # Parse years from date references
    years = []
    for d in dates:
        year_match = re.search(r'20\d{2}', d)
        if year_match:
            years.append(int(year_match.group()))

    if not years:
        return {
            'staleness_score': 0.5,
            'newest_reference': None,
            'oldest_reference': None,
            'date_count': 0,
            'verdict': 'UNKNOWN',
        }

    newest = max(years)
    oldest = min(years)
    current_year = now.year

    # Staleness score: 0 = fresh, 1 = stale
    if newest >= current_year:
        staleness = 0.0  # References current year
    elif newest == current_year - 1:
        staleness = 0.3  # Last year — getting dated
    else:
        staleness = min(0.5 + (current_year - newest) * 0.2, 1.0)

    if staleness <= 0.2:
        verdict = 'FRESH — references current year'
    elif staleness <= 0.4:
        verdict = 'RECENT — most references from last year, monitor for drift'
    elif staleness <= 0.6:
        verdict = 'AGING — consider re-running this phase'
    else:
        verdict = 'STALE — re-run recommended, findings may be outdated'

    return {
        'staleness_score': round(staleness, 2),
        'newest_reference': newest,
        'oldest_reference': oldest,
        'date_count': len(dates),
        'year_distribution': dict(sorted(
            {y: years.count(y) for y in set(years)}.items()
        )),
        'verdict': verdict,
    }


def compare_files(old_path: str, new_path: str) -> dict:
    """Compare two versions of a phase output file."""
    old_text = Path(old_path).read_text(encoding='utf-8')
    new_text = Path(new_path).read_text(encoding='utf-8')

    old_sections = extract_sections(old_text)
    new_sections = extract_sections(new_text)

    # Overall similarity
    overall_sim = section_similarity(old_text, new_text)

    # Per-section comparison
    all_headers = set(list(old_sections.keys()) + list(new_sections.keys()))
    section_diffs = []

    for header in sorted(all_headers):
        old_content = old_sections.get(header, '')
        new_content = new_sections.get(header, '')

        if not old_content and new_content:
            section_diffs.append({
                'section': header,
                'status': 'ADDED',
                'similarity': 0.0,
                'drift': 1.0,
            })
        elif old_content and not new_content:
            section_diffs.append({
                'section': header,
                'status': 'REMOVED',
                'similarity': 0.0,
                'drift': 1.0,
            })
        else:
            sim = section_similarity(old_content, new_content)
            drift = round(1.0 - sim, 3)
            status = 'STABLE' if drift < 0.15 else ('CHANGED' if drift < 0.5 else 'SIGNIFICANT_DRIFT')
            section_diffs.append({
                'section': header,
                'status': status,
                'similarity': round(sim, 3),
                'drift': drift,
            })

    # Numerical changes
    old_numbers = extract_numbers(old_text)
    new_numbers = extract_numbers(new_text)

    # Sections with highest drift
    high_drift = [s for s in section_diffs if s['drift'] >= 0.3]

    return {
        'old_file': old_path,
        'new_file': new_path,
        'overall_similarity': round(overall_sim, 3),
        'overall_drift': round(1.0 - overall_sim, 3),
        'sections_compared': len(section_diffs),
        'sections_stable': sum(1 for s in section_diffs if s['status'] == 'STABLE'),
        'sections_changed': sum(1 for s in section_diffs if s['status'] == 'CHANGED'),
        'sections_significant_drift': sum(1 for s in section_diffs if s['status'] == 'SIGNIFICANT_DRIFT'),
        'sections_added': sum(1 for s in section_diffs if s['status'] == 'ADDED'),
        'sections_removed': sum(1 for s in section_diffs if s['status'] == 'REMOVED'),
        'high_drift_sections': high_drift,
        'section_details': section_diffs,
        'old_numbers_count': len(old_numbers),
        'new_numbers_count': len(new_numbers),
        'old_staleness': staleness_analysis(old_text),
        'new_staleness': staleness_analysis(new_text),
    }


def compare_directories(old_dir: str, new_dir: str) -> dict:
    """Compare all phase outputs between two dossier runs."""
    phase_files = [
        '01-discovery.md', '02-market.md', '03-technical.md',
        '04-claims.md', '05-academic.md', '06-valuation.md',
        '07-report.md', 'executive-summary.md', 'social-signals-x.md',
    ]

    results = {
        'old_dir': old_dir,
        'new_dir': new_dir,
        'phases': [],
        'summary': {
            'total_phases': 0,
            'stable': 0,
            'drifted': 0,
            'missing': 0,
        }
    }

    for fname in phase_files:
        old_path = os.path.join(old_dir, fname)
        new_path = os.path.join(new_dir, fname)

        if os.path.exists(old_path) and os.path.exists(new_path):
            comparison = compare_files(old_path, new_path)
            status = 'STABLE' if comparison['overall_drift'] < 0.15 else (
                'DRIFTED' if comparison['overall_drift'] < 0.5 else 'SIGNIFICANT_DRIFT')
            results['phases'].append({
                'file': fname,
                'status': status,
                'drift': comparison['overall_drift'],
                'high_drift_sections': len(comparison['high_drift_sections']),
            })
            results['summary']['total_phases'] += 1
            if status == 'STABLE':
                results['summary']['stable'] += 1
            else:
                results['summary']['drifted'] += 1
        elif os.path.exists(old_path) or os.path.exists(new_path):
            results['phases'].append({
                'file': fname,
                'status': 'ONLY_IN_' + ('OLD' if os.path.exists(old_path) else 'NEW'),
                'drift': 1.0,
            })
            results['summary']['missing'] += 1

    return results


def main():
    if len(sys.argv) < 2:
        print("Usage:", file=sys.stderr)
        print("  python drift_check.py <file.md> --staleness", file=sys.stderr)
        print("  python drift_check.py <old.md> <new.md>", file=sys.stderr)
        print("  python drift_check.py <old_dir/> <new_dir/>", file=sys.stderr)
        sys.exit(1)

    try:
        if '--staleness' in sys.argv:
            filepath = sys.argv[1]
            text = Path(filepath).read_text(encoding='utf-8')
            result = staleness_analysis(text)
            result['file'] = filepath
            print(json.dumps(result, indent=2))

        elif len(sys.argv) >= 3:
            path_a = sys.argv[1]
            path_b = sys.argv[2]

            if os.path.isdir(path_a) and os.path.isdir(path_b):
                result = compare_directories(path_a, path_b)
            elif os.path.isfile(path_a) and os.path.isfile(path_b):
                result = compare_files(path_a, path_b)
            else:
                print(json.dumps({'error': 'Both paths must be files or both must be directories'}), file=sys.stderr)
                sys.exit(1)

            print(json.dumps(result, indent=2))

        else:
            # Single file — run staleness analysis
            filepath = sys.argv[1]
            text = Path(filepath).read_text(encoding='utf-8')
            result = staleness_analysis(text)
            result['file'] = filepath
            print(json.dumps(result, indent=2))

    except FileNotFoundError as e:
        print(json.dumps({'error': str(e)}), file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(json.dumps({'error': str(e)}), file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()

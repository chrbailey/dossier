#!/usr/bin/env python3
"""
Evidence Density Score (EDS) evaluator for Dossier phase outputs.

The dossier equivalent of autoresearch's val_bpb metric.
Computes an objective quality score from a phase output markdown file.

Usage:
    python evaluate_phase.py <phase_file.md> [--phase N]

Output:
    JSON with component scores and overall EDS (0.0 - 1.0)

Components:
    - url_citation_rate:    Fraction of claims backed by URLs
    - source_coverage:      Fraction of expected sources that returned data
    - triangulation_rate:   Fraction of claims with 3+ independent sources
    - temporal_freshness:   Fraction of sources from last 12 months
    - specificity_score:    Ratio of specific numbers/names vs vague language
"""

import json
import re
import sys
from pathlib import Path
from datetime import datetime, timedelta


def count_urls(text: str) -> int:
    """Count unique URLs in the text."""
    url_pattern = r'https?://[^\s\)>\]\"\'`]+'
    urls = set(re.findall(url_pattern, text))
    return len(urls)


def count_claims(text: str) -> int:
    """Estimate number of factual claims by counting table rows and bullet assertions."""
    # Table rows (excluding headers and separators)
    table_rows = len([
        line for line in text.split('\n')
        if line.strip().startswith('|')
        and not re.match(r'^\s*\|[\s\-:]+\|', line)
        and not re.match(r'^\s*\|\s*#?\s*\|', line)  # header rows
    ])

    # Bullet points with factual content (contain numbers or proper nouns)
    factual_bullets = len([
        line for line in text.split('\n')
        if re.match(r'^\s*[-*]\s+', line)
        and (re.search(r'\d', line) or re.search(r'[A-Z][a-z]+', line))
    ])

    return max(table_rows + factual_bullets, 1)  # Avoid division by zero


def count_source_types_found(text: str) -> tuple[int, int]:
    """Count how many of the 11 source types returned data vs were attempted."""
    source_keywords = {
        'glassdoor': r'glassdoor',
        'blind': r'(?:team)?blind',
        'reddit': r'reddit|r/',
        'hackernews': r'hacker\s*news|news\.ycombinator|HN\b',
        'linkedin': r'linkedin',
        'layoffs': r'layoffs?\.fyi|layoff',
        'arxiv': r'arxiv',
        'jobboards': r'indeed|job\s*(?:posting|board|listing)',
        'g2_capterra': r'g2\.com|capterra|trustpilot',
        'producthunt': r'product\s*hunt',
        'twitter': r'twitter|x\.com|\btweet',
    }

    found = 0
    attempted = len(source_keywords)

    text_lower = text.lower()
    for _name, pattern in source_keywords.items():
        if re.search(pattern, text_lower):
            # Check it's not just "No results" or "Not found"
            for match in re.finditer(pattern, text_lower):
                context_start = max(0, match.start() - 50)
                context_end = min(len(text_lower), match.end() + 100)
                context = text_lower[context_start:context_end]
                if not re.search(r'no\s+(results?|data|reviews?|information)', context):
                    found += 1
                    break

    return found, attempted


def count_triangulations(text: str) -> int:
    """Count claims where 3+ sources are cited together."""
    # Look for patterns like "3+ sources", "multiple sources", triangulation markers
    patterns = [
        r'3\+?\s*(?:independent\s+)?sources',
        r'(?:three|four|five|multiple)\s+(?:independent\s+)?sources',
        r'triangulat',
        r'corroborat(?:ed|ing|es)',
        r'converge(?:nce|s|d)',
    ]
    count = 0
    for pattern in patterns:
        count += len(re.findall(pattern, text, re.IGNORECASE))
    return count


def temporal_freshness(text: str) -> float:
    """Estimate what fraction of cited dates are within the last 12 months."""
    now = datetime.now()
    cutoff = now - timedelta(days=365)
    cutoff_year = cutoff.year

    # Find year references
    year_pattern = r'\b(20[12]\d)\b'
    years = [int(y) for y in re.findall(year_pattern, text)]

    if not years:
        return 0.5  # No temporal data — neutral score

    recent = sum(1 for y in years if y >= cutoff_year)
    return recent / len(years)


def specificity_score(text: str) -> float:
    """Ratio of specific data (numbers, percentages, proper nouns, dates) to total content."""
    lines = [line for line in text.split('\n') if line.strip()]
    if not lines:
        return 0.0

    specific_patterns = [
        r'\$[\d,.]+[BMK]?',           # Dollar amounts
        r'\d+\.?\d*%',                 # Percentages
        r'\d{1,3}(?:,\d{3})+',        # Large numbers with commas
        r'\d+/\d+',                    # Ratios like 4/5
        r'\b\d{4}-\d{2}',             # ISO dates
        r'Q[1-4]\s*20\d{2}',          # Quarter references
        r'(?:Series\s+[A-F])',         # Funding rounds
        r'SOC\s*2|HIPAA|GDPR|ISO\s*27001',  # Compliance standards
    ]

    lines_with_specifics = 0
    for line in lines:
        for pattern in specific_patterns:
            if re.search(pattern, line):
                lines_with_specifics += 1
                break

    return lines_with_specifics / len(lines)


def evaluate(filepath: str, phase: int = 0) -> dict:
    """Compute Evidence Density Score for a phase output file."""
    text = Path(filepath).read_text(encoding='utf-8')

    n_urls = count_urls(text)
    n_claims = count_claims(text)
    sources_found, sources_attempted = count_source_types_found(text)
    n_triangulations = count_triangulations(text)
    freshness = temporal_freshness(text)
    specificity = specificity_score(text)

    # Component scores (all 0.0 - 1.0)
    url_rate = min(n_urls / max(n_claims, 1), 1.0)
    source_rate = sources_found / max(sources_attempted, 1)
    tri_rate = min(n_triangulations / max(n_claims * 0.3, 1), 1.0)  # Expect 30% of claims triangulated

    # Weighted EDS
    # Phase 4 weights triangulation and source coverage higher
    # Other phases weight URL citations and specificity higher
    if phase == 4:
        weights = {
            'url_citation_rate': 0.15,
            'source_coverage': 0.30,
            'triangulation_rate': 0.25,
            'temporal_freshness': 0.15,
            'specificity_score': 0.15,
        }
    elif phase == 6:
        weights = {
            'url_citation_rate': 0.20,
            'source_coverage': 0.15,
            'triangulation_rate': 0.15,
            'temporal_freshness': 0.20,
            'specificity_score': 0.30,
        }
    else:
        weights = {
            'url_citation_rate': 0.25,
            'source_coverage': 0.20,
            'triangulation_rate': 0.15,
            'temporal_freshness': 0.15,
            'specificity_score': 0.25,
        }

    components = {
        'url_citation_rate': round(url_rate, 3),
        'source_coverage': round(source_rate, 3),
        'triangulation_rate': round(tri_rate, 3),
        'temporal_freshness': round(freshness, 3),
        'specificity_score': round(specificity, 3),
    }

    eds = sum(components[k] * weights[k] for k in weights)

    return {
        'file': filepath,
        'phase': phase,
        'eds': round(eds, 3),
        'components': components,
        'raw_counts': {
            'urls': n_urls,
            'claims': n_claims,
            'sources_found': sources_found,
            'sources_attempted': sources_attempted,
            'triangulations': n_triangulations,
        },
        'weights': weights,
    }


def main():
    if len(sys.argv) < 2:
        print("Usage: python evaluate_phase.py <phase_file.md> [--phase N]", file=sys.stderr)
        sys.exit(1)

    filepath = sys.argv[1]
    phase = 0

    if '--phase' in sys.argv:
        idx = sys.argv.index('--phase')
        if idx + 1 < len(sys.argv):
            phase = int(sys.argv[idx + 1])

    # Auto-detect phase from filename if not specified
    if phase == 0:
        match = re.search(r'0(\d)-', filepath)
        if match:
            phase = int(match.group(1))

    try:
        result = evaluate(filepath, phase)
        print(json.dumps(result, indent=2))
    except FileNotFoundError:
        print(json.dumps({'error': f'File not found: {filepath}'}), file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(json.dumps({'error': str(e)}), file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()

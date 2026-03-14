#!/usr/bin/env python3
"""
X Account Relevance Scorer for Dossier social signal discovery.

Parses the social-signals-x.md output file and computes aggregate
metrics: category distribution, score distribution, coverage gaps,
and an overall Social Signal Coverage Score (SSCS).

Usage:
    python score_x_accounts.py <social-signals-x.md>

Output:
    JSON with scoring summary and quality metrics
"""

import json
import re
import sys
from pathlib import Path
from collections import Counter


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


def parse_account_table(text: str) -> list[dict]:
    """Parse the Top 100 Accounts table from markdown."""
    accounts = []

    # Find the ranked accounts table
    # Format: | Rank | Handle | Name | Category | Relevance | Followers | Signal Summary |
    in_table = False
    header_found = False

    for line in text.split('\n'):
        line = line.strip()
        if not line.startswith('|'):
            if in_table and header_found:
                break  # End of table
            continue

        cols = [c.strip() for c in line.split('|')[1:-1]]  # Strip empty first/last

        if len(cols) < 5:
            continue

        # Skip separator rows
        if all(re.match(r'^[-:]+$', c) for c in cols):
            header_found = in_table
            continue

        # Detect header row
        if any('rank' in c.lower() for c in cols) and any('handle' in c.lower() for c in cols):
            in_table = True
            continue

        if in_table and header_found:
            try:
                # Extract relevance score (handle formats like "85/100" or "85")
                relevance_str = cols[4] if len(cols) > 4 else "0"
                relevance_match = re.search(r'(\d+)', relevance_str)
                relevance = int(relevance_match.group(1)) if relevance_match else 0

                # Extract follower count (handle K, M suffixes)
                followers_str = cols[5] if len(cols) > 5 else "0"
                followers = parse_follower_count(followers_str)

                account = {
                    'rank': int(re.search(r'\d+', cols[0]).group()) if re.search(r'\d+', cols[0]) else 0,
                    'handle': cols[1] if len(cols) > 1 else "",
                    'name': cols[2] if len(cols) > 2 else "",
                    'category': cols[3] if len(cols) > 3 else "Other",
                    'relevance': relevance,
                    'followers': followers,
                    'signal': cols[6] if len(cols) > 6 else "",
                }
                accounts.append(account)
            except (ValueError, IndexError, AttributeError):
                continue

    return accounts


def parse_follower_count(s: str) -> int:
    """Parse follower count strings like '150K', '1.2M', '500'."""
    s = s.strip().replace(',', '')
    match = re.match(r'([\d.]+)\s*([KkMmBb])?', s)
    if not match:
        return 0
    num = float(match.group(1))
    suffix = (match.group(2) or '').upper()
    multiplier = {'K': 1000, 'M': 1_000_000, 'B': 1_000_000_000}.get(suffix, 1)
    return int(num * multiplier)


def categorize(accounts: list[dict]) -> dict:
    """Compute category distribution and identify gaps."""
    cat_counts = Counter()
    for acc in accounts:
        # Normalize category names
        cat = acc['category'].strip()
        matched = False
        for expected in EXPECTED_CATEGORIES:
            if expected.lower() in cat.lower() or cat.lower() in expected.lower():
                cat_counts[expected] += 1
                matched = True
                break
        if not matched:
            cat_counts["Other"] += 1

    # Identify gaps (categories with fewer than 3 accounts)
    gaps = []
    for cat in EXPECTED_CATEGORIES:
        count = cat_counts.get(cat, 0)
        if count < 3:
            gaps.append({'category': cat, 'count': count, 'status': 'missing' if count == 0 else 'underrepresented'})

    return {
        'distribution': dict(cat_counts),
        'gaps': gaps,
        'categories_covered': sum(1 for cat in EXPECTED_CATEGORIES if cat_counts.get(cat, 0) > 0),
        'categories_total': len(EXPECTED_CATEGORIES),
    }


def compute_sscs(accounts: list[dict], categories: dict) -> dict:
    """
    Compute Social Signal Coverage Score (SSCS) — 0.0 to 1.0.

    Components:
      - account_count:      How close to 100 target accounts (0-1)
      - category_coverage:  Fraction of 9 categories with ≥3 accounts (0-1)
      - score_distribution: Evenness of relevance scores (want variety, not all 50s)
      - insider_ratio:      Fraction of accounts that are employees/former employees (want ≥20%)
      - high_signal_ratio:  Fraction of accounts scoring ≥70/100 (want ≥15%)
    """
    n = len(accounts)

    # Account count (100 = 1.0, 50 = 0.5, >100 still 1.0)
    account_score = min(n / 100, 1.0)

    # Category coverage
    well_covered = sum(1 for cat in EXPECTED_CATEGORIES
                       if categories['distribution'].get(cat, 0) >= 3)
    category_score = well_covered / len(EXPECTED_CATEGORIES)

    # Score distribution (want high-scoring accounts)
    if accounts:
        relevances = [a['relevance'] for a in accounts]
        avg_relevance = sum(relevances) / len(relevances)
        score_dist = min(avg_relevance / 70, 1.0)  # 70/100 avg = perfect
    else:
        score_dist = 0.0

    # Insider ratio (employees + former employees)
    insider_cats = {'Current employees', 'Former employees', 'Leadership'}
    insider_count = sum(1 for a in accounts
                        if any(ic.lower() in a['category'].lower() for ic in insider_cats))
    insider_ratio = min((insider_count / max(n, 1)) / 0.25, 1.0)  # Want ≥25% insiders

    # High-signal ratio
    high_signal = sum(1 for a in accounts if a['relevance'] >= 70)
    high_signal_ratio = min((high_signal / max(n, 1)) / 0.15, 1.0)  # Want ≥15% scoring 70+

    # Weighted SSCS
    weights = {
        'account_count': 0.15,
        'category_coverage': 0.30,
        'score_distribution': 0.20,
        'insider_ratio': 0.20,
        'high_signal_ratio': 0.15,
    }

    components = {
        'account_count': round(account_score, 3),
        'category_coverage': round(category_score, 3),
        'score_distribution': round(score_dist, 3),
        'insider_ratio': round(insider_ratio, 3),
        'high_signal_ratio': round(high_signal_ratio, 3),
    }

    sscs = sum(components[k] * weights[k] for k in weights)

    return {
        'sscs': round(sscs, 3),
        'components': components,
        'weights': weights,
    }


def count_search_queries(text: str) -> int:
    """Count WebSearch queries logged in the output."""
    return len(re.findall(r'WebSearch', text, re.IGNORECASE))


def evaluate(filepath: str) -> dict:
    """Full evaluation of a social-signals-x.md file."""
    text = Path(filepath).read_text(encoding='utf-8')

    accounts = parse_account_table(text)
    categories = categorize(accounts)
    sscs = compute_sscs(accounts, categories)

    # Count deep profiles (Top 10 section)
    deep_profiles = len(re.findall(r'###\s+\d+\.\s+@', text))

    return {
        'file': filepath,
        'total_accounts': len(accounts),
        'sscs': sscs['sscs'],
        'sscs_components': sscs['components'],
        'category_distribution': categories['distribution'],
        'category_gaps': categories['gaps'],
        'categories_covered': f"{categories['categories_covered']}/{categories['categories_total']}",
        'deep_profiles': deep_profiles,
        'search_queries_logged': count_search_queries(text),
        'top_5_accounts': [
            {'handle': a['handle'], 'category': a['category'], 'relevance': a['relevance']}
            for a in sorted(accounts, key=lambda x: x['relevance'], reverse=True)[:5]
        ],
    }


def main():
    if len(sys.argv) < 2:
        print("Usage: python score_x_accounts.py <social-signals-x.md>", file=sys.stderr)
        sys.exit(1)

    filepath = sys.argv[1]

    try:
        result = evaluate(filepath)
        print(json.dumps(result, indent=2))
    except FileNotFoundError:
        print(json.dumps({'error': f'File not found: {filepath}'}), file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(json.dumps({'error': str(e)}), file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()

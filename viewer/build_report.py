#!/usr/bin/env python3
"""Dossier Report Builder

Compiles markdown phase outputs into a self-contained HTML report.
Zero external dependencies — uses built-in markdown-to-HTML converter.

Usage:
    python3 viewer/build_report.py [domain]
    python3 viewer/build_report.py              # reads from target.env
"""
from __future__ import annotations

import html as html_mod
import os
import re
import sys
from pathlib import Path
from urllib.parse import urlsplit

# URL schemes allowed in rendered links. Anything else (javascript:, data:,
# vbscript:, ...) is rejected and rendered as inert text. Scheme-less URLs
# (relative paths, #fragments, //protocol-relative) have an empty scheme and
# are always allowed — they cannot carry an executable scheme.
SAFE_URL_SCHEMES = {'http', 'https', 'mailto'}


def _url_is_safe(url):
    """True if the URL has no scheme or an allowlisted one."""
    scheme = urlsplit(html_mod.unescape(url)).scheme.lower()
    return scheme == '' or scheme in SAFE_URL_SCHEMES

DOSSIER_ROOT = Path(__file__).resolve().parent.parent

# ─── Markdown to HTML Converter (zero dependencies) ─────────────────────

STATUS_KEYWORDS = {
    'VERIFIED': 'verified', 'PLAUSIBLE': 'plausible',
    'EXAGGERATED': 'exaggerated', 'CONTRADICTED': 'contradicted',
    'UNVERIFIABLE': 'unverifiable', 'CRITICAL': 'critical',
    'NOTABLE': 'notable', 'MINOR': 'minor',
    'HIGH': 'high', 'MEDIUM': 'medium', 'LOW': 'low',
}


def _inline(text):
    """Process inline markdown: bold, italic, code, links, status tags.

    Security model: the source text is UNTRUSTED (phase outputs are built from
    scraped third-party web content). We HTML-escape the whole line first, so
    any raw markup like <script> becomes inert, then layer trusted markdown
    markup on top. Generated fragments (code spans, links) are stashed behind
    placeholders so later substitution passes cannot corrupt their contents
    (e.g. a status keyword inside a URL rewriting the href attribute).
    """
    # 1. Escape everything first — inert-ifies raw HTML in untrusted content.
    #    escape() touches only & < > " ' and leaves markdown syntax intact.
    text = html_mod.escape(text)

    stash = []

    def _stash(html):
        stash.append(html)
        return f'\x00{len(stash) - 1}\x00'

    # 2. Inline code (before bold/italic to avoid conflicts).
    text = re.sub(
        r'`([^`]+)`',
        lambda m: _stash(f'<code class="inline">{m.group(1)}</code>'),
        text,
    )

    # 3. Links — reject non-allowlisted schemes, stash the rest so later
    #    passes can't rewrite inside the href. label/url are already escaped.
    def _link(m):
        label, url = m.group(1), m.group(2)
        if not _url_is_safe(url):
            return f'[{label}]({url})'  # inert literal text (already escaped)
        return _stash(
            f'<a href="{url}" target="_blank" rel="noopener">{label}</a>'
        )
    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', _link, text)

    # 4. Bold status keywords: **VERIFIED** → styled span
    for kw, cls in STATUS_KEYWORDS.items():
        text = text.replace(
            f'**{kw}**',
            f'<span class="status status-{cls}">{kw}</span>'
        )
    # Bold
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    # Italic (not matching inside bold stars)
    text = re.sub(r'(?<!\*)\*([^*]+?)\*(?!\*)', r'<em>\1</em>', text)
    # Bare status keywords in table cells (without bold markers)
    for kw, cls in STATUS_KEYWORDS.items():
        text = re.sub(
            rf'(?<![">a-zA-Z]){kw}(?![<a-zA-Z])',
            f'<span class="status status-{cls}">{kw}</span>',
            text
        )

    # 5. Restore stashed fragments. Reverse order so a link containing a
    #    stashed code span resolves its inner placeholder too.
    for i in reversed(range(len(stash))):
        text = text.replace(f'\x00{i}\x00', stash[i])
    return text


def md_to_html(text):
    """Convert markdown text to styled HTML. No external dependencies."""
    lines = text.split('\n')
    out = []
    i = 0
    n = len(lines)

    while i < n:
        line = lines[i]
        stripped = line.strip()

        # ── Fenced code block ──
        if stripped.startswith('```'):
            lang = stripped[3:].strip()
            code_lines = []
            i += 1
            while i < n and not lines[i].strip().startswith('```'):
                code_lines.append(html_mod.escape(lines[i]))
                i += 1
            i += 1  # skip closing ```
            cls = f' class="language-{lang}"' if lang else ''
            out.append(f'<pre><code{cls}>{chr(10).join(code_lines)}</code></pre>')
            continue

        # ── Table block ──
        if '|' in stripped and stripped.startswith('|') and stripped.endswith('|'):
            rows = []
            while i < n and '|' in lines[i].strip() and lines[i].strip().startswith('|'):
                cells = [c.strip() for c in lines[i].strip().strip('|').split('|')]
                rows.append(cells)
                i += 1
            if len(rows) >= 2:
                out.append('<div class="table-wrap"><table>')
                # Header
                out.append('<thead><tr>')
                for c in rows[0]:
                    out.append(f'<th>{_inline(c)}</th>')
                out.append('</tr></thead><tbody>')
                # Skip separator row (row[1] if it matches ---pattern)
                start = 2 if re.match(r'^[\s|:-]+$', '|'.join(rows[1])) else 1
                for row in rows[start:]:
                    out.append('<tr>')
                    for c in row:
                        out.append(f'<td>{_inline(c)}</td>')
                    out.append('</tr>')
                out.append('</tbody></table></div>')
            continue

        # ── Header ──
        m = re.match(r'^(#{1,6})\s+(.*)', stripped)
        if m:
            level = len(m.group(1))
            txt = m.group(2)
            slug = re.sub(r'[^a-z0-9]+', '-', txt.lower()).strip('-')
            out.append(f'<h{level} id="{slug}">{_inline(txt)}</h{level}>')
            i += 1
            continue

        # ── Horizontal rule ──
        if re.match(r'^---+\s*$', stripped) or re.match(r'^\*\*\*+\s*$', stripped):
            out.append('<hr>')
            i += 1
            continue

        # ── Unordered list ──
        if re.match(r'^[-*]\s', stripped):
            out.append('<ul>')
            while i < n and re.match(r'^\s*[-*]\s', lines[i]):
                li_match = re.match(r'^\s*[-*]\s+(.*)', lines[i])
                if li_match:
                    content = li_match.group(1)
                    # Checkbox handling
                    if content.startswith('[x] ') or content.startswith('[X] '):
                        out.append(f'<li class="checked">{_inline(content[4:])}</li>')
                    elif content.startswith('[ ] '):
                        out.append(f'<li class="unchecked">{_inline(content[4:])}</li>')
                    else:
                        out.append(f'<li>{_inline(content)}</li>')
                i += 1
            out.append('</ul>')
            continue

        # ── Ordered list ──
        if re.match(r'^\d+\.\s', stripped):
            out.append('<ol>')
            while i < n and re.match(r'^\s*\d+\.\s', lines[i]):
                li_match = re.match(r'^\s*\d+\.\s+(.*)', lines[i])
                if li_match:
                    out.append(f'<li>{_inline(li_match.group(1))}</li>')
                i += 1
            out.append('</ol>')
            continue

        # ── Blockquote ──
        if stripped.startswith('>'):
            bq_lines = []
            while i < n and lines[i].strip().startswith('>'):
                bq_lines.append(re.sub(r'^>\s?', '', lines[i].strip()))
                i += 1
            out.append(f'<blockquote>{_inline(" ".join(bq_lines))}</blockquote>')
            continue

        # ── Blank line ──
        if stripped == '':
            i += 1
            continue

        # ── Paragraph ──
        para_lines = []
        while i < n and lines[i].strip() and not lines[i].strip().startswith('#') \
                and not lines[i].strip().startswith('```') \
                and not lines[i].strip().startswith('|') \
                and not re.match(r'^[-*]\s', lines[i].strip()) \
                and not re.match(r'^\d+\.\s', lines[i].strip()) \
                and not re.match(r'^---+\s*$', lines[i].strip()) \
                and not lines[i].strip().startswith('>'):
            para_lines.append(lines[i].strip())
            i += 1
        if para_lines:
            out.append(f'<p>{_inline(" ".join(para_lines))}</p>')
        continue

    return '\n'.join(out)


# ─── Score Extraction ────────────────────────────────────────────────────

def _extract_first(pattern, text, default='—'):
    m = re.search(pattern, text)
    return m.group(1) if m else default


def _score_to_pct(score_str):
    """Convert a score string like '3.5/5' or '73%' to percentage."""
    m = re.match(r'([\d.]+)/([\d.]+)', score_str)
    if m:
        return str(int(float(m.group(1)) / float(m.group(2)) * 100))
    m = re.match(r'([\d.]+)%', score_str)
    if m:
        return m.group(1)
    return '0'


def extract_scores(exec_md, report_md, claims_md, valuation_md):
    """Extract scorecard values from phase outputs."""
    combined = exec_md + '\n' + report_md + '\n' + claims_md + '\n' + valuation_md

    scores = {}

    # Company name from exec summary title
    m = re.search(r'#\s*Executive Summary:\s*(.+)', exec_md)
    scores['company_name'] = m.group(1).strip() if m else 'Unknown Company'

    # Date
    m = re.search(r'Date:\s*(\S+)', exec_md)
    scores['date'] = m.group(1).strip() if m else ''

    # Ticker — look for NYSE/NASDAQ pattern
    m = re.search(r'(NYSE|NASDAQ):\s*(\w+)', combined)
    scores['ticker'] = f'{m.group(1)}: {m.group(2)}' if m else ''

    # AI Reality Score — flexible: handles bold markers, "out of", prose
    # "AI Reality Score: 3.5/5", "**AI reality score:** 3.8/5", "3 out of 5"
    scores['ai'] = _extract_first(
        r'AI\s*[Rr]eality\s*[Ss]core\D{0,15}(\d+\.?\d*/5)', combined, '—'
    )
    if scores['ai'] == '—':
        scores['ai'] = _extract_first(
            r'AI\s*[Rr]eality\s*[Ss]core\D{0,15}(\d+)\s*out\s*of\s*5', combined, '—'
        )
        if scores['ai'] != '—':
            scores['ai'] = f"{scores['ai']}/5"

    # Revenue Quality — "Revenue Quality: 9/10" or "Revenue Quality Score: 7/10"
    scores['revenue'] = _extract_first(
        r'Revenue\s*Quality\D{0,15}(\d+\.?\d*/10)', combined, '—'
    )

    # Build vs Buy — multiple strategies with increasing specificity
    # Note: X/4 may have spaces around slash: "2.95 / 4.0"
    bvb_num = r'(\d+\.?\d*)\s*/\s*4(?:\.0)?'

    scores['bvb'] = _extract_first(
        r'Build\s*vs\.?\s*Buy.{0,80}?' + bvb_num, combined, '—'
    )
    if scores['bvb'] == '—':  # "Composite score of **3.25/4.0**"
        scores['bvb'] = _extract_first(
            r'[Cc]omposite\s*score\D{0,40}' + bvb_num, combined, '—'
        )
    if scores['bvb'] == '—':  # "replication difficulty score of 3.25/4.0"
        scores['bvb'] = _extract_first(
            r'replication\s*(?:difficulty\s*)?score\D{0,40}' + bvb_num, combined, '—'
        )
    if scores['bvb'] == '—':  # "Overall Score: **2.95 / 4.0**"
        scores['bvb'] = _extract_first(
            r'Overall\s*Score\D{0,20}' + bvb_num, combined, '—'
        )
    if scores['bvb'] == '—':  # "OVERALL | X.X (Hard)" table row → X.X/4
        m = re.search(
            r'OVERALL.*?(\d+\.?\d*)\s*\((?:Easy|Moderate|Hard|Near.impossible)\)',
            combined, re.IGNORECASE
        )
        if m:
            scores['bvb'] = m.group(1)
    if scores['bvb'] == '—':  # Wide bridge for scores deep in tables
        m = re.search(
            r'Build\s*vs\.?\s*Buy[\s\S]{0,5000}?' + bvb_num, combined
        )
        if m:
            scores['bvb'] = m.group(1)
    # Normalize: ensure X/4 format
    if scores['bvb'] != '—' and '/' not in scores['bvb']:
        scores['bvb'] = f"{scores['bvb']}/4"

    # Claims Accuracy — many formats, try each:
    # 1. "Accuracy Rate: 73%"
    scores['accuracy'] = _extract_first(
        r'[Aa]ccuracy\s*(?:[Rr]ate)?[:\s]*(\d+%)', combined, '—'
    )
    # 2. "X/Y verified or plausible" → convert to percentage
    if scores['accuracy'] == '—':
        m = re.search(r'(\d+)/(\d+)\s*(?:claims?\s*)?(?:verified|plausible)', combined, re.IGNORECASE)
        if m:
            num, denom = int(m.group(1)), int(m.group(2))
            if denom > 0:
                scores['accuracy'] = f'{int(num / denom * 100)}%'
    # 3. "73% (11/15..."
    if scores['accuracy'] == '—':
        scores['accuracy'] = _extract_first(r'(\d+)%\s*\(?\d+/\d+\s*(?:claim|verif)', combined, '—')
    # 4. "X of Y claims verified" or "X/Y claim"
    if scores['accuracy'] == '—':
        m = re.search(r'(\d+)\s*(?:of|/)\s*(\d+)\s*claim', combined, re.IGNORECASE)
        if m:
            num, denom = int(m.group(1)), int(m.group(2))
            if denom > 0:
                scores['accuracy'] = f'{int(num / denom * 100)}%'
    # 5. "X verified (Y%)" → extract percentage from parens
    if scores['accuracy'] == '—':
        scores['accuracy'] = _extract_first(
            r'verified\s*\((\d+)%\)', combined, '—'
        )
        if scores['accuracy'] != '—':
            scores['accuracy'] = f"{scores['accuracy']}%"
    # 6. "Y% claims verified"
    if scores['accuracy'] == '—':
        scores['accuracy'] = _extract_first(
            r'(\d+%)\s*claims?\s*verified', combined, '—'
        )

    # Recommendation — broad pattern matching
    rec_patterns = [
        (r'PROCEED WITH CAUTION', 'PROCEED WITH CAUTION'),
        (r'STRONG CANDIDATE', 'STRONG CANDIDATE'),
        (r'QUALIFIED CANDIDATE', 'QUALIFIED CANDIDATE'),
        (r'PROCEED\s*\(', 'PROCEED'),
        (r'(?:Overall|Recommendation)[:\s]*\*{0,2}\s*INVESTIGATE', 'INVESTIGATE'),
        (r'(?:Overall|Recommendation)[:\s]*\*{0,2}\s*PASS\b', 'PASS'),
    ]
    scores['recommendation'] = 'UNKNOWN'
    for pattern, label in rec_patterns:
        if re.search(pattern, combined, re.IGNORECASE):
            scores['recommendation'] = label
            break

    # Map recommendation to CSS class
    rec_map = {
        'PROCEED WITH CAUTION': 'rec-caution',
        'STRONG CANDIDATE': 'rec-strong',
        'QUALIFIED CANDIDATE': 'rec-strong',
        'PROCEED': 'rec-strong',
        'PASS': 'rec-pass',
        'INVESTIGATE': 'rec-investigate',
    }
    scores['recommendation_class'] = rec_map.get(scores['recommendation'], 'rec-unknown')

    # Percentages for bar fills
    scores['ai_pct'] = _score_to_pct(scores['ai'])
    scores['revenue_pct'] = _score_to_pct(scores['revenue'])
    scores['bvb_pct'] = _score_to_pct(scores['bvb'])
    scores['accuracy_pct'] = _score_to_pct(scores['accuracy'])

    return scores


# ─── Quadrant Chart ──────────────────────────────────────────────────────

def extract_quadrant_data(market_md):
    """Parse competitive positioning table from P2 for the quadrant chart."""
    companies = []
    in_table = False
    headers = []

    for line in market_md.split('\n'):
        stripped = line.strip()
        if not stripped.startswith('|'):
            if in_table:
                break
            continue

        cells = [c.strip() for c in stripped.strip('|').split('|')]

        if not in_table:
            # Require BOTH 'vision' AND 'execut' in header to avoid
            # false matches from data rows in earlier tables
            header_text = ' '.join(cells).lower()
            if 'vision' in header_text and 'execut' in header_text:
                headers = cells
                in_table = True
            continue

        # Skip separator
        if re.match(r'^[\s|:-]+$', stripped):
            continue

        # Parse data row — expect: Company | Vision score | Execution score | ...
        if len(cells) >= 3:
            name = re.sub(r'\*+', '', cells[0]).strip()
            try:
                # Find numeric columns
                nums = []
                for c in cells[1:]:
                    m = re.search(r'(\d+\.?\d*)', c)
                    if m:
                        nums.append(float(m.group(1)))
                if len(nums) >= 2:
                    companies.append({
                        'name': name,
                        'vision': nums[0],
                        'execution': nums[1],
                    })
            except (ValueError, IndexError):
                continue

    return companies


def build_quadrant_svg(companies):
    """Generate an SVG quadrant chart from positioning data."""
    if not companies:
        return ''

    svg_parts = [
        '<div class="quadrant-container">',
        '<div class="quadrant-title">Competitive Positioning</div>',
        '<div class="quadrant-chart">',
        '<svg viewBox="0 0 500 500" xmlns="http://www.w3.org/2000/svg">',
        # Background
        '<rect width="500" height="500" fill="#0e1117" rx="4"/>',
        # Grid
        '<line x1="50" y1="450" x2="480" y2="450" stroke="#1e2636" stroke-width="1"/>',
        '<line x1="50" y1="50" x2="50" y2="450" stroke="#1e2636" stroke-width="1"/>',
        # Midlines (quadrant dividers)
        '<line x1="50" y1="250" x2="480" y2="250" stroke="#1e2636" stroke-width="1" stroke-dasharray="4,4"/>',
        '<line x1="265" y1="50" x2="265" y2="450" stroke="#1e2636" stroke-width="1" stroke-dasharray="4,4"/>',
        # Quadrant labels
        '<text x="370" y="150" fill="#2a3348" font-size="13" font-family="DM Mono" text-anchor="middle">Leaders</text>',
        '<text x="155" y="150" fill="#2a3348" font-size="13" font-family="DM Mono" text-anchor="middle">Challengers</text>',
        '<text x="370" y="380" fill="#2a3348" font-size="13" font-family="DM Mono" text-anchor="middle">Visionaries</text>',
        '<text x="155" y="380" fill="#2a3348" font-size="13" font-family="DM Mono" text-anchor="middle">Niche</text>',
        # Axis labels
        '<text x="265" y="490" fill="#7a8295" font-size="11" font-family="Outfit" text-anchor="middle">Completeness of Vision</text>',
        '<text x="15" y="250" fill="#7a8295" font-size="11" font-family="Outfit" text-anchor="middle" transform="rotate(-90,15,250)">Ability to Execute</text>',
    ]

    # Scale: scores 0-10 mapped to pixel range 50-480
    def sx(v):
        return 50 + (v / 10.0) * 430

    def sy(v):
        return 450 - (v / 10.0) * 400

    # Plot companies
    colors = ['#c9a84c', '#60a5fa', '#34d399', '#f59e0b', '#a78bfa',
              '#f87171', '#818cf8', '#fb923c', '#38bdf8', '#4ade80']
    for idx, c in enumerate(companies):
        x = sx(c['vision'])
        y = sy(c['execution'])
        color = colors[idx % len(colors)]
        # Dot
        svg_parts.append(
            f'<circle cx="{x:.0f}" cy="{y:.0f}" r="6" fill="{color}" opacity="0.9"/>'
        )
        # Label (offset to avoid overlap)
        label_x = x + 10
        label_y = y - 10
        svg_parts.append(
            f'<text x="{label_x:.0f}" y="{label_y:.0f}" fill="{color}" '
            f'font-size="11" font-family="Outfit">{html_mod.escape(c["name"])}</text>'
        )

    svg_parts.extend(['</svg>', '</div>', '</div>'])
    return '\n'.join(svg_parts)


# ─── Report Builder ──────────────────────────────────────────────────────

PHASE_FILES = [
    ('executive-summary', 'summary'),
    ('01-discovery', 'p1'),
    ('02-market', 'p2'),
    ('03-technical', 'p3'),
    ('04-claims', 'p4'),
    ('04.5-red-team', 'p45'),
    ('05-academic', 'p5'),
    ('06-valuation', 'p6'),
    ('07-report', 'p7'),
]


def read_target_env():
    """Read domain from target.env."""
    env_file = DOSSIER_ROOT / 'target.env'
    if not env_file.exists():
        print('Error: target.env not found', file=sys.stderr)
        sys.exit(1)
    for line in env_file.read_text().splitlines():
        line = line.strip()
        if line.startswith('DOMAIN='):
            return line.split('=', 1)[1].strip()
    print('Error: DOMAIN not found in target.env', file=sys.stderr)
    sys.exit(1)


def build_report(domain):
    """Build the HTML report for the given domain."""
    output_dir = DOSSIER_ROOT / 'output' / domain
    template_path = DOSSIER_ROOT / 'viewer' / 'template.html'

    if not output_dir.exists():
        print(f'Error: output directory not found: {output_dir}', file=sys.stderr)
        sys.exit(1)
    if not template_path.exists():
        print(f'Error: template not found: {template_path}', file=sys.stderr)
        sys.exit(1)

    # Read template
    template = template_path.read_text()

    # Read all phase files
    phases = {}
    for filename, key in PHASE_FILES:
        filepath = output_dir / f'{filename}.md'
        if filepath.exists():
            phases[key] = filepath.read_text()
        else:
            phases[key] = f'*Phase file not found: {filename}.md*'

    # Extract scores
    scores = extract_scores(
        phases.get('summary', ''),
        phases.get('p7', ''),
        phases.get('p4', ''),
        phases.get('p6', ''),
    )

    # Extract and build quadrant chart
    quadrant_data = extract_quadrant_data(phases.get('p2', ''))
    quadrant_html = build_quadrant_svg(quadrant_data)

    # Convert all phases to HTML
    phase_html = {}
    for key, md in phases.items():
        phase_html[key] = md_to_html(md)

    # Scalar values are regex-extracted from untrusted phase markdown, so
    # HTML-escape them before injecting into the template.
    scalar = {
        '{{COMPANY_NAME}}': scores['company_name'],
        '{{TICKER}}': scores['ticker'],
        '{{DATE}}': scores['date'],
        '{{SCORE_AI}}': scores['ai'],
        '{{SCORE_AI_PCT}}': scores['ai_pct'],
        '{{SCORE_REVENUE}}': scores['revenue'],
        '{{SCORE_REVENUE_PCT}}': scores['revenue_pct'],
        '{{SCORE_BVB}}': scores['bvb'],
        '{{SCORE_BVB_PCT}}': scores['bvb_pct'],
        '{{SCORE_ACCURACY}}': scores['accuracy'],
        '{{SCORE_ACCURACY_PCT}}': scores['accuracy_pct'],
        '{{RECOMMENDATION}}': scores['recommendation'],
        '{{RECOMMENDATION_CLASS}}': scores['recommendation_class'],
    }
    # HTML values are already sanitized by md_to_html / build_quadrant_svg.
    html_values = {
        '{{EXEC_SUMMARY_HTML}}': phase_html.get('summary', ''),
        '{{PHASE_1_HTML}}': phase_html.get('p1', ''),
        '{{QUADRANT_HTML}}': quadrant_html,
        '{{PHASE_2_HTML}}': phase_html.get('p2', ''),
        '{{PHASE_3_HTML}}': phase_html.get('p3', ''),
        '{{PHASE_4_HTML}}': phase_html.get('p4', ''),
        '{{PHASE_4_5_HTML}}': phase_html.get('p45', ''),
        '{{PHASE_5_HTML}}': phase_html.get('p5', ''),
        '{{PHASE_6_HTML}}': phase_html.get('p6', ''),
        '{{PHASE_7_HTML}}': phase_html.get('p7', ''),
    }
    replacements = {k: html_mod.escape(v) for k, v in scalar.items()}
    replacements.update(html_values)

    # Single-pass substitution: each placeholder is replaced exactly once, so
    # a value that happens to contain another placeholder token is not
    # re-expanded (prevents injected {{...}} tokens from pulling in other slots).
    pattern = re.compile('|'.join(re.escape(k) for k in replacements))
    result = pattern.sub(lambda m: replacements[m.group(0)], template)

    # Write output
    output_path = output_dir / 'dossier-report.html'
    output_path.write_text(result)

    # Summary
    size_kb = output_path.stat().st_size / 1024
    print(f'Built: {output_path}')
    print(f'Size:  {size_kb:.0f} KB')
    print(f'Scores: AI={scores["ai"]} Revenue={scores["revenue"]} '
          f'BvB={scores["bvb"]} Accuracy={scores["accuracy"]}')
    print(f'Recommendation: {scores["recommendation"]}')
    if quadrant_data:
        print(f'Quadrant: {len(quadrant_data)} companies plotted')
    else:
        print('Quadrant: no positioning data found (skipped)')


if __name__ == '__main__':
    domain = sys.argv[1] if len(sys.argv) > 1 else read_target_env()
    build_report(domain)

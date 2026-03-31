# Phase 5: Academic & IP Analysis

## Goal
Assess the company's research credibility, intellectual property landscape, and the availability of open-source alternatives.

## Inputs
- `output/{DOMAIN}/01-discovery.md` — company name, founders, tech keywords, product category

## Steps

### 5.1 arXiv Paper Search
Search for academic publications by the company and its founders:
```bash
cd "/Volumes/OWC drive/Dev/dossier"
source target.env
# Search by company name
scripts/.venv/bin/python scripts/arxiv_search.py "{COMPANY_NAME}" 20 > "output/${DOMAIN}/raw/arxiv-papers.json"
```

Also search by:
- Founder/CTO names (from Phase 1)
- Core technology terms (e.g., "transformer architecture", "graph neural network")

### 5.2 Research Landscape
Use WebSearch to understand the broader research context:
- What academic work underpins this product category?
- Are there seminal papers that define the approach?
- Is the core technology based on well-known research or novel methods?
- Are there competing research groups working on the same problem?

### 5.3 Patent Landscape
Use WebSearch to check for:
- Patents filed by the company (`site:patents.google.com "{COMPANY_NAME}"`)
- Patent applications by founders
- Competitor patents in the same space
- Freedom-to-operate considerations

### 5.4 Open-Source Alternatives
Search for open-source projects that overlap with the product:
```bash
# Search GitHub for similar projects
gh search repos "{product category keywords}" --sort=stars --limit=20 --json fullName,description,stargazersCount,language,updatedAt
```

Also WebSearch for:
- "open source alternative to {COMPANY_NAME}"
- "{product category} open source"
- Awesome lists related to the product category

For each alternative found:
- Stars, activity level, maturity
- Feature overlap with target company
- Community size and health
- Licensing (permissive vs copyleft)

### 5.5 Research Credibility Assessment
Evaluate:
- Do founders have relevant academic backgrounds?
- Are company papers cited by others?
- Is the technology based on published, peer-reviewed research?
- Does the team contribute back to the academic community?

## Output

Write `output/{DOMAIN}/05-academic.md`:
```markdown
# Academic & IP Analysis: {COMPANY_NAME}

## Company Publications
| Title | Authors | Year | Venue | Citations | Relevance |
|-------|---------|------|-------|-----------|-----------|
| | | | | | |

## Research Foundation
(what academic work underpins the product)

## Patent Landscape
| Patent/Application | Filed By | Year | Relevant Claims |
|-------------------|----------|------|-----------------|
| | | | |

## Open-Source Alternatives
| Project | Stars | Language | Activity | Feature Overlap | License |
|---------|-------|----------|----------|----------------|---------|
| | | | | | |

## Research Credibility
(team academic backgrounds, publication record, citation impact)

## Build-vs-Buy Implication
(how available is the core technology in open source?)

## Key Findings
- (3-5 most important academic/IP insights)
```

## Source Trust Rules

- arXiv papers authored by the company's own team = FIRST-PARTY. They demonstrate
  research activity but are self-selected (companies don't publish their failures).
- arXiv papers by independent researchers in the same space = INDEPENDENT.
- Patent filings are legal documents — relatively trustworthy as evidence of IP
  investment, but patent CLAIMS about capability are aspirational, not proven.
- If the company's llms.txt or website claims "published research" or "PhD team,"
  verify against actual arXiv/Scholar results. Log discrepancies.
- Open-source alternative searches via GitHub = INDEPENDENT evidence.

## Quality Criteria
- Clearly distinguish company publications from general research
- Note when founders have no academic track record (that's data too)
- Open-source alternatives should be genuinely comparable, not superficially similar
- Patent analysis is necessarily surface-level from public data — note this limitation
- Tag each source with trust class (FIRST-PARTY / INDEPENDENT)

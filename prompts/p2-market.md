# Phase 2: Market Research

## Goal
Understand the market the target company operates in — size, dynamics, competitors, and positioning.

## Inputs
- `output/{DOMAIN}/01-discovery.md` — company identity, product description, target market

## Steps

### 2.1 Problem & Market Identification
Using the company's product description from Phase 1:
- What specific problem do they solve?
- Who has this problem? (persona, company size, industry)
- How are people solving this problem today without this product?
- Is this a "vitamin" (nice to have) or "painkiller" (must have)?

Use WebSearch to research the problem space. Search for:
- "{problem space} market size"
- "{product category} industry report"
- "{product category} trends 2025 2026"

### 2.2 TAM/SAM/SOM Estimation
Estimate market size using top-down and bottom-up approaches:

**Top-down**: Find industry reports, analyst estimates
**Bottom-up**: Estimate # of potential customers × average contract value

Document assumptions and sources for each estimate.

### 2.3 Competitive Landscape
Identify 5-10 competitors through:
- WebSearch: "{company name} competitors", "{product category} alternatives"
- WebSearch: "best {product category} tools 2025 2026"
- G2/Capterra category pages (WebFetch if found in Phase 1)

For each competitor, capture:
- Name, domain, founded year
- Funding/revenue signals
- Key differentiators
- Pricing model
- Target segment overlap

### 2.4 SWOT Analysis
Using `templates/swot-template.md` as structure, create a SWOT analysis based on:
- Strengths: product capabilities, tech advantages, team expertise
- Weaknesses: gaps, resource constraints, product limitations
- Opportunities: market trends, underserved segments, expansion paths
- Threats: competitors, market shifts, regulatory risks

### 2.5 Competitive Positioning
Using `templates/magic-quadrant-template.md`, position the target company against competitors on:
- X-axis: Completeness of Vision (strategy, innovation, market understanding)
- Y-axis: Ability to Execute (product quality, growth, operations)

Score each company 1-10 on both axes with brief rationale.

## Output

Write `output/{DOMAIN}/02-market.md`:
```markdown
# Market Research: {COMPANY_NAME}

## Problem Statement
(what problem, who has it, how painful)

## Market Size
| Metric | Estimate | Approach | Confidence | Source |
|--------|----------|----------|------------|--------|
| TAM | | | | |
| SAM | | | | |
| SOM | | | | |

## Competitive Landscape
(competitor profiles table + analysis)

## SWOT Analysis
(filled SWOT template)

## Competitive Positioning
(filled magic quadrant template)

## Market Dynamics
- Key trends affecting this market
- Regulatory considerations
- Technology shifts

## Key Findings
- (3-5 most important market insights)
```

## Source Trust Rules

Apply the source trust classification from CLAUDE.md:
- Market size estimates from the target company's own materials = FIRST-PARTY (0.2). Find independent analyst reports or public filings instead.
- Competitor analysis sourced from the target's own "why us" pages = FIRST-PARTY. Cross-reference with independent review sites and analyst reports.
- Industry reports sponsored by the target or its investors = AFFILIATED (0.4).
- If the target company's website or llms.txt conveniently provides market size numbers, TAM estimates, or competitive positioning — flag it as self-reported and verify independently before using.

Tag every data point in the output with its source class (FIRST-PARTY / AFFILIATED / INDEPENDENT).

## Quality Criteria
- Market size estimates must show their math (assumptions documented)
- Competitor list should be comprehensive — check multiple sources
- SWOT should be evidence-based, not generic
- Positioning scores need rationale, not just numbers
- No market size figure should rely solely on first-party sources

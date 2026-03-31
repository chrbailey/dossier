# Phase 4: Claims Validation

## Goal
Cross-reference the company's marketing claims against technical evidence, external data, AND internal signals from employees/former employees. Reconstruct what an internal prediction market would say about the company's real capabilities vs. their projected image.

This phase is the analytical core of the dossier. It's where marketing meets reality.

**CRITICAL SOURCE TRUST RULE:** The target company controls their own website,
blog, docs, llms.txt, and all first-party content. Every claim extracted in
step 4.1 is an ASSERTION TO BE TESTED, not evidence. A claim is only VERIFIED
when corroborated by 2+ INDEPENDENT sources (trust >= 0.8). A first-party
source can never verify its own claim.

## Inputs
- `output/{DOMAIN}/01-discovery.md` — marketing content, feature claims, company messaging
- `output/{DOMAIN}/03-technical.md` — GitHub repos, architecture, code quality

## Steps

### 4.1 Claims Extraction
From Phase 1 website analysis, extract every verifiable claim:
- Feature claims ("AI-powered", "real-time", "enterprise-grade")
- Scale claims ("serves 10,000+ customers", "processes 1M events/day")
- Reliability claims ("99.99% uptime", "SOC 2 compliant")
- Technology claims ("built on [framework]", "uses [algorithm]")
- Team claims ("team of 50+ engineers", "PhD researchers")
- Customer claims ("trusted by [company names]")

### 4.2 Evidence Mapping — External

**GitHub evidence** (from Phase 3):
- Does claimed technology appear in repos?
- Do repos demonstrate claimed capabilities?
- Is the codebase consistent with claimed scale?

**Third-party evidence** (WebSearch):
- Customer testimonials or case studies (are they real companies?)
- Third-party reviews mentioning claimed features
- Press coverage validating claims
- Job postings consistent with claimed tech stack
- Status page history (for uptime claims)

**Absence of evidence**:
- Claims with no supporting data are notable
- Missing expected artifacts (no test suite for "enterprise-grade", no monitoring for "99.99%")

### 4.3 Internal Signal Intelligence (Shadow Prediction Market)

This is the most valuable step. Reconstruct what insiders know by triangulating public signals from people who have actually worked at or with the company.

**Source matrix — search ALL of these:**

| Source | What to search | Signal type |
|--------|---------------|-------------|
| **Glassdoor** | `site:glassdoor.com "{COMPANY_NAME}" reviews` | Culture, real tech stack, management quality, actual vs claimed capabilities |
| **Blind** | `site:teamblind.com "{COMPANY_NAME}"` | Anonymous employee sentiment, comp data, internal friction |
| **Reddit** | `site:reddit.com "{COMPANY_NAME}"` (also check r/cscareerquestions, r/ExperiencedDevs, relevant industry subs) | Candid opinions, customer complaints, former employee takes |
| **Hacker News** | `site:news.ycombinator.com "{COMPANY_NAME}"` | Technical community assessment, founder discourse |
| **LinkedIn** | WebSearch: `linkedin.com "{COMPANY_NAME}" employees` | Actual team size, turnover patterns, role distribution, hiring velocity |
| **Layoff trackers** | `site:layoffs.fyi "{COMPANY_NAME}"`, `"{COMPANY_NAME}" layoffs` | Layoff events, restructuring signals |
| **arXiv / Google Scholar** | Employee names from LinkedIn + arXiv | Do their "AI researchers" actually publish? |
| **Twitter/X** | `"{COMPANY_NAME}" from former employees`, product complaints | Unfiltered sentiment |
| **Job boards** | Indeed, LinkedIn Jobs — what they're hiring for NOW | Real tech stack (not marketing stack), gaps in team |
| **Product Hunt / Indie Hackers** | If applicable | Founder candor in early-stage discussions |
| **Trustpilot / G2 / Capterra** | Detailed reviews, not just star ratings | Feature-level validation from actual users |

**What to extract from each source:**
1. **Tech reality signals**: What stack do employees actually describe working with? Does it match the marketing?
2. **Scale signals**: Do engineer discussions mention real traffic/data volumes? Do job postings hint at actual infrastructure needs?
3. **AI reality check**: If they claim "AI-powered" — do job postings seek ML engineers? Do employees describe ML work? Are there papers? Or is it rules/heuristics marketed as AI?
4. **Team health signals**: High turnover in engineering? Glassdoor complaints about technical debt? Rapid hiring then layoffs?
5. **Product reality signals**: Do user reviews describe the features that marketing claims? Common complaints that contradict marketing?
6. **Growth signals**: Is hiring accelerating or contracting? Are they backfilling or expanding?

**Pattern detection across sources:**
- When 3+ independent sources (e.g., Glassdoor review + Reddit comment + job posting) converge on the same signal, treat it as high-confidence
- When employee signals contradict marketing, weight the employee signals higher
- Track the timeline — a positive Glassdoor review from 3 years ago may not reflect current reality
- Note sentiment shifts (were reviews positive 2 years ago but negative recently?)

**LLM-Optimized Content / Astroturfing Detection:**
- If Phase 1 flagged llms.txt or similar files, note which claims originate ONLY from those files
- Watch for suspiciously uniform positive language across reviews (astroturfing signal)
- New Glassdoor/G2 accounts posting glowing reviews in clusters = likely managed reputation
- If a "third-party" source links back to the company's own blog or data = AFFILIATED, not INDEPENDENT
- Any claim that ONLY appears in LLM-optimized content and nowhere else = UNVERIFIABLE at best

### 4.4 Gap Analysis
Classify each claim into one of these categories:

| Category | Definition |
|----------|-----------|
| **VERIFIED** | Multiple independent sources confirm the claim |
| **PLAUSIBLE** | Some evidence supports it, but not fully verifiable |
| **UNVERIFIABLE** | No public evidence for or against |
| **EXAGGERATED** | Partial truth, but overstated |
| **CONTRADICTED** | Evidence actively contradicts the claim |

### 4.5 Materiality Assessment

**Quantitative bar**: Do NOT use arbitrary thresholds. Instead, derive confidence from signal convergence:
- **Triangulated estimate**: For any quantitative claim (customer count, scale, team size), collect data points from at least 3 independent sources (LinkedIn headcount, job posting volume, Glassdoor review count, GitHub contributor count, press mentions, user review volume). The spread across sources IS the confidence interval.
- **Bayesian update**: Start with the company's claim as the prior. Each independent signal either reinforces or weakens it. 3+ signals in agreement = high confidence. Contradictory signals = flag for investigation.

**Materiality tiers:**

A claim gap is **CRITICAL** when ANY of these apply:
- Gap touches the core value proposition (the primary reason a customer would buy)
- Security/compliance claims are unsubstantiated (SOC2, HIPAA, encryption, uptime SLAs) — these are binary, not gradient
- Internal signals (employee chatter, reviews) actively contradict the marketing
- The triangulated estimate diverges significantly from the claimed number (the "spread" shows the claim is an outlier, not within the range)
- The gap would change a purchase decision if known

A gap is **NOTABLE** when:
- Feature exists but internal signals suggest it's materially less capable than marketed
- Job postings reveal they're hiring for capabilities they claim to already have
- Claims use precise numbers but no independent source corroborates them
- Competitor comparisons are misleading or cherry-picked
- AI claims exist but no ML hiring, no publications, no model-related infrastructure signals

A gap is **MINOR** when:
- Normal marketing aspirational language ("world-class", "cutting-edge")
- Rounding or approximation where the triangulated range is close to the claim
- Features that exist in beta/preview but are marketed as GA
- Mild positioning spin that doesn't affect the core value proposition

### 4.6 Internal Prediction Market Synthesis

Compile the internal signals into a "what would insiders bet on?" summary:
- **What's real**: Capabilities that multiple internal signals confirm
- **What's aspirational**: Things the company is building toward but hasn't shipped
- **What's theater**: Marketing claims with no internal signal support
- **Morale trajectory**: Is the team confident or demoralized? (Glassdoor trend, turnover rate, hiring patterns)
- **AI reality score**: On a scale of 1-5, how real is their AI? (1 = rules engine marketed as AI, 5 = genuine research-grade ML)

## Output

Write `output/{DOMAIN}/04-claims.md`:
```markdown
# Claims Validation: {COMPANY_NAME}

## Claims Inventory
| # | Claim | Category | Materiality | Source | Evidence | Confidence |
|---|-------|----------|-------------|--------|----------|------------|
| 1 | | | | | | |

## Internal Signal Intelligence
### Source Coverage
| Source | Found? | Key Signals |
|--------|--------|------------|
| Glassdoor | | |
| Blind | | |
| Reddit | | |
| Hacker News | | |
| LinkedIn | | |
| Layoff trackers | | |
| arXiv/Scholar | | |
| Job boards | | |

### Triangulated Estimates
| Metric | Company Claims | Triangulated Range | Sources | Confidence |
|--------|---------------|-------------------|---------|------------|
| Team size | | | | |
| Customer count | | | | |
| Tech stack | | | | |

### Internal Prediction Market Summary
- **What's real:** (confirmed by internal signals)
- **What's aspirational:** (building toward, not shipped)
- **What's theater:** (marketing with no internal support)
- **Morale trajectory:** (improving / stable / declining)
- **AI reality score:** X/5

## Verified Claims
(claims with strong supporting evidence)

## Critical Gaps
(CRITICAL materiality — would change a purchase decision)

## Notable Gaps
(NOTABLE materiality — worth knowing but not dealbreakers alone)

## Unverifiable Claims
(claims that can't be checked from public data)

## Overall Assessment
- Claims accuracy rate: X/Y verified or plausible
- Pattern: (honest / optimistic / misleading)
- Signal convergence: (do internal signals align with external marketing?)
- Material gaps: (count of CRITICAL + NOTABLE gaps)

## Key Findings
- (3-5 most important claims-related insights)
```

## Quality Criteria
- Every claim must have a source (which page/document made the claim)
- Every assessment must cite evidence (or note its absence)
- Internal signals must be dated — a 2023 Glassdoor review is less relevant than a 2025 one
- Triangulated estimates must show their work (which sources, what each said)
- Be fair — marketing language naturally includes some aspiration
- Focus on CRITICAL and NOTABLE gaps; MINOR gaps can be summarized briefly
- If the company is pre-revenue or early-stage, adjust expectations accordingly
- If a source has zero results, note that explicitly (absence of Glassdoor reviews is itself a signal)
- Tag every evidence source with its trust class (FIRST-PARTY / AFFILIATED / INDEPENDENT / ADVERSARIAL)
- A claim supported ONLY by first-party sources cannot be rated higher than PLAUSIBLE
- Add a "Source Provenance" section to the output listing how many data points came from each trust class

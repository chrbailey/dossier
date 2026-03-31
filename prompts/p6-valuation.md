# Phase 6: Valuation & Replication Assessment

## Goal
Estimate the company's value signals and assess the feasibility and cost of replicating their product using an AI agent swarm.

## Inputs
Read ALL prior phase outputs:
- `output/{DOMAIN}/01-discovery.md` — company profile, team size
- `output/{DOMAIN}/02-market.md` — market size, competitive position
- `output/{DOMAIN}/03-technical.md` — architecture, repos, code quality
- `output/{DOMAIN}/04-claims.md` — verified capabilities
- `output/{DOMAIN}/05-academic.md` — IP landscape, open-source alternatives

## Steps

### 6.1 Business Model Analysis
From Phase 1 and Phase 2, assess:
- Revenue model (subscription, usage-based, freemium, enterprise)
- Pricing tiers and implied ACV (annual contract value)
- Customer segments (SMB, mid-market, enterprise)
- Go-to-market strategy (PLG, sales-led, partner-led)
- Estimated revenue range (use signals: team size, funding, pricing)

### 6.2 SaaS Metrics Estimation
Estimate where possible (note confidence level):
- ARR range (from team size, funding, pricing signals)
- Customer count range (from marketing claims, review counts)
- Growth signals (hiring pace, product releases, market expansion)
- Churn signals (feature maturity, switching costs, competitor pressure)
- Net revenue retention signals (expansion products, usage-based pricing)

### 6.3 Replication Assessment
Estimate what it would take to rebuild this product:

**Scope estimation:**
- Estimated total LOC (from GitHub + inference about private code)
- Number of major components/services
- Data requirements (training data, knowledge bases, integrations)
- Infrastructure complexity (cloud services, scaling requirements)

**Team estimation:**
- Engineering roles needed (frontend, backend, ML, infra, etc.)
- Minimum viable team size
- Timeline to MVP vs full parity
- Non-engineering needs (design, data, domain expertise)

**Cost estimation:**
- Engineering cost (team × timeline × market rate)
- Infrastructure cost (cloud, data, tooling)
- Data acquisition cost (training data, content, partnerships)
- Go-to-market cost (ignored — separate concern)

### 6.4 Agent Swarm Replication Plan
Design a Claude Code agent swarm that could rebuild key components:

For each major component:
- Which sub-agent type handles it (code generation, testing, research)
- What MCP tools/servers would be needed
- Estimated agent-hours
- Dependencies between agent tasks
- What can't be automated (data, partnerships, domain expertise)

### 6.5 Build vs Buy Assessment
Weigh:
- Time-to-market: build from scratch vs buying/licensing
- Competitive moat: what's defensible vs easily replicated
- Technical differentiation: proprietary tech vs commodity stack
- Team expertise: specialized knowledge vs general engineering

Score each factor:
- **Easy to replicate** (1): Commodity technology, well-documented approaches
- **Moderate effort** (2): Non-trivial but achievable with competent team
- **Hard to replicate** (3): Requires specialized expertise, data, or time
- **Near-impossible** (4): Unique data, network effects, regulatory approvals

## Output

Write `output/{DOMAIN}/06-valuation.md`:
```markdown
# Valuation & Replication: {COMPANY_NAME}

## Business Model
(revenue model, pricing, GTM strategy)

## SaaS Metrics (Estimated)
| Metric | Estimate | Confidence | Basis |
|--------|----------|------------|-------|
| ARR Range | | | |
| Customer Count | | | |
| Growth Rate | | | |
| ACV | | | |

## Replication Assessment
### Scope
| Component | Estimated LOC | Complexity | Notes |
|-----------|--------------|------------|-------|
| | | | |

### Team & Timeline
| Scenario | Team Size | Timeline | Cost |
|----------|-----------|----------|------|
| MVP | | | |
| Feature Parity | | | |
| Full Platform | | | |

## Agent Swarm Plan
### Component Breakdown
| Component | Agent Type | Tools Needed | Agent-Hours | Automatable? |
|-----------|-----------|--------------|-------------|-------------|
| | | | | |

### What Can't Be Automated
- (data moats, partnerships, domain expertise, network effects)

## Build vs Buy Score
| Factor | Score (1-4) | Rationale |
|--------|------------|-----------|
| Core Technology | | |
| Data/Content | | |
| Integrations | | |
| UX/Design | | |
| Domain Expertise | | |
| **Overall** | | |

## Key Findings
- (3-5 most important valuation/replication insights)
```

## Source Trust Rules

This phase synthesizes all prior phases. Apply these rules:
- Revenue/growth estimates from the company's own materials = FIRST-PARTY (0.2).
  Prefer triangulated estimates from P4 over self-reported figures.
- If P4.5 (Red Team) downgraded any claims used here, use the downgraded ratings.
- SaaS metrics should be derived from INDEPENDENT signals (team size from LinkedIn,
  customer count from review volume, growth from hiring pace) not company press releases.
- Replication assessment should use CODE-VERIFIED findings from P3, not CLAIMED capabilities.

## Quality Criteria
- All estimates must show their reasoning — no numbers without rationale
- Clearly separate facts from inferences
- Replication assessment should be honest — some things are genuinely hard
- Agent swarm plan should be concrete enough to act on
- Build vs Buy scoring should help decision-making, not just be academic
- Note which inputs came from red-team-adjusted vs original P4 ratings

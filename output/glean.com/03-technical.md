# Phase 3: Technical Analysis — Glean Technologies

**Target:** glean.com
**Date:** 2026-02-19
**Analyst:** Claude (Phase 3 sub-agent)
**Status:** COMPLETE

---

## GitHub Presence

| Metric | Value |
|--------|-------|
| GitHub Org | [gleanwork](https://github.com/gleanwork) |
| Org Created | 2022-02-24 |
| Total Public Repos | 26 (3 archived) |
| Total Stars (public) | ~352 |
| Primary Languages | TypeScript (9 repos), Python (8 repos), Java (2), Go (1), JavaScript (3), Shell (1) |
| Active Contributors (across top 6 repos) | ~40 unique (some overlap) |
| Repository Stability Policy | Formal 3-tier: Experimental / Prerelease / GA |
| License | MIT (majority), some unlicensed |

**Critical caveat:** Glean is a private company with ~1,400 employees. These 26 public repos represent the developer-facing surface area only. The core search platform, Knowledge Graph, RAG pipeline, crawler infrastructure, ML models, and production services are entirely private. Based on the engineering team size (estimated 400-600 engineers across Palo Alto, Bellevue, Bengaluru), the private codebase is likely hundreds of repositories.

---

## Repository Inventory

### Active Repositories (sorted by stars)

| Repo | Stars | Forks | Language | Last Updated | CI | Tests | License | Stability |
|------|-------|-------|----------|-------------|-----|-------|---------|-----------|
| [remote-mcp-server](https://github.com/gleanwork/remote-mcp-server) | 158 | 1 | -- (config only) | 2026-02-13 | -- | -- | MIT | GA |
| [mcp-server](https://github.com/gleanwork/mcp-server) | 55 | 19 | TypeScript | 2026-02-12 | 5 workflows (CI, Docker, deploy-docs, format, publish) | Yes (vitest) | MIT | Prerelease |
| [glean-agent-toolkit](https://github.com/gleanwork/glean-agent-toolkit) | 53 | 11 | Python | 2026-01-17 | 2 workflows (CI, publish) | Yes (pytest, 10+ test files, VCR cassettes) | MIT | -- |
| [api-client-python](https://github.com/gleanwork/api-client-python) | 14 | 6 | Python | 2026-02-19 | 4 workflows (test, SDK gen, SDK publish, patch) | Yes (37 test files, mock server) | MIT | -- |
| [langchain-glean](https://github.com/gleanwork/langchain-glean) | 10 | 3 | Python | 2026-02-18 | 2 workflows (CI, publish) | Yes (unit + integration) | MIT | -- |
| [indexing-api-connectors](https://github.com/gleanwork/indexing-api-connectors) | 10 | 9 | Python | 2026-02-15 | -- | -- | None | -- |
| [claude-plugins](https://github.com/gleanwork/claude-plugins) | 10 | 0 | Shell | 2026-02-18 | -- | -- | MIT | -- |
| [api-client-typescript](https://github.com/gleanwork/api-client-typescript) | 9 | 3 | TypeScript | 2026-02-19 | -- | -- | MIT | -- |
| [mcp-config](https://github.com/gleanwork/mcp-config) | 7 | 0 | TypeScript | 2026-02-17 | -- | -- | MIT | -- |
| [glean-agent-examples](https://github.com/gleanwork/glean-agent-examples) | 5 | 3 | Python | 2025-07-30 | -- | -- | MIT | -- |
| [open-api](https://github.com/gleanwork/open-api) | 4 | 5 | JavaScript | 2026-02-19 | 8 workflows (transform, test, code-samples, deploy, diff, trigger-client-gen, trigger-site-redeploy, commit-changes) | Yes (vitest) | None | -- |
| [mcp-server-tester](https://github.com/gleanwork/mcp-server-tester) | 4 | 0 | TypeScript | 2026-02-17 | -- | Yes (Playwright + vitest) | MIT | -- |
| [glean-developer-site](https://github.com/gleanwork/glean-developer-site) | 4 | 7 | TypeScript | 2026-02-19 | -- | -- | None | -- |
| [api-client-go](https://github.com/gleanwork/api-client-go) | 3 | 0 | Go | 2026-02-19 | -- | -- | MIT | -- |
| [api-client-java](https://github.com/gleanwork/api-client-java) | 3 | 0 | Java | 2026-02-19 | -- | -- | MIT | -- |
| [querycsv](https://github.com/gleanwork/querycsv) | 3 | 2 | Python | 2025-12-11 | -- | -- | MIT | -- |
| [glean-indexing-sdk](https://github.com/gleanwork/glean-indexing-sdk) | 2 | 0 | Python | 2026-02-05 | -- | -- | MIT | -- |
| [glean-proxy](https://github.com/gleanwork/glean-proxy) | 0 | 2 | Java | 2026-02-03 | -- | Yes (JUnit + Mockito) | MIT | -- |
| [n8n-nodes-gleanclient](https://github.com/gleanwork/n8n-nodes-gleanclient) | 0 | 0 | JavaScript | 2025-11-20 | -- | -- | MIT | -- |
| [configure-mcp-server](https://github.com/gleanwork/configure-mcp-server) | 0 | 1 | TypeScript | 2026-02-02 | -- | -- | MIT | -- |
| [web-sdk-embed-examples](https://github.com/gleanwork/web-sdk-embed-examples) | 0 | 0 | JavaScript | 2025-12-11 | -- | -- | MIT | -- |
| [glean-partner-workshop-ptob](https://github.com/gleanwork/glean-partner-workshop-ptob) | 0 | 1 | Python | 2025-04-07 | -- | -- | MIT | -- |

### Archived Repositories

| Repo | Language | Archived Date | Notes |
|------|----------|---------------|-------|
| typescript-sdk | TypeScript | ~2026-01 | Fork of MCP TypeScript SDK, superseded by upstream |
| connect-mcp-server | TypeScript | ~2026-01 | Early MCP server attempt, superseded by mcp-server |
| mcp-config-glean | TypeScript | 2026-01-13 | Superseded by mcp-config |

---

## Architecture Assessment

### Confirmed Production Infrastructure (from Google Cloud partnership)

| Layer | Technology | Evidence |
|-------|-----------|----------|
| **Cloud Provider** | Google Cloud Platform (primary) | [Google Cloud Blog](https://cloud.google.com/blog/products/data-analytics/glean-uses-bigquery-and-google-ai-to-enhance-enterprise-search) |
| **Compute** | Google Kubernetes Engine (GKE) | Google Cloud Blog — search index hosted on GKE |
| **App Hosting** | Google App Engine | Google Cloud Blog |
| **Data Processing** | Google Cloud Dataflow | Joins signals with parsed content, extracts relevance features |
| **Analytics** | BigQuery, BigQuery ML | Google Cloud Blog |
| **ML Training** | Vertex AI | Vector embeddings trained on Vertex AI |
| **Task Queue** | Google Cloud Tasks | Google Cloud Blog |
| **Storage** | Google Cloud Storage, Cloud SQL | SiliconANGLE partnership coverage |
| **Secondary Cloud** | AWS (Amazon Bedrock integration, RDS) | [AWS Marketplace Blog](https://aws.amazon.com/blogs/awsmarketplace/transform-enterprise-search-knowledge-discovery-glean-amazon-bedrock/) |
| **On-Premises** | Dell AI Factory | [Dell partnership](https://www.dell.com/en-us/blog/dell-glean-on-premises-solution-enterprise-ai-search/) (May 2025) |

### Architecture Style: Microservices on Kubernetes

**Evidence:**
- GKE as primary compute (container orchestration)
- Dedicated data processing pipelines (Cloud Dataflow)
- Separate API namespaces: Client API (`/rest/api/v1`), Indexing API (`/api/index/v1`), Admin API (`/rest/api/v1`)
- Custom HTTP proxy (`glean-proxy`) built on LittleProxy/Netty for network egress — signals a microservices architecture with controlled egress patterns
- Bazel build system in `glean-proxy` — typical for large-scale microservices shops (Google-heritage engineers)
- Monorepo structure in `mcp-server` (pnpm workspaces)
- Dockerfile present in mcp-server with Docker-based CI

### API Design: REST (OpenAPI 3.0)

**Three distinct API surfaces documented in `open-api` repo:**

1. **Client REST API** (`client_rest.yaml`) — Search, chat, activity reporting, feedback, documents, entities, calendar, governance, tools. Bearer token auth.
2. **Indexing API** (`indexing.yaml`) — Document indexing, people data, permissions management, datasource configuration. Separate token namespace from Client API.
3. **Admin REST API** (`admin_rest.yaml`) — Governance policies, admin operations. Supports both bearer token and cookie auth.

**API characteristics:**
- OpenAPI 3.0 spec (not 3.1)
- Server URL pattern: `https://{domain}-be.glean.com/...` — tenant-isolated backend per customer domain
- 6-month sunset policy for breaking changes (documented)
- SDKs auto-generated via [Speakeasy](https://speakeasyapi.dev/) (confirmed by `.speakeasy/` directory in api-client-python)
- `x-visibility: Public` annotations on operations — implies internal-only operations exist on same spec

### MCP (Model Context Protocol) Strategy

Glean has invested heavily in MCP as a strategic integration layer:

1. **Remote MCP Server** (GA) — Hosted by Glean, OAuth 2.0 auth with SSO, Streamable HTTP transport. Listed on [MCP Registry](https://registry.modelcontextprotocol.io). Zero code deployment — just point any MCP client at the org URL.
2. **Local MCP Server** (v0.9.1) — Self-hosted TypeScript server wrapping Glean APIs. Tools: `chat`, `search`, `people_profile_search`, `read_documents`. Published as npm package `@gleanwork/local-mcp-server`.
3. **MCP Config** — Type-safe configuration builder for MCP client setups.
4. **MCP Server Tester** — Playwright-based testing and eval framework with LLM-as-a-judge. Novel approach to MCP quality assurance.
5. **Claude Plugins** — Official Glean plugins for Claude Code integration.
6. **Configure MCP Server** — CLI tool for MCP server setup.

### Agent Framework Integration

The `glean-agent-toolkit` provides adapters for 5 agent frameworks:

| Framework | Adapter | Status |
|-----------|---------|--------|
| OpenAI Agents SDK | `openai.py` | Supported |
| Google ADK | `adk.py` | Supported |
| LangChain | `langchain.py` | Supported (also standalone `langchain-glean` package) |
| CrewAI | `crewai.py` | Supported |
| Base (custom) | `base.py` | Abstract adapter for custom frameworks |

**Tools exposed through agent toolkit:**
- `search` — Enterprise search
- `employee_search` — People lookup
- `code_search` — Code-specific search
- `calendar_search` — Calendar events
- `gmail_search` — Email search
- `outlook_search` — Outlook email search
- `web_search` — Web search through Glean
- `read_document` — Document retrieval

### Knowledge Graph Architecture (Inferred from public sources)

**Three data pillars:**
1. **Content** — Documents, messages, tickets across 100+ connectors. Full content analysis (titles, body, comments, media) plus metadata extraction.
2. **People** — User identities, roles, teams, organizational hierarchies. Personal graph per employee (projects, collaborators, work style).
3. **Activity** — User interactions, document history, engagement patterns. Feeds relevance ranking.

**Technical implementation signals:**
- ML pipeline infers higher-level entities (projects, customers, products, teams) from raw data structures
- Entity extraction: descriptive terms + relationship predicates (e.g., "document authored by person", "project led by")
- Iterative quality filters to reduce over-inclusion
- Hybrid search: lexical + vector, constrained by graph neighborhoods
- Vector embeddings stored in search index on GKE
- Amazon RDS for structured graph storage ([AWS Blog](https://aws.amazon.com/blogs/awsmarketplace/transform-enterprise-search-knowledge-discovery-glean-amazon-bedrock/))
- Real-time permission syncing from source systems

### LLM Strategy: Model-Agnostic Abstraction Layer

| Supported Model | Provider | Integration |
|-----------------|----------|-------------|
| Claude 3 Sonnet | AWS Bedrock | Confirmed |
| Gemini 1.5 Pro | Google Vertex AI | Confirmed |
| GPT-3.5 / GPT-4 | OpenAI | Confirmed |
| Open-source models | Various | Via Model Hub |
| Proprietary Glean models | In-house | Enterprise context-specific (not foundation LLMs) |

**Key insight:** Glean's in-house model work focuses on enterprise context understanding (entity extraction, relevance ranking, permission inference) rather than building general-purpose LLMs. The company positions itself as the "abstraction layer" between models and enterprise data — allowing customers to swap LLMs without retraining. This is a significant architectural bet: context and governance are the moat, not the model.

---

## Code Quality Signals

### Build & Tooling Ecosystem

| Tool | Usage | Repos |
|------|-------|-------|
| **TypeScript** | Primary language for developer tools | mcp-server, api-client-typescript, mcp-config, mcp-server-tester |
| **Python** | Agent toolkit, API clients | glean-agent-toolkit, api-client-python, langchain-glean |
| **pnpm** | JS package manager | mcp-server (monorepo with workspaces) |
| **uv** | Python package manager | glean-agent-toolkit, langchain-glean |
| **mise** | Task runner / polyglot tool manager | mcp-server, glean-agent-toolkit, api-client-python, open-api, langchain-glean |
| **Bazel** | Build system | glean-proxy (Google-heritage) |
| **Hatchling** | Python build backend | glean-agent-toolkit |
| **Poetry** | Python dependency management | api-client-python |
| **Speakeasy** | SDK auto-generation | api-client-python, api-client-typescript, api-client-go, api-client-java |
| **Vitest** | Test runner (JS) | mcp-server, open-api |
| **Pytest** | Test runner (Python) | glean-agent-toolkit, api-client-python, langchain-glean |
| **Playwright** | E2E testing | mcp-server-tester |
| **ESLint** | JS/TS linting | mcp-server |
| **Ruff** | Python linting + formatting | glean-agent-toolkit |
| **Pyright** | Python type checking | glean-agent-toolkit |
| **VitePress** | Documentation site | mcp-server |
| **release-it** | Release automation | mcp-server, remote-mcp-server |
| **Commitizen** | Conventional commits | glean-agent-toolkit |
| **pre-commit** | Git hooks | glean-agent-toolkit, glean-proxy |

### CI/CD Coverage

| Repo | CI Workflows | Automated Tests | Release Automation |
|------|-------------|-----------------|-------------------|
| mcp-server | 5 (CI, Docker test, deploy-docs, format-on-merge, publish-docker) | vitest | release-it + CHANGELOG |
| api-client-python | 4 (test, SDK gen, SDK publish, patch-speakeasy-pr) | pytest (37 files) | Speakeasy auto-gen |
| open-api | 8 (transform, test, code-samples, diff-report, deploy-pages, trigger-client-gen, trigger-site-redeploy, commit-changes) | vitest | Automated spec pipeline |
| glean-agent-toolkit | 2 (CI, publish) | pytest | Commitizen |
| langchain-glean | 2 (CI, publish) | pytest | -- |

### Testing Maturity

**Strongest testing:** `api-client-python` (37 test files covering activities, agents, announcements, answers, auth, calendar, chat, client, collections, datasources, entities, governance, indexing, insights, messages, people, pins, policies, reports, search, summarize, tools, troubleshooting, visibility overrides + mock server).

**Notable testing pattern:** `glean-agent-toolkit` uses VCR cassettes (recorded HTTP interactions) for repeatable API testing without live Glean access. Marks include `load_json` fixtures and `vcr_record_with_real_auth`.

**`mcp-server-tester`** is a novel open-source contribution — a Playwright-based framework for testing MCP servers with LLM-as-a-judge evaluation. This signals engineering maturity around the MCP ecosystem.

### Documentation Quality

- **README quality:** High across major repos. remote-mcp-server has polished README with badges, feature list, and docs links.
- **CONTRIBUTING.md:** Present in 8 repos.
- **AGENTS.md:** Present in glean-agent-toolkit — instructions for AI coding agents.
- **CLAUDE.md:** Present in langchain-glean and mcp-server-tester — Claude Code specific context files.
- **CHANGELOG.md:** Present in 7 repos with proper versioning.
- **Developer site:** Full developer portal at developers.glean.com with docs, API reference, SDKs, MCP guide, changelog.
- **Repository stability policy:** Formal 3-tier classification (Experimental/Prerelease/GA) at org level.
- **CODEOWNERS:** Present in glean-agent-toolkit, open-api, langchain-glean.

### Security Practices

- **SECURITY.md:** Not found in public repos (likely handled at org level).
- **NullAway** (annotation-based null safety) in glean-proxy — static analysis for null pointer prevention.
- **pip-audit** in glean-agent-toolkit dev dependencies — automated dependency vulnerability scanning.
- **Dependabot:** Active (evidence: automated dependency bump PRs on mcp-server).
- **GPG signing:** Maven GPG plugin configured in glean-proxy.
- `.pre-commit-config.yaml` in glean-agent-toolkit and glean-proxy.

---

## Dependency Analysis

### MCP Server (TypeScript)

| Dependency | Purpose | Risk |
|------------|---------|------|
| `@gleanwork/api-client` 0.13.0 | Glean's own API client | Internal ecosystem dependency |
| `@modelcontextprotocol/sdk` ^1.26.0 | Official MCP SDK | Actively maintained |
| `zod` ^4.1.13 | Schema validation | Zod 4 is latest — up to date |
| `dotenv` ^17.2.3 | Environment config | Standard |
| `meow` ^14.0.0 | CLI framework | Standard |
| `tldts` ^7.0.19 | Domain parsing | Niche but well-maintained |

### Agent Toolkit (Python)

| Dependency | Purpose | Risk |
|------------|---------|------|
| `pydantic` >=2.7,<3.0 | Data validation | Current |
| `glean-api-client` >=0.6.0,<1.0 | Glean's own API client | Internal dependency |
| Optional: `openai` >=1.0,<2.0 | OpenAI integration | Current |
| Optional: `openai-agents` >=0.0.11,<1.0 | OpenAI Agents SDK | Very early (0.0.x) |
| Optional: `langchain` >=0.1.0,<1.0 | LangChain | Current |
| Optional: `crewai` >=0.28.0,<1.0 | CrewAI | Current |
| Optional: `google-adk` >=1.7.0,<2.0 | Google ADK | Current |

### Glean Proxy (Java)

| Dependency | Purpose | Risk |
|------------|---------|------|
| `littleproxy` 2.4.0 | HTTP proxy core | Niche but maintained |
| `netty-codec-http` 4.1.127.Final | Network framework | Current |
| `gson` 2.10.1 | JSON parsing | Current |
| `httpclient` 4.5.14 | HTTP client | Legacy (Apache HttpClient 4.x) |
| `nullaway` 0.10.9 | Null safety | Active — Uber's null checker |
| Java 17 target | -- | Current LTS |

### Internal Ecosystem

Glean maintains a self-referencing dependency chain:
```
open-api (source specs)
  --> Speakeasy generates --> api-client-{python,typescript,go,java}
  --> api-client-python --> glean-agent-toolkit
  --> api-client-typescript --> mcp-server (@gleanwork/api-client)
  --> langchain-glean depends on glean-api-client
```

The `open-api` repo has 8 CI workflows including `trigger-client-generation` and `trigger-developer-site-redeploy` — when API specs change, SDK clients are automatically regenerated and the developer site is redeployed. This is a sophisticated CI pipeline.

---

## Security Architecture (from public documentation)

| Control | Implementation | Source |
|---------|---------------|--------|
| **Encryption at rest** | AES-256 | [Glean Security](https://www.glean.com/security) |
| **Encryption in transit** | TLS 1.3 | Glean Security |
| **Key management** | KMS (FIPS 140-2 compliant) | Glean Security |
| **Data model** | Zero-copy — content stays in source systems, only vectors/metadata cached | Glean Security |
| **Permissions** | Real-time ACL sync from source systems, enforced at index and query time | Glean Blog, Docs |
| **Tenant isolation** | Per-customer backend deployment (`{domain}-be.glean.com`) | OpenAPI spec URL pattern |
| **SOC 2 Type II** | Certified | [Glean Security](https://www.glean.com/security) |
| **ISO 27001** | Certified | Glean Security |
| **GDPR compliance** | Supported | Glean Security |
| **HIPAA compliance** | Supported | Glean Security |
| **Audit logging** | Full | Glean Security |
| **Governance API** | Policy management via Admin REST API | admin_rest.yaml spec |

**Notable:** The Admin REST API includes `/governance/data/policies/{id}` endpoints — a first-class governance API for data access policies. This is rare in the enterprise search space and aligns with Glean's "permission-aware AI" positioning.

---

## Open Source Health

### Maintenance Activity

- **API clients** (Python, TypeScript, Go, Java): Updated daily/weekly via Speakeasy auto-generation. Python client at v0.12.7 (released 2026-02-19 — today). TypeScript at v0.14.6 (released today). High automation, low manual effort.
- **mcp-server:** Active development. Last release v0.9.1 (Dec 2025). 9 contributors. Open issues: 9 (including Dependabot, feature requests, bugs).
- **glean-agent-toolkit:** 5 contributors. Last release v0.3.0 (Jul 2025). More sporadic release cadence.
- **langchain-glean:** 4 contributors. Last release v0.3.4 (Jan 2026). Steady updates.
- **open-api:** Updated today. 8 CI workflows. This is the canonical source of truth for all API specs — the most operationally important repo.

### Community Engagement

- **External contributors:** Limited. Most repos show primarily Glean employees. Some community PRs on mcp-server (e.g., feature request for pagination from external user `aaronsb`).
- **Issue response time:** Mixed. Some issues open since mid-2025 without resolution (mcp-server #206, #239, #254). The Dependabot PR (#324) has been open since Jan 2026.
- **Fork activity:** mcp-server (19 forks), glean-agent-toolkit (11 forks), indexing-api-connectors (9 forks) — decent for developer tooling repos.

### Versioning Discipline

- API clients: Automated semantic versioning via Speakeasy.
- mcp-server: release-it with lerna-changelog. Proper CHANGELOG.md.
- glean-agent-toolkit: Commitizen (conventional commits). CHANGELOG.md present.
- Repository stability labels: Formal policy (Experimental/Prerelease/GA) — mature governance.

---

## Technical Strengths

1. **Sophisticated CI/CD pipeline.** The `open-api` repo orchestrates a multi-repo automation chain: spec changes trigger SDK regeneration across 4 languages, developer site redeployment, and diff reports. This is enterprise-grade release engineering.

2. **Deep MCP investment.** Six MCP-related repos including a novel testing framework (mcp-server-tester with Playwright + LLM-as-a-judge). Remote MCP Server at GA stability. This positions Glean as the MCP-first enterprise data provider.

3. **Multi-framework agent support.** The agent-toolkit supports 5 major agent frameworks (OpenAI, Google ADK, LangChain, CrewAI, custom) through a clean adapter pattern with a `@tool_spec` decorator. Well-architected for extensibility.

4. **Google-caliber infrastructure.** GKE, Cloud Dataflow, Vertex AI, BigQuery stack with auto-scaling. Bazel build system in production code. This is consistent with the founding team's Google engineering pedigree.

5. **Model-agnostic architecture.** Supports Claude, Gemini, and GPT models simultaneously. Enterprise Graph (context layer) is decoupled from the LLM layer. This is a defensible architectural choice that avoids model vendor lock-in.

6. **Permission-aware by design.** Real-time ACL sync, query-time permission enforcement, tenant-isolated backends. Security is structural, not bolted on. SOC 2 Type II + ISO 27001 certified.

7. **Professional open-source governance.** Repository stability policy, CODEOWNERS, AGENTS.md/CLAUDE.md for AI coding assistants, CONTRIBUTING.md, automated releases, conventional commits.

---

## Technical Concerns

1. **Open-source community engagement is weak.** Despite 26 public repos, there is minimal external contributor activity. Issues go unanswered for months (mcp-server #206 open since Jun 2025, #239 since Jul 2025). Dependabot PRs stale. This suggests the open-source repos are primarily a distribution channel, not a community effort.

2. **Star counts are low for a $7.2B company.** Total ~352 stars across all repos. For comparison, similar-stage companies like Pinecone (~4K stars on main repo) or LangChain (~100K+ stars) have orders of magnitude more. This reflects that Glean's value is in the proprietary platform, not the open-source tooling.

3. **SDK auto-generation carries quality risk.** All 4 API clients are Speakeasy-generated. While efficient, auto-generated SDKs can have ergonomic issues, inconsistent error handling, and documentation gaps. The `api-client-python` has 7 open issues and the mock server in tests suggests known integration challenges.

4. **No public engineering blog or deep technical content.** Glean's blog publishes marketing-oriented content about Knowledge Graphs and RAG, but no engineering-depth posts about their actual implementation (indexing pipelines, ML architecture, scaling challenges). This is a missed opportunity for technical credibility and hiring.

5. **Single cloud concentration risk.** Primary infrastructure is GCP-dependent (GKE, Dataflow, Vertex AI, BigQuery, Cloud Tasks, Cloud SQL). The Dell on-premises option and AWS Bedrock integration mitigate this partially, but a GCP outage would be critical. The `glean-proxy` (LittleProxy/Netty) suggests they have built custom networking infrastructure — possibly to maintain egress control across cloud boundaries.

6. **Agent toolkit release cadence is slow.** v0.3.0 released Jul 2025, no new release in 7 months despite active development. The agent framework landscape moves fast (OpenAI Agents SDK is at 0.0.x) — falling behind on adapter updates could lose developer mindshare.

7. **Missing SECURITY.md.** No public security disclosure policy found across any repo. For a company handling enterprise data with SOC 2 / ISO 27001 certification, the absence of a public vulnerability reporting process is a gap.

---

## Key Findings

1. **Glean's public repos are the tip of the iceberg.** The 26 public repos are developer integration points (API clients, MCP servers, agent adapters). The core value — Knowledge Graph, RAG pipeline, crawler infrastructure, ML models, permission engine — is entirely private. This is strategically sound (the moat is the platform, not the SDK) but limits independent technical assessment.

2. **MCP is Glean's strategic bet for developer adoption.** With 6 MCP-related repos, a GA-status remote server on the MCP Registry, and a novel testing framework, Glean is positioning as the canonical enterprise data source for the MCP ecosystem. The `remote-mcp-server` (158 stars) is their most-starred repo — developers care about this integration path.

3. **The API spec pipeline reveals production engineering maturity.** The `open-api` repo's 8-workflow CI chain (spec transform → code sample generation → client SDK trigger → developer site redeploy → diff reporting) is a sophisticated multi-repo automation system. When Glean ships an API change, it propagates automatically to 4 SDK languages, the developer portal, and documentation. This is enterprise-grade developer tooling infrastructure.

4. **Google DNA is evident in the tech choices.** GKE + Cloud Dataflow + Vertex AI + BigQuery + Bazel. The founding team's Google heritage (Arvind Jain: Distinguished Engineer, Tony Gentilcore: Chrome Speed Team) manifests in infrastructure choices optimized for large-scale data processing and search. This is a competitive advantage — they are building on the same patterns that scaled Google Search.

5. **The "context, not models" architectural bet is the key strategic differentiator.** Glean is not building LLMs. They are building the Enterprise Graph — a comprehensive model of organizational knowledge with real-time permissions, personal context, and activity signals. This allows them to be model-agnostic (swap Claude/Gemini/GPT as needed) while customers remain locked into Glean's context layer. If this bet is correct, Glean becomes the "data layer" that persists regardless of which LLM wins.

---

## Appendix: API Surface Summary (from OpenAPI Specs)

### Client API Endpoints (Partial)
- `POST /activity` — Report document activity
- `POST /feedback` — Report client UI events
- `POST /search` — Enterprise search
- `POST /chat` — AI assistant chat
- `GET /documents` — Document retrieval
- `GET /entities` — Entity lookup
- `GET /people` — People search
- `POST /summarize` — Document summarization
- `GET /calendar` — Calendar search
- `POST /tools` — Tool execution

### Indexing API Endpoints (Partial)
- `POST /indexdocument` — Index a document
- `POST /bulkindexdocuments` — Bulk index
- `POST /deletedocument` — Delete a document
- `POST /indexemployee` — Index people data
- `POST /indexgroup` — Index permission groups
- `POST /indexmembership` — Index group membership
- `POST /datasource` — Configure datasource

### Admin API Endpoints (Partial)
- `GET /governance/data/policies/{id}` — Get governance policy
- `PUT /governance/data/policies` — Update governance policy
- Supports both bearer token and cookie authentication

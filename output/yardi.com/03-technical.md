# Technical Analysis: Yardi Systems

**Phase:** P3 Technical
**Date:** 2026-07-08
**Method note:** `gh` CLI unavailable in this container; GitHub data gathered via GitHub MCP search tools + WebFetch of github.com/raw.githubusercontent.com (per-file MCP access was repo-restricted in this session). yardi.com itself remains 403-blocked (Cloudflare), so first-party claims come via search snippets. Raw repo data: `raw/github-repos.json` (+ `raw/github-org-yardisystems.json`).

**Tagging convention (per P3 prompt):** CODE-OBSERVED = seen in Yardi's own public repos (FIRST-PARTY, trust 0.2 — internal-consistency evidence only). CLAIMED = asserted by Yardi with no repo artifact. Third-party code/repos/postings are tagged INDEPENDENT (trust 0.8).

---

## GitHub Presence

| Metric | Value |
|--------|-------|
| GitHub Org | `YardiSystems` — **entire org archived by an administrator ~Sep 15, 2025** |
| Total Repos | 13 — **all 13 are forks; zero original repositories, ever** |
| Total Stars | 2 (both on the `llm-retrieval-plugin` fork) |
| Primary Languages | JavaScript (7), TypeScript (2), plus Go, Java, Python, C# forks |
| Active Contributors | Not measurable — no original code; no external contributions to Yardi-owned code exist |

The company has never practiced open source. The org was a **consumption mirror**: pinned forks of third-party libraries (presumably vendored into products) plus a few tooling forks. Its September 2025 archiving removed even that minimal public surface.

## Repository Inventory (all archived, all forks)

| Repo | Fork of | Language | Last Push | License | Read |
|------|---------|----------|-----------|---------|------|
| FlowiseArchive | FlowiseAI/Flowise (LLM flow builder) | TypeScript | **2025-09-13** (2 days before archive) | Apache-2.0 | AI experimentation |
| bolt.diy | stackblitz-labs/bolt.diy (LLM app builder) | TypeScript | **2025-09-11** | MIT | AI experimentation |
| websocketd | joewalnes/websocketd | Go | 2025-04-28 | BSD-2 | infra tooling |
| angularjs-xlsx-export | (excel export util) | JS | 2025-01-15 | none | front-end vendoring |
| TESTING-jmeter | apache/jmeter | Java | 2025-01-15 | Apache-2.0 | load-testing practice |
| microsoft-teams-apps-callrecord-insights | Microsoft template | C# | 2024-05-13 | MIT | internal M365 tooling |
| llm-retrieval-plugin | OpenAI retrieval plugin | Python | 2023-11-15 | MIT | AI experimentation (2023) |
| quill | quilljs/quill (WYSIWYG) | JS | 2023-07-20 | BSD-3 | front-end vendoring |
| FileSaver.js | eligrey/FileSaver.js | JS | 2023-05-19 | — | front-end vendoring |
| pdf.js-viewer | pdf.js embed build | JS | 2020-09-04 | Apache-2.0 | front-end vendoring |
| ment.io | Angular mentions lib | JS | 2018-12-17 | MIT | front-end vendoring |
| rrule | jakubroztocil/rrule | JS | 2018-04-17 | — | front-end vendoring |
| angular-mailcheck | Angular wrapper | JS | 2017-03-14 | none | front-end vendoring |

**What the fork inventory reveals (CODE-OBSERVED, first-party — internal-consistency value only):**
- The front-end fork cluster (quill, FileSaver.js, rrule, ment.io, angular-mailcheck, angularjs-xlsx-export, pdf.js-viewer) is a **jQuery/AngularJS-era toolkit** — consistent with independent job postings (jQuery/AngularJS) and user complaints about a dated UI. AngularJS reached end-of-life Dec 2021; several of these forks were still being touched in 2023–2025.
- The JMeter fork implies a load-testing practice exists (weak signal).
- Three AI-tooling forks (llm-retrieval-plugin 2023; Flowise and bolt.diy pushed **days before the org was archived** in Sep 2025) show sustained internal LLM experimentation. The rename to "FlowiseArchive" plus fresh pushes immediately before archiving suggests the org was **deliberately tidied and moved private** (likely internal/enterprise hosting), not that engineering stopped. *Inference, medium confidence.*

## Third-Party Ecosystem (the real INDEPENDENT technical signal)

Yardi's public technical footprint exists almost entirely in *other people's* repos — a shadow ecosystem of workarounds:

| Signal | Evidence | Trust |
|---|---|---|
| API is SOAP/WSDL, XML envelopes, HTTP Basic Auth, per-interface WSDL URL + credentials | `yhavin/yardi-sdk` (Python, 21★, active Jun 2026; wraps 7 interfaces: Billing & Payments, Vendor Invoicing, Service Requests, ILS/Guest Card, Revenue Management, Lease Renewals, Common Data, via `zeep`); `api-evangelist/yardi` OpenAPI/Postman docs (2026) | INDEPENDENT, 2+ sources — **VERIFIED** |
| No public REST API, no official SDK, no self-serve developer portal, no official MCP server | `protectnil/epic-ai-chariot` code audit note (Mar 2026): "Yardi does not publish a public REST API… access requires Yardi Interface Partner enrollment"; Truto integration-vendor analysis; absence confirmed by existence of community SDKs | INDEPENDENT, convergent — **VERIFIED** (as absence) |
| Voyager served from client-specific tenant URLs at `{client}.yardiasp13.com/...` — Yardi's own hosted ASP/cloud, not a hyperscaler-fronted multi-tenant SaaS | Third-party integration code (epic-ai-chariot); consistent with partner docs pattern "obtain URL from Voyager Administration > About" | INDEPENDENT — high confidence |
| API design frictions: endpoint name clashes across interfaces; WSDL drift; XML namespace pain; per-tenant field mapping; integrations take ~6 months | yardi-sdk README (author worked around name clashes with submodules); Truto blog (note: Truto sells integration middleware — commercially motivated, treat as ADVERSARIAL-adjacent) | INDEPENDENT/mixed — PLAUSIBLE-to-VERIFIED |
| Partner gating: 2+ years in business, 3+ active Voyager clients required; reportedly **$25,000/year per interface** | Eligibility bar: Yardi's own partner pages (FIRST-PARTY) + P1 partner docs; the $25k/yr figure: one independent source (`mariourquia/cre-skills-plugin`) — **PLAUSIBLE only, single source, verify in P4** | mixed |
| API friction pushes integrators to screen-scraping | `Browser-Automation-Hub/yardi-voyager-browser-automation` (2026, Playwright/Puppeteer): automates rent rolls, work orders, invoices "without relying on an official API"; plus a copycat repo | INDEPENDENT — telling ecosystem symptom |
| "450+ interface partners" | Yardi partner directory | CLAIMED (FIRST-PARTY) — plausible but unverified count |
| Older community clients existed a decade ago | `curiosity26/YardiClient` (PHP, 2015), `cal-am/calam-voyager` (Python, 2021), `jonschr/rent-fetch` (WordPress) | INDEPENDENT — long-standing pattern |

**Anomaly for P4:** `Kooboo/Kooboo` (open-source .NET CMS) carries source headers "Copyright (c) 2018 **Yardi Technology Limited**. Http://www.kooboo.com". Whether this entity relates to Yardi Systems, Inc. is unconfirmed — flag, don't conclude.

## Architecture Assessment

**All architecture statements below are INFERENCE from independent artifacts unless tagged otherwise.**

- **Voyager (core, enterprise):** classic ASP.NET/C#/SQL Server **monolith** delivered in a hosted-ASP model — per-client instances at `{client}.yardiasp13.com` (INDEPENDENT), matching Yardi's own tiering of "SaaS (shared app, dedicated database) / SaaS Select (dedicated app) / Private Cloud (dedicated VMs + VPN)" (CLAIMED). This is single-tenant-per-database architecture, not modern pooled multi-tenancy. ~40 years of accreted code plus 19–24 acquisitions implies significant integration sprawl (inference, medium confidence).
- **Hosting:** Yardi runs its **own data-center network** — currently "15 data centers worldwide" (CLAIMED); an earlier press release cited 10 DCs, 2,000+ physical servers, 2,200 TB (CLAIMED, dated); a new Sydney DC announcement corroborates ongoing own-DC expansion (CLAIMED). Corporate DNS is on AWS Route 53 and the website fronts through Cloudflare (INDEPENDENT, from P1 DNS) — edge is modern, core is self-hosted. No evidence Voyager production runs on a hyperscaler.
- **Modern pockets:** a 2026 DevOps posting (San Francisco office, via job aggregators) asks for **Kubernetes/EKS, Terraform, GitHub Actions, AWS, SLOs** (INDEPENDENT — attribution to which product line is uncertain; possibly an acquired or newer unit). A Senior System Reliability Engineer role in Santa Barbara also open. So cloud-native practice exists somewhere inside, alongside the legacy estate.
- **Front end:** AngularJS/jQuery-era (CODE-OBSERVED fork cluster + INDEPENDENT job postings). No evidence of a modern framework migration in public artifacts.
- **API design:** SOAP/WSDL exclusively for the official surface; no GraphQL/gRPC/REST public layer (INDEPENDENT, convergent). Breeze (the newer SMB SaaS) has **no open API at all** (INDEPENDENT, from P1 reviews + integration vendors).
- **Data layer:** Microsoft SQL Server, dedicated DB per client on the flagship (INDEPENDENT job postings + hosting-tier descriptions).
- **AI/ML:** genuinely hired — "SDE II, Machine Learning" (Santa Barbara, LinkedIn) describes **PyTorch, spaCy, Pandas models in production** (INDEPENDENT). Product-side, "Yardi Virtuoso" AI platform with "Connectors" bridging Yardi data to LLMs "starting with Anthropic's Claude" and "78% of support queries resolved without escalation" — **CLAIMED (FIRST-PARTY marketing, unverified)**. The org's Flowise/bolt.diy/llm-retrieval forks (CODE-OBSERVED) are internally consistent with real AI work predating the marketing.

## Code Quality Signals

**Essentially unobservable.** Zero original public code means no visible CI/CD, tests, security policy, changelogs, or review culture. Weak proxies only: the JMeter fork (load testing exists), the Teams call-record-insights fork (internal observability tooling), and the fact that a company shipping to thousands of enterprise clients for decades necessarily has *some* functioning release discipline (inference, not evidence). No third-party security audit of Yardi code is public. SOC/ISO attestations were not verified this phase — P4 should check certifications independently.

## Dependency Analysis

Only inferable from the fork set (CODE-OBSERVED): front-end dependencies were pinned as forks rather than consumed via package managers — a 2010s vendoring practice implying conservative, manually-managed upgrades. Several vendored libraries sit at or past EOL (AngularJS ecosystem). No manifests of Yardi's own are public; server-side dependency posture (NuGet, .NET version currency) is invisible.

## Open Source Health

**None — by design.** No maintained OSS, no external contributors, no issues/PR responsiveness to measure, no versioning discipline visible. The archived org confirms a fully closed posture. Meanwhile a community ecosystem (yardi-sdk, browser-automation tools, PHP/Python clients, third-party OpenAPI docs) has grown **despite** Yardi, to route around its gated SOAP surface — healthy demand, unhealthy official supply. For an enterprise incumbent this is common, but competitors (e.g. RealPage, AppFolio — check in P2) should be benchmarked on developer experience, where Yardi is weakest.

## Technical Strengths

- Operates its own global data-center network at real scale (15 DCs claimed; own-DC model independently corroborated by `yardiasp13.com` tenancy URLs) — infrastructure independence, no hyperscaler margin stack.
- 40+ years of platform continuity; the SOAP interfaces, however dated, are stable enough that third parties build multi-year businesses on them.
- Genuine ML engineering hiring (PyTorch/spaCy in production — INDEPENDENT), with AI experimentation visible in public artifacts since 2023, i.e. the AI story is not purely marketing.
- Modern edge/security posture (Cloudflare, Proofpoint, Route 53) and pockets of cloud-native practice (EKS/Terraform/GitHub Actions posting).
- Load-testing practice signal (JMeter fork) consistent with operating high-load enterprise SaaS.

## Technical Concerns

- **Closed, legacy integration surface as strategy:** SOAP/XML + partner gating (+ reported $25k/yr/interface) is a moat but also a liability — integrators now ship *browser automation* to bypass it, and the AI-agent era punishes platforms without clean APIs. Breeze having no API at all narrows the SMB ecosystem.
- **Front-end/UI debt:** AngularJS/jQuery-era stack (EOL frameworks) matches independent user complaints ("dated UI," "slow reports"). No public evidence of a framework migration.
- **Own-DC, per-client-instance architecture:** capital-intensive, slower elasticity than pooled multi-tenant cloud; modernization of a 40-year monolith plus ~20 acquisitions is a large latent engineering cost (inference).
- **Zero code transparency:** nothing about internal quality, security practice, or .NET modernization ("\.NET Core migration" is asserted in some job posts but not confirmed for the Voyager core) can be assessed from outside; due diligence would require data-room access.
- **Org archiving (Sep 2025):** closing even the consumption mirror further reduces external auditability; timing (days after fresh AI-fork pushes) suggests policy-driven withdrawal from public GitHub.

## Key Findings

1. **Yardi has never done open source.** The 13-repo GitHub org was 100% forks (0 original code, 2 stars total) and the entire org was archived ~Sep 15, 2025 — after AI-tooling forks (Flowise, bolt.diy) were pushed just days earlier, indicating a move to private hosting rather than an engineering halt.
2. **The official API surface is 2000s-era SOAP/WSDL, partner-gated, with no public REST/SDK/portal** — verified by 2+ independent sources (community Python SDK, third-party OpenAPI docs, integration-vendor analyses). Independent integrators resort to Playwright browser automation to get data out; a single source pegs partner access at $25k/yr per interface (PLAUSIBLE, verify in P4).
3. **Voyager runs as per-client instances in Yardi's own ~15 data centers** (`{client}.yardiasp13.com` observed independently) — an ASP-era hosted-monolith architecture with dedicated databases, not pooled cloud multi-tenancy. Modern cloud-native practice (EKS/Terraform) appears only in pockets.
4. **Real ML capability exists** (production PyTorch/spaCy hiring — INDEPENDENT), lending internal consistency to the first-party "Virtuoso" AI platform claims, which remain otherwise unverified marketing (including the Claude connector and "78% deflection" figures).
5. **Almost everything is invisible.** With ~thousands of engineers and zero public code, this phase can characterize the perimeter (APIs, hosting, hiring) but not code quality, security practice, or true modernization progress — the largest single evidence gap in the dossier so far.

## Gaps / Can't-See List

- All product source code, CI/CD, tests, internal repo count (could be 3 or 3,000 private repos).
- Actual .NET version currency of the Voyager core; status of any .NET Core/.NET 8 migration (CLAIMED in scattered job posts, unconfirmed).
- Voyager production topology beyond tenancy URLs; DR posture beyond a claimed Phoenix BC/DR center.
- SOC 2 / ISO 27001 attestations (not checked this phase — P4).
- The $25k/yr interface fee (single source) and the "450+ partners" count (first-party).
- Attribution of the SF EKS/Terraform DevOps posting to a specific Yardi product line.
- Whether "Yardi Technology Limited" (Kooboo CMS copyright holder) is related to Yardi Systems, Inc.

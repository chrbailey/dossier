# Phase 3: Technical Analysis — Salesforce, Inc.

**Target:** salesforce.com | NYSE: CRM
**Date:** 2026-03-05
**Data Sources:** GitHub API (gh CLI), Salesforce Engineering Blog, public architecture documentation

---

## 1. GitHub Presence Summary

| Metric | Value |
|---|---|
| **Primary GitHub org** | `salesforce` — 404 public repos, 3,278 followers |
| **AI Research org** | `SalesforceAIResearch` — 83 public repos, 426 followers (est. 2023) |
| **Developer community org** | `developerforce` — 31 repos (largely archived) |
| **Foundation/Nonprofit org** | `SalesforceFoundation` — 37 repos (Apex-heavy, NPSP/EDA) |
| **Total public repos (across 4 orgs)** | ~555 |
| **Top repo by stars** | LAVIS (11,177 stars) — vision-language AI |
| **Most actively maintained** | lwc (pushed 2026-03-05), cloudsplaining (pushed 2026-03-04) |
| **Repo health (top 100)** | 56 active, 44 archived (44% archive rate) |
| **Open source portal** | https://opensource.salesforce.com |

**Note:** The vast majority of Salesforce's production code — the core CRM platform, Apex runtime, Data Cloud (Data 360), Agentforce, MuleSoft, Tableau, Slack — is proprietary and invisible on GitHub. The public repos represent research output, developer tooling, and security utilities, not the core product.

---

## 2. Repository Inventory — Top Repos by Stars

### salesforce org (top 25)

| Repo | Stars | Forks | Language | License | Status | Contributors | Last Push | Category |
|---|---|---|---|---|---|---|---|---|
| LAVIS | 11,177 | 1,096 | Jupyter/Python | BSD-3 | Active | 22 | 2024-11 | AI Research |
| BLIP | 5,690 | 761 | Jupyter/Python | — | Archived | — | — | AI Research |
| CodeGen | 5,171 | 418 | Python | Apache-2.0 | Active | 11 | 2025-10 | AI Research |
| Merlion | 4,477 | 354 | Python | BSD-3 | Active | 17 | 2024-06 | AI/ML |
| akita | 3,675 | 344 | TypeScript | — | Archived | — | — | State Mgmt |
| CodeT5 | 3,098 | 490 | Python | BSD-3 | Active | 2 | 2024-01 | AI Research |
| ja3 | 3,074 | 310 | Python | — | Archived | — | — | Security |
| decaNLP | 2,339 | 465 | Python | — | Archived | — | — | AI Research |
| TransmogrifAI | 2,272 | 401 | Scala | BSD-3 | Active* | — | 2023-09 | AutoML |
| cloudsplaining | 2,187 | 214 | JavaScript | BSD-3 | Active | 29 | 2026-03 | Cloud Security |
| policy_sentry | 2,137 | 151 | Python | MIT | Active | 30 | 2026-03 | Cloud Security |
| awd-lstm-lm | 1,990 | 486 | Python | — | Archived | — | — | AI Research |
| ctrl | 1,884 | 202 | Python | — | Archived | — | — | AI Research |
| WikiSQL | 1,800 | 330 | HTML | — | Archived | — | — | AI Dataset |
| ALBEF | 1,756 | 222 | Python | — | Archived | — | — | AI Research |
| lwc | 1,755 | 439 | JavaScript | Custom | Active | 30 | 2026-03 | Platform |
| sloop | 1,563 | 135 | Go | BSD-3 | Active | — | 2026-02 | Infrastructure |
| CodeTF | 1,481 | 96 | Python | — | Archived | — | — | AI Research |
| jarm | 1,285 | 150 | Python | — | Active | — | 2026-03 | Security |
| tough-cookie | 1,060 | 295 | TypeScript | BSD-3 | Active | — | 2026-03 | Web/Node.js |
| design-system-react | 970 | 435 | JavaScript | BSD-3 | Active | — | 2026-01 | UI/Design |
| OmniXAI | 962 | 106 | Jupyter/Python | — | Active | — | 2026-02 | Explainable AI |
| reactive-grpc | 842 | 122 | Java | BSD-3 | Active | — | 2025-07 | gRPC |
| logai | 782 | 120 | Python | — | Active | — | 2026-03 | AIOps |
| xgen | 725 | 38 | Python | Apache-2.0 | Active | — | 2025-01 | LLMs |

*TransmogrifAI technically not archived but last push was Sep 2023 — effectively dormant.

### SalesforceAIResearch org (top 10)

| Repo | Stars | Forks | Language | License | Last Push | Category |
|---|---|---|---|---|---|---|
| uni2ts | 1,431 | 192 | Jupyter/Python | Apache-2.0 | 2026-01 | Time Series |
| enterprise-deep-research | 1,129 | 177 | Python | Apache-2.0 | 2026-01 | Deep Research |
| promptomatix | 927 | 94 | Python | — | 2026-03 | Prompt Optimization |
| DiffusionDPO | 667 | 47 | Python | — | — | Diffusion Models |
| AgentLite | 640 | 82 | Jupyter/Python | Apache-2.0 | 2025-11 | Agent Framework |
| xLAM | 601 | 51 | Python | Apache-2.0 | 2025-08 | Action Models |
| MCP-Universe | 566 | 72 | Python | Apache-2.0 | 2026-03 | Agent Benchmarking |
| gift-eval | 197 | 67 | Jupyter/Python | — | 2026-03 | Evaluation |
| MCPEval | 145 | 18 | Python | Apache-2.0 | 2026-02 | MCP Evaluation |
| CRMArena | 133 | 26 | Python | — | 2026-02 | CRM Benchmarks |

---

## 3. Architecture Assessment

### 3.1 Architecture Style: Hybrid Multi-Tenant + Microservices

**Observable signals (public sources):**

- **Multi-tenant monolith core.** The original Salesforce CRM platform is a metadata-driven multi-tenant architecture built on Java/Apex running atop Oracle (historically) and custom database layers. This is the "classic" architecture that serves the core CRM product. Not visible on GitHub.
- **Microservices migration (Hyperforce).** Since ~2021, Salesforce has been migrating to Hyperforce — a containerized, microservices-based architecture running on public cloud providers (AWS, GCP, Azure). As of 2025, 78% of enterprise customers run multi-cloud deployments across 38+ regions.
- **Data 360 (formerly Data Cloud)** uses a fully microservices architecture, containerized and orchestrated via Kubernetes, built on Apache Iceberg and Parquet with a petabyte-scale Lakehouse.
- **Kubernetes at massive scale.** Salesforce operates 1,000+ EKS clusters (AWS). They migrated from Cluster Autoscaler to Karpenter across their entire fleet in mid-2025 to early 2026, developing custom tooling for the migration. They also run Kubernetes on bare metal for some workloads.
- **Acquired services maintain independent architectures.** Slack (Electron/React), Tableau (C++/Java), MuleSoft (Java/Spring), Heroku (polyglot PaaS) — each runs on separate stacks.

**Architectural principles (from Hyperforce documentation):**
1. Immutable Infrastructure
2. Multi-Availability-Zone Design
3. Zero Trust Security
4. Infrastructure-as-Code
5. Clean Slate (no legacy carryover)

**Inference confidence:** HIGH for infrastructure patterns (documented extensively). LOW for internal service decomposition (proprietary).

### 3.2 Language Diversity

| Rank | Language | Count (top 100 repos) | Primary Use |
|---|---|---|---|
| 1 | Python | 54 | AI/ML research, security tools, automation |
| 2 | JavaScript | 11 | LWC, UI components, web tooling |
| 3 | Jupyter Notebook | 10 | Research reproducibility |
| 4 | TypeScript | 7 | Web libraries (tough-cookie, akita) |
| 5 | Java | 7 | gRPC, enterprise tooling |
| 6 | Go | 2 | Infrastructure (sloop, K8s tooling) |
| 7 | Scala | 1 | AutoML (TransmogrifAI, Spark) |
| 8 | HCL | 1 | Terraform/IaC |

**SalesforceAIResearch** is nearly 100% Python (40/49 repos), reflecting the AI/ML ecosystem's language preferences.

**Not visible on GitHub but known from public sources:** Apex (proprietary language for Salesforce platform), Java (core backend), C++ (Tableau), Ruby/Node.js (Heroku), and extensive use of Terraform, Splunk, HashiCorp Vault.

### 3.3 Infrastructure Signals

| Signal | Evidence |
|---|---|
| **Kubernetes** | 1,000+ EKS clusters; `sloop` (K8s visualization tool, 1.5K stars); Karpenter migration documented |
| **Multi-cloud** | AWS (primary for Hyperforce), GCP, Azure — 38+ regions |
| **IaC** | HCL repos present; Infrastructure-as-Code stated as Hyperforce principle |
| **CI/CD** | Jenkins (documented), GitHub Actions (visible in LWC, cloudsplaining, policy_sentry, Merlion) |
| **Data platform** | Apache Iceberg, Parquet, petabyte-scale Lakehouse (Data 360) |
| **Monitoring** | Splunk (acquired 2024, $28B), LogAI (open-source log analytics) |
| **Security** | Cloudsplaining, policy_sentry, JA3, JARM, HASSH — strong security tooling DNA |
| **Container registry** | Docker implied by Kubernetes scale; no public Docker Hub presence examined |

### 3.4 API Design

| API Pattern | Evidence |
|---|---|
| **REST** | Core Salesforce APIs are REST-based; Force.com REST toolkit (archived) |
| **gRPC** | `reactive-grpc` (842 stars) — reactive stubs for gRPC, indicating internal gRPC adoption |
| **GraphQL** | Not directly visible in repos but supported in Salesforce platform (GraphQL Wire Adapter for LWC) |
| **SOAP** | Legacy Salesforce APIs (still supported, declining) |
| **Streaming** | Salesforce Streaming API client in SalesforceFoundation; Bayeux protocol client |
| **MCP** | MCP-Universe and MCPEval repos in AI Research — active engagement with Model Context Protocol for agent systems |

### 3.5 Data Layer Signals

- **Relational (multi-tenant):** Custom shared-schema relational database for core CRM (historically Oracle-backed)
- **Lakehouse:** Apache Iceberg + Parquet for Data 360 — zero-copy integration with Snowflake, Databricks, AWS
- **Real-time streaming:** Event-driven architecture with streaming ingestion for Data 360
- **Search:** Platform search capabilities (not visible as OSS)
- **Vector/embeddings:** Implied by AI Research activity but no dedicated vector DB repo visible

---

## 4. Code Quality Signals

### Top 5 Repos — Quality Matrix

| Repo | CI/CD | Tests | Docs | Security Policy | Changelog | README Quality |
|---|---|---|---|---|---|---|
| **lwc** | 7 workflows (unit, webdriver, benchmark, release) | Yes (multi-package) | Yes | Not found | Via releases | Excellent — badges, examples, contributing guide |
| **cloudsplaining** | 7 workflows (test, publish, security, release-drafter) | Yes | Yes | Yes (security.yml workflow) | Release drafter | Excellent — comprehensive README |
| **policy_sentry** | 5 workflows (ci, publish, release-drafter, update) | Yes | Yes | Implied | Release drafter | Excellent — well-documented CLI |
| **Merlion** | 3 workflows (docs, tests, publish) | Yes | Yes | Not found | Via releases | Good — academic style |
| **LAVIS** | 1 workflow (docs only) | Minimal | Yes | Not found | Not found | Good — research paper focus |

**Observations:**
- **Platform/security repos** (lwc, cloudsplaining, policy_sentry) show mature engineering practices: comprehensive CI/CD, automated testing, release automation, dependency management.
- **AI research repos** (LAVIS, Merlion, CodeT5) are primarily paper companions — documentation is academic (paper links, citations), CI is minimal or absent, and community PRs accumulate without response.
- **License consistency:** BSD-3-Clause is the dominant license, with some Apache-2.0 (especially newer AI research repos).

---

## 5. Dependency Analysis

### Inferred from repository analysis:

| Domain | Key Dependencies / Frameworks |
|---|---|
| **AI/ML Research** | PyTorch (dominant), Hugging Face Transformers, JAX (jaxformer), Apache Spark (TransmogrifAI) |
| **Web Components** | LWC (proprietary framework, open-source core), React (design-system-react) |
| **Cloud Security** | AWS SDK (cloudsplaining, policy_sentry), Node.js |
| **Infrastructure** | Kubernetes, Karpenter, EKS, Terraform |
| **Agent Systems** | LangChain (enterprise-deep-research), FastAPI, E2B, Tailwind CSS, React |
| **Data Platform** | Apache Iceberg, Apache Parquet, Apache Spark |
| **gRPC** | reactive-grpc (Java), Protocol Buffers |
| **Node.js** | tough-cookie (widely depended upon — 295 forks) |

**Notable:** `tough-cookie` is a foundational npm package with ~1,060 stars and 295 forks — it is widely used across the Node.js ecosystem as an RFC6265 cookie implementation. Salesforce maintaining this is a signal of their contribution to foundational web infrastructure.

---

## 6. Open Source Health

### 6.1 Maintenance Activity

| Category | Signal | Assessment |
|---|---|---|
| **Actively maintained** | lwc, cloudsplaining, policy_sentry, tough-cookie | Strong — regular commits, dependency updates, releases |
| **Research-then-archive** | BLIP, ja3, decaNLP, ctrl, WikiSQL, ALBEF, CodeTF | Common pattern — publish paper, open-source code, archive when superseded |
| **Dormant but not archived** | TransmogrifAI (last push 2023-09), Merlion (last push 2024-06), CodeT5 (last push 2024-01) | Concerning — stars suggest community interest but no maintenance |
| **New and active (AI Research org)** | enterprise-deep-research, promptomatix, MCP-Universe | Growing fast — recent repos with high engagement |

### 6.2 Community Engagement

- **Issue responsiveness:** Mixed. Platform repos (lwc) show active triage. Research repos accumulate issues — LAVIS has 499 open issues, CodeT5 has 86.
- **External contributors:** Highest in security tools (cloudsplaining: 29, policy_sentry: 30) and lwc (30). Research repos tend toward internal-only contribution.
- **Hacktoberfest participation:** cloudsplaining and policy_sentry carry `hacktoberfest` topic — indicates intentional community building.

### 6.3 Documentation Quality

- **Platform repos:** Professional documentation with contributing guides, code of conduct, comprehensive READMEs.
- **Research repos:** Paper-oriented documentation — good for reproducibility, poor for adoption. Typically: paper link, model checkpoints, inference instructions.
- **Design system:** `design-system-react` has 970 stars with extensive component documentation.

### 6.4 Versioning Discipline

- **lwc:** Semantic versioning, automated canary releases, structured release process.
- **Security tools:** Release drafter automation, version bump workflows.
- **Research repos:** Typically unversioned or tagged by paper revision.

---

## 7. AI Research Capability — Deep Dive

Salesforce has one of the most prolific AI research open-source presences of any enterprise software company. The research spans:

| Research Area | Key Repos | Stars | Status |
|---|---|---|---|
| **Vision-Language Models** | LAVIS, BLIP, ALBEF | 18,623 | Foundational — BLIP/BLIP-2 widely adopted |
| **Code Generation** | CodeGen, CodeT5, CodeTF, CodeRL | 10,312 | Competitive with Codex (at time of release) |
| **Time Series** | Merlion, uni2ts, ETSformer, CoST, DeepTime | 6,816 | Comprehensive — anomaly detection to forecasting |
| **LLMs** | xgen, ctrl, decaNLP | 4,948 | Own LLM family (xgen with 8K context) |
| **Agent Systems** | AgentLite, xLAM, MCP-Universe, MCPEval | 1,952 | Fast-growing — MCP integration notable |
| **Protein/Bio** | ProGen, provis | 997 | Niche but notable |
| **Security/Fingerprinting** | ja3, jarm, hassh | 4,905 | Industry-standard fingerprinting tools |
| **Prompt Engineering** | promptomatix | 927 | Automatic prompt optimization |
| **Deep Research** | enterprise-deep-research, LiveResearchBench | 1,241 | Multi-agent research systems |

**Total combined stars across AI/ML repos: ~50,000+** — this is exceptional for a non-AI-native company.

---

## 8. Technical Strengths

1. **World-class AI research output.** Salesforce AI Research publishes prolifically, with repos like LAVIS (11K stars) and BLIP achieving widespread adoption. The transition to the SalesforceAIResearch org (2023) shows increasing investment.

2. **Cloud security tooling leadership.** Cloudsplaining, policy_sentry, ja3, jarm, and hassh are industry-standard security tools — ja3 fingerprinting in particular has become a de facto standard for SSL client identification.

3. **Massive infrastructure scale.** Operating 1,000+ Kubernetes clusters, migrating to Karpenter, running multi-cloud across AWS/GCP/Azure with 38+ regions demonstrates operational excellence at scale.

4. **Hyperforce architecture modernization.** The clean-slate migration from proprietary data centers to public cloud with immutable infrastructure, zero trust, and IaC principles represents a major, well-executed architectural transition.

5. **Agent/MCP investment.** The SalesforceAIResearch org's MCP-Universe, MCPEval, xLAM, and AgentLite repos — plus the Agentforce product platform — position Salesforce well in the emerging agentic AI paradigm.

6. **Data platform sophistication.** Data 360 built on Apache Iceberg/Parquet with zero-copy integration to Snowflake/Databricks shows modern data architecture thinking.

---

## 9. Technical Concerns

1. **Research-production gap.** The most-starred repos are research paper companions, not production tools. LAVIS has 499 open issues and was last pushed in Nov 2024. Many high-star repos are archived. The open-source presence does not represent the production platform.

2. **High archive rate.** 44% of top 100 repos are archived. While archiving is better than neglect, it suggests a "publish and move on" culture for research repos rather than sustained community building.

3. **Dormant high-value repos.** TransmogrifAI (2.2K stars, last push 2023), Merlion (4.5K stars, last push mid-2024), CodeT5 (3.1K stars, last push 2024) — significant community interest but no active maintenance. This creates dependency risk for downstream users.

4. **Core platform opacity.** The production CRM platform, Apex runtime, Data Cloud internals, Einstein AI infrastructure, and Agentforce runtime are entirely proprietary. Technical due diligence of the actual revenue-generating code is impossible from public sources alone.

5. **Org fragmentation.** Four GitHub orgs (salesforce, SalesforceAIResearch, developerforce, SalesforceFoundation) with no clear cross-referencing. The SalesforceAIResearch org was created in 2023 but older AI repos remain in the salesforce org — creates discoverability issues.

6. **Acquisition integration complexity.** Slack, Tableau, MuleSoft, Heroku, and Splunk each brought different tech stacks. Technical debt from integrating these acquisitions into a coherent platform is a known challenge (not visible from GitHub).

---

## 10. Key Findings

1. **Salesforce's open-source presence is overwhelmingly an AI research portfolio, not a reflection of their production platform.** Of the top 25 repos by stars, ~18 are AI/ML research paper companions. The core CRM platform is entirely proprietary. Assess the research output for talent signal and innovation capacity, not as evidence of product architecture.

2. **The SalesforceAIResearch org (est. 2023) shows accelerating investment in agentic AI.** MCP-Universe, xLAM, AgentLite, and enterprise-deep-research indicate Salesforce is building foundational agentic infrastructure — directly supporting the Agentforce product. This research-to-product pipeline (research org -> Agentforce platform) is a competitive advantage.

3. **Cloud security tools are Salesforce's most community-engaged open-source contribution.** Cloudsplaining (29 contributors), policy_sentry (30 contributors), and the JA3/JARM/HASSH fingerprinting tools have genuine community adoption and active maintenance. This is a stronger signal of engineering culture than the research repos.

4. **Infrastructure operates at impressive scale but is invisible.** 1,000+ Kubernetes clusters, Karpenter migration, multi-cloud Hyperforce across 38+ regions — these represent serious operational capability. The sloop K8s visualization tool (1.5K stars) is the only public repo that surfaces this.

5. **The platform is in active architectural transition.** Hyperforce (multi-tenant on public cloud), Data 360 (Iceberg-based lakehouse), Agentforce (agentic AI platform) — Salesforce is simultaneously modernizing infrastructure, data, and AI layers. Execution risk is real but the direction is architecturally sound.

---

*Raw data: `output/salesforce.com/raw/github-repos.json`*
*Phase 3 complete. Data collected 2026-03-05 via GitHub API.*

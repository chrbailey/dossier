# Okta, Inc. -- Technical Analysis (Phase 3)

**Target:** okta.com
**Date:** 2026-02-18
**Data Sources:** GitHub API (gh CLI), web search, public documentation

---

## 1. GitHub Presence Summary

Okta operates **4 GitHub organizations** (plus Auth0's inherited org), with a combined **943+ public repositories** and significant open-source influence in the identity/JWT ecosystem.

| Organization | Public Repos | Followers | Created | Purpose |
|---|---|---|---|---|
| [okta](https://github.com/okta) | 87 | 622 | 2010-08 | Core SDKs, sign-in widget, Terraform provider, MCP server |
| [auth0](https://github.com/auth0) | 330 | 1,915 | 2012-11 | JWT libraries, Auth0 SDKs, framework integrations (acquired 2021) |
| [oktadev](https://github.com/oktadev) | 500 | 510 | 2015-07 | Developer advocacy, example apps, blog code samples |
| [okta-samples](https://github.com/okta-samples) | 26 | 35 | 2020-08 | Official quickstart/sample applications |
| **Total** | **943** | **3,082** | | |

### Aggregate Metrics

| Metric | Value |
|---|---|
| Total public repositories | 943 |
| Total GitHub followers (combined orgs) | 3,082 |
| Repos with 1,000+ stars | 7 (all Auth0 JWT/SDK repos) |
| Repos with 100+ stars | 30+ |
| Highest-starred repo | auth0/node-jsonwebtoken (18,145 stars) |
| npm weekly downloads (jsonwebtoken alone) | ~26 million |
| Languages represented | 15+ (TS, JS, Java, Go, Python, C#, Swift, Kotlin, PHP, Ruby, Objective-C, PowerShell, Groovy, Vue, Lua) |

---

## 2. Repository Inventory -- Top Repos by Stars

### Auth0 Organization (Acquired 2021) -- Infrastructure-Level OSS

These repos are foundational internet infrastructure, used by millions of applications:

| Repository | Stars | Forks | Open Issues | Language | License | Last Updated |
|---|---|---|---|---|---|---|
| [node-jsonwebtoken](https://github.com/auth0/node-jsonwebtoken) | 18,145 | 1,264 | 185 | JavaScript | MIT | 2026-02-18 |
| [java-jwt](https://github.com/auth0/java-jwt) | 6,204 | 943 | 26 | Java | MIT | 2026-02-18 |
| [express-jwt](https://github.com/auth0/express-jwt) | 4,512 | 440 | 66 | TypeScript | MIT | 2026-02-13 |
| [jwt-decode](https://github.com/auth0/jwt-decode) | 3,387 | 341 | 14 | TypeScript | MIT | 2026-02-18 |
| [angular2-jwt](https://github.com/auth0/angular2-jwt) | 2,638 | 477 | 8 | TypeScript | MIT | 2026-02-16 |
| [nextjs-auth0](https://github.com/auth0/nextjs-auth0) | 2,282 | 452 | 32 | TypeScript | MIT | 2026-02-18 |
| [go-jwt-middleware](https://github.com/auth0/go-jwt-middleware) | 1,184 | 209 | 11 | Go | MIT | 2026-02-17 |
| [lock](https://github.com/auth0/lock) | 1,140 | 558 | -- | JavaScript | MIT | 2026-02-18 |
| [auth0.js](https://github.com/auth0/auth0.js) | 1,041 | 497 | -- | JavaScript | MIT | 2026-02-13 |
| [auth0-react](https://github.com/auth0/auth0-react) | 984 | 291 | 6 | TypeScript | MIT | 2026-02-17 |
| [auth0-spa-js](https://github.com/auth0/auth0-spa-js) | 982 | 405 | 6 | TypeScript | MIT | 2026-02-18 |
| [node-auth0](https://github.com/auth0/node-auth0) | 677 | 317 | -- | TypeScript | MIT | 2026-02-11 |
| [auth0-python](https://github.com/auth0/auth0-python) | 574 | 185 | 9 | Python | MIT | 2026-02-13 |
| [auth0-cli](https://github.com/auth0/auth0-cli) | 306 | 68 | 9 | Go | MIT | 2026-02-17 |
| [terraform-provider-auth0](https://github.com/auth0/terraform-provider-auth0) | 206 | 112 | 6 | Go | MPL-2.0 | 2026-02-17 |

### Okta Organization -- Core Product SDKs

| Repository | Stars | Forks | Open Issues | Language | License | Last Updated |
|---|---|---|---|---|---|---|
| [okta-auth-js](https://github.com/okta/okta-auth-js) | 480 | 274 | 225 | TypeScript | Proprietary | 2026-02-08 |
| [okta-signin-widget](https://github.com/okta/okta-signin-widget) | 395 | 329 | 356 | JavaScript | Apache-2.0 | 2026-02-18 |
| [okta-spring-boot](https://github.com/okta/okta-spring-boot) | 362 | 142 | 33 | Java | Proprietary | 2026-02-13 |
| [terraform-provider-okta](https://github.com/okta/terraform-provider-okta) | 323 | 245 | 258 | Go | MPL-2.0 | 2026-02-17 |
| [okta-sdk-python](https://github.com/okta/okta-sdk-python) | 260 | 162 | 56 | Python | Apache-2.0 | 2026-01-31 |
| [okta-sdk-golang](https://github.com/okta/okta-sdk-golang) | 203 | 161 | 9 | Go | Apache-2.0 | 2026-02-13 |
| [okta-sdk-dotnet](https://github.com/okta/okta-sdk-dotnet) | 176 | 105 | 5 | C# | Proprietary | 2026-02-11 |
| [okta-aws-cli](https://github.com/okta/okta-aws-cli) | 175 | 43 | -- | Go | -- | 2026-02-18 |
| [okta-developer-docs](https://github.com/okta/okta-developer-docs) | 158 | 655 | -- | SCSS | -- | 2026-02-17 |
| [okta-sdk-java](https://github.com/okta/okta-sdk-java) | 157 | 136 | -- | HTML | -- | 2026-02-17 |
| [okta-react](https://github.com/okta/okta-react) | 139 | 80 | -- | JavaScript | -- | 2026-02-05 |
| [workflows-templates](https://github.com/okta/workflows-templates) | 129 | 57 | -- | JavaScript | -- | 2026-02-11 |
| [odyssey](https://github.com/okta/odyssey) | 109 | 34 | 1 | TypeScript | Proprietary | 2026-02-17 |
| [okta-mcp-server](https://github.com/okta/okta-mcp-server) | 18 | 17 | 7 | Python | Apache-2.0 | 2026-02-18 |

### Oktadev Organization -- Developer Advocacy

| Repository | Stars | Forks | Language | Description |
|---|---|---|---|---|
| [java-microservices-examples](https://github.com/oktadev/java-microservices-examples) | 625 | 321 | Java | Spring Boot, Spring Cloud, JHipster microservices |
| [okta-aws-cli-assume-role](https://github.com/oktadev/okta-aws-cli-assume-role) | 338 | 175 | HTML | AWS CLI role assumption with Okta IdP |
| [spring-boot-microservices-example](https://github.com/oktadev/spring-boot-microservices-example) | 334 | 153 | TypeScript | Bootiful Microservices with Spring Boot |
| [okta-spring-boot-react-crud-example](https://github.com/oktadev/okta-spring-boot-react-crud-example) | 303 | 169 | Java | CRUD with React and Spring Boot 3 |
| [okta-blog](https://github.com/oktadev/okta-blog) | 45 | 69 | SCSS | Developer blog content |

---

## 3. Architecture Assessment

### 3.1 Cell-Based Architecture (HIGH confidence)

Okta's core infrastructure uses a **cell-based architecture** -- isolated, shared-nothing replicas that include edge routing, load balancing, application tier, and database services. Key characteristics:

| Aspect | Detail |
|---|---|
| **Architecture style** | Cell-based, shared-nothing isolation |
| **Primary cloud** | AWS (multi-AZ, active-active-active) |
| **Secondary cloud** | GCP (first cell deployed, multi-cloud expansion underway) |
| **Regions** | North America, Europe, Australia, Japan, Canada (Q1 2026) |
| **Scaling model** | Linear cell rollout as user base grows |
| **Disaster recovery** | Enhanced DR with <5 minute recovery target |
| **Container orchestration** | Kubernetes (1,000+ clusters managed via Argo CD GitOps) |
| **Container runtime** | Docker on AWS ECS (legacy), Kubernetes (current) |

### 3.2 Language & Framework Diversity

Okta maintains SDKs across 10+ languages, indicating a polyglot platform strategy designed for maximum developer ecosystem coverage:

| Language/Runtime | Usage Context | Key Repos |
|---|---|---|
| **TypeScript/JavaScript** | Auth JS SDK, sign-in widget, React/Angular/Vue SDKs, Auth0 JWT libs | okta-auth-js, okta-signin-widget, node-jsonwebtoken |
| **Java** | Spring Boot starter, management SDK, JWT verifier, enterprise SDKs | okta-spring-boot, okta-sdk-java, java-jwt |
| **Go** | Terraform providers, management SDK, CLI tools, middleware | terraform-provider-okta, okta-sdk-golang, okta-aws-cli |
| **Python** | Management SDK, MCP server, Auth0 SDK | okta-sdk-python, okta-mcp-server, auth0-python |
| **C# / .NET** | Management SDK, ASP.NET integration, Auth0 SDK | okta-sdk-dotnet, okta-aspnet, auth0.net |
| **Swift** | iOS/macOS mobile SDKs | okta-mobile-swift, okta-auth-swift, Auth0.swift |
| **Kotlin** | Android mobile SDKs | okta-mobile-kotlin, Auth0.Android |
| **PHP** | Auth0 SDK, Laravel integration (Okta PHP SDK archived) | auth0-PHP, laravel-auth0 |
| **Ruby** | Auth0 SDK, OmniAuth strategy | ruby-auth0, omniauth-auth0 |
| **PowerShell** | Admin CLI for Windows | okta-powershell-cli |

### 3.3 API Design & Protocol Standards

| Standard | Implementation |
|---|---|
| **OAuth 2.0** | Full authorization server, certified provider |
| **OpenID Connect (OIDC)** | Certified OIDC provider, SDKs for all major frameworks |
| **SCIM 2.0 / 1.1** | RESTful user/group provisioning (both versions supported) |
| **SAML 2.0** | IdP and SP support |
| **PKCE** | Authorization Code Grant with PKCE in all SPA SDKs |
| **DPoP (RFC 9449)** | Proof-of-possession token binding (auth0-spa-js, nextjs-auth0) |
| **MCP (Model Context Protocol)** | AI agent integration via okta-mcp-server (new, Sep 2025) |
| **REST API** | Primary management API style, JSON payloads |
| **OpenAPI** | SDKs auto-generated from OpenAPI specs (openapi-generator) |

### 3.4 Infrastructure & DevOps Signals

| Component | Evidence |
|---|---|
| **IaC** | Terraform providers for both Okta and Auth0 (well-maintained, high star count) |
| **CI/CD** | GitHub Actions, CircleCI (.circleci dirs), Travis CI (.travis.yml in older repos) |
| **GitOps** | Argo CD for Kubernetes deployments (1,000+ clusters) |
| **Security scanning** | Snyk, Semgrep, CodeQL, RL-Secure workflows in Auth0 repos |
| **Dependency management** | Dependabot (active in multiple repos), automated stale issue management |
| **Release management** | Semantic versioning, GitHub Releases, automated release workflows |
| **Container registry** | Docker support in MCP server, Docker Compose for local dev |
| **Engineering governance** | "Engineering Radar" for tech stack decisions (databases, messaging, frameworks) |

### 3.5 Data Layer Signals

| Signal | Source |
|---|---|
| **Elasticsearch** | DNS/subdomain signals from P1 discovery |
| **Redis** | DNS/subdomain signals from P1 discovery |
| **Database per cell** | Cell architecture implies isolated DB per cell |
| **WAL/transactional** | Identity workloads require strong consistency |
| **SQLite (edge)** | MCP server uses lightweight local storage patterns |

---

## 4. Code Quality Signals

### 4.1 CI/CD & Workflow Coverage

| Repository | CI System | Workflows |
|---|---|---|
| okta/terraform-provider-okta | GitHub Actions | ci.yml, release.yml, stale.yml, vcr.yml, pull_request_reviewer.yml |
| okta/okta-auth-js | Travis CI | .travis.yml (legacy) |
| okta/okta-signin-widget | Internal (Bacon) | .bacon.yml (Okta's internal CI system) |
| okta/okta-sdk-python | GitHub Actions | python-package.yml, python.yml |
| okta/okta-sdk-golang | GitHub Actions + CircleCI | release.yml, stale.yml |
| okta/okta-mcp-server | CircleCI + GitHub | .circleci dir |
| auth0/nextjs-auth0 | GitHub Actions | test.yml, codeql.yml, snyk.yml, claude-code-review.yml, playwright.yml, release.yml |
| auth0/auth0-spa-js | GitHub Actions | test.yml, codeql.yml, snyk.yml, claude-code-review.yml, browserstack.yml, release.yml |
| auth0/java-jwt | GitHub Actions | build-and-test.yml, semgrep.yml, snyk.yml, rl-secure.yml, release.yml |
| auth0/node-jsonwebtoken | GitHub Actions | test.yml, semgrep.yml |

**Notable finding:** Auth0 repos use **claude-code-review.yml** -- automated AI code review via Claude -- in nextjs-auth0 and auth0-spa-js. This is a leading-edge practice.

### 4.2 Testing Infrastructure

| Repository | Test Framework | Test Dirs | E2E |
|---|---|---|---|
| okta-auth-js | Jest | test/, jest.*.js (5 configs) | jest.integration.js |
| okta-signin-widget | Jest + TestCafe | test/ | .testcaferc.js |
| terraform-provider-okta | Go testing | test/ | VCR test recordings |
| okta-sdk-python | pytest/tox | tests/ | tox.ini |
| okta-mcp-server | pytest | tests/ | -- |
| auth0/nextjs-auth0 | Vitest + Playwright | tests/, e2e/ | playwright.config.ts |
| auth0/auth0-spa-js | Jest + Cypress + BrowserStack | __tests__/, cypress/ | cypress.config.js |
| auth0/java-jwt | JUnit (Gradle) | lib/src/test | -- |

### 4.3 Documentation & Developer Experience

| Repository | README | CONTRIBUTING | SECURITY | AGENTS.md | CHANGELOG | Migration Guides |
|---|---|---|---|---|---|---|
| okta-auth-js | Yes | Yes | Yes | No | Yes | No |
| okta-signin-widget | Yes | Yes | No | No | No | MIGRATING.md |
| terraform-provider-okta | Yes | Yes (in .github) | No | No | Yes | No |
| okta-sdk-python | Yes | Yes | Yes | No | Yes | UPGRADE_GUIDE.md |
| auth0/nextjs-auth0 | Yes | Yes | SECURITY.md | **Yes** | Yes | V1-V4 migration guides |
| auth0/auth0-spa-js | Yes | Yes | No | **Yes** | Yes | MIGRATION_GUIDE.md |
| auth0/java-jwt | Yes | No | No | No | Yes | MIGRATION_GUIDE.md |
| auth0/node-jsonwebtoken | Yes | No | No | No | Yes | No |

**Notable:** Auth0 repos include `AGENTS.md` files -- structured documentation designed for AI coding agents (Codex, Claude Code). These contain architecture maps, data flow diagrams, command references, and anti-patterns. This is a forward-looking practice that few organizations have adopted.

### 4.4 Licensing

| Pattern | Repos | Notes |
|---|---|---|
| MIT | Auth0 SDKs, JWT libraries | Standard permissive OSS |
| Apache-2.0 | Okta sign-in widget, Python SDK, Go SDK, MCP server | Standard permissive OSS |
| MPL-2.0 | Terraform providers (both Okta + Auth0) | Standard for Terraform ecosystem |
| NOASSERTION / Proprietary | okta-auth-js, okta-sdk-dotnet, odyssey | Some core Okta repos use custom/proprietary licenses |

**Concern:** Several high-visibility Okta-branded repos (okta-auth-js, okta-sdk-dotnet, odyssey) have `NOASSERTION` licenses, meaning the license terms are unclear or proprietary despite the code being public. This creates friction for enterprise adopters who need clear license compliance.

---

## 5. Dependency Analysis

### 5.1 okta-auth-js (TypeScript SDK)

**Runtime dependencies:** 14 packages including cross-fetch, js-cookie, node-cache, webcrypto-shim, tiny-emitter.

**Build tooling:** Babel, Rollup, Webpack, TypeScript 4.7, Jest 28.

**Observations:**
- Uses `p-cancelable`, `atob`, `btoa` -- recent commits show active cleanup of legacy dependencies
- Maintains browser polyfill compatibility (webcrypto-shim, fast-text-encoding)
- TypeScript 4.7 is dated (current is 5.x) -- tech debt signal

### 5.2 terraform-provider-okta (Go)

**Go version:** 1.24.0 (current)

**Key dependencies:**
- hashicorp/terraform-plugin-framework v1.17.0
- hashicorp/terraform-plugin-sdk/v2 v2.38.2
- okta/okta-sdk-golang/v4 v4.1.2
- okta/okta-governance-sdk-golang v1.0.1
- crewjam/saml v0.5.1
- go-jose/go-jose/v4 v4.1.3

**Observations:**
- Uses both Terraform Plugin Framework (new) and SDK v2 (legacy) -- migration in progress
- References internal `okta-governance-sdk-golang` -- governance is a first-class concern
- Modern Go version (1.24), goreleaser for binary releases

### 5.3 okta-mcp-server (Python)

**Python version:** 3.13+ (requires-python >= 3.13)

**Dependencies:** mcp[cli] >= 1.9.2, okta >= 2.9.13, loguru, requests, ruff, keyring, keyrings.alt

**Build system:** Hatchling

**Observations:**
- Very new project (Sep 2025), small codebase (312 KB)
- Tools cover: users, groups, applications, policies, system_logs
- Docker + docker-compose support
- Supports Device Authorization Grant and Private Key JWT authentication
- Security policy (SECURITY.md) present
- Minimum Python 3.13 is aggressive -- limits adoption for enterprises still on 3.9-3.11

---

## 6. Open Source Health

### 6.1 Maintenance Activity

| Repository | Last Commit | Release Cadence | Latest Release |
|---|---|---|---|
| okta-signin-widget | 2026-02-18 (today) | Active (7.41.0) | v7.41.0 |
| okta-auth-js | 2025-11-25 | Quarterly | v7.14.1 (Nov 2025) |
| okta-spring-boot | 2026-02-02 | Monthly | v3.0.10 (Feb 2026) |
| terraform-provider-okta | 2026-02-17 | Monthly | v6.5.5 (Jan 2026) |
| okta-sdk-python | 2026-01-30 | Quarterly | v3.1.0 (Jan 2026) |
| auth0/nextjs-auth0 | 2026-02-17 | Bi-weekly | v4.15.0 (Feb 2026) |
| auth0/auth0-spa-js | 2026-02-17 | Weekly | v2.16.0 (Feb 2026) |
| auth0/java-jwt | 2026-02-18 | Quarterly | (via tags: v9.0.3) |
| auth0/node-jsonwebtoken | 2026-02-18 | Infrequent (tags only) | v9.0.3 |

**Assessment:** Auth0 repos generally have faster release cadence than Okta-branded repos. Auth0 SPA and Next.js SDKs release weekly/bi-weekly, while core Okta repos release monthly to quarterly. The sign-in widget is very actively maintained (commit today with translation updates).

### 6.2 Issue Responsiveness

| Repository | Open Issues | Signal |
|---|---|---|
| okta-signin-widget | 356 | HIGH backlog -- sign of broad adoption + limited triage bandwidth |
| terraform-provider-okta | 258 | HIGH backlog -- community-driven, many feature requests |
| okta-auth-js | 225 | HIGH backlog -- widely used, complex surface area |
| auth0/node-jsonwebtoken | 185 | MODERATE -- infrastructure-level project, many are feature requests |
| auth0/express-jwt | 66 | MODERATE |
| auth0/nextjs-auth0 | 32 | HEALTHY -- actively triaged |
| auth0/java-jwt | 26 | HEALTHY |
| auth0/auth0-spa-js | 6 | EXCELLENT |

**Issue closure example (terraform-provider-okta):** Issue #2588 (nil pointer crash) was open 2+ months (Dec 2025 to Feb 2026) before fix. PR-driven issues close faster than community-reported bugs.

**Issue closure example (okta-auth-js):** Recent issues (Feb 2026) closed within 1-3 days -- internal dependency cleanup PRs, not external bug reports.

### 6.3 External Contributors

| Repository | Total Contributors | External Contribution Signal |
|---|---|---|
| auth0/node-jsonwebtoken | 89+ | HIGH -- internet infrastructure, community-driven |
| okta/okta-auth-js | 58+ | MODERATE -- mix of internal Okta engineers + community |
| okta/terraform-provider-okta | 30+ (likely 50+) | HIGH -- Terraform providers attract community PRs |
| auth0/nextjs-auth0 | 30+ | MODERATE -- framework-specific |
| okta/okta-developer-docs | 655 forks | HIGH -- documentation PRs from community |

### 6.4 Versioning & Compatibility

- **Semantic versioning** used across all repos
- **Major version migrations** well-documented (nextjs-auth0 has V1 through V4 migration guides)
- **Multi-version support** maintained (okta-auth-js backports to 7.13 and 7.14 branches)
- **Peer dependency ranges** are generous (nextjs-auth0 supports Next.js 14, 15, and 16)

---

## 7. Forward-Looking Technical Signals

### 7.1 AI/MCP Integration

Okta shipped an official MCP server (`okta/okta-mcp-server`) in September 2025 -- early in the MCP adoption wave. The server enables LLM agents to manage Okta organizations via natural language.

- **Tools:** CRUD for users, groups, applications, policies, and system logs
- **Auth:** Device Authorization Grant (interactive) + Private Key JWT (server-to-server)
- **Stack:** Python, FastMCP, Okta Python SDK
- **Docker support:** Yes, docker-compose included
- **Maturity:** Early (0.1.0), 18 stars, active development

Additionally, Auth0 repos use **Claude-powered code review** (`claude-code-review.yml` workflow) and include **AGENTS.md** files structured for AI agent consumption.

`okta-samples` org also has an `okta-xaa-dev-mcp-client-example` repo (updated 2026-02-18) -- suggesting an "XAA" (cross-app architecture?) MCP client initiative.

### 7.2 Odyssey Design System

The [Odyssey design system](https://github.com/okta/odyssey) is a monorepo (1.2 GB, lerna + yarn workspaces) for building consistent UIs across all Okta products. TypeScript, actively maintained, only 1 open issue. This suggests strong internal UI standardization.

### 7.3 Workflows Platform

`okta/workflows-templates` (129 stars) contains templates for Okta Workflows -- a low-code/no-code automation platform. 57 forks indicate community engagement with the automation layer.

---

## 8. Technical Strengths

| Strength | Evidence |
|---|---|
| **Massive open-source footprint** | 943 repos, 26M+ weekly npm downloads from jsonwebtoken alone |
| **Industry-standard JWT libraries** | node-jsonwebtoken (18K stars) is de facto standard for Node.js JWT |
| **Comprehensive SDK coverage** | 10+ languages with active maintenance |
| **Cell-based architecture** | Proven scalability model, multi-cloud (AWS + GCP), data sovereignty |
| **Infrastructure-as-Code maturity** | Two Terraform providers (Okta + Auth0), both well-maintained |
| **Protocol standards leadership** | Certified OIDC provider, SCIM 2.0, SAML 2.0, DPoP (RFC 9449) |
| **AI-forward engineering** | MCP server, Claude code review, AGENTS.md in repos |
| **Kubernetes at scale** | 1,000+ clusters managed via Argo CD |
| **Developer advocacy depth** | 500+ example repos (oktadev), dedicated dev blog |

---

## 9. Technical Concerns

| Concern | Severity | Evidence |
|---|---|---|
| **High open issue counts** | MEDIUM | Sign-in widget (356), Terraform provider (258), auth-js (225) -- triage bandwidth concern |
| **License ambiguity** | MEDIUM | Several core Okta repos have NOASSERTION license -- unclear terms for enterprise adopters |
| **Auth0 integration debt** | LOW-MEDIUM | Two parallel ecosystems (Okta SDKs + Auth0 SDKs) -- separate Terraform providers, separate React/Angular SDKs, separate design systems |
| **Legacy CI in some repos** | LOW | okta-auth-js still uses Travis CI and .bacon.yml (Okta internal); modern GH Actions only in newer repos |
| **TypeScript version lag** | LOW | okta-auth-js uses TypeScript 4.7 (current is 5.x) |
| **okta-auth-js release slowdown** | LOW-MEDIUM | Last release Nov 2025 (3+ months ago), active commits only on backports |
| **MCP server Python 3.13 requirement** | LOW | Limits enterprise adoption where Python 3.9-3.11 is standard |
| **node-jsonwebtoken maintenance burden** | LOW | 185 open issues, no GitHub Releases (tags only), critical security infrastructure |

---

## 10. Key Findings

1. **Auth0 acquisition dramatically expanded Okta's OSS influence.** Auth0's JWT libraries (18K+ stars, 26M+ weekly downloads) are foundational internet infrastructure. The combined GitHub presence is among the largest in the identity space.

2. **Architecture is production-proven at scale.** Cell-based, shared-nothing architecture on AWS/GCP with 1,000+ Kubernetes clusters managed via Argo CD. Enhanced DR with <5 minute recovery targets. Canadian data cell launching Q1 2026 for sovereignty compliance.

3. **Two-SDK ecosystem is both a strength and a liability.** Okta maintains parallel SDK ecosystems (Okta-branded + Auth0-branded) across all major languages. This provides maximum market coverage but creates maintenance burden and developer confusion about which SDK to use.

4. **AI integration is early but strategic.** Official MCP server (Sep 2025), Claude-powered code review in CI, AGENTS.md files for AI agent consumption. Okta is positioning to be the identity layer for AI agents, not just human users.

5. **Open-source health varies by org.** Auth0 repos are generally better maintained (faster releases, cleaner issue counts, better docs). Okta-branded repos carry more technical debt and higher issue backlogs.

6. **Developer advocacy is a competitive moat.** 500+ repos in oktadev, a dedicated developer blog, extensive example apps covering every major framework combination. This drives top-of-funnel developer adoption.

---

## Appendix: Data Sources

- GitHub API via `gh` CLI (repos, issues, releases, contents, contributors)
- [Okta Architecture Whitepaper](https://www.okta.com/resources/whitepaper/how-okta-builds-and-runs-scalable-infrastructure/)
- [Okta Scaling Architecture eBook](https://www.okta.com/sites/default/files/2020-10/Okta's-Architecture-eBook.pdf)
- [How Okta Scaled to 1,000 Kubernetes Clusters (The New Stack)](https://thenewstack.io/how-okta-scaled-from-12-to-1000-kubernetes-clusters-with-argo-cd/)
- [Unpacking Okta's Tech Architecture (Plato Community)](https://platocommunity.substack.com/p/unpacking-oktas-tech-architecture)
- [Okta Canadian Cell Launch (BetaKit)](https://betakit.com/okta-to-launch-canadian-data-cell-as-sovereignty-debate-intensifies/)
- [jsonwebtoken on npm](https://www.npmjs.com/package/jsonwebtoken)
- [Okta Developer Docs](https://developer.okta.com/docs/)
- Raw data: `raw/github-repos.json`

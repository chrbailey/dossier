# Phase 1: Discovery — Cerebras Systems (cerebras.ai)

**Date:** 2026-02-19
**Analyst:** Dossier Pipeline (automated)
**Confidence Level:** HIGH — Cerebras is a well-documented pre-IPO company with extensive public disclosure via S-1 filing, press releases, and media coverage.

---

## 1. Company Identity

| Field | Value | Source |
|-------|-------|--------|
| **Legal Name** | Cerebras Systems, Inc. | [SEC S-1 Filing](https://www.sec.gov/Archives/edgar/data/2021728/000162828024041596/cerebras-sx1.htm) |
| **Founded** | March 2016 | [Crunchbase](https://www.crunchbase.com/organization/cerebras-systems), [Wikipedia](https://en.wikipedia.org/wiki/Cerebras) |
| **Headquarters** | 1237 E Arques Ave, Sunnyvale, CA 94085 | [D&B](https://www.dnb.com/business-directory/company-profiles.cerebras_systems_inc.9c901924d97ccf0d76f97e87d64a0497.html) |
| **CEO** | Andrew Feldman (Co-Founder) | [LinkedIn](https://www.linkedin.com/in/andrewdfeldman/) |
| **Employees** | ~700-784 (estimates vary by source) | [PitchBook](https://pitchbook.com/profiles/company/163733-59), [LeadIQ](https://leadiq.com/c/cerebras-systems/5a1d9dfc23000059008df279/employee-directory) |
| **Industry** | AI Hardware / Semiconductor / Cloud Inference | — |
| **Ticker (Pending)** | CBRS (Nasdaq, planned Q2 2026) | [Seeking Alpha](https://seekingalpha.com/article/4867744-cerebras-nvidia-rival-gearing-up-for-ipo) |
| **Valuation** | $23 billion (Series H, Feb 2026) | [Bloomberg](https://www.bloomberg.com/news/articles/2026-02-04/cerebras-raises-1-billion-in-funding-at-23-billion-valuation) |

**NOTE:** This is a HARDWARE + CLOUD INFRASTRUCTURE company, not a typical SaaS. Revenue model combines hardware system sales, cloud inference (pay-per-token), and large-scale compute capacity deals.

---

## 2. Domain & DNS

| Field | Value | Source |
|-------|-------|--------|
| **Primary Domain** | cerebras.ai | Direct observation |
| **Secondary Domain** | cerebras.net | [RankChart](https://rankchart.org/site/cerebras.net) — uses GoDaddy NS (NS43/NS44.DOMAINCONTROL.COM) |
| **Registrar** | Not confirmed (.ai WHOIS data limited) | [NamePros](https://www.namepros.com/threads/no-registered-date-for-ai-domains-anymore.1319192/) — .ai domains no longer show registration dates publicly |
| **Subdomains** | cloud.cerebras.ai, chat.cerebras.ai, inference-docs.cerebras.ai, docs.cerebras.ai, sdk.cerebras.net, api.cerebras.ai | WebSearch results |
| **CDN/Proxy** | Cloudflare (confirmed — Cerebras is a Cloudflare AI Gateway provider) | [Cloudflare AI Gateway Docs](https://developers.cloudflare.com/ai-gateway/usage/providers/cerebras/) |
| **AWS Presence** | Yes — AWS Marketplace listing for Fast Inference Cloud | [AWS Marketplace](https://aws.amazon.com/marketplace/pp/prodview-ph4bdvplhhz3o) |

**LIMITATION:** Bash was denied, so `dig`/`whois`/`nslookup` commands could not be run. DNS details for cerebras.ai nameservers, A records, and MX records were not directly confirmed. The cerebras.net domain is confirmed on GoDaddy nameservers with Amazon hosting (ASN 16509).

---

## 3. Leadership & Founding Team

All five co-founders previously worked together at **SeaMicro**, a microserver company founded in 2007 by Feldman and Lauterbach, sold to AMD in 2012 for ~$334-357M. This is a reunited team with deep hardware architecture experience.

| Name | Title | Background | Source |
|------|-------|-----------|--------|
| **Andrew Feldman** | CEO & Co-Founder | Stanford BA (Econ/PoliSci) + MBA. Founded SeaMicro, Force10 Networks, RiverStone Networks | [Clay Dossier](https://www.clay.com/dossier/cerebras-systems-ceo), [LinkedIn](https://www.linkedin.com/in/andrewdfeldman/) |
| **Sean Lie** | CTO & Co-Founder | MIT BS/MS EE/CS. 5 years AMD advanced architecture → SeaMicro lead HW architect | [The Org](https://theorg.com/org/cerebras-systems/teams/leadership-team), [Contrary Research](https://research.contrary.com/company/cerebras) |
| **Gary Lauterbach** | CTO Emeritus & Co-Founder | SeaMicro co-founder, later CTO AMD data center server business. PI on $9.3M DOE grant | [LinkedIn](https://www.linkedin.com/in/gary-lauterbach-9689064/) |
| **Jean-Philippe Fricker** | Chief System Architect & Co-Founder | Sr. HW Architect at DSSD (→ EMC). Lead System Architect at SeaMicro. 30 patents | [Contrary Research](https://research.contrary.com/company/cerebras) |
| **Michael James** | Chief Architect, Advanced Technologies & Co-Founder | SeaMicro co-founder | [Wikipedia](https://en.wikipedia.org/wiki/Cerebras) |

---

## 4. Funding History

| Round | Date | Amount | Valuation | Lead Investor(s) | Source |
|-------|------|--------|-----------|-------------------|--------|
| Series A | May 2016 | $27M | — | Benchmark, Foundation Capital, Eclipse Ventures | [Crunchbase](https://www.crunchbase.com/organization/cerebras-systems) |
| Series B | Dec 2016 | Undisclosed | — | Coatue Management | [MicroVentures](https://microventures.com/microventures-portfolio-company-cerebras-history-and-milestones) |
| Series C | Jan 2017 | Undisclosed | — | VY Capital | [MicroVentures](https://microventures.com/microventures-portfolio-company-cerebras-history-and-milestones) |
| Series D | Nov 2018 | $88M | $1B+ (unicorn) | Undisclosed | [MicroVentures](https://microventures.com/microventures-portfolio-company-cerebras-history-and-milestones) |
| Series E | Late 2019 | $272M | — | Undisclosed | [Tracxn](https://tracxn.com/d/companies/cerebras/__5GJhVFyQgDSkZDyg_ziAYBV4hporw2szCP-mpAUwOf4/funding-and-investors) |
| Series F | Nov 2021 | $250M | — | Alpha Wave Global, Abu Dhabi Growth Fund | [Wikipedia](https://en.wikipedia.org/wiki/Cerebras) |
| Series G | Sep 2025 | $1.1B | $8.1B | Fidelity, Atreides Management | [Cerebras PR](https://www.cerebras.ai/press-release/series-g), [TechCrunch](https://techcrunch.com/2025/09/30/a-year-after-filing-to-ipo-still-private-cerebras-systems-raises-1-1b/) |
| **Series H** | **Feb 2026** | **$1.0B** | **$23B** | **Tiger Global** (w/ Benchmark $225M, AMD, Fidelity, Atreides, Coatue, Altimeter, Alpha Wave, 1789 Capital) | [Bloomberg](https://www.bloomberg.com/news/articles/2026-02-04/cerebras-raises-1-billion-in-funding-at-23-billion-valuation), [Cerebras PR](https://www.cerebras.ai/press-release/cerebras-systems-raises-usd1-billion-series-h) |

**Total Raised:** ~$2.55B across 8 rounds.

### Benchmark's $225M Special Investment

Benchmark Capital — Cerebras' original Series A lead — committed at least $225M to the Series H round. Because Benchmark deliberately caps its funds under $450M, the firm created **two separate special purpose vehicles** both called "Benchmark Infrastructure" specifically for this investment. This is an extraordinary signal of conviction from a top-tier VC.

**Source:** [TechCrunch](https://techcrunch.com/2026/02/06/benchmark-raises-225m-in-special-funds-to-double-down-on-cerebras/), [TechBuzz](https://www.techbuzz.ai/articles/benchmark-raises-225m-for-cerebras-as-ai-chip-war-heats-up)

### AMD as Strategic Investor

AMD's first investment in Cerebras came via the Series H round (Feb 2026). This is notable because the SeaMicro acquisition by AMD in 2012 is the founding team's origin story — AMD is re-investing in the same team a decade later.

**Source:** [Cerebras PR](https://www.cerebras.ai/press-release/cerebras-systems-raises-usd1-billion-series-h)

---

## 5. Products & Technology

### 5.1 Hardware: Wafer-Scale Engine 3 (WSE-3)

| Spec | Value | Source |
|------|-------|--------|
| Process | TSMC 5nm | [Cerebras PR](https://www.cerebras.ai/press-release/cerebras-announces-third-generation-wafer-scale-engine) |
| Transistors | 4 trillion | [Cerebras PR](https://www.cerebras.ai/press-release/cerebras-announces-third-generation-wafer-scale-engine) |
| Compute Cores | 900,000 AI-optimized | [Cerebras Chip Page](https://www.cerebras.ai/chip) |
| On-Chip SRAM | 44 GB | [Tom's Hardware](https://www.tomshardware.com/tech-industry/artificial-intelligence/cerebras-launches-900000-core-125-petaflops-wafer-scale-processor-for-ai-theoretically-equivalent-to-about-62-nvidia-h100-gpus) |
| Memory Bandwidth | 21 PBytes/s | [Tom's Hardware](https://www.tomshardware.com/tech-industry/artificial-intelligence/cerebras-launches-900000-core-125-petaflops-wafer-scale-processor-for-ai-theoretically-equivalent-to-about-62-nvidia-h100-gpus) |
| Die Size | 46,255 mm² (entire 300mm wafer) | [IEEE Spectrum](https://spectrum.ieee.org/cerebras-chip-cs3) |
| Peak Performance | 125 PetaFLOPS | [Tom's Hardware](https://www.tomshardware.com/tech-industry/artificial-intelligence/cerebras-launches-900000-core-125-petaflops-wafer-scale-processor-for-ai-theoretically-equivalent-to-about-62-nvidia-h100-gpus) |
| Size Comparison | 56x larger than largest GPU | [Cerebras](https://www.cerebras.ai/) |
| Announced | March 2024 | [EE Times](https://www.eetimes.com/cerebras-third-gen-wafer-scale-chip-doubles-performance/) |

**Key Innovation:** Rather than cutting a silicon wafer into hundreds of individual chips, Cerebras uses the entire wafer as one monolithic processor. The SRAM is ~1,000x faster than HBM4 found on NVIDIA's upcoming Rubin GPUs.

**Source:** [Tom's Hardware](https://www.tomshardware.com/tech-industry/artificial-intelligence/openai-lauches-gpt-53-codes-spark-on-cerebras-chips)

### 5.2 CS-3 System

The complete compute system housing the WSE-3. In cluster configuration, supports up to 1.2 petabytes of memory. Cerebras claims 2,048 CS-3 systems can train Llama 70B from scratch in a single day.

**Source:** [Cerebras](https://www.cerebras.ai/chip), [NextPlatform](https://www.nextplatform.com/2024/03/14/cerebras-goes-hyperscale-with-third-gen-waferscale-supercomputers/)

### 5.3 Cerebras Inference (Cloud Service)

| Model | Price (per M tokens) | Speed | Source |
|-------|---------------------|-------|--------|
| Llama 3.1 8B | $0.10 | 1,800 tok/s | [Cerebras Pricing](https://www.cerebras.ai/pricing) |
| Llama 3.1 70B | $0.60 | 450 tok/s | [Cerebras Pricing](https://www.cerebras.ai/pricing) |
| Llama 3.1 405B | $6.00 input / $12.00 output | 969 tok/s | [Cerebras Blog](https://www.cerebras.ai/blog/llama-405b-inference) |
| DeepSeek R1 Llama 70B | — | 1,500 tok/s (57x GPUs) | [Cerebras Blog](https://www.cerebras.ai/blog/2026Insights) |
| Llama 4 Scout | — | 2,600 tok/s (19x fastest GPU) | [Cerebras PR](https://www.cerebras.ai/press-release/llama4PR) |
| GPT-OSS-120B (OpenAI) | — | 3,000 tok/s | [Cerebras Blog](https://www.cerebras.ai/blog/openai-codexspark) |

**API:** OpenAI-compatible (drop-in replacement). Available via direct API, AWS Marketplace, OpenRouter, Quora Poe, Cloudflare AI Gateway.

**Free Tier:** 1 million tokens/day for developers.

### 5.4 OpenAI Partnership — GPT-5.3-Codex-Spark

On February 12, 2026, OpenAI released its **first model running on non-NVIDIA silicon** — GPT-5.3-Codex-Spark, optimized for Cerebras WSE. This is a code-focused model with 128K context, running at 1,000+ tokens/s. Available to Codex Pro users and select API partners.

**Source:** [The Register](https://www.theregister.com/2026/02/12/openai_model_cerebras/), [Bloomberg](https://www.bloomberg.com/news/articles/2026-02-12/openai-debuts-first-model-using-chips-from-nvidia-rival-cerebras), [Tom's Hardware](https://www.tomshardware.com/tech-industry/artificial-intelligence/openai-lauches-gpt-53-codes-spark-on-cerebras-chips)

---

## 6. Revenue & Key Deals

| Metric | Value | Period | Source |
|--------|-------|--------|--------|
| Revenue | $136.4M | H1 2024 | [Sacra](https://sacra.com/c/cerebras-systems/) |
| Revenue | ~$206.5M (annualized) | 12 months ending Jun 2024 | [Stock Analysis](https://stockanalysis.com/stocks/cbrs/revenue/) |
| Revenue (est.) | ~$272M | Full Year 2024 (est.) | [Sacra](https://sacra.com/c/cerebras-systems/) |
| YoY Growth | ~245% | 2024 vs 2023 | [Sacra](https://sacra.com/c/cerebras-systems/) |
| Revenue (est.) | >$1B | 2025 (est.) | [TechBuzz](https://www.techbuzz.ai/articles/benchmark-raises-225m-for-cerebras-as-ai-chip-war-heats-up) |

### Major Customer Contracts

| Customer | Deal Value | Duration | Details | Source |
|----------|-----------|----------|---------|--------|
| **OpenAI** | >$10B | Through 2028 | 750 MW of compute capacity for AI inference | [CNBC](https://www.cnbc.com/2026/01/14/cerebras-scores-openai-deal-worth-over-10-billion.html) |
| **Meta** | Undisclosed | Ongoing | Powers Llama API (18x faster than GPU solutions) | [Cerebras News](https://www.cerebras.ai/news/meta-unleashes-llama-api-running-18x-faster-than-openai-cerebras-partnership-delivers-2-600) |
| **IBM** | Undisclosed | Ongoing | Referenced as major customer | [TechBuzz](https://www.techbuzz.ai/articles/benchmark-raises-225m-for-cerebras-as-ai-chip-war-heats-up) |
| **U.S. DOE** | Undisclosed | Ongoing | Genesis Mission commitment | [Cerebras Blog](https://www.cerebras.ai/blog/2026Insights) |
| **G42** | Historical dominant | Through ~2024 | Was 87% of revenue in H1 2024; relationship restructured | [Sherwood News](https://sherwood.news/markets/ai-cerebras-ipo-g42-customer-relationship/) |

### G42 Revenue Concentration — CRITICAL RISK (Historical)

G42, a UAE-based AI conglomerate, accounted for **87% of Cerebras revenue in H1 2024** and **83% in FY 2023**. G42's historical ties to Chinese technology companies triggered a **CFIUS national security review**, which delayed Cerebras' IPO. By late 2024/early 2025, G42 was restructured to hold non-voting shares, and has since been removed from Cerebras' investor list. The OpenAI deal, Meta partnership, IBM, and DOE contracts have significantly diversified the customer base.

**Source:** [Sherwood News](https://sherwood.news/markets/ai-cerebras-ipo-g42-customer-relationship/), [InsiderFinance](https://www.insiderfinance.io/news/openai-cerebras-deal-diversifies-cerebras)

---

## 7. IPO Timeline

| Date | Event | Source |
|------|-------|--------|
| Mid-2024 | Confidential IPO filing | [EBC](https://www.ebc.com/forex/when-is-the-cerebras-ipo-date-valuation-and-more) |
| Sep 30, 2024 | S-1 filed with SEC (NASDAQ: CBRS) | [SEC](https://www.sec.gov/Archives/edgar/data/2021728/000162828024041596/cerebras-sx1.htm) |
| Oct 2024 | IPO delayed — CFIUS review of G42 investment | [US News](https://www.usnews.com/news/technology/articles/2024-10-08/exclusive-cerebras-likely-to-postpone-ipo-due-to-cfius-review-delay-on-g42-deal-sources-say) |
| Mar 2025 | CFIUS clears investment (G42 → non-voting shares) | [Capital.com](https://capital.com/en-int/learn/ipo/cerebras-ipo) |
| Oct 2025 | S-1 formally withdrawn | [DCD](https://www.datacenterdynamics.com/en/news/wafer-scale-ai-chip-company-cerebras-drops-ipo-plans/) |
| Sep 2025 | Series G ($1.1B at $8.1B) — chose private round over IPO | [TechCrunch](https://techcrunch.com/2025/09/30/a-year-after-filing-to-ipo-still-private-cerebras-systems-raises-1-1b/) |
| Feb 2026 | Series H ($1B at $23B) — pre-IPO round | [Bloomberg](https://www.bloomberg.com/news/articles/2026-02-04/cerebras-raises-1-billion-in-funding-at-23-billion-valuation) |
| **Q2 2026** | **IPO expected (NASDAQ: CBRS)** | [Seeking Alpha](https://seekingalpha.com/article/4867744-cerebras-nvidia-rival-gearing-up-for-ipo), [FinancialContent](https://markets.financialcontent.com/wral/article/marketminute-2026-1-15-the-wafer-scale-revolution-cerebras-systems-eyes-landmark-2026-ipo-to-challenge-nvidias-ai-throne) |

---

## 8. Digital Footprint & Social Presence

### Online Properties

| Platform | URL / Handle | Status | Source |
|----------|-------------|--------|--------|
| **Website** | cerebras.ai, cerebras.net | Active | Direct |
| **LinkedIn** | [Cerebras Systems](https://www.linkedin.com/company/cerebras-systems) | Active (201-500 listed, actual ~700-784) | [LinkedIn](https://www.linkedin.com/company/cerebras-systems) |
| **X (Twitter)** | [@CerebrasSystems](https://x.com/CerebrasSystems), [@cerebras](https://x.com/cerebras) | Active | [X](https://x.com/CerebrasSystems) |
| **GitHub** | [Cerebras](https://github.com/cerebras), [CerebrasResearch](https://github.com/CerebrasResearch) | Active | [GitHub](https://github.com/cerebras) |
| **Crunchbase** | [cerebras-systems](https://www.crunchbase.com/organization/cerebras-systems) | Active | [Crunchbase](https://www.crunchbase.com/organization/cerebras-systems) |
| **Wikipedia** | [Cerebras](https://en.wikipedia.org/wiki/Cerebras) | Well-maintained article | [Wikipedia](https://en.wikipedia.org/wiki/Cerebras) |
| **AWS Marketplace** | [Cerebras Fast Inference Cloud](https://aws.amazon.com/marketplace/pp/prodview-ph4bdvplhhz3o) | Listed | [AWS](https://aws.amazon.com/marketplace/pp/prodview-ph4bdvplhhz3o) |
| **PyPI** | cerebras-cloud-sdk | Published | [PyPI](https://pypi.org/project/cerebras-cloud-sdk/) |
| **npm** | @ai-sdk/cerebras | Published | [npm](https://www.npmjs.com/package/@ai-sdk/cerebras) |
| **Product Hunt** | Not found | — | WebSearch returned no results |
| **G2** | Not found (hardware companies typically absent) | — | WebSearch returned no results |

### GitHub Repositories (Notable)

| Repo | Language | License | Last Updated | Purpose |
|------|----------|---------|-------------|---------|
| Cerebras/modelzoo | Python | Apache 2.0 | Jan 2026 | Reference ML model implementations for Cerebras hardware |
| Cerebras/cerebras-cloud-sdk-python | Python | — | Recent | Python SDK for Cerebras Inference API |
| Cerebras/vscode-cerebras-chat | TypeScript | MIT | Jan 2026 | VS Code extension for Cerebras inference |
| Cerebras/cerebras-code-mcp | JavaScript | MIT | Jan 2026 | MCP server for Cerebras code integration |
| Cerebras/Cerebras-Inference-Cookbook | Jupyter | — | Jan 2026 | Example notebooks for inference API |
| CerebrasResearch/REAP | — | — | Dec 2025 | Router-weighted Expert Activation Pruning |
| CerebrasResearch/Sparse-IFT | — | — | 2023 | Sparse Instruction Fine-Tuning |

---

## 9. Tech Stack Signals

### Internal Engineering (from job postings)

| Area | Technologies | Source |
|------|-------------|--------|
| Chip Design | ASIC/SoC, 3D physical design, power/clock/cooling analysis | [Careers](https://www.cerebras.ai/open-positions) |
| Compiler | LLVM toolchain, PyTorch frontend compilation | [Careers](https://www.cerebras.ai/open-positions) |
| ML | vLLM, TensorRT-LLM, TGI, agent frameworks | [Careers](https://www.cerebras.ai/open-positions) |
| Systems | x86 CPU/memory optimization, embedded test frameworks | [Careers](https://www.cerebras.ai/open-positions) |
| Manufacturing | TSMC 5nm (sole fabrication partner) | [Wikipedia](https://en.wikipedia.org/wiki/Cerebras) |
| ATS | Greenhouse | [Greenhouse](https://job-boards.greenhouse.io/cerebrassystems) |

### SDK/API Stack

| Component | Technology | Source |
|-----------|-----------|--------|
| API Protocol | OpenAI-compatible REST API | [Inference Docs](https://inference-docs.cerebras.ai/resources/openai) |
| Python SDK | httpx-based, async/sync, typed | [GitHub](https://github.com/Cerebras/cerebras-cloud-sdk-python) |
| JS Integration | Vercel AI SDK provider | [npm](https://www.npmjs.com/package/@ai-sdk/cerebras) |
| Developer Tools | VS Code extension, MCP server | [GitHub](https://github.com/cerebras) |
| Docs Platform | ReadTheDocs | [ReadTheDocs](https://app.readthedocs.com/projects/cerebras-systems-cerebras-systems-developer-documentation/) |

---

## 10. Competitive Landscape

| Company | Approach | Funding | Valuation | Status | Source |
|---------|---------|---------|-----------|--------|--------|
| **Cerebras** | Wafer-scale (WSE-3) | $2.55B | $23B | IPO Q2 2026 | [Bloomberg](https://www.bloomberg.com/news/articles/2026-02-04/cerebras-raises-1-billion-in-funding-at-23-billion-valuation) |
| **NVIDIA** | GPUs (H100, H200, Blackwell, Rubin) | Public (NVDA) | ~$3T+ market cap | Dominant incumbent | — |
| **Groq** | LPU (deterministic streaming) | $750M+ | $6.9B | NVIDIA licensing + asset deal (Dec 24, 2025); Groq continues operating independently | [Fortune](https://fortune.com/2026/01/05/nvidia-groq-deal-ai-chip-startups-in-play/) |
| **SambaNova** | RDU (reconfigurable dataflow) | Hundreds of millions | — | Intel term sheet stalled; raising $350-500M independently | [Fortune](https://fortune.com/2026/01/05/nvidia-groq-deal-ai-chip-startups-in-play/) |
| **Graphcore** | IPU (Intelligence Processing Unit) | $700M+ | — | Restructured | — |
| **Tenstorrent** | RISC-V AI accelerator | — | — | Growing | — |

**Key Differentiator:** Cerebras is the only company using full-wafer-scale integration (entire 300mm wafer = one chip). NVIDIA's Groq licensing + asset deal (Dec 24, 2025) and Intel's SambaNova term sheet are consolidating the competitive field, potentially leaving Cerebras as the primary independent alternative to NVIDIA. *[Note: NVIDIA now has Groq LPU IP for integration into Rubin -- potentially more threatening to Cerebras than Groq as an independent competitor.]*

---

## 11. Data Center Infrastructure

| Location | Status | Notes | Source |
|----------|--------|-------|--------|
| Santa Clara, CA | Operational | — | [Cerebras PR](https://www.cerebras.ai/press-release/cerebras-announces-six-new-ai-datacenters-across-north-america-and-europe-to-deliver-industry-s) |
| Stockton, CA | Operational | — | [Cerebras PR](https://www.cerebras.ai/press-release/cerebras-announces-six-new-ai-datacenters-across-north-america-and-europe-to-deliver-industry-s) |
| Dallas, TX | Operational | — | [Cerebras PR](https://www.cerebras.ai/press-release/cerebras-announces-six-new-ai-datacenters-across-north-america-and-europe-to-deliver-industry-s) |
| Minneapolis, MN | Q2 2025 | — | [DCD](https://www.datacenterdynamics.com/en/news/cerebras-plans-six-new-ai-data-centers-in-north-america-and-europe/) |
| Oklahoma City, OK | Jun 2025 | 300+ CS-3 systems, tornado/seismic shielded, triple redundant power | [VentureBeat](https://venturebeat.com/ai/cerebras-just-announced-6-new-ai-datacenters-that-process-40m-tokens-per-second-and-it-could-be-bad-news-for-nvidia) |
| Montreal, Canada | Jul 2025 | Enovum facility | [DCD](https://www.datacenterdynamics.com/en/news/cerebras-plans-six-new-ai-data-centers-in-north-america-and-europe/) |
| Atlanta, GA | Q4 2025 | — | [DCD](https://www.datacenterdynamics.com/en/news/cerebras-plans-six-new-ai-data-centers-in-north-america-and-europe/) |
| France | Q4 2025 | — | [DCD](https://www.datacenterdynamics.com/en/news/cerebras-plans-six-new-ai-data-centers-in-north-america-and-europe/) |
| New York | TBD | — | [Nasdaq](https://www.nasdaq.com/press-release/cerebras-announces-six-new-ai-datacenters-across-north-america-and-europe-deliver) |

**Aggregate Capacity Target:** 40+ million tokens/second (20x expansion). 85% of capacity in the US.

---

## 12. Supply Chain Risks

| Risk | Severity | Details | Source |
|------|----------|---------|--------|
| **TSMC sole supplier** | HIGH | All WSE fabrication at TSMC. No alternative foundry can produce wafer-scale chips. Competes with Apple, NVIDIA for TSMC 5nm capacity | [Digitimes](https://www.digitimes.com/news/a20241002PD218/cerebras-tsmc-g42-supply-chain-ipo.html) |
| **Taiwan geopolitical** | HIGH | Taiwan Strait disruption would halt all chip production | [Contrary Research](https://research.contrary.com/company/cerebras) |
| **Yield sensitivity** | MEDIUM | Wafer-scale dies: yield losses per defect cost more than traditional chips | [AnandTech](https://www.anandtech.com/show/16626/cerebras-unveils-wafer-scale-engine-two-wse2-26-trillion-transistors-100-yield) |
| **HBM supply** | MEDIUM | Relies on small number of high-bandwidth-memory suppliers | [Contrary Research](https://research.contrary.com/company/cerebras) |

---

## 13. Key Partnerships

| Partner | Nature | Date | Significance | Source |
|---------|--------|------|-------------|--------|
| **OpenAI** | $10B+ compute capacity (750 MW through 2028) | Jan 2026 | Largest deal ever; first non-NVIDIA silicon for OpenAI | [CNBC](https://www.cnbc.com/2026/01/14/cerebras-scores-openai-deal-worth-over-10-billion.html) |
| **Meta** | Powers Llama API | Apr 2025 | 18x faster than traditional GPU solutions | [Cerebras](https://www.cerebras.ai/news/meta-unleashes-llama-api-running-18x-faster-than-openai-cerebras-partnership-delivers-2-600) |
| **TSMC** | Sole fabricator | Ongoing (3 generations) | WSE-1 → WSE-2 → WSE-3 spanning 16nm → 7nm → 5nm | [Digitimes](https://www.digitimes.com/news/a20240315PD203/tsmc-cerebras-ic-design-ai-supercomputing.html) |
| **AMD** | Strategic investor (Series H) | Feb 2026 | Former acquirer of founders' company (SeaMicro) re-investing | [Cerebras PR](https://www.cerebras.ai/press-release/cerebras-systems-raises-usd1-billion-series-h) |
| **MBZUAI / Inception** | JAIS2 LLM collaboration | 2025 | Arabic language AI model | [Cerebras Blog](https://www.cerebras.ai/blog/2026Insights) |
| **U.S. DOE** | Genesis Mission | 2025 | Government/scientific computing | [Cerebras Blog](https://www.cerebras.ai/blog/2026Insights) |
| **IBM** | Customer | Ongoing | Enterprise AI infrastructure | [TechBuzz](https://www.techbuzz.ai/articles/benchmark-raises-225m-for-cerebras-as-ai-chip-war-heats-up) |

---

## 14. Summary Assessment

### Company Profile (One Paragraph)

Cerebras Systems is a Sunnyvale-based AI hardware company founded in 2016 by the five co-founders of SeaMicro (acquired by AMD for $334M in 2012). The company's core innovation is wafer-scale integration — using an entire 300mm silicon wafer as a single chip (WSE-3: 4 trillion transistors, 900,000 cores, 44GB SRAM). With $2.55B in total funding at a $23B valuation, Cerebras is the leading independent challenger to NVIDIA in AI compute, differentiated by inference speeds 20x+ faster than GPU-based alternatives. A $10B+ OpenAI partnership (Jan 2026) and Meta's Llama API deal have transformed Cerebras from a single-customer-dependent hardware vendor (87% revenue from G42 in 2024) into a diversified AI infrastructure platform. The company is targeting a Q2 2026 IPO on NASDAQ under the ticker CBRS.

### Strengths (Confirmed)
- **Unique technology moat:** Only company doing wafer-scale integration; 10 years of development
- **Reunited founding team:** All 5 co-founders worked together at SeaMicro — proven execution
- **Marquee customers:** OpenAI ($10B+), Meta, IBM, U.S. DOE
- **Speed advantage:** Consistently 20x+ faster inference than GPU alternatives, validated by third parties
- **Investor quality:** Benchmark (2016 Series A through 2026 $225M SPV), Tiger Global, Fidelity, AMD
- **Revenue growth:** ~245% YoY (2024), estimated >$1B in 2025

### Risks (Confirmed)
- **TSMC sole-source dependency:** No alternative foundry for wafer-scale chips
- **Historical customer concentration:** 87% revenue from G42 (H1 2024) — now diversifying
- **CFIUS/geopolitical exposure:** G42 ties triggered national security review; Taiwan supply chain risk
- **IPO execution risk:** S-1 withdrawn once; second attempt pending
- **Competitive consolidation:** NVIDIA secured Groq LPU IP via licensing + asset deal (Dec 24, 2025; Groq continues operating independently); may acquire others, increasing competitive pressure
- **Profitability unknown:** Revenue growing rapidly but profitability metrics not publicly disclosed

### Open Questions for Phase 2+
1. What are Cerebras' gross margins on hardware vs. cloud inference?
2. What is the actual G42 revenue percentage as of late 2025 / early 2026?
3. What does the OpenAI deal's revenue recognition timeline look like?
4. What is the current fabrication yield on WSE-3 at TSMC 5nm?
5. How does the AMD strategic investment affect competitive positioning vs. NVIDIA?
6. What is the team attrition rate — are key engineers being poached?
7. What does the patent portfolio look like (Jean-Philippe Fricker holds 30+ patents)?
8. What are the unit economics of the data center buildout?

---

## Appendix: Sources Index

All sources cited inline. Key primary sources:
- [Cerebras S-1 (SEC)](https://www.sec.gov/Archives/edgar/data/2021728/000162828024041596/cerebras-sx1.htm)
- [Cerebras Official Website](https://www.cerebras.ai/)
- [Wikipedia: Cerebras](https://en.wikipedia.org/wiki/Cerebras)
- [Crunchbase](https://www.crunchbase.com/organization/cerebras-systems)
- [Bloomberg: $1B Series H](https://www.bloomberg.com/news/articles/2026-02-04/cerebras-raises-1-billion-in-funding-at-23-billion-valuation)
- [TechCrunch: Benchmark $225M](https://techcrunch.com/2026/02/06/benchmark-raises-225m-in-special-funds-to-double-down-on-cerebras/)
- [CNBC: OpenAI $10B Deal](https://www.cnbc.com/2026/01/14/cerebras-scores-openai-deal-worth-over-10-billion.html)
- [The Register: GPT-5.3-Codex-Spark](https://www.theregister.com/2026/02/12/openai_model_cerebras/)
- [Sacra: Revenue Estimates](https://sacra.com/c/cerebras-systems/)
- [Contrary Research: Company Deep-Dive](https://research.contrary.com/company/cerebras)

---

*Raw data saved to: `/Volumes/OWC drive/Dev/dossier/output/cerebras.ai/raw/website-content.json`*
*Phase 1 complete. Ready for Phase 2 (Market Analysis).*

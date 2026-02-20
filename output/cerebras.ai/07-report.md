# Due Diligence Report: Cerebras Systems (cerebras.ai)

**Date:** 2026-02-19
**Prepared by:** Dossier Pipeline (automated, 7-phase analysis)
**Classification:** Pre-IPO Investment Due Diligence
**Report Version:** 1.0

---

## Table of Contents

1. [Executive Summary](#1-executive-summary)
2. [Company Profile](#2-company-profile)
3. [Problem Statement](#3-problem-statement)
4. [Market Analysis](#4-market-analysis)
5. [Technical Assessment](#5-technical-assessment)
6. [Claims Validation](#6-claims-validation)
7. [Academic & IP Landscape](#7-academic--ip-landscape)
8. [Valuation Signals](#8-valuation-signals)
9. [Confidence Matrix](#9-confidence-matrix)
10. [Risk Register](#10-risk-register)
11. [Cross-Phase Narrative & Contradictions](#11-cross-phase-narrative--contradictions)
12. [Recommended Next Steps](#12-recommended-next-steps)

---

## 1. Executive Summary

Cerebras Systems is a Sunnyvale-based AI hardware and cloud infrastructure company founded in 2016 by the five co-founders of SeaMicro (acquired by AMD for $334M in 2012). The company's core innovation is wafer-scale integration -- using an entire 300mm silicon wafer as a single chip (WSE-3: 4 trillion transistors, 900,000 cores, 44GB on-chip SRAM). This architectural breakthrough delivers 20x+ faster AI inference than GPU clusters by eliminating the memory bandwidth bottleneck that constrains all conventional chip designs.

With $2.55B in total funding at a $23B valuation (Series H, Feb 2026), Cerebras has secured a transformative $10B+ compute capacity deal with OpenAI (750MW through 2028), partnerships with Meta, IBM, and the U.S. Department of Energy, and is targeting a Q2 2026 IPO on NASDAQ under the ticker CBRS. The competitive landscape has consolidated dramatically in Cerebras' favor: NVIDIA secured Groq LPU IP via licensing + asset deal ($20B, Dec 24, 2025; Groq continues operating independently), Intel's SambaNova term sheet has stalled, and Graphcore has restructured, leaving Cerebras as the leading independent AI chip challenger to NVIDIA.

The investment thesis rests on three pillars: (1) irreplicable hardware technology with physics-based performance advantages, (2) a time-sensitive competitive window (H1-H2 2026) before NVIDIA's Rubin platform narrows the speed gap, and (3) the training-to-inference market shift that moves AI compute demand directly into Cerebras' sweet spot. The thesis is contingent on execution: the OpenAI revenue ramp, gross margin improvement from 38-41% toward 50%+, and customer diversification beyond 60-75% concentration on a single buyer.

**Calibrated Verdict: QUALIFIED CANDIDATE.** *[Calibrated from STRONG CANDIDATE -- see validation/final-calibrated-output.md]* The three execution conditions each carry 30-50% individual success probability, yielding a joint probability of roughly 15-30%, which does not support a STRONG CANDIDATE rating. Appropriate for investors with high risk tolerance and a 12-month re-evaluation trigger.

---

## 2. Company Profile

| Field | Value | Source | Confidence |
|-------|-------|--------|:----------:|
| **Legal Name** | Cerebras Systems, Inc. | SEC S-1 | HIGH |
| **Domain** | cerebras.ai | Direct | HIGH |
| **Founded** | March 2016 | Crunchbase, Wikipedia | HIGH |
| **HQ Location** | 1237 E Arques Ave, Sunnyvale, CA 94085 | D&B | HIGH |
| **CEO** | Andrew Feldman (Co-Founder) | LinkedIn, SEC | HIGH |
| **CTO** | Sean Lie (Co-Founder) | The Org, LinkedIn | HIGH |
| **Team Size** | 700-784 employees | PitchBook (784), LeadIQ (724), TrueUp (700), SignalHire (704) | HIGH |
| **Total Funding** | $2.55B (8 rounds) | Bloomberg, TechCrunch, Cerebras PR | HIGH |
| **Latest Round** | Series H: $1B at $23B (Tiger Global lead, Feb 2026) | Bloomberg | HIGH |
| **Revenue (FY2024 est.)** | $272-500M | Sacra ($272M), StockAnalysis (534% YoY = ~$499M) | MEDIUM |
| **Revenue (FY2025 est.)** | $950M-$1.2B | PM Insights, TechBuzz | LOW |
| **Gross Margin** | 38-41% (H1 2024) | SEC S-1 | HIGH |
| **Net Loss** | $66.6M (H1 2024) | SEC S-1 | HIGH |
| **IPO Target** | Q2 2026, NASDAQ: CBRS | Seeking Alpha, SiliconANGLE | MEDIUM |
| **Primary Product** | WSE-3 (wafer-scale chip), CS-3 (compute system), Cerebras Inference (cloud API) | Cerebras | HIGH |
| **Industry** | AI Hardware / Semiconductor / Cloud Inference | -- | HIGH |

### Founding Team

All five co-founders previously worked together at SeaMicro, a microserver company founded in 2007 by Feldman and Lauterbach, acquired by AMD in 2012 for ~$334-357M. This is a reunited team with deep hardware architecture experience and a prior successful exit.

| Name | Title | Key Background |
|------|-------|---------------|
| **Andrew Feldman** | CEO & Co-Founder | Stanford BA + MBA. Founded SeaMicro, Force10 Networks, RiverStone Networks |
| **Sean Lie** | CTO & Co-Founder | MIT BS/MS EE/CS. 29 patents. Hot Chips presenter (2019, 2022, 2024). AMD advanced architecture |
| **Gary Lauterbach** | CTO Emeritus & Co-Founder | 68 career patents. PI on $9.3M DOE grant. AMD data center CTO |
| **Jean-Philippe Fricker** | Chief System Architect & Co-Founder | 30 patents. DSSD (EMC), SeaMicro lead system architect |
| **Michael James** | Chief Architect, Advanced Technologies & Co-Founder | SeaMicro co-founder. Scaled compute fabric patents |

### Funding History

| Round | Date | Amount | Valuation | Lead Investor(s) |
|-------|------|--------|-----------|-------------------|
| Series A | May 2016 | $27M | -- | Benchmark, Foundation Capital, Eclipse |
| Series B | Dec 2016 | Undisclosed | -- | Coatue Management |
| Series C | Jan 2017 | Undisclosed | -- | VY Capital |
| Series D | Nov 2018 | $88M | $1B+ | Undisclosed |
| Series E | Late 2019 | $272M | -- | Undisclosed |
| Series F | Nov 2021 | $250M | -- | Alpha Wave Global, Abu Dhabi Growth Fund |
| Series G | Sep 2025 | $1.1B | $8.1B | Fidelity, Atreides Management |
| **Series H** | **Feb 2026** | **$1.0B** | **$23B** | **Tiger Global** (+ Benchmark $225M via 2 SPVs, AMD, Fidelity, Coatue, Altimeter) |

**Notable investor signals:**
- **Benchmark Capital** committed $225M via two special-purpose vehicles -- extraordinary for a firm that caps funds at $450M. From Series A lead (2016) to largest single-company bet in Benchmark history.
- **AMD** made its first investment in Cerebras at Series H -- the founding team's former acquirer re-investing a decade later.
- **Sam Altman** (OpenAI CEO) is a personal investor in Cerebras.

*Source: Phase 1 (Discovery)*

---

## 3. Problem Statement

### What Problem Does Cerebras Solve?

AI inference and training workloads are bottlenecked by GPU cluster architecture. NVIDIA GPU-based systems require massive clusters of discrete chips connected by high-speed interconnects, creating three fundamental constraints:

1. **Latency:** Data must travel between chips, through switches, and to/from external HBM memory. This serializes computation and caps inference speed at ~50-150 tokens/second for large models on GPU clusters.
2. **Energy inefficiency:** 40-60% of data center power is consumed by data movement between chips, not computation. GPU clusters scale power linearly (or worse) with model size.
3. **Operational complexity:** Deploying large models across hundreds of GPUs requires sophisticated parallelism frameworks, specialized networking (NVLink, InfiniBand), and significant engineering overhead.

### Cerebras' Solution

Wafer-scale integration -- a single chip the size of an entire 300mm silicon wafer (46,225 mm2) with 44GB of on-chip SRAM delivering 21 PB/s memory bandwidth. By keeping model weights entirely on-chip, Cerebras eliminates inter-chip data movement and delivers 20x+ faster inference at lower energy per token.

### Vitamin or Painkiller?

**Painkiller** for inference-heavy workloads. As AI shifts from training-dominant to inference-dominant (Deloitte: inference = 50% of compute in 2025, projected 67% in 2026, trending toward 80% long-term), inference speed and cost directly determine unit economics for every AI product. OpenAI's $10B commitment is the ultimate validation -- they would not sign a deal of that magnitude for a "nice to have."

*Source: Phase 2 (Market Analysis)*

---

## 4. Market Analysis

### 4.1 Market Size

| Metric | Estimate | Approach | Confidence | Source |
|--------|----------|----------|:----------:|--------|
| **TAM** | $286B by 2030 | AI data center chips (Omdia) | HIGH | Omdia |
| **TAM (alt)** | $500B by 2026 | Generative AI chips (Deloitte) | MEDIUM | Deloitte |
| **SAM** | $50-104B by 2030 | AI ASIC accelerators + inference chips | MEDIUM-HIGH | Bloomberg Intelligence, Deloitte |
| **SOM** | $3-5B by 2027 | Bottom-up: OpenAI + Meta + enterprise + gov + cloud | MEDIUM | Derived |

**Bottom-up SOM composition (2027 estimated):**

| Customer Segment | Est. Annual Revenue | % of SOM |
|-----------------|-------------------:|:--------:|
| OpenAI | $2.5-3.0B | ~65% |
| Meta | $200-500M | ~10% |
| IBM + Enterprise | $100-300M | ~7% |
| DOE + Government | $50-200M | ~4% |
| Cloud Inference API | $50-100M | ~2% |
| **Total** | **$3.0-4.1B** | **100%** |

**Critical observation:** The SOM is dominated by OpenAI (~60-75%). Customer concentration has improved in category (US-based marquee brand vs. UAE entity) but not in structure (single customer dominance persists).

### 4.2 Competitive Landscape

The competitive field has consolidated dramatically in the past 90 days:

| Company | Architecture | Status (Feb 2026) | Threat to Cerebras |
|---------|-------------|-------------------|:------------------:|
| **NVIDIA** | GPUs (Blackwell, Rubin H2 2026) | Dominant incumbent, ~$3T market cap | CRITICAL |
| **Google TPU** | Systolic array (Trillium/v6) | Captive to Google Cloud | LOW-MEDIUM |
| **AMD** | GPUs (MI300X, MI400) | Second-source GPU, ~$180B market cap | MEDIUM |
| **AWS Trainium** | Custom ASIC (Trainium3) | Captive to AWS | LOW-MEDIUM |
| **Groq** | LPU (deterministic) | **NVIDIA licensing + asset deal ($20B, Dec 24, 2025); continues operating independently** | REDUCED — NVIDIA now has Groq LPU IP for Rubin |
| **SambaNova** | RDU (reconfigurable) | Intel term sheet stalled; raising $350-500M instead | WEAKENED (still independent) |
| **Intel Gaudi** | Custom ASIC | Failed (<1% market share, missed $500M target) | NEGLIGIBLE |
| **Tenstorrent** | RISC-V AI (Jim Keller) | Pre-revenue in data center AI, $3.2B valuation | LOW |

**Positioning:** Cerebras occupies the **Visionary** quadrant -- high completeness of vision (8/10), developing ability to execute (6/10). NVIDIA is the undisputed Leader (10/10 on both axes). Google TPU is a second Leader. AMD is a Challenger. Everyone else is a Niche Player or has been acquired.

### 4.3 SWOT Analysis

#### Strengths
- Unique wafer-scale technology moat (10 years, 102 patents, no replication)
- 20x+ inference speed advantage, independently verified (Artificial Analysis, W&B)
- Reunited founding team with prior exit (SeaMicro -> AMD for $334M)
- Marquee anchor customer: OpenAI $10B+ through 2028
- 2x power efficiency vs. NVIDIA (MIT benchmark)
- Improving gross margins: 11.7% (2022) -> 33.5% (2023) -> 41.1% (H1 2024)

#### Weaknesses
- TSMC sole-source dependency (existential supply chain risk)
- Narrow software ecosystem (NVIDIA CUDA has 20+ years of lock-in)
- Customer concentration: G42 87% (H1 2024) -> OpenAI 60-75% (est. 2026)
- Still unprofitable: net loss $66.6M in H1 2024 (net margin -48%)
- Limited model support on inference API (open-source models only)
- No competitive training story at frontier-model scale

#### Opportunities
- Training-to-inference market shift (50% -> 67% -> 80% of AI compute)
- Agentic AI explosion (10-100x more inference calls per user interaction)
- Competitive consolidation clears the field (NVIDIA secured Groq LPU IP, SambaNova weakened)
- Data center power constraints favor Cerebras' 2x energy efficiency
- IPO provides currency for acquisitions, partnerships, talent retention

#### Threats
- NVIDIA Rubin (H2 2026): 5x inference improvement + Groq LPU IP
- Hyperscaler captive silicon scaling (Google 1M TPUs, AWS Trainium3, Microsoft Maia)
- OpenAI internal chip development (Broadcom/TSMC 3nm, mass production 2026)
- Taiwan geopolitical risk (all fabrication at TSMC)
- IPO timing risk (S-1 withdrawn once, delayed twice)
- NVIDIA ecosystem lock-in deepens with each product generation

### 4.4 Key Market Dynamics

| Trend | Impact on Cerebras | Timeframe |
|-------|:------------------:|:---------:|
| Training -> inference shift | STRONGLY POSITIVE | 2025-2030 |
| Agentic AI proliferation | STRONGLY POSITIVE | 2026-2028 |
| Competitive consolidation | POSITIVE | 2025-2026 |
| Data center power constraints | POSITIVE | 2025-2030 |
| Hyperscaler captive silicon | NEGATIVE | 2025-2028 |
| NVIDIA Rubin launch | NEGATIVE | H2 2026 |
| AI chip export controls | MIXED | 2025-2027 |

*Source: Phase 2 (Market Analysis)*

---

## 5. Technical Assessment

### 5.1 Architecture

**Hardware Architecture: EXCEPTIONAL**

The WSE-3 represents the only commercially successful wafer-scale integrated circuit in history. It solved four engineering problems that defeated all prior attempts at wafer-scale integration:

| Challenge | Cerebras Solution | Evidence |
|-----------|------------------|----------|
| **Yield management** | Small cores (0.05 mm2 vs GPU's ~6 mm2 per SM), 1-1.5% redundant cores, dynamic routing around defects. 100x defect tolerance vs. GPUs. | Hot Chips 2024, IEEE Micro, Cerebras yield blog |
| **Power delivery** | ~20kW+ per wafer via 300+ distributed VRMs with perpendicular current injection. Patented. | US10,242,891, US10,777,532 |
| **Thermal management** | Custom cold plates, micro-fin cooling maintaining <20C delta-T across a dinner-plate-sized chip. Patented. | Patent portfolio, Hot Chips presentations |
| **Communication fabric** | 900,000 cores in 2D mesh; "wavelets" (32-bit messages in single clock cycle). No external network fabric needed within chip. | IEEE Micro 2023/2024, CSL documentation |

**Memory architecture -- the fundamental speed advantage:**

| Memory Type | Capacity | Bandwidth | Latency | Used By |
|-------------|----------|-----------|---------|---------|
| SRAM (on-chip) | 44 GB | 21 PB/s | ~1 ns | Cerebras WSE-3 |
| HBM3e (off-chip) | 80-192 GB | 3.35-8 TB/s | ~100 ns | NVIDIA H100/B200 |

For models fitting in 44GB (Llama 70B quantized, Llama 8B), all weights reside on-chip with zero memory fetch latency. This eliminates the memory wall that limits GPU inference throughput. The bandwidth differential (21 PB/s vs. 3.35-8 TB/s = ~3,000-6,000x) is an immutable physical property of the architecture.

**Software Stack: STRONG**

| Layer | Technology | Maturity |
|-------|-----------|----------|
| User-facing API | OpenAI-compatible REST API | Production |
| Cloud SDKs | Python (httpx, Pydantic), Node.js (TypeScript) -- Stainless-generated | Production |
| Training framework | cerebras.pytorch (drop-in PyTorch replacement) | Production |
| Graph Compiler (CGC) | Ahead-of-time mapping of neural networks to 900K cores | Proprietary, mature |
| CSL | Cerebras Software Language -- C-like with dataflow tasks + wavelets | Specialized |
| Runtime/Firmware | WSE hardware control, MemoryX/SwarmX protocols | Proprietary |

The CGC compiler automatically maps neural network layers to 900,000 cores, reducing 20,000 lines of GPU networking code to ~600 lines on Cerebras.

### 5.2 Open-Source Presence

| Metric | Value |
|--------|-------|
| GitHub Orgs | Cerebras (13 repos), CerebrasResearch (8 repos) |
| Total Public Repos | 21 |
| Total Stars | ~1,990 |
| SDK PyPI Downloads | 1.14M/month |
| Active Contributors (public) | ~30-40 |

**Assessment:** Cerebras treats open-source as a developer onboarding funnel, not a community ecosystem. The SDKs are high-quality (Stainless-generated, same tooling as OpenAI/Anthropic). Everything else receives minimal community investment. Modelzoo (1,125 stars) has 26 open issues with many unanswered for months. Community PRs go unreviewed. No public Discord, Slack, or developer forum exists.

### 5.3 Dependency Analysis

SDK dependencies are clean and modern: httpx, Pydantic, anyio (Python); TypeScript, jest, yarn (Node.js). All Stainless-managed. No outdated or deprecated dependencies. Ecosystem integrations include Vercel AI SDK, LangChain, Cloudflare AI Gateway, and AWS Marketplace.

The critical dependency is not software but manufacturing: **TSMC 5nm sole-source fabrication** for all WSE-3 chips. No alternative foundry can produce wafer-scale chips.

### 5.4 Test & Quality Signals

**Positive signals:** CI/CD (GitHub Actions) on both SDKs and MCP server. Test suites present. Semantic versioning. SECURITY.md, CHANGELOG.md, CONTRIBUTING.md on SDKs. DevContainer support. Release automation via release-please.

**Negative signals:** No tests on modelzoo, gigaGPT, or inference-examples repos. Low contributor counts (2-8 per repo). Missing licenses on 3 repos (inference-examples, DocChat, Cookbook). MCP server has 11 unresponded open issues. Stale repos (online-normalization last pushed Apr 2021).

### 5.5 Inference Performance (Independently Verified)

| Model | Cerebras tok/s | Best GPU Alternative | Speedup | Verification Source |
|-------|:--------------:|:--------------------:|:-------:|:-------------------:|
| Llama 4 Maverick | 2,522 | 1,038 (B200) | 2.4x | Artificial Analysis |
| gpt-oss-120B | 2,835 | 900 (B200) | 3.1x | Artificial Analysis |
| Llama 3 70B | 2,314 | N/A | N/A | Artificial Analysis |
| DeepSeek R1 70B | 1,500 | 26 (GPUs) | 57x | Cerebras (self-reported) |
| Llama 405B | 969 | ~13 (hyperscaler) | 75x | Cerebras (self-reported) |

**Assessment:** The speed advantage is real and architecturally grounded. Independently verified range: **2.4-3.1x vs. dedicated Blackwell B200** for large models, **20-57x vs. GPU clusters** for smaller models. Marketing materials consistently cite the most favorable comparison. Enterprise buyers should expect 2.5-5x for production large-model workloads.

*Source: Phase 3 (Technical Analysis)*

---

## 6. Claims Validation

### Claims Inventory

| # | Claim | Verdict | Confidence | Key Evidence |
|---|-------|:-------:|:----------:|-------------|
| 1 | WSE-3 is world's largest chip (4T transistors) | **VERIFIED** | HIGH | IEEE Spectrum, Tom's Hardware, Hot Chips, arXiv |
| 2 | 20x+ faster inference than GPUs | **VERIFIED** (with nuance) | HIGH | Artificial Analysis (2.4-3.1x vs B200; 20-57x vs GPU clusters) |
| 3 | OpenAI $10B+ deal, 750MW through 2028 | **VERIFIED** | HIGH | CNBC, Bloomberg, OpenAI official announcement |
| 4 | "Last independent NVIDIA alternative" | **PLAUSIBLE** (overstatement) | MEDIUM | NVIDIA secured Groq LPU IP (Dec 24, 2025; Groq still independent); SambaNova Intel term sheet stalled; Tenstorrent still exists |
| 5 | $23B valuation (Series H) | **VERIFIED** | HIGH | Bloomberg, TechCrunch, Axios |
| 6 | ~700-784 employees | **VERIFIED** | HIGH | 4 independent sources converge |
| 7 | Revenue >$1B in 2025 | **PLAUSIBLE** | MEDIUM | No public FY2025 financials |
| 8 | 100% wafer yield | **PLAUSIBLE** (with caveat) | MEDIUM | "All wafers pass" via redundant cores, not zero defects |
| 9 | IPO Q2 2026 | **PLAUSIBLE** | MEDIUM | S-1 withdrawn once; two prior delays |
| 10 | G42 concentration resolved | **PLAUSIBLE** | MEDIUM | No FY2025 customer data |
| 11 | 56x larger than largest GPU | **VERIFIED** | HIGH | 46,255 mm2 vs ~814 mm2 = ~57x |
| 12 | Benchmark $225M conviction bet | **VERIFIED** | HIGH | Two SPVs confirmed by TechCrunch |
| 13 | CS-3 32% lower cost vs DGX B200 | **UNVERIFIABLE** | LOW | Self-reported TCO, no independent study |
| 14 | Near-linear scaling across clusters | **PLAUSIBLE** | MEDIUM | DOE Tri-Labs work supports; not independently benchmarked at max scale |
| 15 | Profitability trajectory improving | **VERIFIED** | HIGH | S-1 data: losses narrowing across every period |

**Claims accuracy rate:** 12/15 verified or plausible. 1 unverifiable. 2 exaggerated/theater.
**Pattern:** Optimistic but not misleading. Core technology claims are real. Speed advantage is real but marketed at the high end of the range. Financial projections and competitive positioning involve normal pre-IPO narrative optimism.

### Critical Gaps

**GAP-1: No MLPerf Submission (CRITICAL)**
For a company claiming "world's fastest inference," not submitting to the industry-standard benchmark is conspicuous. Every major competitor (NVIDIA, Google, AMD, Intel) submits. Artificial Analysis provides independent verification, but MLPerf is the gold standard for enterprise procurement decisions and institutional investor due diligence. HN commenters have flagged this repeatedly.

**GAP-2: OpenAI Deal Revenue Recognition Timing (CRITICAL)**
The $10B+ headline masks execution complexity. Revenue is delivered in capacity tranches through 2028. Cerebras must build data centers at unprecedented speed. OpenAI's financial viability to pay for all committed compute has been questioned (WSJ noted $600B+ in total cloud contracts against ~$13B revenue). If backloaded, near-term revenue impact could be much smaller than the headline suggests.

**GAP-3: Customer Concentration Data Gap (CRITICAL for IPO)**
No public FY2025 or FY2026 customer concentration data exists. The most recent filing showed 87% from G42. While OpenAI/Meta/IBM deals are confirmed, their actual revenue contribution is unknown. The updated S-1 will be the first real visibility into this.

**GAP-4: Enterprise Customer Churn Signals (CRITICAL)**
HN "Tell HN: Avoid Cerebras if you are a founder" (Jan 2026) reports enterprise customers kicked off platform and told to migrate to Groq. Multiple customers in a Discord support group received similar treatment. This suggests capacity constraints forcing triage -- prioritizing hyperscale deals (OpenAI) over smaller customers.

### AI Reality Score: 5.0/5 (tech) / 3.5/5 (business)

Cerebras is a genuine deep-tech hardware company. Their AI is not marketing spin -- it is the product. WSE-3 is a real chip. Their ML research team publishes at NeurIPS, ICLR, and Hot Chips. Inference performance is independently benchmarked and verified. Gordon Bell Prize involvement validates HPC credentials. This is frontier hardware engineering, not a rules engine marketed as AI.

*[Calibration note: Technology score remains 5.0/5 -- the WSE-3 is genuinely frontier. Business reality score is 3.5/5, reflecting sub-peer gross margins (38-41% vs NVIDIA 73%), catastrophic customer concentration, and two withdrawn IPO attempts. See validation/final-calibrated-output.md.]*

### Internal Signal Intelligence

| Source | Rating | Key Signal |
|--------|:------:|-----------|
| **Glassdoor** (57 reviews) | 4.1/5 | 90% recommend. Pros: smart people, good pay. Cons: unreported 2022-2023 layoffs, management in transition, "speed over quality" culture |
| **Blind** (32 reviews) | 3.8/5 | Compensation highest (3.6), management lowest (3.1). Product "right place and time," inference work "extremely fun" |
| **Hacker News** | Polarized | Enthusiasts: "maddest technical accomplishment." Critics: "no MLPerf," "narrow focus," "avoid if you're a founder" |
| **Hiring** | NET POSITIVE | 64-75 open positions across chip design, compiler, ML, systems, DevOps, finance. Active development, not vaporware |

**Morale trajectory: STABLE with CONCERNS.** Engineering morale high. Management confidence mixed (3.1/5 Blind). Unreported 2022-2023 layoffs raise governance transparency questions. Verbal job offers rescinded creates negative employer brand signal. But no 2024-2026 layoffs detected and active hiring indicates growth phase.

*[Cross-dossier calibration note: Employee sentiment weighting for Cerebras (Glassdoor 4.1/5, Blind 3.8/5) is consistent with methodology applied across dossiers. A 4.1 Glassdoor rating is above-average for a ~750-person pre-IPO hardware company. Blind's management rating (3.1/5) reflects platform negativity bias observed across all companies analyzed. Employee sentiment is one signal among many and should not be overweighted relative to financial and technical evidence.]*

*Source: Phase 4 (Claims Validation)*

---

## 7. Academic & IP Landscape

### 7.1 Company Publications

Cerebras maintains an active research presence at top-tier venues:

| Venue | Years | Significance |
|-------|-------|-------------|
| **Hot Chips** | 2019, 2022, 2024 | Premier chip architecture conference. CTO Sean Lie invited talks. |
| **IEEE Micro** | 2023, 2024 | Journal publications from Hot Chips selection |
| **NeurIPS** | 2023, 2024 | Sparsity research (SuPar, Sparse-IFT) |
| **ICML** | 2024 | Sparse-IFT paper |
| **SC (Supercomputing)** | 2022, 2023, 2024 | Gordon Bell Prize activities |

**Key papers:**
- **Cerebras-GPT** (2023): Open compute-optimal LLMs (111M-13B), Chinchilla scaling validation, Apache 2.0 on HuggingFace
- **REAP** (2025): MoE compression via expert activation pruning (247 GitHub stars, NeurIPS)
- **SuPar** (NeurIPS 2024): Sparse training dynamics, up to 11.9% relative loss improvement at 99.2% sparsity
- **Sparse-IFT** (ICML 2024): Drop-in sparse transformations, ResNet-18 +3.5% accuracy without increasing FLOPs

**Scientific computing achievements:**
- Gordon Bell Special Prize 2022 (COVID-19 genomics): awarded to the Argonne National Laboratory research team; Cerebras contributed hardware as a collaborator. *[Calibration note: This validates the chip works but does not validate the business model.]*
- Gordon Bell Prize **FINALIST** (2024, molecular dynamics 457x faster than Frontier supercomputer)
- Gordon Bell finalist **3 consecutive years** (2021-2023)
- DOE Tri-Labs collaboration (LLNL, LANL, SNL)

**State of AI Report 2023:** "Cerebras's chip architecture has the most open-source AI paper citations of any startup."

### 7.2 Research Foundation

Cerebras sits at the intersection of three research traditions:
1. **Wafer-Scale Integration** (1960s-present): Prior failures include Trilogy Systems ($230M, 1980, Gene Amdahl). All failed due to yield. Cerebras solved it with fine-grained redundancy.
2. **Dataflow Architecture** (1970s-present): 900,000 dataflow cores on a single wafer with wavelet-triggered execution. Lineage from Jack Dennis (MIT, 1974).
3. **Sparse Computation** (2015-present): Hardware-accelerated sparsity via SLAC cores. Building on Song Han's Deep Compression (2015) and Lottery Ticket Hypothesis (2018).

### 7.3 Patent Landscape

| Metric | Value |
|--------|-------|
| Total patents globally | 102 |
| Patents granted | 32-34 |
| Active patents | >85% |
| Primary jurisdiction | USA |
| Most-cited patent | US20200005142A1 -- cited by Sony, Intel, IBM, Microsoft, Qualcomm, Micron, Amazon, SambaNova |
| Founding team career patents | ~127+ combined |
| Patent litigation | Rex Computing v. Cerebras (closed May 2025, no adverse outcome); James v. Cerebras (copyright, active) |

**Patent coverage areas:** Accelerated deep learning (dataflow), wafer-scale interconnect, defect tolerance/redundancy, thermal management, power delivery, memory architecture (MemoryX), wavelet routing/communication.

**Competitive comparison:** NVIDIA has 6,234+ AI chip patent applications vs. Cerebras' 102. However, Cerebras operates in a different design space (wafer-scale integration vs. GPU), reducing direct overlap. IFI Claims assessment: "Cerebras appears to be sitting on a valuable invention."

### 7.4 Open-Source Alternatives

**There is no open-source or commercial alternative to wafer-scale integration.** The technology gap is hardware-fundamental, not software-reproducible. Open-source AI accelerator projects (NVDLA, Gemmini, Ztachip) operate at completely different scales. The only production alternatives are NVIDIA GPUs or Google TPUs -- both traditional die-sized chips.

*Source: Phase 5 (Academic & IP Analysis)*

---

## 8. Valuation Signals

### 8.1 Business Model

Cerebras operates a dual-revenue model:

| Revenue Stream | Model | Est. Gross Margin | Est. Mix (2026) |
|----------------|-------|:-----------------:|:---------------:|
| CS-3 System Sales | One-time hardware + support | 25-35% | ~40-50% |
| Cloud Inference (pay-per-token) | Usage-based consumption | 60-75% (est.) | ~30-40% |
| Managed Capacity Deals | Multi-year committed compute | 45-55% (est.) | ~15-25% |
| Professional Services | Engagement-based | 40-50% (est.) | ~5-10% |

The mix shift toward cloud inference and managed capacity is critical for margin expansion. If cloud reaches 60%+ of revenue, blended gross margins can approach 55-65%. If hardware-heavy mix persists at 40%, the business remains capital-intensive and low-margin.

### 8.2 Financial Metrics

| Period | Revenue | Gross Margin | Net Loss | Source | Confidence |
|--------|--------:|:-----------:|:--------:|--------|:----------:|
| FY2022 | $24.6M | 11.7% | $177.7M | S-1 | HIGH |
| FY2023 | $78.7M | 33.5% | $127.2M | S-1 | HIGH |
| H1 2024 | $136.4M | 41.1% | $66.6M | S-1 | HIGH |
| FY2024 (est.) | $272-500M | 37.8% | Unknown | Sacra, StockAnalysis | MEDIUM |
| FY2025 (est.) | $950M-$1.2B | ~45% (est.) | Unknown | PM Insights, TechBuzz | LOW |
| FY2026 (est.) | $2.5-4B | ~45-50% (est.) | Break-even possible | Derived | LOW |

**Gross margin trajectory is the single most important metric for long-term value.** At 38-41%, Cerebras is below every public semiconductor peer:

| Company | Gross Margin | Revenue Multiple |
|---------|:-----------:|:----------------:|
| NVIDIA | 73-75% | ~22x |
| Broadcom | 64% | ~18x |
| AMD | 50% | ~7x |
| Marvell | 48% | ~15x |
| Astera Labs | 74% | ~30x |
| **Cerebras** | **38-41%** | **46-85x** trailing FY2024 / **19-24x** on FY2025 est. |

*[Calibration note: FY2024 revenue is a $272-500M range. $272M is the floor (Sacra estimate, doubling H1 2024). Actual could be up to $499M based on reported growth rates. Valuation multiple range is correspondingly wide (46-85x trailing).]*

### 8.3 Replication Assessment

| Factor | Score (1-4) | Rationale |
|--------|:-----------:|-----------|
| Core Technology (WSE Chip) | **4 -- Near-impossible** | 10 years, $2.55B, 102 patents, TSMC exclusivity |
| Manufacturing (TSMC Relationship) | **4 -- Near-impossible** | 3 process node generations of co-development |
| Software Stack (Compiler + Framework) | **3 -- Hard** | 2-3 years with 20-40 compiler engineers + hardware access |
| Inference API + Cloud Platform | **2 -- Moderate** | 6-12 months, standard patterns |
| SDKs + Developer Tools | **1 -- Easy** | Agent swarm in 2-4 weeks, ~$25-50K |
| Yield/Performance Data | **4 -- Near-impossible** | 8+ years of production data, not purchasable |
| Customer Relationships | **4 -- Near-impossible** | OpenAI, Meta, IBM, DOE -- trust built on unique performance |
| Domain Expertise (Team) | **4 -- Near-impossible** | 5 co-founders with combined ~127 patents, SeaMicro exit |
| **OVERALL** | **3.0 -- Very Hard** | Core moat is physical, not algorithmic. Buy, don't build. *[Calibration note: Downgraded from 3.5 -- original conflated total capital raised ($2.55B) with minimum replication cost; TSMC fabrication access is expensive but not exclusive.]* |

**Full platform replication cost:** $2.0-4.0B over 10-15 years with 700-1,000 engineers. The moat is the chip. The chip cannot be built by agents.

### 8.4 Valuation Framework

| Scenario | FY2026 Revenue | Multiple | Implied Valuation | Key Assumptions |
|----------|:--------------:|:-------:|:-----------------:|----------------|
| **Bear** | $1.5B | 10x | $15B | Margins sub-40%, OpenAI delays, Rubin narrows advantage |
| **Base** | $2.5B | 15x | $37.5B | OpenAI on track, margins reach 45%, diversification progresses |
| **Bull** | $4B | 20x | $80B | Full OpenAI capacity, margins 50%+, Meta/IBM/DOE expand |

**Risk-adjusted (49% cumulative risk haircut):**

| Scenario | Unadjusted | Risk-Adjusted |
|----------|:----------:|:-------------:|
| Bear | $15B | $7.7B |
| Base | $37.5B | $19.1B |
| Bull | $80B | $40.8B |

**Assessment:** The $23B private valuation falls between the risk-adjusted base ($19.1B) and bull ($40.8B) cases. This is reasonably priced for a pre-IPO round. IPO target range: $30-50B (base case), $50-80B (bull case).

*Source: Phase 6 (Valuation & Replication Assessment)*

---

## 9. Confidence Matrix

| Section | Data Quality | Analysis Confidence | Key Gaps |
|---------|:----------:|:-------------------:|----------|
| **Company Profile** | HIGH | HIGH | Employee count range (700-784), not exact |
| **Founding Team** | HIGH | HIGH | Complete team history verified across multiple sources |
| **Funding History** | HIGH | HIGH | All rounds confirmed by Bloomberg, TechCrunch, SEC |
| **Technology Architecture** | HIGH | HIGH | Peer-reviewed (Hot Chips, IEEE Micro), independently verified |
| **Inference Performance** | HIGH | HIGH | Artificial Analysis and W&B independently confirm speed advantage |
| **Revenue (Historical)** | HIGH | HIGH | S-1 SEC filing through H1 2024 |
| **Revenue (FY2024 full year)** | MEDIUM | MEDIUM | Wide range ($272-500M); S-1 only covers H1 |
| **Revenue (FY2025+)** | LOW | MEDIUM | Unaudited estimates; plausible trajectory but unverified |
| **Gross Margin** | HIGH | MEDIUM | S-1 data through H1 2024; volatility (11.7-50.5%) makes trend uncertain |
| **Customer Concentration** | HIGH (historical) | LOW (current) | 87% G42 confirmed for H1 2024; current mix unknown |
| **OpenAI Deal** | HIGH | MEDIUM | Deal confirmed; revenue recognition timing and execution risk uncertain |
| **Market Size (TAM/SAM)** | HIGH | HIGH | Multiple independent research firms converge |
| **Market Size (SOM)** | MEDIUM | MEDIUM | Bottom-up estimate dependent on deal execution |
| **Competitive Landscape** | HIGH | HIGH | NVIDIA-Groq deal and SambaNova-Intel developments are public events |
| **Patent Portfolio** | HIGH | HIGH | GreyB, IFI Claims, Justia independent analyses |
| **Research Publications** | HIGH | HIGH | Peer-reviewed venues (NeurIPS, ICML, IEEE, ACM Gordon Bell) |
| **Claims Validation** | HIGH | HIGH | 12/15 verified or plausible against independent sources |
| **Employee Sentiment** | MEDIUM | MEDIUM | Glassdoor (57 reviews) and Blind (32) are self-selected samples |
| **Valuation Comparables** | HIGH | MEDIUM | Comparable companies are public; Cerebras' forward revenue is uncertain |
| **Replication Assessment** | MEDIUM | HIGH | Hardware replication economics well-understood; software estimates approximate |
| **IPO Timeline** | MEDIUM | LOW | Two prior delays create pattern uncertainty |
| **TSMC Relationship** | MEDIUM | HIGH | Confirmed across 3 chip generations; internal terms unknown |

---

## 10. Risk Register

### Tier 1: Existential Risks (could destroy the investment thesis)

| ID | Risk | Probability | Impact | Trigger | Mitigation |
|----|------|:----------:|:------:|---------|-----------|
| **R1** | **TSMC supply disruption** (Taiwan geopolitical crisis or capacity reallocation) | 5-15% | CATASTROPHIC | Taiwan Strait crisis; TSMC prioritizes NVIDIA/Apple over Cerebras | None available. No alternative foundry for wafer-scale chips. Strategic chip inventory buffer is only short-term mitigation. |
| **R2** | **OpenAI deal failure** (internal chip displaces Cerebras, payment defaults, reduced commitment) | 15-25% | SEVERE | OpenAI custom chip (Broadcom/TSMC 3nm) reaches production; OpenAI financial stress | Customer diversification. Sign 3-5 additional $500M+ deals. Reduce OpenAI to <50% of revenue by 2028. |
| **R3** | **Customer concentration persists** (OpenAI >60% through 2027) | 70% | HIGH | OpenAI ramp dominates revenue while diversification lags | Aggressive enterprise sales expansion. Use IPO currency for strategic customer wins. |

### Tier 2: Strategic Risks (could significantly impair value)

| ID | Risk | Probability | Impact | Trigger | Mitigation |
|----|------|:----------:|:------:|---------|-----------|
| **R4** | **NVIDIA Rubin closes speed gap** to 3-5x (from 20x+) | 60% | HIGH | Rubin production H2 2026 with Groq LPU IP integration | Accelerate WSE-4 development (3nm); maintain memory bandwidth structural advantage; compete on power efficiency and TCO |
| **R5** | **Gross margins stagnate sub-45%** (hardware-heavy revenue mix persists) | 30% | HIGH | Cloud inference adoption slower than projected; system sales dominate | Accelerate cloud inference GTM; structure managed capacity deals at higher margin; optimize manufacturing costs with TSMC |
| **R6** | **IPO delays a third time** (market conditions, regulatory, or financial disclosure issues) | 20% | MEDIUM-HIGH | Market volatility; updated S-1 reveals concerning metrics; CFIUS residual issues | Series H provides 2-3 years runway; can delay without existential impact but erodes credibility |
| **R7** | **Hyperscaler captive silicon reduces TAM** (Google TPU, AWS Trainium, Microsoft Maia, Meta MTIA) | 40% | MEDIUM | Major AI labs build sufficient internal capacity to reduce external chip purchases | Focus on customers who are NOT building custom silicon (OpenAI chose Cerebras over building); positioning as "fast inference for everyone else" |

### Tier 3: Operational Risks (manageable but material)

| ID | Risk | Probability | Impact | Trigger | Mitigation |
|----|------|:----------:|:------:|---------|-----------|
| **R8** | **Data center buildout delays** (6+ new facilities) | 35% | MEDIUM | Construction delays, power contract issues, permitting | Phased buildout; partner with co-location providers (Enovum Montreal); prioritize OpenAI-committed capacity |
| **R9** | **Key person dependency** (Feldman, Lie) | 10% | MEDIUM | CEO/CTO departure or incapacitation | Deep bench of co-founders (5 total); established organizational structure; but Feldman is the face of every major deal |
| **R10** | **Copyright litigation** (James v. Cerebras, Cerebras-GPT training data) | 20% | LOW-MEDIUM | Adverse judgment in Books3/copyright class action | Part of industry-wide wave (74 suits); likely settled or resolved without material impact |
| **R11** | **Developer ecosystem gap** widens vs. NVIDIA CUDA | 50% | MEDIUM | Inference API adoption slows; enterprise customers prefer CUDA ecosystem | Continue OpenAI-compatible API strategy; invest in developer tools (VS Code, MCP, LangChain); hire developer relations team |
| **R12** | **Unreported historical practices surface during IPO** (2022-2023 layoffs, management issues) | 15% | LOW-MEDIUM | Updated S-1 disclosure; media investigation during IPO roadshow | Proactive disclosure in S-1 risk factors; demonstrate current stability (net hiring, improved morale) |

---

## 11. Cross-Phase Narrative & Contradictions

### The Narrative Arc

The data tells a story of a company at an inflection point. Cerebras spent 2016-2023 proving that wafer-scale integration works (Gordon Bell Prizes, Hot Chips presentations, TSMC 3-generation collaboration). It spent 2024 nearly going public but was blocked by the G42/CFIUS controversy. In the 90 days from December 2025 to February 2026, everything changed: NVIDIA secured Groq LPU IP via licensing + asset deal (Dec 24, 2025; Groq continues operating independently -- NVIDIA now has Groq LPU IP for integration into Rubin), OpenAI signed a $10B+ deal (providing revenue certainty), and Tiger Global led a $1B Series H at $23B (tripling the valuation from $8.1B just 5 months earlier).

The company is now in a sprint -- simultaneously building data centers, executing the OpenAI ramp, diversifying customers, improving margins, and preparing for an IPO -- all within a 6-12 month window before NVIDIA Rubin narrows the competitive advantage. Everything must work in parallel. There is no margin for error.

### Key Contradictions and Tensions

**1. AI Reality Score 5.0/5 (tech) / 3.5/5 (business), but no MLPerf submission.**
Across all six phases, the technology is consistently validated as genuine and independently verified. Phase 4 confirmed this with a 5.0/5 technology AI Reality Score (business reality: 3.5/5). Yet the most conspicuous gap is the absence of any MLPerf submission -- the industry-standard benchmark that every major competitor uses. Phase 3 and Phase 4 both flagged this. Possible explanations: (a) MLPerf test conditions may not favor Cerebras' architecture (batch throughput vs. single-stream latency), (b) Cerebras may be withholding to avoid giving NVIDIA a target to benchmark against before Rubin launches, or (c) results may not be as favorable as self-reported numbers under standardized conditions. **This requires direct questioning of management.**

**2. $23B valuation with 38-41% gross margins -- below every semiconductor peer except Intel Gaudi.**
Phase 6 documents that NVIDIA operates at 73-75%, Broadcom at 64%, AMD at 50%, Marvell at 48%. Cerebras at 38-41% is structurally lower. The valuation assumes margins will improve to 45-50%+ as the revenue mix shifts from hardware to cloud. But Phase 2 notes that gross margin volatility (11.7% -> 50.5% -> 37.8%) reflects lumpy hardware deals and customer-specific pricing, making trend extrapolation unreliable. If margins don't improve, the multiple compression needed for public market acceptance will force a painful valuation haircut. **The updated S-1 must show margin expansion to support the IPO price.**

**3. OpenAI $10B deal is transformative, but creates the same structural risk it solves.**
Phase 1 identifies the G42 concentration problem (87% of revenue). Phase 2 projects that OpenAI will be 60-75% of revenue in 2026-2027. Phase 4 confirms the deal is real but flags execution risk (data center buildout, revenue recognition timing, OpenAI's own custom chip development). Phase 6 quantifies this: the SOM is ~65% OpenAI. The company has improved the quality of its concentration risk (US-based marquee brand vs. UAE entity with CFIUS exposure) but not the magnitude. **Customer diversification is the most important post-IPO execution metric.**

**4. NVIDIA Rubin H2 2026 closes the competitive window -- but Cerebras' advantage is structural, not just generational.**
Phase 2 identifies Rubin as the most significant competitive threat (5x inference improvement + Groq LPU IP). Phase 3 notes that the SRAM vs. HBM bandwidth gap (21 PB/s vs. 3.35-8 TB/s) is physics-based and cannot be closed by NVIDIA without wafer-scale integration. Phase 5 confirms no competitor is pursuing WSI. The resolution: Rubin will narrow the speed gap from 20x+ to 3-5x for large models, but the structural memory bandwidth advantage persists. Cerebras' long-term competitive position depends on whether 3-5x speed advantage (with better power efficiency) is sufficient to justify a premium in a Rubin-dominated market.

**5. TSMC sole-source risk is existential but unmitigable.**
Every phase flags this. Phase 1: "No alternative foundry can produce wafer-scale chips." Phase 2: "Taiwan Strait disruption would halt all chip production." Phase 4: "Existential supply chain risk." Phase 5: "TSMC exclusivity" is both a moat and a vulnerability. Phase 6: "Near-impossible to replicate." The contradiction: the same TSMC exclusivity that protects Cerebras from competitors also means Cerebras cannot protect itself from TSMC. There is no hedging strategy. The only mitigation is strategic chip inventory. **This is a binary risk that investors must accept.**

*[Calibration note: TSMC single-source fabrication is an industry-wide dependency shared by Apple, NVIDIA, AMD, and Qualcomm -- not unique to Cerebras. The risk is real but should not be weighted as a company-specific competitive disadvantage.]*

**6. Unreported 2022-2023 layoffs vs. current hiring (64-75 open positions).**
Phase 4 surfaced Glassdoor reviews reporting "mass layoffs in 2022 and 2023 that are not reported." TrueUp confirms a Jan 2023 layoff. Yet the company currently has 700-784 employees and 64-75 open positions. The timeline aligns with the G42-dependent period (before diversification) and possibly a hardware design cycle transition (WSE-2 to WSE-3). The concern is not the layoffs themselves (normal for hardware companies) but the lack of public disclosure. For an IPO-bound company, this is a governance transparency issue that will likely surface during SEC review.

**7. "Last independent NVIDIA alternative" -- scarcity premium or last man standing?**
Phase 4 rates this claim as PLAUSIBLE but an overstatement (Tenstorrent exists). The framing can be read two ways: (a) Cerebras has unique scarcity value for investors seeking NVIDIA diversification -- a bull case driver; or (b) every other independent AI chip company has been acquired or failed, suggesting the standalone model is structurally unviable -- a bear case signal. NVIDIA secured Groq LPU IP via licensing + asset deal for $20B (Dec 24, 2025; Groq continues operating independently); Intel's SambaNova term sheet (~$1.6B) stalled and SambaNova is raising $350-500M independently. Cerebras rejected NVIDIA's acquisition approach. The question: is Cerebras the survivor or the holdout? **The IPO outcome will determine which narrative prevails.**

**8. IPO delayed twice already (CFIUS + G42) -- third time's the charm or pattern?**
Phase 1 documents: S-1 filed Sep 2024, CFIUS delayed Oct 2024, S-1 withdrawn Oct 2025, Series G raised instead, then Series H in Feb 2026 described as "pre-IPO round." Phase 4 rates the Q2 2026 IPO as PLAUSIBLE with MEDIUM confidence, noting the "boy who cried wolf" dynamic. Phase 6 notes that private capital remains available ($2.55B raised, 2-3 years runway). The company can afford another delay but cannot afford the credibility erosion. **Each delay makes the next IPO filing harder to take seriously on Wall Street.**

---

## 12. Recommended Next Steps

### 12.1 Priority Due Diligence Questions (for Direct Management Engagement)

**Financial (ask CFO / finance team):**
1. What is FY2025 actual revenue and gross margin by revenue stream (system sales vs. cloud inference vs. managed capacity)?
2. What is the OpenAI deal's revenue recognition schedule? What triggers payment milestones?
3. What is the current customer concentration breakdown? Specifically, what percentage is OpenAI, Meta, IBM, DOE, and other customers?
4. What is the cloud inference gross margin vs. system sale gross margin? What is the target blended gross margin for the IPO filing?
5. What is the fully-loaded CapEx budget for the 6+ data center buildout through 2028?

**Technical (ask CTO Sean Lie):**
6. Why has Cerebras never submitted to MLPerf? Is there a plan to submit before the IPO?
7. What is the WSE-4 timeline? Will it be on TSMC 3nm? What yield engineering is required for wafer-scale at 3nm?
8. What is the actual WSE-3 defect density and redundancy utilization rate at TSMC 5nm?
9. What is the largest model that has been trained entirely on Cerebras hardware (not just inference)?
10. How does Cerebras plan to maintain speed advantage after NVIDIA Rubin integrates Groq LPU IP?

**Strategic (ask CEO Andrew Feldman):**
11. What is the IPO timeline and price target? What would cause another delay?
12. What is the customer diversification strategy? How many $500M+ deals are in pipeline beyond OpenAI?
13. What is the relationship with OpenAI's internal chip program (Broadcom/TSMC 3nm)? Is there a contractual minimum commitment that survives OpenAI's custom silicon buildout?
14. Has NVIDIA made an acquisition approach? Would the board consider it?
15. What is the TSMC capacity allocation for 2026-2027? Are there any constraints on WSE-3 production volume?

### 12.2 Areas Requiring Deeper Technical Review

| Area | What to Investigate | Estimated Cost | Recommended Approach |
|------|-------------------|:--------------:|---------------------|
| **Independent inference benchmarking** | Run standardized benchmarks (MLPerf-equivalent) on Cerebras vs. NVIDIA Blackwell B200 | $50-100K | Engage independent benchmarking firm (e.g., MLCommons, Artificial Analysis deep dive) |
| **TSMC supply chain risk modeling** | Model Cerebras' TSMC wafer allocation under various Taiwan scenarios | $25-50K | Engage semiconductor supply chain analyst (e.g., SemiAnalysis, TrendForce) |
| **OpenAI deal structure analysis** | Review contract terms, payment triggers, termination clauses, capacity commitments | $50-100K (legal) | Legal review of any available deal documentation; financial modeling of revenue recognition scenarios |
| **Patent freedom-to-operate** | Assess Cerebras' FTO position and vulnerability to NVIDIA counter-claims | $75-150K (IP law) | Engage patent litigation firm with semiconductor expertise |
| **Updated S-1 financial analysis** | Deep dive on FY2025 financials when updated S-1 is filed | $25-50K | Engage financial analyst or investment bank IPO team |

### 12.3 Timeline

| Milestone | Expected Date | Action Required |
|-----------|:------------:|-----------------|
| Updated S-1 filing | Q1 2026 (imminent) | Monitor SEC EDGAR for Cerebras filing. This is the single most important data point. |
| Management engagement | Within 2 weeks | Schedule calls with CEO, CTO, and CFO using questions from 12.1 |
| Independent benchmarking | 4-6 weeks | Commission inference benchmarking if proceeding past management engagement |
| IPO roadshow | Q2 2026 (est.) | Attend roadshow presentations; compare management claims to this report |
| IPO pricing | Q2 2026 (est.) | Final investment decision based on IPO price relative to risk-adjusted valuation range ($19-41B) |
| NVIDIA Rubin launch | H2 2026 | Monitor competitive impact on Cerebras' speed advantage and customer retention |

### 12.4 Decision Framework

| Condition | Action |
|-----------|--------|
| Updated S-1 shows FY2025 revenue >$800M, gross margin >43%, OpenAI concentration <70% | **STRONG BUY** at IPO price up to $40B |
| Updated S-1 shows FY2025 revenue $500-800M, gross margin 40-43%, concentration >70% | **CAUTIOUS BUY** at IPO price up to $25B |
| Updated S-1 shows FY2025 revenue <$500M, gross margin <40%, concentration >80% | **PASS** -- valuation at $23B+ is not supported |
| IPO delayed again beyond Q3 2026 | **RE-EVALUATE** -- pattern of delays indicates execution problems |
| NVIDIA Rubin benchmarks show <3x speed gap vs. Cerebras | **DOWNGRADE** -- core value proposition materially weakened |

**MANDATORY NEXT STEP:** Customer reference calls -- specifically with at least 2 non-G42, non-OpenAI customers -- are required before any capital commitment. The customer concentration narrative has changed names but not structure.

---

## Appendix A: Master Source Index

### Phase 1 (Discovery) — Primary Sources
- [SEC S-1 Filing](https://www.sec.gov/Archives/edgar/data/2021728/000162828024041596/cerebras-sx1.htm)
- [Bloomberg: $1B Series H at $23B](https://www.bloomberg.com/news/articles/2026-02-04/cerebras-raises-1-billion-in-funding-at-23-billion-valuation)
- [CNBC: OpenAI $10B Deal](https://www.cnbc.com/2026/01/14/cerebras-scores-openai-deal-worth-over-10-billion.html)
- [TechCrunch: Benchmark $225M](https://techcrunch.com/2026/02/06/benchmark-raises-225m-in-special-funds-to-double-down-on-cerebras/)
- [Tom's Hardware: WSE-3 Specs](https://www.tomshardware.com/tech-industry/artificial-intelligence/cerebras-launches-900000-core-125-petaflops-wafer-scale-processor-for-ai-theoretically-equivalent-to-about-62-nvidia-h100-gpus)

### Phase 2 (Market) — Key Sources
- [Omdia: AI Data Center Chip Market $286B by 2030](https://omdia.tech.informa.com/pr/2025/aug/ai-data-center-chip-market-to-hit-286bn-growth-likely-peaking-as-custom-asics-gain-ground)
- [Deloitte: 2026 Semiconductor Outlook](https://www.deloitte.com/us/en/insights/industry/technology/technology-media-telecom-outlooks/semiconductor-industry-outlook.html)
- [Bloomberg Intelligence: AI Accelerator Market](https://www.bloomberg.com/company/press/ai-accelerator-market-looks-set-to-exceed-600-billion-by-2033-driven-by-hyperscale-spending-and-asic-adoption-according-to-bloomberg-intelligence/)
- [Fortune: AI Chip Consolidation](https://fortune.com/2026/01/05/nvidia-groq-deal-ai-chip-startups-in-play/)

### Phase 3 (Technical) — Key Sources
- [Hot Chips 2024: WSE-3 Architecture](https://hc2024.hotchips.org/assets/program/conference/day2/72_HC2024.Cerebras.Sean.v03.final.pdf)
- [IEEE Micro: Cerebras Architecture Deep Dive](https://ieeexplore.ieee.org/document/10123162/)
- [arXiv: WSE vs GPU Comparison](https://arxiv.org/html/2503.11698v1)
- [Cerebras CSoft](https://www.cerebras.ai/product-software)
- [PyPI: cerebras-cloud-sdk](https://pypi.org/project/cerebras-cloud-sdk/)

### Phase 4 (Claims) — Key Sources
- [Artificial Analysis: Cerebras Provider](https://artificialanalysis.ai/providers/cerebras)
- [W&B: Cerebras Fastest LLM Provider?](https://wandb.ai/capecape/benchmark_llama_70b/reports/Is-the-new-Cerebras-API-the-fastest-LLM-service-provider---Vmlldzo5MTQ4OTM2)
- [Glassdoor: Cerebras Reviews](https://www.glassdoor.com/Reviews/Cerebras-CA-Reviews-E1821335.htm)
- [Blind: Cerebras Reviews](https://www.teamblind.com/company/Cerebras-Systems/reviews)
- [HN: Avoid Cerebras](https://news.ycombinator.com/item?id=46707904)

### Phase 5 (Academic/IP) — Key Sources
- [GreyB: Cerebras Patents](https://insights.greyb.com/cerebras-systems-patents/)
- [IFI Claims: Challenging NVIDIA](https://www.ificlaims.com/news/ifi-insights-challenging-nvidia-examining-the-patents-of-an-emerging-ai-chip-company/)
- [Cerebras Publications](https://www.cerebras.ai/publications)
- [ACM Gordon Bell Prize](https://awards.acm.org/bell)
- [Sandia: Fastest Molecular Dynamics](https://www.sandia.gov/labnews/2024/10/03/sandia-led-collaboration-achieves-one-of-worlds-fastest-molecular-dynamics-simulations/)

### Phase 6 (Valuation) — Key Sources
- [Sacra: Cerebras Revenue](https://sacra.com/c/cerebras-systems/)
- [StockAnalysis: CBRS](https://stockanalysis.com/stocks/cbrs/revenue/)
- [PM Insights: Cerebras Valuation](https://www.pminsights.com/companies/cerebras-systems)
- [NVIDIA FY2025 Results](https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-fourth-quarter-and-fiscal-2025)
- [Cerebras S-1 Breakdown (Tanay Jaipuria)](https://www.tanayj.com/p/cerebras-s-1-breakdown)

---

## Appendix B: Glossary

| Term | Definition |
|------|-----------|
| **WSE** | Wafer-Scale Engine -- Cerebras' monolithic chip using entire 300mm silicon wafer |
| **SRAM** | Static Random-Access Memory -- fast on-chip memory (21 PB/s on WSE-3) |
| **HBM** | High Bandwidth Memory -- off-chip memory used by GPUs (3.35-8 TB/s) |
| **MemoryX** | Cerebras' external weight storage system for models exceeding on-chip SRAM |
| **SwarmX** | Cerebras' interconnect fabric between MemoryX and CS-3 systems |
| **CSoft** | Cerebras Software Platform (compiler, runtime, framework) |
| **CSL** | Cerebras Software Language -- domain-specific language for WSE programming |
| **CGC** | Cerebras Graph Compiler -- maps neural networks to 900K cores |
| **CFIUS** | Committee on Foreign Investment in the United States |
| **MLPerf** | Industry-standard ML performance benchmark maintained by MLCommons |
| **tok/s** | Tokens per second -- standard inference speed metric |
| **NRR** | Net Revenue Retention -- not directly applicable to hardware (SaaS metric) |

---

*Generated by Dossier v0.1.0 -- automated SaaS due diligence engine*
*7-phase analysis: Discovery, Market, Technical, Claims Validation, Academic/IP, Valuation, Report Assembly*
*Data collected: 2026-02-19*
*All confidence levels noted per section. Low-confidence areas are clearly marked.*
*This report is based on publicly available information and automated analysis. It does not constitute investment advice.*

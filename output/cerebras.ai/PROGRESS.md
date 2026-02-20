# Dossier: cerebras.ai
Started: 2026-02-19
Iteration: 0

## Phases
- [x] P1 Discovery — COMPLETE (2026-02-19)
- [x] P2 Market — COMPLETE (2026-02-19)
- [x] P3 Technical — COMPLETE (2026-02-19)
- [x] P4 Claims — COMPLETE (2026-02-19)
- [x] P5 Academic — COMPLETE (2026-02-19)
- [x] P6 Valuation — COMPLETE (2026-02-19)
- [x] P7 Report — COMPLETE (2026-02-19)

## Blockers
- WebFetch denied — used WebSearch as fallback (adequate for discovery)
- Bash denied — could not run dig/whois/nslookup for DNS details
- .ai WHOIS data limited (registrars no longer show registration dates for .ai domains)

## P1 Discovery Summary
- **Legal Name:** Cerebras Systems, Inc. (Sunnyvale, CA)
- **Founded:** March 2016 by 5 co-founders from SeaMicro (AMD acquisition, $334M)
- **CEO:** Andrew Feldman (Stanford BA/MBA)
- **Employees:** ~700-784
- **Total Funding:** $2.55B across 8 rounds (Series A through H)
- **Latest Round:** Series H, $1B at $23B valuation (Feb 2026, led by Tiger Global)
- **Benchmark:** $225M via two SPVs ("Benchmark Infrastructure"), originally led Series A in 2016
- **AMD:** First investment in Series H — notable given SeaMicro acquisition history
- **Core Product:** WSE-3 (4T transistors, 900K cores, 44GB SRAM, TSMC 5nm, full 300mm wafer)
- **Cloud Service:** Cerebras Inference — OpenAI-compatible API, 20x+ faster than GPU inference
- **Key Deals:** OpenAI $10B+ (750MW through 2028), Meta Llama API, IBM, U.S. DOE
- **IPO:** NASDAQ CBRS, Q2 2026 expected. S-1 filed Sep 2024, withdrawn Oct 2025 after CFIUS delay
- **Critical Risk:** TSMC sole-source dependency; historical G42 revenue concentration (87% H1 2024, now diversifying)
- **Competitive:** NVIDIA secured Groq LPU IP via licensing + asset deal (Dec 24, 2025; Groq continues operating independently); Intel/SambaNova term sheet stalled (SambaNova remains independent). Cerebras is leading independent alternative to NVIDIA.

## P2 Market Summary
- **TAM:** $286B AI data center chips by 2030 (Omdia); $500B gen AI chips in 2026 (Deloitte)
- **SAM:** $50B+ inference-optimized chips in 2026; $104B ASIC/inference segment by 2030
- **SOM:** $3-5B by 2027 (dominated by OpenAI $10B deal phased over 3 years)
- **Competitive field consolidating:** Groq ($20B NVIDIA), SambaNova (~$1.6B Intel), Intel Gaudi (<1% share). Cerebras is last independent NVIDIA alternative at scale.
- **NVIDIA 90%+ market share** in AI accelerators. Rubin (H2 2026) = 5x inference improvement over Blackwell, integrates Groq LPU IP. Key competitive threat.
- **Inference market shift:** 50% of compute (2025) → 67% (2026) → 80% (long-term). Strongest secular tailwind for Cerebras.
- **Gross margins:** 41.1% (H1 2024), improving from 11.7% (2022). Below NVIDIA 70%+. Mix shift to cloud inference critical.
- **6-12 month window:** Before NVIDIA Rubin production ramp (H2 2026-H1 2027), Cerebras has maximum competitive advantage. OpenAI deal, Meta, and IPO must execute during this window.
- **Customer concentration persists:** G42 (87%, H1 2024) replaced by OpenAI (est. 60-75%, 2026-2027). Directionally better but still concentrated.
- **OpenAI internal chip threat:** Custom chip with Broadcom/TSMC 3nm targeting mass production 2026. Long-term risk to $10B deal value.

## P3 Technical Summary
- **GitHub:** 21 public repos across 2 orgs (Cerebras, CerebrasResearch). ~1,990 total stars. Python dominant.
- **SDK quality:** Enterprise-grade. Stainless-generated (same as OpenAI/Anthropic). Python SDK at v1.67.0, 1.14M PyPI downloads/month. Node SDK at v1.64.1. Both have CI, tests, SECURITY.md, CHANGELOG.
- **API design:** OpenAI-compatible drop-in replacement. Free tier 1M tokens/day. Integrations: Vercel AI SDK, LangChain, Cloudflare AI Gateway, AWS Marketplace.
- **Architecture moat:** WSE-3 = 44GB SRAM at 21 PB/s bandwidth vs. GPU HBM at 3.35-8 TB/s. 1,000x memory bandwidth advantage. 100% yield via 0.05mm² core design + dynamic routing + 1-1.5% redundant cores.
- **Inference benchmarks:** 2.5x-75x faster than GPUs depending on model size. Self-reported but physics-grounded. No independent MLPerf submission.
- **Software stack:** CSoft Graph Compiler maps neural networks to 900K cores automatically. CSL (Cerebras Software Language) for HPC users. cerebras.pytorch for ML training. Inference API for cloud developers.
- **MemoryX/SwarmX:** Weight streaming for models >44GB. Elastic 4TB-2.4PB memory. Near-linear scaling across up to 192 CS-3 systems.
- **Research:** NeurIPS 2024/2025, ICLR 2025, Hot Chips 2024. REAP (247 stars). DOE Tri-Labs collaboration.
- **Weakness:** Modelzoo (1,125 stars) has 26 open issues with 0 comments. Community PRs unreviewed. No developer Discord/Slack. Missing licenses on 3 repos. Open-source is adoption funnel, not community ecosystem.
- **Developer tools:** VS Code extension, MCP server (Claude Code/Cursor/Cline), inference cookbook, 14 integration examples.

## P4 Claims Validation Summary
- **Claims accuracy:** 12/15 verified or plausible. Pattern: OPTIMISTIC but not misleading.
- **AI reality score:** 5/5 — genuine deep-tech hardware company with peer-reviewed research and independent benchmarks.
- **Shadow Prediction Market:** 11 sources searched (Glassdoor, Blind, Reddit, HN, LinkedIn, layoff trackers, arXiv, Twitter/X, job boards, Product Hunt, G2/analyst).
- **Glassdoor:** 4.1/5 (57 reviews), 90% recommend. Pros: smart people, good pay. Cons: management in transition, "speed over quality," unreported 2022-2023 layoffs.
- **Blind:** 3.8/5 (32 reviews). Management lowest at 3.1/5. Inference work "extremely fun." Interview process complaints (verbal offers rescinded).
- **Hacker News:** Polarized. Enthusiasts vs "imminent collapse" critics. "Tell HN: Avoid Cerebras" (enterprise customer kicked off, told to use Groq). No MLPerf submission flagged.
- **4 CRITICAL gaps:** (1) No MLPerf submission, (2) OpenAI deal revenue timing unknown, (3) Customer diversification unverified, (4) Enterprise customer churn signals.
- **6 NOTABLE gaps:** (5) "Last independent" overstatement, (6) Cherry-picked speed comparisons, (7) TSMC sole-source risk, (8) Unreported layoffs, (9) CUDA ecosystem gap, (10) IPO delay pattern.
- **Benchmark credibility:** Independently verified by Artificial Analysis (#1 fastest provider), W&B, and 3 AWS Marketplace reviews. But MLPerf absence is conspicuous.
- **Morale:** STABLE with CONCERNS. Engineering morale high. Management confidence mixed. Rapid growth creating organizational strain. Net hiring (64-75 open positions).

## P5 Academic & IP Summary
- **Patent portfolio:** 102 patents globally (34 granted, >85% active). 37 USPTO applications, 22 granted. Primary class: G06F (Computing/Calculating).
- **Most-cited patent:** US20200005142A1 (Accelerated Deep Learning) — cited by Sony, Intel, IBM, Microsoft, Qualcomm, Micron, Amazon, SambaNova.
- **IFI Claims assessment:** "Cerebras appears to be sitting on a valuable invention." Quality citations despite small portfolio (102 vs NVIDIA's 6,234+).
- **Key patent families:** Dataflow architecture, wafer-scale interconnect (scribe-line repurposing), defect tolerance/redundancy, thermal management (23-26 kW/wafer), power delivery (300+ distributed VRMs), MemoryX weight streaming.
- **Inventor depth:** Sean Lie (29 patents), Gary Lauterbach (68 career), Jean-Philippe Fricker (30 career). Combined ~127+ patents across founding team careers.
- **Litigation:** Rex Computing v. Cerebras (2021-2025, closed, no adverse outcome). James v. Cerebras (copyright/Books3, active, class action).
- **Publication record:** 3 Hot Chips talks (2019/2022/2024), 2 IEEE Micro papers, NeurIPS/ICML papers, 10+ arXiv papers. Gordon Bell Prize winner (2022) and finalist (2024).
- **Sparsity research:** 4 papers (Sparse-IFT, SuPar, High-Sparsity Llama, REAP). Genuine HW/SW co-design, not just hardware marketing.
- **Scientific computing:** Partnerships with Argonne, Sandia, LLNL, LANL, NETL, DOE. 457x-748x faster than Frontier supercomputer on molecular dynamics.
- **Open-source alternatives:** NONE for wafer-scale integration. Gap is hardware-fundamental, not software-reproducible. Open-source AI accelerators (NVDLA, Gemmini) operate at completely different scales.
- **Build-vs-buy:** Cannot replicate. $2.55B invested, 10 years R&D, sole TSMC relationship. Only alternatives are NVIDIA GPUs or Google TPUs (traditional die-sized chips).

## Corrections Pass (2026-02-19)

Applied calibration corrections from `validation/final-calibrated-output.md`:

- **COR-001/002:** AI Reality Score split from 5/5 to 5.0/5 (tech) / 3.5/5 (business) — in 07-report.md, executive-summary.md
- **COR-003/004/005:** Build vs Buy downgraded from 3.5/4 to 3.0/4 — in 07-report.md, executive-summary.md, 06-valuation.md
- **COR-006/007:** Verdict downgraded from STRONG CANDIDATE to QUALIFIED CANDIDATE — in 07-report.md, executive-summary.md
- **COR-008–012:** NVIDIA-Groq corrected from "Jan 2026 acquisition" to "Dec 24, 2025 licensing + asset deal; Groq continues operating independently" — in 01-discovery.md, 02-market.md, 05-academic.md, 06-valuation.md, 07-report.md
- **COR-013/014:** Gordon Bell Prize attribution corrected: awarded to Argonne National Lab team; Cerebras contributed hardware as collaborator — in 05-academic.md, 07-report.md
- **COR-015:** FY2024 revenue range explicitly noted as $272-500M with corresponding multiple range (46-85x trailing) — in 06-valuation.md, 07-report.md
- **COR-016:** Gross margin caution note added: 45-50% projection unproven at scale — in 02-market.md
- **COR-017:** TSMC risk context added: industry-wide dependency, not Cerebras-specific — in 07-report.md
- **COR-058:** Employee sentiment weighting calibrated with cross-dossier methodology note — in 07-report.md
- **COR-059:** NRR BLOCKING DATA GAP section added — in executive-summary.md
- **COR-060:** Customer reference calls MANDATORY next step added — in 07-report.md

Previously applied (skipped):
- SambaNova "acquired" → "term sheet stalled" — already in exec-summary, 02-market, 07-report, PROGRESS

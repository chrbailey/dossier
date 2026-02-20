# Phase 5: Academic & IP Analysis — Cerebras Systems

**Date:** 2026-02-19
**Analyst:** Dossier Pipeline (automated)
**Confidence Level:** HIGH — Cerebras is a hardware company with extensive published research, multiple patent families, conference presentations at top venues, and an S-1 filing with IP disclosures.

---

## 1. Company Publications

Cerebras maintains an official publications page ([cerebras.ai/publications](https://www.cerebras.ai/publications)) and has built a substantial research corpus spanning hardware architecture, sparsity, LLM training, and scientific computing.

### 1.1 Peer-Reviewed & Conference Papers

| Title | Authors | Year | Venue | Significance |
|-------|---------|------|-------|-------------|
| **Cerebras Architecture Deep Dive: First Look Inside the HW/SW Co-Design for Deep Learning** | Sean Lie | 2022/2023 | Hot Chips 34 / IEEE Micro Vol. 43 No. 3 (May/Jun 2023) | First detailed public disclosure of WSE architecture — dataflow cores, SRAM design, routing fabric. IEEE Micro invited paper from Hot Chips selection. |
| **Inside the Cerebras Wafer-Scale Cluster** | Sean Lie | 2024 | IEEE Micro Vol. 44 No. 3 | Describes MemoryX (external weight storage), SwarmX (broadcast-reduce fabric), and how cluster achieves exaFLOP-scale with pure data parallelism — no model parallelism needed. |
| **Cerebras Wafer-Scale AI** | Sean Lie | 2024 | Hot Chips 2024 (HC36) | WSE-3 architecture presentation — 900K cores, 44GB SRAM, inference performance (1,800 tok/s on Llama 3.1 8B). |
| **Cerebras-GPT: Open Compute-Optimal Language Models Trained on the Cerebras Wafer-Scale Cluster** | Nolan Dey et al. (8 authors) | 2023 | arXiv:2304.03208 | Family of 7 open models (111M-13B params) trained following Chinchilla scaling laws. First open reproduction of compute-optimal training. Apache 2.0 licensed. Models on HuggingFace. |
| **Sparse-IFT: Sparse Iso-FLOP Transformations for Maximizing Training Efficiency** | Cerebras Research team | 2023/2024 | ICML 2024 (NeurIPS 2024 per some listings) | Drop-in sparse layer replacements that improve accuracy without increasing FLOPs. ResNet-18 +3.5%, GPT-3 Small -0.4 PPL. Code open-sourced on GitHub. |
| **Sparse Maximal Update Parameterization (SuPar): A Holistic Approach to Sparse Training Dynamics** | Cerebras Research team | 2024 | NeurIPS 2024 (arXiv:2405.15743) | Ensures activations, gradients, and weight updates scale independently of sparsity level. Up to 11.9% relative loss improvement at 99.2% sparsity. 4.1x compute efficiency gain via Chinchilla scaling law. |
| **Enabling High-Sparsity Foundational Llama Models with Efficient Pretraining and Deployment** | Abhinav Agarwalla, Cerebras + Neural Magic | 2024 | arXiv:2405.03594 | 70% sparsity Llama-2 7B with full accuracy recovery. 3x inference speedup on CPUs, 8.6x with sparse-quantized models. Training on CS-3 matches theoretical sparsity scaling. |
| **REAP: Router-weighted Expert Activation Pruning for SMoE Compression** | Cerebras Research | 2025 | arXiv:2510.13999 | One-shot MoE compression method. Prunes 50% of experts with near-lossless accuracy on code generation. Applied to DeepSeek-V3, Qwen3-Coder, Kimi models. Open-sourced code + pruned checkpoints on HuggingFace. |
| **Massively Distributed Finite-Volume Flux Computation** | Ryuichi Sai et al. | 2023 | arXiv:2304.11274 | CFD stencil operations on WSE architecture. Evaluates viability of matrix-free finite-volume operators on Cerebras hardware. |
| **Benchmarking the Performance of Large Language Models on the Cerebras Wafer Scale Engine** | External authors | 2024 | arXiv:2409.00287 | Independent benchmarking of LLMs on WSE-2 (850K cores, 40GB SRAM). Evaluates SLAC (Sparse Linear Algebra Compute) cores. |

### 1.2 Scientific Computing Collaborations (Peer-Reviewed / Award-Nominated)

| Collaboration | Partners | Year | Achievement | Source |
|--------------|----------|------|-------------|--------|
| **Gordon Bell Special Prize (COVID-19)** | Argonne National Lab, Caltech, Harvard, U. Chicago, NVIDIA, Cerebras (34-author team) | 2022 | Gordon Bell Prize 2022 was awarded to the Argonne National Laboratory research team; Cerebras contributed hardware as a collaborator. *[Calibration note: This validates the chip works but does not validate the business model.]* | [ACM Awards](https://awards.acm.org/bell) |
| **Molecular Dynamics on WSE-2** | Sandia, LLNL, LANL, Cerebras | 2024 | **Gordon Bell Prize Finalist** — 457x faster than Frontier exascale supercomputer. 699,000 timesteps/sec for 800K tantalum atoms. | [Sandia](https://www.sandia.gov/labnews/2024/10/03/sandia-led-collaboration-achieves-one-of-worlds-fastest-molecular-dynamics-simulations/) |
| **Molecular Dynamics World Record** | Cerebras + national labs | 2024 | 1.1 million simulations/sec — 748x faster than Frontier | [Cerebras PR](https://www.cerebras.ai/press-release/cerebras-sets-new-world-record-in-molecular-dynamics-at-1.1-million-simulations-per-second-748x-faster-than-the-worlds-1-supercomputer-frontier) |
| **Stream-AI-MD (Protein Folding)** | Argonne National Lab, Cerebras | 2023 | Deep learning-driven adaptive MD — 50x time-to-solution improvement for BBA protein folding | [LLNL](https://www.llnl.gov/article/52081/nnsa-researchers-break-molecular-dynamics-timescale-barrier-worlds-largest-chip) |
| **CFD / Field Equations** | NETL (Nat'l Energy Technology Lab) | 2022-2023 | CS-2 was 470x faster than NETL's Joule Supercomputer on field equation modeling | [Cerebras](https://www.cerebras.ai/industry-scientific-computing) |
| **Epigenomic Language Models** | GSK (GlaxoSmithKline) | 2021 | Pre-trained complex epigenomic models on CS-1 previously considered too large to train | [arXiv:2112.07571](https://arxiv.org/abs/2112.07571) |

### 1.3 Conference Presence Summary

| Venue | Years | Presentation Type |
|-------|-------|------------------|
| **Hot Chips** (premier chip architecture) | 2019 (HC31), 2022 (HC34), 2024 (HC36) | Invited talks by CTO Sean Lie |
| **IEEE Micro** (journal) | 2023, 2024 | Two invited papers (from Hot Chips selection) |
| **NeurIPS** | 2023, 2024 | Workshop talks (sparsity), poster sessions (SuPar, Sparse-IFT) |
| **ICML** | 2024 | Sparse-IFT paper |
| **SC (Supercomputing)** | 2022, 2023, 2024 | Gordon Bell Prize activities, national lab collaborations |
| **arXiv** | 2021-2025 | 10+ papers |

---

## 2. Research Foundation

### 2.1 Core Technology Lineage

Cerebras' Wafer-Scale Engine sits at the intersection of three research traditions:

**Wafer-Scale Integration (WSI) — 1960s-present:**
The idea of using an entire silicon wafer as a single chip dates to the 1960s. Notable prior failures include **Trilogy Systems** (Gene Amdahl, 1980, $230M invested, failed due to yield problems) and efforts by Texas Instruments and ITT Corporation in the 1970s-80s. All prior WSI attempts failed because defect rates made whole-wafer yield impossible. Cerebras' breakthrough is engineering around this: fine-grained redundancy (1% spare cores), dynamic routing around defects, and 100x greater defect tolerance than GPUs. The WSE is now displayed at the **Computer History Museum** as a milestone achievement.

**Dataflow Architecture — 1970s-present:**
The WSE uses fine-grained dataflow compute cores rather than the von Neumann model used by GPUs/CPUs. Each core is a small (38,000 um^2) independent processor with 48KB local SRAM, running at 1.1 GHz and consuming only 30mW. The dataflow paradigm — where execution is triggered by data availability rather than program counters — traces to Jack Dennis (MIT, 1974) and the Manchester Dataflow Machine. Cerebras' implementation is novel: 900,000 dataflow cores on a single wafer with a 2D mesh interconnect.

**Sparse Computation — 2015-present:**
Cerebras has invested heavily in hardware-accelerated sparsity. The WSE's SLAC (Sparse Linear Algebra Compute) cores natively skip multiply-by-zero operations. This is architecturally distinct from GPUs, which waste cycles on zeros in sparse matrices. The academic foundation includes work by Song Han (MIT, "Deep Compression," 2015) and the Lottery Ticket Hypothesis (Frankle & Carlin, 2018). Cerebras has extended this with SuPar, Sparse-IFT, and high-sparsity LLM pretraining.

### 2.2 Seminal Papers That Define the Approach

| Paper | Authors | Year | Relevance to Cerebras |
|-------|---------|------|----------------------|
| Manchester Dataflow Machine | Gurd, Kirkham, Watson | 1985 | Foundational dataflow architecture concept |
| Deep Compression | Song Han et al. (Stanford) | 2015 | Proved neural network sparsity viable |
| Lottery Ticket Hypothesis | Frankle & Carlin (MIT) | 2018 | Theoretical basis for sparse training |
| Chinchilla: Training Compute-Optimal LLMs | Hoffmann et al. (DeepMind) | 2022 | Scaling laws Cerebras used for Cerebras-GPT |
| Maximal Update Parameterization (muP) | Yang et al. (Microsoft) | 2022 | Hyperparameter transfer across model scales — adopted by Cerebras |

---

## 3. Patent Landscape

### 3.1 Portfolio Overview

| Metric | Value | Source |
|--------|-------|--------|
| **Total patents globally** | 102 | [GreyB/Insights;Gate](https://insights.greyb.com/cerebras-systems-patents/) |
| **Patents granted** | 32-34 | [GreyB](https://insights.greyb.com/cerebras-systems-patents/) |
| **Active patents** | >85% of portfolio | [GreyB](https://insights.greyb.com/cerebras-systems-patents/) |
| **USPTO applications** | 37 (excl. Design/PCT) | [GreyB](https://insights.greyb.com/cerebras-systems-patents/) |
| **USPTO grants** | 22 | [GreyB](https://insights.greyb.com/cerebras-systems-patents/) |
| **Primary jurisdiction** | USA, followed by Europe and Japan | [GreyB](https://insights.greyb.com/cerebras-systems-patents/) |
| **Primary CPC class** | G06F (Computing/Calculating) — 82 patents | [GreyB](https://insights.greyb.com/cerebras-systems-patents/) |
| **Trademarks** | 5 registered (Scientific/Electric class) | [GreyB](https://insights.greyb.com/cerebras-systems-patents/) |

### 3.2 Key Patent Families

| Patent | Title | Inventors | Year | Cited By | Key Claims |
|--------|-------|-----------|------|----------|------------|
| **US20200005142A1 / US10,699,189** | Accelerated Deep Learning | Cerebras team | 2018/2020 | 8 citations (Sony, Intel, IBM) | Array of processing elements with flow-based wavelet computations, 2D mesh routing, SGD/mini-batch training on wafer-scale fabric. **Most-cited patent in portfolio.** |
| **US10,777,532** | Apparatus and Method for Multi-Die Interconnection | Jean-Philippe Fricker et al. | 2019 | — | Die-to-die connections extending between adjacent pairs of die on wafer. Scribe-line repurposing for inter-die communication with same-bandwidth-as-intra-die connectivity. |
| **US11,328,207** | Scaled Compute Fabric for Accelerated Deep Learning | Gary Lauterbach, Srikanth Arekapudi, Michael James, Sean Lie, Michael Morrison | 2022 | — | Scalable compute fabric architecture for deep learning acceleration with distributed memory. |
| **US10,242,891** | Apparatus and Method for Securing Components of an Integrated Circuit | Cerebras team | 2019 | — | Physical securing of wafer-scale components — thermal and mechanical integrity. |
| **US11,145,530** | System and Method for Alignment of an Integrated Circuit | Fricker et al. | 2021 | — | Precision alignment of wafer-scale integrated circuits — manufacturing process IP. |

### 3.3 Patent Category Analysis

Based on IFI Claims' independent analysis ([source](https://www.ificlaims.com/news/ifi-insights-challenging-nvidia-examining-the-patents-of-an-emerging-ai-chip-company/)):

| Category | Coverage | Strategic Importance |
|----------|----------|---------------------|
| **Accelerated deep learning (dataflow)** | Core architecture patents | CRITICAL — defines the WSE compute model |
| **Wafer-scale interconnect** | Multi-die communication, scribe-line repurposing | CRITICAL — enables the "one wafer = one chip" paradigm |
| **Defect tolerance / redundancy** | Dynamic routing, spare core allocation | CRITICAL — solves the yield problem that killed all prior WSI attempts |
| **Thermal management** | Custom cold plates, micro-fin cooling, perpendicular power delivery | HIGH — 23-26 kW/wafer cooling with <20C delta-T |
| **Power delivery** | 300+ distributed VRMs, perpendicular current injection | HIGH — novel approach to feeding power into a wafer-scale chip |
| **Memory architecture** | MemoryX external weight storage, weight streaming | HIGH — enables models larger than on-chip SRAM |
| **Wavelet routing / communication** | Dynamic configurable on-chip fabric | HIGH — the software-defined interconnect |

### 3.4 Inventor Analysis

| Inventor | Patent Count | Role | Background |
|----------|-------------|------|-----------|
| **Sean Lie** | 29 patents | CTO & Co-Founder | MIT BS/MS EE/CS, AMD advanced architecture, SeaMicro lead HW architect |
| **Gary R. Lauterbach** | 68 patents (career total) | CTO Emeritus & Co-Founder | SeaMicro co-founder, AMD data center CTO. PI on $9.3M DOE grant |
| **Jean-Philippe Fricker** | 30 patents (career total) | Chief System Architect & Co-Founder | DSSD (EMC), SeaMicro. Focus: multi-die interconnect, alignment, packaging |
| **Michael James** | Multiple | Chief Architect & Co-Founder | SeaMicro co-founder. Scaled compute fabric patents |

**Assessment:** The founding team's combined patent portfolio (~127+ patents across careers) represents deep expertise in computer architecture, interconnect design, and system integration. The SeaMicro experience (microserver architecture, AMD acquisition) directly informed the WSE's distributed, many-core design philosophy.

### 3.5 Competitive Patent Comparison

| Company | AI Chip Patent Applications (since 2018) | Grants | Forward Citations (quality signal) | Source |
|---------|------------------------------------------|--------|-----------------------------------|--------|
| **NVIDIA** | 6,234 | 2,355 | #1 in forward citations (most cited by other applicants) | [IFI Claims](https://www.ificlaims.com/news/ifi-insights-challenging-nvidia-examining-the-patents-of-an-emerging-ai-chip-company/) |
| **Cerebras** | ~102 (global) | ~34 | Most-cited patent (US20200005142A1) cited by Sony, Intel, IBM, Microsoft, Qualcomm, Micron, Amazon, Bank of America, SambaNova | [IFI Claims](https://www.ificlaims.com/news/ifi-insights-challenging-nvidia-examining-the-patents-of-an-emerging-ai-chip-company/) |
| **Google (TPU)** | Thousands | Thousands | Extensive — TPU patents span systolic arrays, interconnect, XLA compiler | Public knowledge |
| **Graphcore** | ~200+ | ~100+ | IPU architecture, BSP execution model, exchange memory | Public knowledge |
| **Groq** | ~50-100 | ~30+ | LPU deterministic scheduling, compiler-driven execution | Public knowledge (now NVIDIA-owned) |

**Key insight from IFI Claims:** "Cerebras appears to be sitting on a valuable invention." Their patents are being cited by major tech companies (Microsoft, IBM, Qualcomm, Amazon), indicating the wafer-scale approach has influenced broader semiconductor thinking. However, NVIDIA's patent portfolio is ~60x larger — the sheer volume difference reflects 30 years of patenting history.

### 3.6 Patent Litigation

| Case | Parties | Filed | Status | Details |
|------|---------|-------|--------|---------|
| **Rex Computing v. Cerebras** | Rex Computing (plaintiff) v. Cerebras (defendant) | Apr 2021 | **Closed** (May 2025) | Rex asserted 3 patents: US10,355,975 ("Latency Guaranteed Network on Chip"), US10,700,968 ("Optimized Function Assignment in Multi-Core Processor"), US10,127,043 ("Conflict-Free Instructions for Concurrent Operation"). Alleged infringement by CS-1, Swarm fabric, and Graph Compiler. Filed in D. Delaware. Case closed after 4 years — outcome not publicly detailed but no injunction or ongoing obligation appears in subsequent filings. |
| **James v. Cerebras** (copyright) | Darius H. James (author) v. Cerebras | Oct 2025 | **Active** | Copyright class action alleging Cerebras-GPT was trained on Books3 dataset containing copyrighted works. Part of broader wave of AI copyright litigation (74 total suits). Not a co-founder dispute. |

**Assessment:** No patent infringement judgments against Cerebras. The Rex Computing case closed without apparent adverse outcome. No NVIDIA, Google, or other major competitor has filed patent claims against Cerebras, suggesting freedom-to-operate for the wafer-scale approach.

---

## 4. Open-Source Alternatives

### 4.1 Direct Comparison: Can You Build a WSE?

**No.** Wafer-scale integration requires:
- Custom TSMC fabrication relationship (sole supplier)
- Proprietary yield management and defect tolerance IP
- Novel thermal management and power delivery hardware
- Years of compiler development for the dataflow architecture
- $2.55B in capital invested over 10 years

There is no open-source or commercially available alternative to wafer-scale integration. The technology gap is hardware-fundamental, not software-reproducible.

### 4.2 Open-Source AI Accelerator Projects

| Project | Stars | Architecture | Maturity | Feature Overlap with Cerebras | License |
|---------|-------|-------------|----------|------------------------------|---------|
| **[NVDLA](https://nvdla.org/)** (NVIDIA) | ~2.5K | Systolic array inference accelerator | Mature (archived) | LOW — small inference only, not training, not wafer-scale | Open (NVIDIA) |
| **[Gemmini](https://github.com/ucb-bar/gemmini)** (UC Berkeley) | ~1K | RISC-V systolic array generator | Research | LOW — FPGA/ASIC generator for DNN accelerators, not wafer-scale | BSD |
| **[Ztachip](https://github.com/ztachip/ztachip)** | ~500 | RISC-V edge AI accelerator | Early | NONE — edge inference on FPGA, completely different scale | MIT |
| **[Cerebras ModelZoo](https://github.com/Cerebras/modelzoo)** | ~1K | ML model implementations | Active (R_1.6.0) | N/A — Cerebras' own open-source models/training code for their hardware | Apache 2.0 |
| **[Cerebras Cloud SDK](https://github.com/Cerebras/cerebras-cloud-sdk-python)** | Recent | Python SDK for inference API | Active | N/A — Cerebras' own API client | — |

### 4.3 Open-Source AI Hardware Ecosystem (Not Cerebras-Equivalent)

| Project | Organization | What It Is | Why It's Not Comparable |
|---------|-------------|-----------|------------------------|
| **EPAC** | European Processor Initiative | RISC-V vector tiles + DL accelerators | Research chip, not production, not wafer-scale |
| **Esperanto ET-SoC-1** | Esperanto Technologies | 1,088 RISC-V cores, 24B transistors | Traditional die, not wafer-scale. Company pivoted to software. |
| **Tenstorrent Wormhole** | Tenstorrent (Jim Keller) | RISC-V AI accelerator | Commercial chip but traditional die size; open ISA, not open chip |
| **Google TPU (papers only)** | Google | Systolic array architecture | Architecture published but hardware is Google-proprietary cloud-only |

### 4.4 Cerebras' Own Open-Source Contributions

| Repository | Purpose | Stars | License | Activity |
|-----------|---------|-------|---------|----------|
| [Cerebras/modelzoo](https://github.com/Cerebras/modelzoo) | Reference ML models for Cerebras hardware | ~1K | Apache 2.0 | Active (Jan 2026) |
| [CerebrasResearch/Sparse-IFT](https://github.com/CerebrasResearch/Sparse-IFT) | Sparse Iso-FLOP Transformations | — | — | 2023 |
| [CerebrasResearch/REAP](https://github.com/CerebrasResearch/reap) | MoE expert pruning | — | — | Dec 2025 |
| [Cerebras/cerebras-cloud-sdk-python](https://github.com/Cerebras/cerebras-cloud-sdk-python) | Python SDK for inference API | — | — | Active |
| [Cerebras/vscode-cerebras-chat](https://github.com/cerebras/vscode-cerebras-chat) | VS Code extension | — | MIT | Jan 2026 |
| [Cerebras/cerebras-code-mcp](https://github.com/cerebras/cerebras-code-mcp) | MCP server integration | — | MIT | Jan 2026 |
| Cerebras-GPT models on HuggingFace | 7 open LLMs (111M-13B) | — | Apache 2.0 | 2023 |
| REAP-pruned models on HuggingFace | Pruned MoE variants (DeepSeek, Qwen3, Kimi) | — | — | 2025-2026 |

---

## 5. Research Credibility Assessment

### 5.1 Team Academic Backgrounds

| Person | Education | Academic Credentials |
|--------|-----------|---------------------|
| **Andrew Feldman** (CEO) | Stanford BA (Econ/PoliSci) + MBA | Business background, not academic. Serial entrepreneur (Force10, RiverStone, SeaMicro). |
| **Sean Lie** (CTO) | MIT BS/MS EE/CS | Strong technical academic foundation. 29 patents. Primary author of all IEEE Micro / Hot Chips publications. |
| **Gary Lauterbach** (CTO Emeritus) | Not publicly disclosed | 68 patents across career. Principal Investigator on $9.3M DOE grant. AMD data center CTO. |
| **Jean-Philippe Fricker** (Chief System Architect) | Not publicly disclosed | 30 patents. Deep hardware architecture expertise (DSSD/EMC, SeaMicro). |
| **Michael James** (Chief Architect) | Not publicly disclosed | SeaMicro co-founder. Scaled compute fabric patents. |

**Assessment:** This is an engineering-driven team, not an academic team. Their credibility comes from **patents, shipped products, and industry publications** (IEEE Micro, Hot Chips) rather than university affiliations or h-indices. This is typical for semiconductor companies — Intel, AMD, and NVIDIA researchers similarly publish primarily at industry conferences.

### 5.2 Publication Quality & Impact

| Signal | Evidence |
|--------|----------|
| **Top-tier venues** | IEEE Micro (journal), Hot Chips (3 consecutive appearances: 2019, 2022, 2024), NeurIPS (2023, 2024), ICML (2024), SC/Gordon Bell (2022, 2023, 2024) |
| **External citations** | Cerebras-GPT widely cited as open compute-optimal baseline. Architecture papers cited by independent researchers. |
| **Reproducibility** | Cerebras-GPT models + weights fully open (Apache 2.0, HuggingFace). Sparse-IFT and REAP code open-sourced. |
| **National lab collaborations** | Argonne, Sandia, LLNL, LANL, NETL — peer-reviewed scientific computing work |
| **Awards** | 2022 Gordon Bell Special Prize (awarded to Argonne National Lab research team; Cerebras contributed hardware as collaborator). 2024 Gordon Bell Prize (finalist). 3 consecutive years of Gordon Bell recognition. |
| **State of AI Report** | "Cerebras's chip architecture has the most open-source AI paper citations of any startup" (2023) |
| **TIME recognition** | WSE-3 named one of TIME's 200 Best Inventions of 2024 |

### 5.3 Research Depth by Domain

| Domain | Papers | Depth | Competitive Position |
|--------|--------|-------|---------------------|
| **Wafer-scale architecture** | 3 IEEE/Hot Chips papers | DEEP — only company publishing in this space | Monopoly (no competitor does WSI) |
| **Sparsity (training + inference)** | 4+ papers (Sparse-IFT, SuPar, High-Sparsity Llama, REAP) | DEEP — active research program with state-of-the-art results | Leading among hardware companies; competing with academic groups (MIT, CMU) |
| **LLM training at scale** | Cerebras-GPT + scaling law work | MODERATE — one major paper, but validated by Chinchilla replication | Behind frontier labs (Google, Meta, OpenAI) on LLM research, but ahead on training infrastructure |
| **Scientific computing / HPC** | 5+ collaborations with national labs | DEEP — Gordon Bell-class work | Unique — no other AI chip startup has this level of HPC credibility |
| **MoE compression** | REAP (2025) | EMERGING — one strong paper with open-source models | Competitive with academic groups |

---

## 6. Competing Architecture Analysis

### 6.1 Architecture Comparison Matrix

| Feature | Cerebras WSE-3 | NVIDIA H100/B200 | Google TPU v5/Trillium | Groq LPU (now NVIDIA) | Graphcore IPU |
|---------|---------------|-----------------|----------------------|---------------------|--------------|
| **Die size** | 46,255 mm^2 (full wafer) | ~814 mm^2 | ~400-600 mm^2 (est.) | ~400 mm^2 (est.) | ~823 mm^2 |
| **Transistors** | 4 trillion | 80B (H100) | Not disclosed | Not disclosed | 59.4B (Bow) |
| **Cores** | 900,000 | 16,896 CUDA + 528 Tensor (H100) | ~varies | ~varies | 1,472 IPU tiles |
| **On-chip memory** | 44 GB SRAM | 50 MB L2 (H100) | ~varies | 230 MB SRAM | 897 MB SRAM |
| **Memory bandwidth** | 21 PB/s (on-chip) | 3.35 TB/s (HBM3) | ~4.8 TB/s (HBM3) | N/A (SRAM only) | 65 TB/s (on-chip) |
| **Compute paradigm** | Dataflow (wavelet) | SIMT (GPU) | Systolic array | Deterministic (compiler-scheduled) | BSP (Bulk Synchronous Parallel) |
| **Sparsity support** | Native hardware (SLAC cores) | Structured sparsity (2:4) | Limited | None | Some |
| **Scaling model** | Data parallelism only (MemoryX/SwarmX) | Tensor/pipeline/data parallelism | Data/model parallelism | Chip-to-chip deterministic | BSP with exchange phases |
| **Status (Feb 2026)** | Production, $23B valuation | Dominant incumbent | Google-internal + cloud | NVIDIA licensing + asset deal (Dec 24, 2025); continues operating independently | Restructured, uncertain future |

### 6.2 Competitive Moat Assessment

**Cerebras' IP moat is STRONG for the following reasons:**

1. **No competitor does wafer-scale integration.** Cerebras is the only company shipping a chip that uses an entire 300mm wafer. This requires solving yield, thermal, power delivery, and interconnect problems that no one else has solved commercially.

2. **The competitive field is consolidating.** NVIDIA secured Groq LPU IP via licensing + asset deal (Dec 24, 2025; Groq continues operating independently). Intel's SambaNova term sheet has stalled. Graphcore restructured. This leaves Cerebras as the leading independent AI chip challenger to NVIDIA — though SambaNova remains independent. *[Note: NVIDIA now has Groq LPU IP for integration into Rubin — potentially more threatening to Cerebras than Groq as an independent competitor.]*

3. **TSMC exclusivity.** Cerebras has exclusive rights to the IP that makes wafer-scale fabrication at TSMC possible. No other company can walk into TSMC and order a wafer-scale chip.

4. **Patent portfolio is defensible.** 102 patents globally covering the full stack: architecture, interconnect, defect tolerance, thermal management, power delivery, and compiler. No adverse patent judgments.

5. **Scientific credibility validates technology.** Gordon Bell Prize recognition, national lab partnerships (DOE, Sandia, LLNL, LANL, Argonne), and IEEE Micro publications provide third-party validation that the technology works.

**Weaknesses in the IP position:**

1. **Small patent portfolio vs. NVIDIA.** 102 patents vs. 6,234+ applications. In a patent war, NVIDIA has overwhelming volume. However, Cerebras operates in a different design space (WSI vs. GPU), reducing direct overlap.

2. **No patent cross-licensing agreements disclosed.** Major semiconductor companies typically have broad cross-licensing deals. Cerebras' position here is unknown.

3. **TSMC dependency.** If TSMC chose to enable another customer to do WSI (unlikely but possible), Cerebras' manufacturing moat would weaken.

---

## 7. Build-vs-Buy Implication

**You cannot build a Cerebras alternative.** This is a fundamental hardware company, not a software product.

The "build" alternatives are:

| Alternative | What You'd Need | Realistic? |
|------------|----------------|-----------|
| **Build your own wafer-scale chip** | $2B+ capital, TSMC relationship, 10 years of R&D, 700+ engineers | No |
| **Use NVIDIA GPUs** | Buy/rent H100/B200 GPUs, accept 20x slower inference | Yes — this is what most companies do |
| **Use Google TPUs** | Use Google Cloud TPUs, accept vendor lock-in | Yes — but Google-only |
| **Use open-source accelerator designs** | NVDLA, Gemmini, etc. on FPGA/ASIC | Only for edge/small-scale; not comparable to WSE |
| **Use Cerebras Inference API** | Pay-per-token cloud pricing (OpenAI-compatible API) | Yes — lowest barrier, $0.10-$12/M tokens |

**Bottom line:** Cerebras' technology is not replicable from open source. The moat is physical (silicon + manufacturing) not algorithmic. For buyers, the question is GPU clusters vs. Cerebras systems vs. Cerebras cloud API — there is no DIY path to wafer-scale compute.

---

## 8. Key Findings

1. **Patent portfolio is strategically valuable despite small size.** 102 patents (34 granted) cover the entire wafer-scale stack. Most-cited patent (US20200005142A1) is referenced by Sony, Intel, IBM, Microsoft, Qualcomm, Micron, Amazon, and SambaNova. IFI Claims assesses Cerebras is "sitting on a valuable invention." No adverse patent judgments.

2. **Research credibility is exceptionally high for a pre-IPO chip startup.** Three Hot Chips presentations (2019, 2022, 2024), two IEEE Micro papers, Gordon Bell Prize winner (2022) and finalist (2024), NeurIPS/ICML publications, and national lab partnerships (Argonne, Sandia, LLNL, LANL, DOE). The State of AI Report 2023 identified Cerebras as having "the most open-source AI paper citations of any startup."

3. **Sparsity is the key software/algorithmic differentiator.** Four published papers (Sparse-IFT, SuPar, High-Sparsity Llama, REAP) demonstrate Cerebras is not just a hardware company — they are advancing the ML research needed to exploit their hardware's unique sparse computation capabilities. This is genuine HW/SW co-design, not marketing.

4. **No open-source or commercial alternative to wafer-scale integration exists.** The technology gap is hardware-fundamental. Open-source AI accelerator projects (NVDLA, Gemmini, Ztachip) operate at completely different scales and capabilities. The only alternatives are NVIDIA GPUs or Google TPUs — both traditional die-sized chips.

5. **The competitive landscape is consolidating in Cerebras' favor.** NVIDIA secured Groq LPU IP via licensing + asset deal (Dec 24, 2025; Groq continues operating independently). Intel's SambaNova term sheet stalled (SambaNova raising $350-500M independently). Graphcore restructured. Cerebras is the leading independent AI chip challenger to NVIDIA, supported by a unique patent portfolio, TSMC manufacturing exclusivity, and customer validation from OpenAI, Meta, IBM, and the U.S. Department of Energy.

---

## Appendix: Source Index

### Patent Sources
- [Justia: Patents Assigned to Cerebras Systems Inc.](https://patents.justia.com/assignee/cerebras-systems-inc)
- [GreyB/Insights;Gate: Cerebras Systems Patents](https://insights.greyb.com/cerebras-systems-patents/)
- [IFI Claims: Challenging NVIDIA — Examining the Patents of an Emerging AI Chip Company](https://www.ificlaims.com/news/ifi-insights-challenging-nvidia-examining-the-patents-of-an-emerging-ai-chip-company/)
- [Google Patents: US20200005142A1](https://patents.google.com/patent/US20200005142A1/en)
- [USPTO Report: US11,328,207](https://uspto.report/patent/grant/11,328,207)
- [USPTO Report: US10,777,532](https://uspto.report/patent/grant/10,777,532)

### Academic / Publication Sources
- [IEEE Micro: Cerebras Architecture Deep Dive (2023)](https://ieeexplore.ieee.org/document/10123162/)
- [IEEE Micro: Inside the Cerebras Wafer-Scale Cluster (2024)](https://ieeexplore.ieee.org/document/10495794/)
- [Hot Chips 2024: Cerebras Wafer-Scale AI (PDF)](https://hc2024.hotchips.org/assets/program/conference/day2/72_HC2024.Cerebras.Sean.v03.final.pdf)
- [Hot Chips 2019: Wafer-Scale Deep Learning (PDF)](https://old.hotchips.org/hc31/HC31_1.13_Cerebras.SeanLie.v02.pdf)
- [arXiv: Cerebras-GPT (2304.03208)](https://arxiv.org/abs/2304.03208)
- [arXiv: Sparse-IFT (2303.11525)](https://arxiv.org/html/2303.11525v3)
- [arXiv: SuPar (2405.15743)](https://arxiv.org/abs/2405.15743)
- [arXiv: High-Sparsity Llama (2405.03594)](https://arxiv.org/abs/2405.03594)
- [arXiv: REAP (2510.13999)](https://arxiv.org/html/2510.13999v1)
- [Cerebras Publications Page](https://www.cerebras.ai/publications)

### Scientific Computing Sources
- [LLNL: Molecular Dynamics Timescale Barrier](https://www.llnl.gov/article/52081/nnsa-researchers-break-molecular-dynamics-timescale-barrier-worlds-largest-chip)
- [Sandia: Fastest Molecular Dynamics Simulations](https://www.sandia.gov/labnews/2024/10/03/sandia-led-collaboration-achieves-one-of-worlds-fastest-molecular-dynamics-simulations/)
- [Cerebras: MD World Record](https://www.cerebras.ai/press-release/cerebras-sets-new-world-record-in-molecular-dynamics-at-1.1-million-simulations-per-second-748x-faster-than-the-worlds-1-supercomputer-frontier)
- [SC24: Gordon Bell Prize Finalists](https://sc24.supercomputing.org/2024/10/presenting-the-finalists-for-the-2024-gordon-bell-prize/)

### Competitive / Industry Sources
- [IFI Claims: NVIDIA Patent Quality Analysis](https://www.digital-science.com/blog/2024/09/nvidia-is-going-for-quality-not-quantity-with-ai-chip-patents/)
- [Wikipedia: Wafer-Scale Integration](https://en.wikipedia.org/wiki/Wafer-scale_integration)
- [TechCrunch: Five Technical Challenges Cerebras Overcame](https://techcrunch.com/2019/08/19/the-five-technical-challenges-cerebras-overcame-in-building-the-first-trillion-transistor-chip/)
- [Cerebras: 100x Defect Tolerance](https://www.cerebras.ai/blog/100x-defect-tolerance-how-cerebras-solved-the-yield-problem)
- [arXiv: Comparison of Cerebras WSI vs NVIDIA GPU Systems](https://arxiv.org/html/2503.11698v1)

### Litigation Sources
- [Justia: Rex Computing v. Cerebras (1:21-cv-00525)](https://dockets.justia.com/docket/delaware/dedce/1:2021cv00525/75162)
- [Justia: James v. Cerebras (3:25-cv-09361)](https://dockets.justia.com/docket/california/candce/3:2025cv09361/458918)

---

*Phase 5 complete. Ready for Phase 6 (Valuation Analysis).*

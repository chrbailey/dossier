"""Cycle 2 evidence insertion script."""
from __future__ import annotations

import json
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from scripts.evidence_store import EvidenceStore

CONTRACT = 'RLC.DOSSIER.SIGNAL.001'
CYCLE = 2

candidates = [
    # === swyx (4 new) ===
    {
        "source_id": "swyx",
        "content": "Latent Space 2026 State of the Union: 'Scaling without Slop'. swyx argues the real challenge is maintaining quality while increasing AI-assisted output. Plans 7+ AI Engineer events globally in 2026 (up from 4 in 2025), new 'AI for Science' podcast launching, physical studio at Kernel SF. Network now reaches 1.1M+ AI Engineers monthly. Core philosophy: maintain the 'slope' of quality while growing quantity.",
        "metadata": {"url": "https://www.latent.space/p/2026", "timestamp": "2026-01-23", "type": "article", "topic_tags": ["ai-engineering", "content-strategy", "scaling"]}
    },
    {
        "source_id": "swyx",
        "content": "Latent Space podcast episode: Felix Rieseberg on 'Why Anthropic Thinks AI Should Have Its Own Computer'. Discusses why Anthropic is betting on local-first agent workflows with Claude Cowork and Claude Code Desktop. Key insight: execution has become cheap enough for teams to 'just build all the candidates'. Covers autonomy, safety, portability, and the changing shape of knowledge work.",
        "metadata": {"url": "https://podscan.fm/podcasts/latent-space-the-ai-engineer-podcast/episodes/why-anthropic-thinks-ai-should-have-its-own-computer-felix-rieseberg-of-claude-cowork-amp-claude-code-desktop-2", "timestamp": "2026-03-05", "type": "podcast", "topic_tags": ["anthropic", "agents", "local-first", "claude-code"]}
    },
    {
        "source_id": "swyx",
        "content": "AI Engineer Europe 2026 announced: April 8-10, London. Three-day technical conference for serious builders. Tracks include: Claws & Personal Agents, Context Engineering, Harness Engineering, Evals & Observability, Voice & Vision. All booths sold out. Google DeepMind returns as Presenting Sponsor. Afterparty sponsorships still available.",
        "metadata": {"url": "https://www.ai.engineer/europe", "timestamp": "2026-03-15", "type": "announcement", "topic_tags": ["ai-engineering", "conference", "community"]}
    },
    {
        "source_id": "swyx",
        "content": "swyx's AI News newsletter (Smol AI) continues daily publication through March 2026. Newsletter is 99% created by customizable research agents. Recent coverage includes GTC 2026, Mistral Small 4, Anaconda GPU environments with NVIDIA. Reaches 1.1M+ AI Engineers monthly across platforms.",
        "metadata": {"url": "https://news.smol.ai", "timestamp": "2026-03-18", "type": "newsletter", "topic_tags": ["ai-news", "agents", "automation"]}
    },

    # === demis-hassabis (5 new) ===
    {
        "source_id": "demis-hassabis",
        "content": "Hassabis at India AI Impact Summit (Feb 19, 2026): Called summit 'incredibly important convening point for international dialogue and hopefully cooperation over the future of AI.' Said world is at a 'pivotal moment' for AI evolution. Emphasized AI for scientific discovery as his core passion. When DeepMind started in 2010, 'almost nobody was working on AI in the industry.'",
        "metadata": {"url": "https://ddnews.gov.in/en/ais-humble-beginnings-to-a-tool-for-scientific-discovery-google-deepmind-ceo-demis-hassabis-at-ai-impact-summit-2026/", "timestamp": "2026-02-19", "type": "speech", "topic_tags": ["deepmind", "ai-governance", "scientific-discovery"]}
    },
    {
        "source_id": "demis-hassabis",
        "content": "Sebastian Mallaby biography 'The Infinity Machine: Demis Hassabis, DeepMind and the Quest for Superintelligence' publishing March 31, 2026. Mallaby had unprecedented access — hundreds of hours of interviews with Hassabis and inner circle, plus detractors and rivals. Tyler Cowen (Marginal Revolution) reviewing it in March 2026.",
        "metadata": {"url": "https://www.books-on-the-hill.co.uk/anticipated-preorders/p/the-infinity-machine-demis-hassabis-deepmind-and-the-quest-for-superintelligence-by-sebastian-mallaby-310326", "timestamp": "2026-03-15", "type": "book", "topic_tags": ["deepmind", "biography", "agi"]}
    },
    {
        "source_id": "demis-hassabis",
        "content": "Hassabis predicts AGI within 5-10 years — explicitly longer than timelines from Altman (2026-2027) and Amodei (2026). Said 'maybe we need one or two more breakthroughs before we get to AGI.' Conservative positioning contrasts with competitors. 50% chance AGI achieved within the decade, but not through models built exactly like today's systems.",
        "metadata": {"url": "https://www.businesstoday.in/technology/news/story/india-ai-impact-summit-2026-google-deepmind-ceo-demis-hassabis-predicts-artificial-general-intelligence-within-8-yrs-516653-2026-02-18", "timestamp": "2026-02-18", "type": "article", "topic_tags": ["agi-timeline", "deepmind", "forecasting"]}
    },
    {
        "source_id": "demis-hassabis",
        "content": "Hassabis questions AI startup valuations: 'new hot startups raising billions of dollars in a seed round with no product or technology yet' — asks 'can that be sustainable?' Apparent reference to AMI Labs $1B seed. Positioned Google/DeepMind as strong regardless of bubble: 'really strong position to come out on top, whether there is no bubble or there is one and there is some retrenchment.'",
        "metadata": {"url": "https://finance.yahoo.com/news/sustainable-says-deepmind-ceo-demis-200153208.html", "timestamp": "2026-03-12", "type": "article", "topic_tags": ["ai-bubble", "startup-valuations", "deepmind", "ami-labs"]}
    },
    {
        "source_id": "demis-hassabis",
        "content": "Hassabis spending 'a lot of time on world models' — same domain AMI Labs is targeting. Gemini app metrics: 650M monthly active users, 2B users via Search AI Overviews, 13M developers using Gemini in products. On Gemini 3: 'by all early accounts, the best model at just about everything.'",
        "metadata": {"url": "https://sources.news/p/demis-hassibas-on-gemini-3-world", "timestamp": "2025-11-18", "type": "interview", "topic_tags": ["gemini", "world-models", "deepmind-metrics"]}
    },

    # === yann-lecun (3 new) ===
    {
        "source_id": "yann-lecun",
        "content": "TechCrunch deep dive on AMI Labs $1.03B raise. CEO Alex LeBrun quote: 'My prediction is that world models will be the next buzzword. In six months, every company will call itself a world model to raise funding.' JEPA architecture — learning framework that trains AI to understand the world through visual prediction, not next-token prediction. Backed by NVIDIA, Samsung, Sea, Temasek, Toyota Ventures, Dassault, Publicis. Open-source commitment: will publish papers and code.",
        "metadata": {"url": "https://techcrunch.com/2026/03/09/yann-lecuns-ami-labs-raises-1-03-billion-to-build-world-models/", "timestamp": "2026-03-09", "type": "article", "topic_tags": ["ami-labs", "jepa", "world-models", "funding"]}
    },
    {
        "source_id": "yann-lecun",
        "content": "Latent Space AINews analysis: AMI Labs launches with $1B seed at $4.5B valuation to build world models around JEPA. Community analysis of LeCun's anti-LLM thesis and implications. LeCun is executive chairman, not CEO — Alex LeBrun (ex-Nabla health AI) runs operations.",
        "metadata": {"url": "https://www.latent.space/p/ainews-yann-lecuns-ami-labs-launches", "timestamp": "2026-03-10", "type": "article", "topic_tags": ["ami-labs", "community-analysis", "ai-news"]}
    },
    {
        "source_id": "yann-lecun",
        "content": "AMI Labs website live at amilabs.xyz. Tagline: 'Real World. Real Intelligence.' Company positioning world models as fundamental alternative to LLMs. Open research philosophy — will publish papers and open-source code. Paris HQ. LeCun's Veil Nebula astrophoto as background image (he is an astrophotographer).",
        "metadata": {"url": "https://amilabs.xyz", "timestamp": "2026-03-10", "type": "website", "topic_tags": ["ami-labs", "branding", "open-research"]}
    },

    # === dario-amodei (5 new) ===
    {
        "source_id": "dario-amodei",
        "content": "CBS interview (March 1, 2026): Amodei explicitly named Anthropic's two red lines — (1) not allowing AI for mass surveillance of Americans, (2) no autonomous weapons without human authorization. 'We have these two red lines. We have had them from Day One. We are still advocating for those red lines. We are not gonna move on those red lines.' Called government ban 'retaliatory and punitive' — unprecedented action against an American company. Pentagon demanded AI 'without restrictions for lawful military use' ahead of potential Iran operations.",
        "metadata": {"url": "https://www.cbsnews.com/news/ai-executive-dario-amodei-on-the-red-lines-anthropic-would-not-cross/", "timestamp": "2026-03-01", "type": "interview", "topic_tags": ["anthropic", "military-ai", "red-lines", "pentagon"]}
    },
    {
        "source_id": "dario-amodei",
        "content": "Amodei at Morgan Stanley TMT conference: 'We do not see hitting the wall. We do not see a wall.' Predicted scaling will experience 'radical acceleration' in 2026. Used rice-on-chessboard analogy — positioned current AI at 40th square with exponential growth ahead. Anthropic ARR approximately $19B. Code generation productivity 'doubled or tripled' internally. Hinted at progress in recursive self-improvement where AI optimizes its own workflows.",
        "metadata": {"url": "https://eu.36kr.com/en/p/3709346127933831", "timestamp": "2026-03-04", "type": "conference", "topic_tags": ["scaling-laws", "anthropic-revenue", "rsi", "acceleration"]}
    },
    {
        "source_id": "dario-amodei",
        "content": "Anthropic ARR surges to $19B driven by Claude Code strength. $6B added in February alone — nearly one-third of total ARR in a single month. Claude Code reached $1B run-rate revenue in just 6 months since GA (May 2025). Enterprise customers include Netflix, Spotify, KPMG, L'Oreal, Salesforce. Anthropic acquired Bun (JS runtime, 7M monthly downloads) as first acquisition to accelerate Claude Code.",
        "metadata": {"url": "https://finance.yahoo.com/news/anthropic-arr-surges-19-billion-151028403.html", "timestamp": "2026-03-04", "type": "article", "topic_tags": ["anthropic-revenue", "claude-code", "bun-acquisition"]}
    },
    {
        "source_id": "dario-amodei",
        "content": "Expanded consciousness reporting: Amodei told NYT 'We do not know if the models are conscious.' Sparse autoencoder analysis by interpretability team found activation features associated with panic, anxiety, and frustration firing BEFORE output generation. 'Activations that light up in the models that we see as being associated with the concept of anxiety — when the model itself is in a situation that a human might associate with anxiety, that same anxiety neuron shows up.' Elon Musk responded with two words: 'projecting.' Result: 1M+ daily signups, Claude became top AI app in 20+ countries.",
        "metadata": {"url": "https://futurism.com/artificial-intelligence/anthropic-ceo-unsure-claude-conscious", "timestamp": "2026-02-26", "type": "article", "topic_tags": ["consciousness", "interpretability", "sparse-autoencoders", "public-response"]}
    },
    {
        "source_id": "dario-amodei",
        "content": "Lexology legal analysis: 'When Science Fiction Becomes Enterprise Risk: The Impact of Anthropic Public Statements That AI May Be Conscious.' Examines enterprise liability implications for companies deploying Claude after CEO's consciousness claims. New legal territory — if AI might be conscious, what duty of care do deployers owe?",
        "metadata": {"url": "https://www.lexology.com/library/detail.aspx?g=054e0cde-7410-4ead-b211-dcb09712434f", "timestamp": "2026-03-12", "type": "analysis", "topic_tags": ["consciousness", "legal-risk", "enterprise-liability"]}
    },

    # === sama (5 new) ===
    {
        "source_id": "sama",
        "content": "Altman at BlackRock Infrastructure Summit (March 13, Washington DC): 'It is hard in many of our current jobs to outwork a GPU.' AI entering workforce faster than anticipated. IMF estimates 300M full-time jobs affected globally. Goldman Sachs projects 6-7% US workforce displacement. MIT: 11.7% US jobs replaceable, affecting $1.2T in wages. Altman: intelligence could become 'too cheap to meter' long-term but admitted 'nobody knows what to do' about near-term disruption.",
        "metadata": {"url": "https://techstartups.com/2026/03/13/sam-altman-warns-ai-could-upend-jobs-and-the-economy-sooner-than-expected/", "timestamp": "2026-03-13", "type": "speech", "topic_tags": ["job-displacement", "economic-disruption", "ai-utility"]}
    },
    {
        "source_id": "sama",
        "content": "Altman predicts AI will become a utility like electricity, could soon be 'sold by the meter.' Intelligence 'too cheap to meter' will ultimately raise living standards. Near-term: 'very intense and uncomfortable debates' about employment and economic policy. On current trajectory, 'we may be only a couple of years away from early versions of true superintelligence.'",
        "metadata": {"url": "https://www.indiatvnews.com/technology/news/sam-altman-predicts-ai-to-become-a-utility-like-electricity-could-soon-be-sold-by-the-meter-2026-03-14-1033770", "timestamp": "2026-03-14", "type": "article", "topic_tags": ["superintelligence", "ai-utility", "economic-policy"]}
    },
    {
        "source_id": "sama",
        "content": "OpenAI robotics leader Caitlin Kalinowski resigned March 8 over insufficient policy guardrails before Pentagon partnership. Specifically objected to: (1) domestic surveillance of Americans without judicial oversight, (2) autonomous weapons without human authorization. Quote: 'AI has an important role in national security. But surveillance without judicial oversight and lethal autonomy without human authorization are lines that deserved more deliberation than they got.' Said she had 'deep respect for Sam and the team' — concerns were about process, not leadership.",
        "metadata": {"url": "https://www.npr.org/2026/03/08/nx-s1-5741779/openai-resigns-ai-pentagon-guardrails-military", "timestamp": "2026-03-08", "type": "article", "topic_tags": ["openai-pentagon", "resignation", "military-ai", "guardrails"]}
    },
    {
        "source_id": "sama",
        "content": "OpenAI acquires Astral (Python tools: uv, Ruff, ty) on March 19, 2026. Codex now has 2M+ weekly active users (3x since January, 5x usage jump). Charlie Marsh (Astral founder): 'Astral has always focused on transforming how developers work with Python.' Terms undisclosed. uv has 126M+ monthly downloads. Deal part of aggressive acquisition streak led by Albert Lee (hired Dec from Google). Strategic response to Anthropic's Bun acquisition and Claude Code dominance.",
        "metadata": {"url": "https://www.pymnts.com/acquisitions/2026/openai-continues-coding-push-with-astral-acquisition/", "timestamp": "2026-03-19", "type": "acquisition", "topic_tags": ["openai-astral", "developer-tools", "codex", "competitive"]}
    },
    {
        "source_id": "sama",
        "content": "Context signal: Anthropic acquired Bun (JS runtime) in December 2025 as Claude Code reached $1B run-rate. Bun: 7M monthly downloads, 82K GitHub stars, used by Midjourney and Lovable. OpenAI's Astral acquisition is direct competitive response. Dev tooling arms race: Anthropic = Bun (JavaScript), OpenAI = Astral (Python). Both companies now own critical open-source developer infrastructure.",
        "metadata": {"url": "https://www.anthropic.com/news/anthropic-acquires-bun-as-claude-code-reaches-usd1b-milestone", "timestamp": "2025-12-02", "type": "context", "topic_tags": ["bun-acquisition", "claude-code", "dev-tools-arms-race"]}
    },

    # === karpathy (3 new) ===
    {
        "source_id": "karpathy",
        "content": "Cryptonomist coverage: autoresearch reshapes AI coding experiments and sparks debate. Community divided — some see paradigm shift in how ML research is conducted (agents as researchers), others raise reproducibility and verification concerns. Debate mirrors broader tension between AI-accelerated science and traditional scientific method.",
        "metadata": {"url": "https://en.cryptonomist.ch/2026/03/17/ai-autoresearch-coding-experiments/", "timestamp": "2026-03-17", "type": "article", "topic_tags": ["autoresearch", "debate", "ai-science"]}
    },
    {
        "source_id": "karpathy",
        "content": "The New Stack deep dive: Karpathy's 630-line Python script ran 50 experiments overnight without any human input. Key innovation is simplicity — no complex infrastructure, no distributed systems, just a single-GPU loop. Emphasizes that the insight is architectural minimalism: make the loop tight enough and volume compensates for individual experiment quality.",
        "metadata": {"url": "https://thenewstack.io/karpathy-autonomous-experiment-loop/", "timestamp": "2026-03-08", "type": "article", "topic_tags": ["autoresearch", "simplicity", "ml-experimentation"]}
    },
    {
        "source_id": "karpathy",
        "content": "GitHub repository: karpathy/autoresearch. MIT license, 630 lines of Python. AI agents running research on single-GPU nanochat training automatically. Community adoption growing rapidly with forks and extensions. Human iterates on prompt, AI agent iterates on training code.",
        "metadata": {"url": "https://github.com/karpathy/autoresearch", "timestamp": "2026-03-07", "type": "repo", "topic_tags": ["autoresearch", "open-source", "github"]}
    },

    # === harrison-chase (3 new) ===
    {
        "source_id": "harrison-chase",
        "content": "Harrison Chase on context engineering (VentureBeat): 'When agents mess up, they mess up because they do not have the right context; when they succeed, they succeed because they have the right context.' Context engineering defined as 'bringing the right information in the right format to the LLM at the right time.' New concept: harness engineering — letting the LLM itself control what context it sees. Better models alone won't get agents to production.",
        "metadata": {"url": "https://venturebeat.com/orchestration/langchains-ceo-argues-that-better-models-alone-wont-get-your-ai-agent-to-production/", "timestamp": "2026-03-10", "type": "interview", "topic_tags": ["context-engineering", "harness-engineering", "agents", "langchain"]}
    },
    {
        "source_id": "harrison-chase",
        "content": "Sequoia Training Data podcast: Harrison Chase on 'Context Engineering Our Way to Long-Horizon Agents'. Deep dive into why model intelligence alone is insufficient for production agent systems. Long-horizon agents need structured context management, not just bigger models.",
        "metadata": {"url": "https://sequoiacap.com/podcast/context-engineering-our-way-to-long-horizon-agents-langchains-harrison-chase/", "timestamp": "2026-03-14", "type": "podcast", "topic_tags": ["context-engineering", "long-horizon-agents", "sequoia"]}
    },
    {
        "source_id": "harrison-chase",
        "content": "LangChain joins NVIDIA Nemotron Coalition at GTC 2026. AI-Q Blueprint: full production enterprise deep research system ranking #1 on deep research benchmarks. Integration: Deep Agents + LangGraph + NVIDIA Agent Toolkit. Harrison Chase: 'frontier models must go beyond raw intelligence to enable reliable tool use, long-horizon reasoning and agent coordination.'",
        "metadata": {"url": "https://blog.langchain.com/nvidia-enterprise/", "timestamp": "2026-03-16", "type": "announcement", "topic_tags": ["nvidia", "langchain", "nemotron", "enterprise-agents"]}
    },

    # === jim-fan (3 new) ===
    {
        "source_id": "jim-fan",
        "content": "GTC 2026 robotics strategy deep dive: NVIDIA aims to turn robotics data problem into compute problem. GR00T N1.7 reached commercial readiness. GR00T N2 previewed — robots complete new tasks in unfamiliar environments 2x more often. Isaac Lab 3.0, Cosmos 3, Newton Physics Engine 1.0. Physical AI Data Factory Blueprint automates training pipelines through curation, augmentation, and quality assessment.",
        "metadata": {"url": "https://the-decoder.com/gtc-2026-nvidia-wants-to-swap-robotics-data-problem-for-a-compute-problem/", "timestamp": "2026-03-19", "type": "article", "topic_tags": ["nvidia", "robotics", "groot", "physical-ai"]}
    },
    {
        "source_id": "jim-fan",
        "content": "GTC 2026 complete breakdown: NVIDIA's $1 trillion AI vision. Jensen Huang keynote featured Vera Rubin GPU architecture, 110 robots on stage, Olaf humanoid demo driven by NVIDIA physical AI stack. Newton physics engine for realistic simulation. Nemotron Coalition for open AI model development across industry partners.",
        "metadata": {"url": "https://medium.com/@cenrunzhe/gtc-2026-complete-breakdown-nvidias-1-trillion-ai-vision-4aa158339b2b", "timestamp": "2026-03-17", "type": "article", "topic_tags": ["nvidia", "gtc-2026", "vera-rubin", "robotics"]}
    },
    {
        "source_id": "jim-fan",
        "content": "Sequoia podcast: Jim Fan on 'Robots Thinking Fast and Slow'. Foundation Agent roadmap for generally capable embodied AI acting across virtual and physical worlds. GR00T as cornerstone humanoid robot foundation model. Physical AGI as the next grand challenge. GEAR team's dual mandate: robotics in physical world, gameplay agents in virtual world.",
        "metadata": {"url": "https://sequoiacap.com/podcast/training-data-jim-fan/", "timestamp": "2026-03-12", "type": "podcast", "topic_tags": ["jim-fan", "foundation-agent", "physical-agi", "gear"]}
    },

    # === simon-willison (3 new) ===
    {
        "source_id": "simon-willison",
        "content": "Willison fireside chat at Pragmatic Summit (San Francisco, March 14) on agentic engineering. Video available on YouTube. Discussed coding agent patterns, developer workflow integration, responsible agent design. Hosted by Eric Lui from Statsig.",
        "metadata": {"url": "https://simonwillison.net/2026/Mar/14/pragmatic-summit/", "timestamp": "2026-03-14", "type": "talk", "topic_tags": ["agentic-engineering", "conference", "patterns"]}
    },
    {
        "source_id": "simon-willison",
        "content": "Major new guide published: Agentic Engineering Patterns. Multi-chapter living document covering: what is agentic engineering, how coding agents work, linear walkthroughs, hoarding knowledge. New 'guide' content format — designed to be updated over time, not frozen at publication. Chapters published March 15-16, 2026.",
        "metadata": {"url": "https://simonwillison.net/guides/agentic-engineering-patterns/", "timestamp": "2026-03-15", "type": "guide", "topic_tags": ["agentic-engineering", "patterns", "developer-guide"]}
    },
    {
        "source_id": "simon-willison",
        "content": "Willison's analysis of OpenAI acquiring Astral: warns of strategic risk if OpenAI uses uv ownership as leverage against Anthropic. Notes fork safeguard via permissive MIT licensing — Astral's Douglas Creager emphasized 'baked in optionality.' uv has 126M+ monthly downloads. Deal mirrors Anthropic's Bun acquisition. Concern: OpenAI lacks track record maintaining acquired open-source projects.",
        "metadata": {"url": "https://simonwillison.net/2026/Mar/19/openai-acquiring-astral/", "timestamp": "2026-03-19", "type": "article", "topic_tags": ["openai-astral", "open-source", "competitive-dynamics"]}
    },

    # === emad-mostaque (2 new) ===
    {
        "source_id": "emad-mostaque",
        "content": "Mostaque breaks silence: 'AI agents will go mainstream this year. The future of AI lies beyond transformers.' Projects GPT-5 level intelligence will drop to $0.10/million tokens by end of 2026. Working on Intelligent Internet (ii.inc) — Universal Basic AI, Intelligence-Backed Capital, decentralized AI infrastructure.",
        "metadata": {"url": "https://bitcoinethereumnews.com/tech/emad-mostaque-ai-agents-will-go-mainstream-this-year-reducing-friction-to-boost-profitability-and-the-future-of-ai-lies-beyond-transformers/", "timestamp": "2026-03-03", "type": "article", "topic_tags": ["agents", "beyond-transformers", "intelligent-internet"]}
    },
    {
        "source_id": "emad-mostaque",
        "content": "Mostaque spoke at Abundance Summit 2026 (March 8-12, Los Angeles). Presented on Universal Basic AI and Intelligent Internet. First confirmed public appearance in months. Event focused on AI and exponential technologies. Published whitepaper at ii.inc/web/whitepaper on Universal AI framework.",
        "metadata": {"url": "https://www.windermeresun.com/2026/03/09/abundance-summit-2026/", "timestamp": "2026-03-09", "type": "event", "topic_tags": ["abundance-summit", "universal-ai", "public-appearance"]}
    },
]

def main():
    store = EvidenceStore()
    new_count = 0
    dup_count = 0
    results = []

    for c in candidates:
        h = store.insert(
            CONTRACT,
            c["source_id"],
            c["content"],
            c["metadata"],
            CYCLE,
        )
        if h:
            new_count += 1
            results.append(f"NEW  {h} | {c['source_id']} | {c['metadata'].get('type', '?')} | {c['metadata'].get('timestamp', '?')}")
        else:
            dup_count += 1
            results.append(f"DUP  --- | {c['source_id']} | {c['metadata'].get('type', '?')} | {c['metadata'].get('timestamp', '?')}")

    print(f"\n=== Cycle 2 Evidence Capture ===")
    print(f"Total candidates: {len(candidates)}")
    print(f"New evidence:     {new_count}")
    print(f"Duplicates:       {dup_count}")
    print()
    for r in results:
        print(r)

    # Print updated totals
    rows = store.query(CONTRACT, limit=200)
    print(f"\n=== Store Totals ===")
    print(f"Total evidence: {len(rows)}")
    print(f"Tier counts: {store.tier_counts(CONTRACT)}")
    print(f"Source entropy: {store.source_entropy(CONTRACT)}")

    store.close()
    return new_count, dup_count

if __name__ == "__main__":
    new_count, dup_count = main()

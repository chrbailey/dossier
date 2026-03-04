# DSPy Dossier Integration — Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Add an offline DSPy optimizer that compiles Dossier phase prompts via Claude Agent SDK (Max subscription), improving prompt quality through metric-driven search.

**Architecture:** Custom `dspy.BaseLM` backend routes all LLM calls through `claude-agent-sdk` (zero API spend). 7 Signatures define phase I/O contracts. `BootstrapFewShotWithRandomSearch` optimizes instructions using 5 existing dossier outputs as training data. Optimized instructions export back to `prompts/p{N}-*.md`.

**Tech Stack:** Python 3.10+, DSPy 2.6+, claude-agent-sdk 0.1.x, litellm (ModelResponse type only), pytest

**Design Doc:** `docs/plans/2026-03-03-dspy-dossier-integration-design.md`

---

### Task 1: Set Up Project Structure and Dependencies

**Files:**
- Create: `dspy/requirements.txt`
- Create: `dspy/__init__.py`
- Create: `dspy/compiled/.gitkeep`
- Create: `tests/__init__.py`
- Create: `tests/conftest.py`

**Step 1: Verify Python 3.10+ is available**

Run: `python3.12 --version || python3.11 --version || python3.10 --version`

If none available:
```bash
brew install python@3.12
```

**Step 2: Create venv with Python 3.10+**

```bash
cd "/Volumes/OWC drive/Dev/dossier"
python3.12 -m venv dspy/.venv
```

**Step 3: Create requirements.txt**

Create `dspy/requirements.txt`:
```
dspy>=2.6.0
claude-agent-sdk>=0.1.40
litellm>=1.50.0
pytest>=8.0.0
pytest-asyncio>=0.24.0
```

**Step 4: Install dependencies**

```bash
cd "/Volumes/OWC drive/Dev/dossier"
dspy/.venv/bin/pip install -r dspy/requirements.txt
```

**Step 5: Create directory structure**

```bash
mkdir -p dspy/compiled tests
touch dspy/__init__.py dspy/compiled/.gitkeep tests/__init__.py
```

**Step 6: Create tests/conftest.py**

```python
"""Shared test fixtures for DSPy integration tests."""
from __future__ import annotations

import json
from pathlib import Path
from unittest.mock import AsyncMock, MagicMock

import pytest

DOSSIER_ROOT = Path(__file__).parent.parent
OUTPUT_DIR = DOSSIER_ROOT / "output"
PROMPTS_DIR = DOSSIER_ROOT / "prompts"


@pytest.fixture
def dossier_root():
    return DOSSIER_ROOT


@pytest.fixture
def output_dir():
    return OUTPUT_DIR


@pytest.fixture
def sample_discovery_output():
    """Load okta.com discovery output as sample data."""
    path = OUTPUT_DIR / "okta.com" / "01-discovery.md"
    if path.exists():
        return path.read_text()
    return "# Discovery: okta.com\n\n## Company Identity\nOkta, Inc.\n"


@pytest.fixture
def sample_claims_output():
    """Load okta.com claims output as sample data."""
    path = OUTPUT_DIR / "okta.com" / "04-claims.md"
    if path.exists():
        return path.read_text()
    return "# Claims Validation: Okta\n\n## Claims Inventory\n| # | Claim |\n"
```

**Step 7: Verify setup**

Run: `cd "/Volumes/OWC drive/Dev/dossier" && dspy/.venv/bin/python -c "import dspy; import claude_agent_sdk; print('OK')"`
Expected: `OK`

**Step 8: Commit**

```bash
cd "/Volumes/OWC drive/Dev/dossier"
git add dspy/requirements.txt dspy/__init__.py dspy/compiled/.gitkeep tests/__init__.py tests/conftest.py
git commit -m "chore: scaffold dspy/ directory with dependencies"
```

---

### Task 2: ClaudeAgentLM Backend

**Files:**
- Create: `dspy/lm.py`
- Create: `tests/test_lm.py`

**Step 1: Write the failing test**

Create `tests/test_lm.py`:
```python
"""Tests for ClaudeAgentLM — DSPy backend via Claude Agent SDK."""
from __future__ import annotations

import asyncio
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from dspy.lm import ClaudeAgentLM


class TestClaudeAgentLM:
    def test_init_defaults(self):
        lm = ClaudeAgentLM()
        assert lm.cli_model == "sonnet"
        assert lm.max_turns == 1
        assert lm.model == "claude-agent/sonnet"
        assert lm.cache is False

    def test_init_custom_model(self):
        lm = ClaudeAgentLM(model="opus")
        assert lm.cli_model == "opus"
        assert lm.model == "claude-agent/opus"

    @pytest.mark.asyncio
    async def test_aforward_returns_model_response(self):
        lm = ClaudeAgentLM()

        # Mock the Agent SDK query() to yield a ResultMessage
        mock_result = MagicMock()
        mock_result.result = "This is the LLM response"
        mock_result.session_id = "test-session-123"

        mock_init = MagicMock()
        mock_init.subtype = "init"
        mock_init.data = {"session_id": "test-session-123"}

        async def mock_query(**kwargs):
            yield mock_init
            yield mock_result

        with patch("dspy.lm.query", side_effect=mock_query):
            response = await lm.aforward(
                messages=[
                    {"role": "system", "content": "You are helpful."},
                    {"role": "user", "content": "Hello"},
                ]
            )

        assert response.choices[0].message.content == "This is the LLM response"
        assert response.choices[0].finish_reason == "stop"
        assert lm._session_id == "test-session-123"

    @pytest.mark.asyncio
    async def test_aforward_with_prompt_string(self):
        lm = ClaudeAgentLM()

        mock_result = MagicMock()
        mock_result.result = "Response text"
        mock_result.session_id = "sess-456"

        async def mock_query(**kwargs):
            yield mock_result

        with patch("dspy.lm.query", side_effect=mock_query):
            response = await lm.aforward(prompt="Simple prompt")

        assert response.choices[0].message.content == "Response text"

    @pytest.mark.asyncio
    async def test_aforward_cli_error_raises(self):
        lm = ClaudeAgentLM()

        async def mock_query(**kwargs):
            raise RuntimeError("CLI connection failed")
            yield  # make it a generator

        with patch("dspy.lm.query", side_effect=mock_query):
            with pytest.raises(RuntimeError, match="CLI connection failed"):
                await lm.aforward(prompt="test")

    def test_forward_sync_wrapper(self):
        lm = ClaudeAgentLM()

        mock_result = MagicMock()
        mock_result.result = "Sync response"
        mock_result.session_id = "sess-789"

        async def mock_query(**kwargs):
            yield mock_result

        with patch("dspy.lm.query", side_effect=mock_query):
            response = lm.forward(prompt="test sync")

        assert response.choices[0].message.content == "Sync response"

    @pytest.mark.asyncio
    async def test_session_resume_passed_to_options(self):
        lm = ClaudeAgentLM()
        lm._session_id = "previous-session"

        mock_result = MagicMock()
        mock_result.result = "Resumed"
        mock_result.session_id = "previous-session"

        captured_options = {}

        async def mock_query(**kwargs):
            captured_options.update(kwargs)
            yield mock_result

        with patch("dspy.lm.query", side_effect=mock_query):
            await lm.aforward(prompt="continue")

        assert captured_options["options"].resume == "previous-session"

    @pytest.mark.asyncio
    async def test_system_prompt_extracted(self):
        lm = ClaudeAgentLM()

        captured_options = {}

        mock_result = MagicMock()
        mock_result.result = "OK"
        mock_result.session_id = "s1"

        async def mock_query(**kwargs):
            captured_options.update(kwargs)
            yield mock_result

        with patch("dspy.lm.query", side_effect=mock_query):
            await lm.aforward(messages=[
                {"role": "system", "content": "Be concise."},
                {"role": "user", "content": "Hi"},
            ])

        assert captured_options["options"].system_prompt == "Be concise."
        assert "Hi" in captured_options["prompt"]
```

**Step 2: Run test to verify it fails**

Run: `cd "/Volumes/OWC drive/Dev/dossier" && dspy/.venv/bin/python -m pytest tests/test_lm.py -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'dspy.lm'`

**Step 3: Write the implementation**

Create `dspy/lm.py`:
```python
"""ClaudeAgentLM — DSPy BaseLM backend routing through Claude Agent SDK.

All LLM calls go through Claude Code Max subscription. Zero API spend.
"""
from __future__ import annotations

import asyncio
from typing import Any

from dspy import BaseLM
from litellm import ModelResponse

from claude_agent_sdk import (
    ClaudeAgentOptions,
    ResultMessage,
    SystemMessage,
    query,
)


class ClaudeAgentLM(BaseLM):
    """Routes DSPy LLM calls through Claude Agent SDK (Max subscription).

    Usage:
        import dspy
        from dspy.lm import ClaudeAgentLM

        dspy.configure(lm=ClaudeAgentLM(model="sonnet"))
    """

    def __init__(
        self,
        model: str = "sonnet",
        max_turns: int = 1,
        timeout: int = 300,
        **kwargs: Any,
    ) -> None:
        super().__init__(
            model=f"claude-agent/{model}",
            model_type="chat",
            temperature=0.0,
            max_tokens=8000,
            cache=False,
            **kwargs,
        )
        self.cli_model = model
        self.max_turns = max_turns
        self.timeout = timeout
        self._session_id: str | None = None

    def forward(
        self,
        prompt: str | None = None,
        messages: list[dict[str, Any]] | None = None,
        **kwargs: Any,
    ) -> ModelResponse:
        """Sync wrapper — bridges DSPy's sync interface to Agent SDK's async API."""
        try:
            loop = asyncio.get_running_loop()
        except RuntimeError:
            loop = None

        if loop and loop.is_running():
            # Already in an async context — create a new thread
            import concurrent.futures
            with concurrent.futures.ThreadPoolExecutor() as pool:
                future = pool.submit(
                    asyncio.run,
                    self.aforward(prompt=prompt, messages=messages, **kwargs),
                )
                return future.result(timeout=self.timeout)
        else:
            return asyncio.run(
                self.aforward(prompt=prompt, messages=messages, **kwargs)
            )

    async def aforward(
        self,
        prompt: str | None = None,
        messages: list[dict[str, Any]] | None = None,
        **kwargs: Any,
    ) -> ModelResponse:
        """Call Claude via Agent SDK and return a ModelResponse."""
        messages = messages or [{"role": "user", "content": prompt or ""}]

        # Split system prompt from conversation
        system_parts: list[str] = []
        conv_parts: list[str] = []
        for msg in messages:
            role = msg.get("role", "user")
            content = msg.get("content", "")
            if role == "system":
                system_parts.append(content)
            elif role == "assistant":
                conv_parts.append(f"[Previous assistant response]:\n{content}")
            else:
                conv_parts.append(content)

        formatted_prompt = "\n\n".join(conv_parts)

        options = ClaudeAgentOptions(
            model=self.cli_model,
            max_turns=self.max_turns,
            system_prompt="\n".join(system_parts) if system_parts else None,
            allowed_tools=[],  # Pure LLM completion — no tool use
        )

        if self._session_id:
            options.resume = self._session_id

        result_text = ""
        async for message in query(prompt=formatted_prompt, options=options):
            # Capture session ID from init or result
            if isinstance(message, SystemMessage) and message.subtype == "init":
                self._session_id = message.data.get("session_id")
            elif isinstance(message, ResultMessage):
                self._session_id = message.session_id
                result_text = message.result or ""
            elif hasattr(message, "session_id"):
                self._session_id = message.session_id
            if hasattr(message, "result") and message.result:
                result_text = message.result

        prompt_tokens = len(str(messages)) // 4
        completion_tokens = len(result_text) // 4

        return ModelResponse(
            choices=[
                {
                    "index": 0,
                    "message": {"role": "assistant", "content": result_text},
                    "finish_reason": "stop",
                }
            ],
            model=self.model,
            usage={
                "prompt_tokens": prompt_tokens,
                "completion_tokens": completion_tokens,
                "total_tokens": prompt_tokens + completion_tokens,
            },
        )
```

**Step 4: Run tests to verify they pass**

Run: `cd "/Volumes/OWC drive/Dev/dossier" && PYTHONPATH=. dspy/.venv/bin/python -m pytest tests/test_lm.py -v`
Expected: All 8 tests PASS

**Step 5: Commit**

```bash
cd "/Volumes/OWC drive/Dev/dossier"
git add dspy/lm.py tests/test_lm.py
git commit -m "feat: add ClaudeAgentLM — DSPy backend via Agent SDK"
```

---

### Task 3: Signatures (7 Phase Contracts)

**Files:**
- Create: `dspy/signatures.py`
- Create: `tests/test_signatures.py`

**Step 1: Write the failing test**

Create `tests/test_signatures.py`:
```python
"""Tests for DSPy Signatures — one per Dossier phase."""
from __future__ import annotations

import dspy
import pytest

from dspy.signatures import (
    AcademicLandscape,
    ClaimsTriangulation,
    Discovery,
    FinalReport,
    MarketAnalysis,
    TechnicalAssessment,
    ValuationModel,
)


class TestSignatureStructure:
    """Verify each Signature has correct input/output fields."""

    def test_discovery_fields(self):
        sig = Discovery
        input_names = {f.name for f in sig.input_fields.values()}
        output_names = {f.name for f in sig.output_fields.values()}
        assert "domain" in input_names
        assert "company_profile" in output_names
        assert "tech_stack" in output_names

    def test_market_analysis_fields(self):
        sig = MarketAnalysis
        input_names = {f.name for f in sig.input_fields.values()}
        output_names = {f.name for f in sig.output_fields.values()}
        assert "company_profile" in input_names
        assert "competitors" in output_names
        assert "swot" in output_names

    def test_technical_assessment_fields(self):
        sig = TechnicalAssessment
        input_names = {f.name for f in sig.input_fields.values()}
        output_names = {f.name for f in sig.output_fields.values()}
        assert "company_profile" in input_names
        assert "architecture" in output_names

    def test_claims_triangulation_fields(self):
        sig = ClaimsTriangulation
        input_names = {f.name for f in sig.input_fields.values()}
        output_names = {f.name for f in sig.output_fields.values()}
        assert "discovery_report" in input_names
        assert "technical_report" in input_names
        assert "claims_inventory" in output_names
        assert "materiality_assessment" in output_names

    def test_academic_landscape_fields(self):
        sig = AcademicLandscape
        input_names = {f.name for f in sig.input_fields.values()}
        output_names = {f.name for f in sig.output_fields.values()}
        assert "company_profile" in input_names
        assert "publications" in output_names

    def test_valuation_model_fields(self):
        sig = ValuationModel
        input_names = {f.name for f in sig.input_fields.values()}
        output_names = {f.name for f in sig.output_fields.values()}
        assert "all_prior_reports" in input_names
        assert "replication_cost" in output_names

    def test_final_report_fields(self):
        sig = FinalReport
        input_names = {f.name for f in sig.input_fields.values()}
        output_names = {f.name for f in sig.output_fields.values()}
        assert "all_prior_reports" in input_names
        assert "executive_summary" in output_names

    def test_all_signatures_have_docstrings(self):
        """Docstrings are the optimizable instructions — they must exist."""
        for sig_cls in [
            Discovery, MarketAnalysis, TechnicalAssessment,
            ClaimsTriangulation, AcademicLandscape, ValuationModel, FinalReport,
        ]:
            assert sig_cls.__doc__ is not None
            assert len(sig_cls.__doc__.strip()) > 20

    def test_signature_count(self):
        """Exactly 7 signatures — one per phase."""
        from dspy import signatures as mod
        sig_classes = [
            v for v in vars(mod).values()
            if isinstance(v, type) and issubclass(v, dspy.Signature) and v is not dspy.Signature
        ]
        assert len(sig_classes) == 7
```

**Step 2: Run test to verify it fails**

Run: `cd "/Volumes/OWC drive/Dev/dossier" && PYTHONPATH=. dspy/.venv/bin/python -m pytest tests/test_signatures.py -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'dspy.signatures'`

**Step 3: Write the implementation**

Create `dspy/signatures.py`:
```python
"""DSPy Signatures for Dossier phases.

Each Signature defines the typed I/O contract for one phase.
The docstring becomes the optimizable instruction that MIPROv2 or
BootstrapFewShot can rewrite during compilation.
"""
from __future__ import annotations

import dspy


class Discovery(dspy.Signature):
    """Establish company identity and digital footprint from a domain name.
    Extract company profile, technology stack signals, and product description
    using WHOIS data, website content, social presence, and job postings.
    Every fact must cite its source. Distinguish confirmed facts from inferences."""

    domain: str = dspy.InputField(desc="Target company domain (e.g., okta.com)")
    whois_data: str = dspy.InputField(desc="Raw WHOIS JSON from whois_lookup.py")
    website_content: str = dspy.InputField(
        desc="Structured JSON: homepage, about, pricing, careers, docs content"
    )

    company_profile: str = dspy.OutputField(
        desc="Structured profile: legal name, founded, HQ, team size, funding, ICP, differentiators"
    )
    tech_stack: str = dspy.OutputField(
        desc="Detected technologies with evidence source per technology"
    )
    product_description: str = dspy.OutputField(
        desc="What the product does, target customer, key differentiators"
    )


class MarketAnalysis(dspy.Signature):
    """Analyze market size, dynamics, and competitive landscape.
    Estimate TAM/SAM/SOM with documented assumptions using both top-down
    (industry reports) and bottom-up (customers x ACV) approaches.
    Profile 5-10 competitors with funding, pricing, and segment overlap."""

    company_profile: str = dspy.InputField(desc="Company identity from Phase 1")
    product_description: str = dspy.InputField(desc="Product description from Phase 1")

    tam_sam_som: str = dspy.OutputField(
        desc="Market size estimates with assumptions: TAM, SAM, SOM"
    )
    competitors: str = dspy.OutputField(
        desc="5-10 competitor profiles: name, funding, pricing, differentiators, overlap"
    )
    swot: str = dspy.OutputField(desc="SWOT analysis using structured template")
    positioning: str = dspy.OutputField(
        desc="Magic quadrant positioning: Completeness of Vision vs Ability to Execute"
    )


class TechnicalAssessment(dspy.Signature):
    """Assess technical capabilities through open-source presence and GitHub activity.
    Analyze repository health, code quality signals, architecture patterns,
    dependencies, and open-source community engagement. Use gh CLI for data."""

    company_profile: str = dspy.InputField(desc="Company identity from Phase 1")
    github_org: str = dspy.InputField(desc="GitHub organization name(s) from Phase 1")

    architecture: str = dspy.OutputField(
        desc="Inferred architecture: monolith/microservices, cloud, API design, data layer"
    )
    repo_stats: str = dspy.OutputField(
        desc="Repository inventory: stars, forks, languages, commit frequency, contributors"
    )
    code_quality: str = dspy.OutputField(
        desc="Quality signals: CI/CD, tests, docs, security policy, dependency health"
    )


class ClaimsTriangulation(dspy.Signature):
    """Cross-reference marketing claims against technical evidence and 11 independent
    signal sources (Glassdoor, Blind, Reddit, HN, LinkedIn, layoff trackers, arXiv,
    Twitter/X, job boards, Product Hunt, review sites). Reconstruct what insiders know.
    Classify each claim as VERIFIED/PLAUSIBLE/UNVERIFIABLE/EXAGGERATED/CONTRADICTED.
    Rate materiality as CRITICAL/NOTABLE/MINOR."""

    discovery_report: str = dspy.InputField(desc="Full Phase 1 discovery output")
    technical_report: str = dspy.InputField(desc="Full Phase 3 technical output")

    claims_inventory: str = dspy.OutputField(
        desc="Table: claim | category | materiality | evidence | confidence"
    )
    signal_intelligence: str = dspy.OutputField(
        desc="11-source triangulation matrix with key signals per source"
    )
    triangulated_estimates: str = dspy.OutputField(
        desc="Team size, customer count, tech stack — 3+ independent sources each with spread"
    )
    materiality_assessment: str = dspy.OutputField(
        desc="CRITICAL/NOTABLE/MINOR classification with justification per claim"
    )


class AcademicLandscape(dspy.Signature):
    """Assess research credibility and IP landscape. Search arXiv for company
    and founder publications, patent databases, and open-source alternatives.
    Evaluate whether claimed technical innovations have academic basis."""

    company_profile: str = dspy.InputField(desc="Company identity from Phase 1")
    key_personnel: str = dspy.InputField(
        desc="Founder/CTO names and technical keywords from Phase 1"
    )

    ip_landscape: str = dspy.OutputField(desc="Patents filed, granted, and pending")
    publications: str = dspy.OutputField(
        desc="arXiv/Scholar papers by company employees with citation counts"
    )
    open_source_alternatives: str = dspy.OutputField(
        desc="Competing OSS projects: stars, activity, feature overlap, license"
    )


class ValuationModel(dspy.Signature):
    """Estimate company value and replication feasibility. Analyze business model,
    estimate SaaS metrics (ARR, growth, churn signals), and assess build-vs-buy
    including an agent swarm replication plan with per-component cost estimates."""

    all_prior_reports: str = dspy.InputField(
        desc="Concatenated outputs from Phases 1-5"
    )

    business_model: str = dspy.OutputField(
        desc="Revenue model, pricing tiers, ACV, customer segments, GTM motion"
    )
    saas_metrics: str = dspy.OutputField(
        desc="Estimated ARR range, customer count, growth/churn signals with confidence"
    )
    replication_cost: str = dspy.OutputField(
        desc="Per-component: agent-hours, dependencies, what can't be automated"
    )
    build_vs_buy: str = dspy.OutputField(
        desc="Score 1-4 on core tech, data moat, integrations, UX, domain expertise"
    )


class FinalReport(dspy.Signature):
    """Synthesize all prior phases into a unified due diligence report.
    Build a confidence matrix (Data Quality x Analysis Confidence per section).
    Write a 2-page executive summary with recommendation:
    INVESTIGATE / PROCEED WITH CAUTION / STRONG CANDIDATE / PASS.
    The report must work even with missing sections — note gaps explicitly."""

    all_prior_reports: str = dspy.InputField(
        desc="Concatenated outputs from Phases 1-6"
    )

    executive_summary: str = dspy.OutputField(
        desc="2-page overview: strengths, risks, assessment, recommendation"
    )
    full_report: str = dspy.OutputField(
        desc="Complete PRD-format report with confidence matrix and next steps"
    )
```

**Step 4: Run tests to verify they pass**

Run: `cd "/Volumes/OWC drive/Dev/dossier" && PYTHONPATH=. dspy/.venv/bin/python -m pytest tests/test_signatures.py -v`
Expected: All 9 tests PASS

**Step 5: Commit**

```bash
cd "/Volumes/OWC drive/Dev/dossier"
git add dspy/signatures.py tests/test_signatures.py
git commit -m "feat: add 7 DSPy Signatures — typed I/O contracts per phase"
```

---

### Task 4: Metrics (Evaluation Functions)

**Files:**
- Create: `dspy/metrics.py`
- Create: `tests/test_metrics.py`

**Step 1: Write the failing test**

Create `tests/test_metrics.py`:
```python
"""Tests for dossier evaluation metrics."""
from __future__ import annotations

import pytest

from dspy.metrics import (
    dossier_phase_metric,
    section_completeness,
    source_diversity,
    substantiation_ratio,
)


class TestSectionCompleteness:
    def test_all_sections_present(self):
        text = "## Company Identity\nOkta\n## Tech Stack\nJava\n## Key Findings\nGood"
        expected = ["Company Identity", "Tech Stack", "Key Findings"]
        assert section_completeness(text, expected) == 1.0

    def test_some_sections_missing(self):
        text = "## Company Identity\nOkta\n## Key Findings\nGood"
        expected = ["Company Identity", "Tech Stack", "Key Findings"]
        assert section_completeness(text, expected) == pytest.approx(2 / 3, abs=0.01)

    def test_no_sections(self):
        text = "Just some plain text without headers"
        expected = ["Company Identity", "Tech Stack"]
        assert section_completeness(text, expected) == 0.0

    def test_empty_expected(self):
        text = "## Something\ntext"
        assert section_completeness(text, []) == 1.0


class TestSourceDiversity:
    def test_multiple_sources(self):
        text = """
        ## Sources
        - Glassdoor reviews indicate...
        - LinkedIn profiles show...
        - Reddit discussions mention...
        - Hacker News thread confirms...
        """
        score = source_diversity(text)
        assert score >= 4 / 11

    def test_no_sources(self):
        text = "No sources mentioned at all."
        assert source_diversity(text) == 0.0

    def test_all_eleven_sources(self):
        text = (
            "Glassdoor LinkedIn Reddit HackerNews Blind "
            "layoffs.fyi arXiv Twitter job posting "
            "Product Hunt G2 Capterra Trustpilot"
        )
        assert source_diversity(text) >= 9 / 11


class TestSubstantiationRatio:
    def test_all_substantiated(self):
        text = """
        | Claim | Evidence |
        |-------|----------|
        | Fast API | GitHub repo shows 50ms p99 |
        | SOC2 | Certificate published on security page |
        """
        assert substantiation_ratio(text) > 0.5

    def test_no_table(self):
        text = "No claims table here."
        assert substantiation_ratio(text) == 0.0


class TestCompositeMetric:
    def test_returns_float_between_0_and_1(self):
        text = "## Company Identity\nOkta\n## Key Findings\nSome finding"
        expected_sections = ["Company Identity", "Key Findings"]
        score = dossier_phase_metric(text, expected_sections)
        assert 0.0 <= score <= 1.0

    def test_high_quality_output_scores_higher(self):
        good = (
            "## Company Identity\nOkta Inc\n"
            "## Tech Stack\nJava, Go\n"
            "## Key Findings\nStrong presence\n"
            "Source: Glassdoor, LinkedIn, Reddit, G2\n"
            "| Claim | Evidence |\n|---|---|\n| Fast | GitHub benchmarks |"
        )
        bad = "Some text with no structure"
        sections = ["Company Identity", "Tech Stack", "Key Findings"]
        assert dossier_phase_metric(good, sections) > dossier_phase_metric(bad, sections)
```

**Step 2: Run test to verify it fails**

Run: `cd "/Volumes/OWC drive/Dev/dossier" && PYTHONPATH=. dspy/.venv/bin/python -m pytest tests/test_metrics.py -v`
Expected: FAIL with `ModuleNotFoundError`

**Step 3: Write the implementation**

Create `dspy/metrics.py`:
```python
"""Evaluation metrics for Dossier phase outputs.

These run locally (no LLM calls) — they parse output text to score quality.
Used by DSPy optimizers as the metric() function.
"""
from __future__ import annotations

import re

# The 11 signal source types from Phase 4's triangulation matrix
SOURCE_PATTERNS: list[tuple[str, re.Pattern[str]]] = [
    ("glassdoor", re.compile(r"glassdoor", re.IGNORECASE)),
    ("blind", re.compile(r"\bblind\b", re.IGNORECASE)),
    ("reddit", re.compile(r"reddit", re.IGNORECASE)),
    ("hackernews", re.compile(r"hacker\s*news|ycombinator|\bHN\b", re.IGNORECASE)),
    ("linkedin", re.compile(r"linkedin", re.IGNORECASE)),
    ("layoffs", re.compile(r"layoffs?\.fyi|layoff tracker", re.IGNORECASE)),
    ("arxiv", re.compile(r"arxiv|arXiv|google\s*scholar", re.IGNORECASE)),
    ("twitter", re.compile(r"twitter|𝕏|\bX\b.*post", re.IGNORECASE)),
    ("jobs", re.compile(r"job\s*(?:posting|board|listing)|indeed|hired", re.IGNORECASE)),
    ("producthunt", re.compile(r"product\s*hunt|indie\s*hackers", re.IGNORECASE)),
    ("reviews", re.compile(r"\bG2\b|capterra|trustpilot|peer\s*review", re.IGNORECASE)),
]


def section_completeness(text: str, expected_sections: list[str]) -> float:
    """Score 0-1: what fraction of expected markdown sections are present."""
    if not expected_sections:
        return 1.0
    found = 0
    for section in expected_sections:
        # Match ## Section Name or ### Section Name (case-insensitive)
        pattern = re.compile(rf"^#{2,3}\s+{re.escape(section)}", re.MULTILINE | re.IGNORECASE)
        if pattern.search(text):
            found += 1
    return found / len(expected_sections)


def source_diversity(text: str) -> float:
    """Score 0-1: fraction of 11 signal source types mentioned."""
    found = sum(1 for _, pattern in SOURCE_PATTERNS if pattern.search(text))
    return found / len(SOURCE_PATTERNS)


def substantiation_ratio(text: str) -> float:
    """Score 0-1: fraction of claims table rows that have non-empty evidence."""
    # Find markdown table rows (lines starting with |)
    table_rows = re.findall(r"^\|(.+)\|$", text, re.MULTILINE)
    # Skip header and separator rows
    data_rows = [
        row for row in table_rows
        if not re.match(r"^[\s\-|:]+$", row) and "Claim" not in row and "Evidence" not in row
    ]
    if not data_rows:
        return 0.0

    substantiated = 0
    for row in data_rows:
        cells = [c.strip() for c in row.split("|")]
        # A row is substantiated if any cell after the first has content
        if any(len(cell) > 3 for cell in cells[1:]):
            substantiated += 1

    return substantiated / len(data_rows)


def dossier_phase_metric(text: str, expected_sections: list[str]) -> float:
    """Composite metric for a single dossier phase output.

    Combines:
    - Section completeness (40%)
    - Source diversity (30%)
    - Substantiation ratio (30%)
    """
    completeness = section_completeness(text, expected_sections)
    diversity = source_diversity(text)
    substantiation = substantiation_ratio(text)

    return 0.4 * completeness + 0.3 * diversity + 0.3 * substantiation
```

**Step 4: Run tests to verify they pass**

Run: `cd "/Volumes/OWC drive/Dev/dossier" && PYTHONPATH=. dspy/.venv/bin/python -m pytest tests/test_metrics.py -v`
Expected: All tests PASS

**Step 5: Commit**

```bash
cd "/Volumes/OWC drive/Dev/dossier"
git add dspy/metrics.py tests/test_metrics.py
git commit -m "feat: add dossier evaluation metrics — completeness, diversity, substantiation"
```

---

### Task 5: Training Data Loader

**Files:**
- Create: `dspy/loader.py`
- Create: `tests/test_loader.py`

**Step 1: Write the failing test**

Create `tests/test_loader.py`:
```python
"""Tests for training data loader — converts dossier outputs to dspy.Examples."""
from __future__ import annotations

from pathlib import Path

import dspy
import pytest

from dspy.loader import (
    PHASE_EXPECTED_SECTIONS,
    load_dossier_outputs,
    load_single_dossier,
    score_dossier,
)


class TestLoadSingleDossier:
    def test_loads_okta(self, output_dir):
        okta_dir = output_dir / "okta.com"
        if not okta_dir.exists():
            pytest.skip("okta.com output not present")
        result = load_single_dossier(okta_dir)
        assert result is not None
        assert result["domain"] == "okta.com"
        assert "discovery" in result
        assert "claims" in result

    def test_returns_none_for_incomplete(self, tmp_path):
        """Incomplete dossier (missing phases) returns None."""
        incomplete = tmp_path / "incomplete.com"
        incomplete.mkdir()
        (incomplete / "01-discovery.md").write_text("# Discovery\n")
        # Missing other phases
        result = load_single_dossier(incomplete)
        assert result is None


class TestScoreDossier:
    def test_scores_okta(self, output_dir):
        okta_dir = output_dir / "okta.com"
        if not okta_dir.exists():
            pytest.skip("okta.com output not present")
        dossier = load_single_dossier(okta_dir)
        scores = score_dossier(dossier)
        assert "p1" in scores
        assert "p4" in scores
        assert all(0.0 <= v <= 1.0 for v in scores.values())


class TestLoadDossierOutputs:
    def test_loads_all_complete_dossiers(self, output_dir):
        if not output_dir.exists():
            pytest.skip("output directory not present")
        examples = load_dossier_outputs(output_dir)
        # Should find at least okta.com if outputs exist
        assert isinstance(examples, list)
        if examples:
            assert isinstance(examples[0], dspy.Example)


class TestPhaseExpectedSections:
    def test_all_seven_phases_defined(self):
        assert len(PHASE_EXPECTED_SECTIONS) == 7
        assert "p1" in PHASE_EXPECTED_SECTIONS
        assert "p7" in PHASE_EXPECTED_SECTIONS
```

**Step 2: Run test to verify it fails**

Run: `cd "/Volumes/OWC drive/Dev/dossier" && PYTHONPATH=. dspy/.venv/bin/python -m pytest tests/test_loader.py -v`
Expected: FAIL with `ModuleNotFoundError`

**Step 3: Write the implementation**

Create `dspy/loader.py`:
```python
"""Load completed dossier outputs as DSPy training examples.

Scans output/ for domain directories with all 7 phases complete.
Scores each phase using metrics.py and produces dspy.Example objects.
"""
from __future__ import annotations

from pathlib import Path
from typing import Any

import dspy

from dspy.metrics import dossier_phase_metric

# Expected markdown sections per phase (used for completeness scoring)
PHASE_EXPECTED_SECTIONS: dict[str, list[str]] = {
    "p1": ["Company Identity", "Domain & Infrastructure", "Digital Footprint",
           "Tech Stack Signals", "Key Findings"],
    "p2": ["Problem Statement", "Market Size", "Competitive Landscape",
           "SWOT Analysis", "Key Findings"],
    "p3": ["GitHub Presence", "Architecture", "Code Quality",
           "Dependencies", "Key Findings"],
    "p4": ["Claims Inventory", "Internal Signal Intelligence",
           "Triangulated Estimates", "Critical Gaps", "Key Findings"],
    "p5": ["Publications", "Patent Landscape",
           "Open-Source Alternatives", "Key Findings"],
    "p6": ["Business Model", "SaaS Metrics", "Replication",
           "Build vs Buy", "Key Findings"],
    "p7": ["Executive Summary", "Confidence Matrix", "Next Steps"],
}

PHASE_FILES: dict[str, str] = {
    "p1": "01-discovery.md",
    "p2": "02-market.md",
    "p3": "03-technical.md",
    "p4": "04-claims.md",
    "p5": "05-academic.md",
    "p6": "06-valuation.md",
    "p7": "07-report.md",
}


def load_single_dossier(domain_dir: Path) -> dict[str, Any] | None:
    """Load all phase outputs for a single domain.

    Returns None if any required phase file is missing.
    """
    domain = domain_dir.name
    result: dict[str, Any] = {"domain": domain}

    phase_keys = {
        "p1": "discovery",
        "p2": "market",
        "p3": "technical",
        "p4": "claims",
        "p5": "academic",
        "p6": "valuation",
        "p7": "report",
    }

    for phase_id, file_name in PHASE_FILES.items():
        path = domain_dir / file_name
        if not path.exists():
            return None  # Incomplete dossier
        result[phase_keys[phase_id]] = path.read_text()

    # Also load executive summary if available
    exec_path = domain_dir / "executive-summary.md"
    if exec_path.exists():
        result["executive_summary"] = exec_path.read_text()

    return result


def score_dossier(dossier: dict[str, Any]) -> dict[str, float]:
    """Score each phase of a loaded dossier using metrics."""
    phase_text_keys = {
        "p1": "discovery",
        "p2": "market",
        "p3": "technical",
        "p4": "claims",
        "p5": "academic",
        "p6": "valuation",
        "p7": "report",
    }

    scores: dict[str, float] = {}
    for phase_id, text_key in phase_text_keys.items():
        text = dossier.get(text_key, "")
        expected = PHASE_EXPECTED_SECTIONS.get(phase_id, [])
        scores[phase_id] = dossier_phase_metric(text, expected)

    return scores


def load_dossier_outputs(output_dir: Path) -> list[dspy.Example]:
    """Load all complete dossier outputs as DSPy training examples.

    Each Example contains:
    - domain: str
    - discovery, market, technical, claims, academic, valuation, report: str (phase texts)
    - scores: dict[str, float] (per-phase metric scores)
    """
    examples: list[dspy.Example] = []

    if not output_dir.exists():
        return examples

    for domain_dir in sorted(output_dir.iterdir()):
        if not domain_dir.is_dir():
            continue
        # Skip non-domain directories
        if not (domain_dir / "01-discovery.md").exists():
            continue

        dossier = load_single_dossier(domain_dir)
        if dossier is None:
            continue

        scores = score_dossier(dossier)
        dossier["scores"] = scores

        example = dspy.Example(**dossier).with_inputs("domain")
        examples.append(example)

    return examples
```

**Step 4: Run tests to verify they pass**

Run: `cd "/Volumes/OWC drive/Dev/dossier" && PYTHONPATH=. dspy/.venv/bin/python -m pytest tests/test_loader.py -v`
Expected: All tests PASS (some may skip if output/ is empty)

**Step 5: Commit**

```bash
cd "/Volumes/OWC drive/Dev/dossier"
git add dspy/loader.py tests/test_loader.py
git commit -m "feat: add training data loader — dossier outputs to DSPy examples"
```

---

### Task 6: Modules (Phase Wrappers)

**Files:**
- Create: `dspy/modules.py`
- Create: `tests/test_modules.py`

**Step 1: Write the failing test**

Create `tests/test_modules.py`:
```python
"""Tests for DSPy Module wrappers — one per Dossier phase."""
from __future__ import annotations

from unittest.mock import MagicMock, patch

import dspy
import pytest

from dspy.modules import DossierPipeline, PhaseModule


class TestPhaseModule:
    def test_init_stores_signature(self):
        from dspy.signatures import Discovery
        mod = PhaseModule(Discovery)
        assert mod.signature_cls is Discovery
        assert mod.predictor is not None

    def test_forward_calls_predictor(self):
        from dspy.signatures import Discovery
        mod = PhaseModule(Discovery)
        # Mock the predictor
        mock_pred = MagicMock()
        mock_pred.return_value = dspy.Prediction(
            company_profile="Okta Inc",
            tech_stack="Java, Go",
            product_description="Identity platform",
        )
        mod.predictor = mock_pred

        result = mod.forward(
            domain="okta.com",
            whois_data="{}",
            website_content="{}",
        )
        assert result.company_profile == "Okta Inc"
        mock_pred.assert_called_once()


class TestDossierPipeline:
    def test_has_seven_phase_modules(self):
        pipeline = DossierPipeline()
        assert len(pipeline.phases) == 7
        assert "p1" in pipeline.phases
        assert "p7" in pipeline.phases

    def test_phase_order(self):
        pipeline = DossierPipeline()
        keys = list(pipeline.phases.keys())
        assert keys == ["p1", "p2", "p3", "p4", "p5", "p6", "p7"]
```

**Step 2: Run test to verify it fails**

Run: `cd "/Volumes/OWC drive/Dev/dossier" && PYTHONPATH=. dspy/.venv/bin/python -m pytest tests/test_modules.py -v`
Expected: FAIL with `ModuleNotFoundError`

**Step 3: Write the implementation**

Create `dspy/modules.py`:
```python
"""DSPy Module wrappers for Dossier phases.

Each PhaseModule wraps a Signature with a dspy.Predict (or ChainOfThought)
predictor. The DossierPipeline composes all 7 phases.
"""
from __future__ import annotations

from collections import OrderedDict
from typing import Any

import dspy

from dspy.signatures import (
    AcademicLandscape,
    ClaimsTriangulation,
    Discovery,
    FinalReport,
    MarketAnalysis,
    TechnicalAssessment,
    ValuationModel,
)


class PhaseModule(dspy.Module):
    """Wraps a single Dossier phase Signature as a DSPy Module."""

    def __init__(self, signature_cls: type[dspy.Signature]) -> None:
        super().__init__()
        self.signature_cls = signature_cls
        self.predictor = dspy.ChainOfThought(signature_cls)

    def forward(self, **kwargs: Any) -> dspy.Prediction:
        return self.predictor(**kwargs)


class DossierPipeline(dspy.Module):
    """Composes all 7 Dossier phases as a DSPy Module.

    Note: In compile mode, phases run independently (one at a time).
    The Ralph Loop handles DAG-aware parallel execution at runtime.
    """

    def __init__(self) -> None:
        super().__init__()
        self.phases: OrderedDict[str, PhaseModule] = OrderedDict(
            p1=PhaseModule(Discovery),
            p2=PhaseModule(MarketAnalysis),
            p3=PhaseModule(TechnicalAssessment),
            p4=PhaseModule(ClaimsTriangulation),
            p5=PhaseModule(AcademicLandscape),
            p6=PhaseModule(ValuationModel),
            p7=PhaseModule(FinalReport),
        )

    def forward(self, **kwargs: Any) -> dspy.Prediction:
        """Run all phases sequentially for optimization.

        In production, the Ralph Loop handles parallelism.
        Here we run sequentially so DSPy can trace the full pipeline.
        """
        results: dict[str, dspy.Prediction] = {}

        # P1: Discovery
        results["p1"] = self.phases["p1"](
            domain=kwargs.get("domain", ""),
            whois_data=kwargs.get("whois_data", ""),
            website_content=kwargs.get("website_content", ""),
        )

        p1_profile = results["p1"].company_profile
        p1_product = results["p1"].product_description

        # P2: Market (needs P1)
        results["p2"] = self.phases["p2"](
            company_profile=p1_profile,
            product_description=p1_product,
        )

        # P3: Technical (needs P1)
        results["p3"] = self.phases["p3"](
            company_profile=p1_profile,
            github_org=kwargs.get("github_org", ""),
        )

        # P4: Claims (needs P1 + P3)
        results["p4"] = self.phases["p4"](
            discovery_report=p1_profile,
            technical_report=results["p3"].architecture,
        )

        # P5: Academic (needs P1)
        results["p5"] = self.phases["p5"](
            company_profile=p1_profile,
            key_personnel=kwargs.get("key_personnel", ""),
        )

        # P6: Valuation (needs P1-P5)
        prior_text = "\n\n---\n\n".join(
            str(results[f"p{i}"]) for i in range(1, 6)
        )
        results["p6"] = self.phases["p6"](all_prior_reports=prior_text)

        # P7: Report (needs P1-P6)
        all_text = "\n\n---\n\n".join(
            str(results[f"p{i}"]) for i in range(1, 7)
        )
        results["p7"] = self.phases["p7"](all_prior_reports=all_text)

        return dspy.Prediction(
            executive_summary=results["p7"].executive_summary,
            full_report=results["p7"].full_report,
        )
```

**Step 4: Run tests to verify they pass**

Run: `cd "/Volumes/OWC drive/Dev/dossier" && PYTHONPATH=. dspy/.venv/bin/python -m pytest tests/test_modules.py -v`
Expected: All tests PASS

**Step 5: Commit**

```bash
cd "/Volumes/OWC drive/Dev/dossier"
git add dspy/modules.py tests/test_modules.py
git commit -m "feat: add DSPy Modules — phase wrappers and pipeline composition"
```

---

### Task 7: Compile Driver

**Files:**
- Create: `dspy/compile.py`
- Create: `tests/test_compile.py`

**Step 1: Write the failing test**

Create `tests/test_compile.py`:
```python
"""Tests for the DSPy compile driver."""
from __future__ import annotations

from pathlib import Path
from unittest.mock import MagicMock, patch

import dspy
import pytest

from dspy.compile import make_metric_fn, compile_dossier


class TestMakeMetricFn:
    def test_returns_callable(self):
        fn = make_metric_fn()
        assert callable(fn)

    def test_scores_example_with_prediction(self):
        fn = make_metric_fn()
        example = dspy.Example(
            domain="test.com",
            scores={"p7": 0.8},
        )
        prediction = dspy.Prediction(
            executive_summary="## Key Strengths\n1. Good\n## Key Risks\n1. Bad",
            full_report="## Executive Summary\n## Confidence Matrix\n## Next Steps\n",
        )
        score = fn(example, prediction)
        assert isinstance(score, float)
        assert 0.0 <= score <= 1.0
```

**Step 2: Run test to verify it fails**

Run: `cd "/Volumes/OWC drive/Dev/dossier" && PYTHONPATH=. dspy/.venv/bin/python -m pytest tests/test_compile.py -v`
Expected: FAIL with `ModuleNotFoundError`

**Step 3: Write the implementation**

Create `dspy/compile.py`:
```python
"""DSPy compile driver — optimize Dossier phase prompts.

Usage:
    cd "/Volumes/OWC drive/Dev/dossier"
    PYTHONPATH=. dspy/.venv/bin/python -m dspy.compile

All LLM calls route through Claude Agent SDK (Max subscription).
"""
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

import dspy

from dspy.loader import load_dossier_outputs, PHASE_EXPECTED_SECTIONS
from dspy.lm import ClaudeAgentLM
from dspy.metrics import dossier_phase_metric
from dspy.modules import DossierPipeline


DOSSIER_ROOT = Path(__file__).parent.parent
OUTPUT_DIR = DOSSIER_ROOT / "output"
COMPILED_DIR = Path(__file__).parent / "compiled"


def make_metric_fn() -> Any:
    """Create a metric function for DSPy optimization.

    Scores the final report phase (P7) since it depends on all prior phases.
    """
    p7_sections = PHASE_EXPECTED_SECTIONS["p7"]

    def metric(example: dspy.Example, prediction: dspy.Prediction, trace=None) -> float:
        report_text = getattr(prediction, "full_report", "") or ""
        summary_text = getattr(prediction, "executive_summary", "") or ""
        combined = f"{summary_text}\n\n{report_text}"
        return dossier_phase_metric(combined, p7_sections)

    return metric


def compile_dossier(
    model: str = "sonnet",
    num_candidates: int = 5,
    max_bootstrapped_demos: int = 2,
    max_labeled_demos: int = 1,
) -> dspy.Module | None:
    """Run DSPy optimization on the Dossier pipeline.

    Args:
        model: Claude model name (sonnet, opus, haiku)
        num_candidates: Number of random seeds for BootstrapFewShotWithRandomSearch
        max_bootstrapped_demos: Max bootstrapped demonstrations per module
        max_labeled_demos: Max labeled demonstrations per module

    Returns:
        Optimized DossierPipeline module, or None if rate limited.
    """
    # Configure LM
    lm = ClaudeAgentLM(model=model)
    dspy.configure(lm=lm)

    # Load training data
    trainset = load_dossier_outputs(OUTPUT_DIR)
    if len(trainset) < 2:
        print(f"Need at least 2 complete dossiers, found {len(trainset)}.")
        print(f"Domains found: {[e.domain for e in trainset]}")
        sys.exit(1)

    print(f"Loaded {len(trainset)} training examples: {[e.domain for e in trainset]}")

    # Build program
    program = DossierPipeline()
    metric = make_metric_fn()

    # Optimize
    optimizer = dspy.BootstrapFewShotWithRandomSearch(
        metric=metric,
        max_bootstrapped_demos=max_bootstrapped_demos,
        max_labeled_demos=max_labeled_demos,
        num_candidate_programs=num_candidates,
    )

    try:
        optimized = optimizer.compile(program, trainset=trainset)
    except RuntimeError as e:
        if "rate limit" in str(e).lower():
            session_id = getattr(lm, "_session_id", None)
            print(f"Rate limited. Session ID for resume: {session_id}")
            return None
        raise

    # Save compiled program
    COMPILED_DIR.mkdir(parents=True, exist_ok=True)
    output_path = COMPILED_DIR / "dossier_latest.json"
    optimized.save(str(output_path))
    print(f"Saved optimized program to {output_path}")

    return optimized


def main() -> None:
    """CLI entry point."""
    import argparse

    parser = argparse.ArgumentParser(description="Compile Dossier prompts with DSPy")
    parser.add_argument("--model", default="sonnet", help="Claude model (sonnet, opus)")
    parser.add_argument("--candidates", type=int, default=5, help="Number of candidate programs")
    parser.add_argument("--bootstrapped-demos", type=int, default=2)
    parser.add_argument("--labeled-demos", type=int, default=1)
    args = parser.parse_args()

    compile_dossier(
        model=args.model,
        num_candidates=args.candidates,
        max_bootstrapped_demos=args.bootstrapped_demos,
        max_labeled_demos=args.labeled_demos,
    )


if __name__ == "__main__":
    main()
```

**Step 4: Run tests to verify they pass**

Run: `cd "/Volumes/OWC drive/Dev/dossier" && PYTHONPATH=. dspy/.venv/bin/python -m pytest tests/test_compile.py -v`
Expected: All tests PASS

**Step 5: Commit**

```bash
cd "/Volumes/OWC drive/Dev/dossier"
git add dspy/compile.py tests/test_compile.py
git commit -m "feat: add DSPy compile driver — rate-limit-aware optimizer"
```

---

### Task 8: Export (Compiled Instructions to Prompts)

**Files:**
- Create: `dspy/export.py`
- Create: `tests/test_export.py`

**Step 1: Write the failing test**

Create `tests/test_export.py`:
```python
"""Tests for exporting optimized instructions back to prompt files."""
from __future__ import annotations

from pathlib import Path

import pytest

from dspy.export import (
    extract_instructions,
    write_optimized_prompt,
    PHASE_PROMPT_FILES,
)


class TestPhasePromptFiles:
    def test_has_seven_entries(self):
        assert len(PHASE_PROMPT_FILES) == 7

    def test_all_files_exist(self, dossier_root):
        prompts_dir = dossier_root / "prompts"
        for phase_id, filename in PHASE_PROMPT_FILES.items():
            path = prompts_dir / filename
            assert path.exists(), f"Missing prompt file: {path}"


class TestExtractInstructions:
    def test_extracts_docstring_from_module(self):
        from dspy.modules import DossierPipeline
        pipeline = DossierPipeline()
        instructions = extract_instructions(pipeline)
        assert "p1" in instructions
        assert "p7" in instructions
        assert isinstance(instructions["p1"], str)
        assert len(instructions["p1"]) > 10


class TestWriteOptimizedPrompt:
    def test_writes_instruction_header(self, tmp_path):
        original = "# Phase 1: Discovery\n\nOriginal instructions here.\n\n## Steps\n1. Do thing\n"
        prompt_file = tmp_path / "p1-discovery.md"
        prompt_file.write_text(original)

        new_instruction = "Improved instruction from DSPy optimization."
        write_optimized_prompt(prompt_file, new_instruction)

        result = prompt_file.read_text()
        assert "Improved instruction from DSPy optimization." in result
        # Original steps should be preserved
        assert "## Steps" in result

    def test_preserves_steps_section(self, tmp_path):
        original = (
            "# Phase 4: Claims Validation\n\n"
            "Cross-reference marketing claims.\n\n"
            "## Steps\n\n"
            "### 4.1 Claims Extraction\n"
            "Extract from Phase 1.\n"
        )
        prompt_file = tmp_path / "p4-claims.md"
        prompt_file.write_text(original)

        write_optimized_prompt(prompt_file, "New DSPy-optimized instruction.")

        result = prompt_file.read_text()
        assert "New DSPy-optimized instruction." in result
        assert "### 4.1 Claims Extraction" in result
```

**Step 2: Run test to verify it fails**

Run: `cd "/Volumes/OWC drive/Dev/dossier" && PYTHONPATH=. dspy/.venv/bin/python -m pytest tests/test_export.py -v`
Expected: FAIL with `ModuleNotFoundError`

**Step 3: Write the implementation**

Create `dspy/export.py`:
```python
"""Export optimized DSPy instructions back to Dossier prompt markdown files.

Replaces the instruction paragraph (between the # title and ## Steps) in each
phase prompt file with the DSPy-optimized instruction. Preserves all other content.
"""
from __future__ import annotations

import re
import shutil
from datetime import datetime
from pathlib import Path

import dspy

from dspy.modules import DossierPipeline

DOSSIER_ROOT = Path(__file__).parent.parent
PROMPTS_DIR = DOSSIER_ROOT / "prompts"

PHASE_PROMPT_FILES: dict[str, str] = {
    "p1": "p1-discovery.md",
    "p2": "p2-market.md",
    "p3": "p3-technical.md",
    "p4": "p4-claims.md",
    "p5": "p5-academic.md",
    "p6": "p6-valuation.md",
    "p7": "p7-report.md",
}


def extract_instructions(pipeline: DossierPipeline) -> dict[str, str]:
    """Extract the current instruction (docstring) from each phase module.

    After DSPy optimization, these docstrings contain the optimized instructions.
    """
    instructions: dict[str, str] = {}
    for phase_id, module in pipeline.phases.items():
        sig_cls = module.signature_cls
        doc = sig_cls.__doc__ or ""
        instructions[phase_id] = doc.strip()
    return instructions


def write_optimized_prompt(prompt_file: Path, new_instruction: str) -> None:
    """Replace the instruction section in a prompt file.

    The instruction is the text between the first # heading and the first ## heading.
    Everything from ## onward is preserved as-is.
    """
    content = prompt_file.read_text()

    # Find the first ## heading (Steps, Goal, etc.)
    match = re.search(r"^(## .+)$", content, re.MULTILINE)

    if match:
        # Everything before the first ## heading gets replaced
        before_steps = content[: match.start()]
        after_steps = content[match.start() :]

        # Preserve the # title line
        title_match = re.match(r"^(# .+\n)", before_steps)
        title = title_match.group(1) if title_match else ""

        new_content = f"{title}\n{new_instruction}\n\n{after_steps}"
    else:
        # No ## heading found — replace everything after title
        title_match = re.match(r"^(# .+\n)", content)
        title = title_match.group(1) if title_match else ""
        new_content = f"{title}\n{new_instruction}\n"

    prompt_file.write_text(new_content)


def export_to_prompts(pipeline: DossierPipeline, backup: bool = True) -> None:
    """Export all optimized instructions from a compiled pipeline to prompt files.

    Args:
        pipeline: The optimized DossierPipeline from DSPy compilation
        backup: If True, create timestamped backup of original prompts
    """
    instructions = extract_instructions(pipeline)

    if backup:
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        backup_dir = PROMPTS_DIR / f"backup-{timestamp}"
        backup_dir.mkdir(exist_ok=True)
        for filename in PHASE_PROMPT_FILES.values():
            src = PROMPTS_DIR / filename
            if src.exists():
                shutil.copy2(src, backup_dir / filename)

    for phase_id, instruction in instructions.items():
        filename = PHASE_PROMPT_FILES.get(phase_id)
        if not filename:
            continue
        prompt_file = PROMPTS_DIR / filename
        if not prompt_file.exists():
            continue
        write_optimized_prompt(prompt_file, instruction)

    print(f"Exported optimized instructions to {PROMPTS_DIR}")
    if backup:
        print(f"Originals backed up to {backup_dir}")
```

**Step 4: Run tests to verify they pass**

Run: `cd "/Volumes/OWC drive/Dev/dossier" && PYTHONPATH=. dspy/.venv/bin/python -m pytest tests/test_export.py -v`
Expected: All tests PASS

**Step 5: Commit**

```bash
cd "/Volumes/OWC drive/Dev/dossier"
git add dspy/export.py tests/test_export.py
git commit -m "feat: add export — compiled DSPy instructions to prompt markdown"
```

---

### Task 9: Integration Test + __main__ Entry Point

**Files:**
- Create: `dspy/__main__.py`
- Create: `tests/test_integration.py`

**Step 1: Write the integration test**

Create `tests/test_integration.py`:
```python
"""Integration tests — verify full pipeline wiring without live LLM calls."""
from __future__ import annotations

from pathlib import Path
from unittest.mock import MagicMock, patch

import dspy
import pytest

from dspy.compile import compile_dossier, make_metric_fn
from dspy.export import export_to_prompts, extract_instructions
from dspy.loader import load_dossier_outputs
from dspy.modules import DossierPipeline


class TestEndToEnd:
    def test_loader_to_metric(self, output_dir):
        """Training data loads and metric scores it."""
        if not output_dir.exists():
            pytest.skip("No output directory")
        examples = load_dossier_outputs(output_dir)
        if not examples:
            pytest.skip("No complete dossiers")

        metric = make_metric_fn()
        # Score the first example's report as if it were a prediction
        ex = examples[0]
        pred = dspy.Prediction(
            executive_summary=ex.get("executive_summary", ""),
            full_report=ex.report,
        )
        score = metric(ex, pred)
        assert 0.0 <= score <= 1.0
        print(f"  {ex.domain}: score={score:.3f}")

    def test_pipeline_structure(self):
        """Pipeline has correct phase ordering and module types."""
        pipeline = DossierPipeline()
        assert list(pipeline.phases.keys()) == [
            "p1", "p2", "p3", "p4", "p5", "p6", "p7"
        ]
        for mod in pipeline.phases.values():
            assert hasattr(mod, "predictor")

    def test_extract_and_export_round_trip(self, tmp_path):
        """Instructions extract from pipeline and write to files."""
        pipeline = DossierPipeline()
        instructions = extract_instructions(pipeline)
        assert len(instructions) == 7

        # Create fake prompt files
        for phase_id, inst in instructions.items():
            from dspy.export import PHASE_PROMPT_FILES
            filename = PHASE_PROMPT_FILES[phase_id]
            prompt_file = tmp_path / filename
            prompt_file.write_text(f"# Phase\n\nOriginal.\n\n## Steps\n1. Do thing\n")

        # Monkeypatch PROMPTS_DIR
        with patch("dspy.export.PROMPTS_DIR", tmp_path):
            export_to_prompts(pipeline, backup=False)

        # Verify instructions were written
        for filename in PHASE_PROMPT_FILES.values():
            content = (tmp_path / filename).read_text()
            assert "## Steps" in content  # Steps preserved
            assert "Original." not in content  # Old instruction replaced

    def test_score_all_existing_dossiers(self, output_dir):
        """Score every completed dossier and print results."""
        if not output_dir.exists():
            pytest.skip("No output directory")
        examples = load_dossier_outputs(output_dir)
        if not examples:
            pytest.skip("No complete dossiers")

        from dspy.loader import score_dossier, load_single_dossier

        print("\n  Dossier Quality Scores:")
        print("  " + "-" * 60)
        for ex in examples:
            domain_dir = output_dir / ex.domain
            dossier = load_single_dossier(domain_dir)
            scores = score_dossier(dossier)
            avg = sum(scores.values()) / len(scores)
            print(f"  {ex.domain:20s}  avg={avg:.3f}  " +
                  "  ".join(f"p{i}={scores[f'p{i}']:.2f}" for i in range(1, 8)))
```

**Step 2: Create __main__.py entry point**

Create `dspy/__main__.py`:
```python
"""Entry point: python -m dspy.compile"""
from dspy.compile import main

main()
```

**Step 3: Run all tests**

Run: `cd "/Volumes/OWC drive/Dev/dossier" && PYTHONPATH=. dspy/.venv/bin/python -m pytest tests/ -v -s`
Expected: All tests PASS, dossier scores printed

**Step 4: Commit**

```bash
cd "/Volumes/OWC drive/Dev/dossier"
git add dspy/__main__.py tests/test_integration.py
git commit -m "feat: add integration tests and __main__ entry point"
```

---

### Task 10: Update .gitignore and Documentation

**Files:**
- Modify: `.gitignore`
- Modify: `ARCHITECTURE.md` (add DSPy section)

**Step 1: Update .gitignore**

Add to `.gitignore`:
```
dspy/.venv/
dspy/compiled/*.json
prompts/backup-*/
```

**Step 2: Add DSPy section to ARCHITECTURE.md**

Append to `ARCHITECTURE.md`:
```markdown

## DSPy Prompt Optimization (Offline Compiler)

The `dspy/` directory contains an offline prompt compiler that uses DSPy to optimize
the phase prompt instructions. All LLM calls route through Claude Agent SDK (Max subscription).

### Architecture

```
Training data (output/*/) → DSPy Signatures → BootstrapFewShotWithRandomSearch → Optimized prompts
```

### Usage

```bash
cd "/Volumes/OWC drive/Dev/dossier"
PYTHONPATH=. dspy/.venv/bin/python -m dspy.compile --model sonnet --candidates 5
```

### Components

| File | Purpose |
|------|---------|
| `dspy/lm.py` | ClaudeAgentLM — custom DSPy backend via Agent SDK |
| `dspy/signatures.py` | 7 Signature classes (typed I/O per phase) |
| `dspy/modules.py` | PhaseModule wrappers + DossierPipeline composition |
| `dspy/metrics.py` | Evaluation: completeness, source diversity, substantiation |
| `dspy/loader.py` | Load completed dossier outputs as training examples |
| `dspy/compile.py` | Optimizer driver (rate-limit aware) |
| `dspy/export.py` | Write optimized instructions → prompts/p{N}.md |
```

**Step 3: Commit**

```bash
cd "/Volumes/OWC drive/Dev/dossier"
git add .gitignore ARCHITECTURE.md
git commit -m "docs: add DSPy section to architecture, update gitignore"
```

---

### Task 11: First Live Optimization Run

**Prerequisites:** Tasks 1-10 complete, all tests passing.

**Step 1: Score existing dossiers (baseline)**

```bash
cd "/Volumes/OWC drive/Dev/dossier"
PYTHONPATH=. dspy/.venv/bin/python -m pytest tests/test_integration.py::TestEndToEnd::test_score_all_existing_dossiers -v -s
```

Record the baseline scores.

**Step 2: Run compilation**

```bash
cd "/Volumes/OWC drive/Dev/dossier"
PYTHONPATH=. dspy/.venv/bin/python -m dspy.compile --model sonnet --candidates 3
```

Start with 3 candidates (lower rate limit budget) for the first run.

**Step 3: Review optimized instructions**

```bash
cd "/Volumes/OWC drive/Dev/dossier"
diff prompts/ prompts/backup-*/
```

Compare original vs optimized instructions. The optimized versions should be more specific and grounded in what worked across the 5 training dossiers.

**Step 4: Commit optimized prompts**

```bash
cd "/Volumes/OWC drive/Dev/dossier"
git add dspy/compiled/ prompts/
git commit -m "feat: first DSPy-optimized phase prompts (v1)"
```

"""Tests for ClaudeAgentLM -- DSPy backend via Claude Agent SDK."""
from __future__ import annotations

import asyncio
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from dspy.lm import ClaudeAgentLM


class TestClaudeAgentLMInit:
    """Tests for __init__ and configuration."""

    def test_init_defaults(self):
        lm = ClaudeAgentLM()
        assert lm.cli_model == "sonnet"
        assert lm.max_turns == 1
        assert lm.model == "claude-agent/sonnet"
        assert lm.cache is False
        assert lm.timeout == 300
        assert lm._session_id is None

    def test_init_custom_model(self):
        lm = ClaudeAgentLM(model="opus")
        assert lm.cli_model == "opus"
        assert lm.model == "claude-agent/opus"

    def test_init_custom_haiku(self):
        lm = ClaudeAgentLM(model="haiku")
        assert lm.cli_model == "haiku"
        assert lm.model == "claude-agent/haiku"

    def test_init_custom_max_turns(self):
        lm = ClaudeAgentLM(max_turns=5)
        assert lm.max_turns == 5

    def test_init_custom_timeout(self):
        lm = ClaudeAgentLM(timeout=600)
        assert lm.timeout == 600

    def test_init_kwargs_passed_to_base(self):
        lm = ClaudeAgentLM(temperature=0.7, max_tokens=4000)
        assert lm.kwargs["temperature"] == 0.7
        assert lm.kwargs["max_tokens"] == 4000

    def test_model_type_is_chat(self):
        lm = ClaudeAgentLM()
        assert lm.model_type == "chat"


class TestClaudeAgentLMAforward:
    """Tests for async forward pass."""

    @pytest.mark.asyncio
    async def test_aforward_returns_model_response(self):
        from claude_agent_sdk import ResultMessage

        lm = ClaudeAgentLM()

        result = ResultMessage(
            subtype="result",
            duration_ms=500,
            duration_api_ms=400,
            is_error=False,
            num_turns=1,
            session_id="test-session-123",
            result="This is the LLM response",
            total_cost_usd=None,
            usage=None,
        )

        async def mock_query(**kwargs):
            yield result

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
    async def test_aforward_with_result_message(self):
        """Test with a proper ResultMessage instance."""
        from claude_agent_sdk import ResultMessage

        lm = ClaudeAgentLM()

        result = ResultMessage(
            subtype="result",
            duration_ms=500,
            duration_api_ms=400,
            is_error=False,
            num_turns=1,
            session_id="sess-real-123",
            result="Real response text",
        )

        async def mock_query(**kwargs):
            yield result

        with patch("dspy.lm.query", side_effect=mock_query):
            response = await lm.aforward(
                messages=[{"role": "user", "content": "Hello"}]
            )

        assert response.choices[0].message.content == "Real response text"
        assert lm._session_id == "sess-real-123"

    @pytest.mark.asyncio
    async def test_aforward_with_system_message_init(self):
        """Test that SystemMessage init captures session ID."""
        from claude_agent_sdk import ResultMessage, SystemMessage

        lm = ClaudeAgentLM()

        init_msg = SystemMessage(
            subtype="init",
            data={"session_id": "init-sess-456"},
        )
        result_msg = ResultMessage(
            subtype="result",
            duration_ms=100,
            duration_api_ms=80,
            is_error=False,
            num_turns=1,
            session_id="init-sess-456",
            result="Done",
        )

        async def mock_query(**kwargs):
            yield init_msg
            yield result_msg

        with patch("dspy.lm.query", side_effect=mock_query):
            response = await lm.aforward(prompt="test")

        assert lm._session_id == "init-sess-456"
        assert response.choices[0].message.content == "Done"

    @pytest.mark.asyncio
    async def test_aforward_with_prompt_string(self):
        from claude_agent_sdk import ResultMessage

        lm = ClaudeAgentLM()

        result = ResultMessage(
            subtype="result",
            duration_ms=100,
            duration_api_ms=80,
            is_error=False,
            num_turns=1,
            session_id="sess-456",
            result="Response text",
        )

        async def mock_query(**kwargs):
            yield result

        with patch("dspy.lm.query", side_effect=mock_query):
            response = await lm.aforward(prompt="Simple prompt")

        assert response.choices[0].message.content == "Response text"

    @pytest.mark.asyncio
    async def test_aforward_cli_error_raises(self):
        lm = ClaudeAgentLM()

        async def mock_query(**kwargs):
            raise RuntimeError("CLI connection failed")
            yield  # make it a generator  # noqa: E501

        with patch("dspy.lm.query", side_effect=mock_query):
            with pytest.raises(RuntimeError, match="CLI connection failed"):
                await lm.aforward(prompt="test")

    @pytest.mark.asyncio
    async def test_aforward_empty_result(self):
        from claude_agent_sdk import ResultMessage

        lm = ClaudeAgentLM()

        result = ResultMessage(
            subtype="result",
            duration_ms=50,
            duration_api_ms=40,
            is_error=False,
            num_turns=1,
            session_id="sess-empty",
            result=None,
        )

        async def mock_query(**kwargs):
            yield result

        with patch("dspy.lm.query", side_effect=mock_query):
            response = await lm.aforward(prompt="test")

        assert response.choices[0].message.content == ""

    @pytest.mark.asyncio
    async def test_aforward_model_in_response(self):
        from claude_agent_sdk import ResultMessage

        lm = ClaudeAgentLM(model="opus")

        result = ResultMessage(
            subtype="result",
            duration_ms=100,
            duration_api_ms=80,
            is_error=False,
            num_turns=1,
            session_id="s1",
            result="OK",
        )

        async def mock_query(**kwargs):
            yield result

        with patch("dspy.lm.query", side_effect=mock_query):
            response = await lm.aforward(prompt="test")

        assert response.model == "claude-agent/opus"

    @pytest.mark.asyncio
    async def test_aforward_usage_estimation(self):
        from claude_agent_sdk import ResultMessage

        lm = ClaudeAgentLM()

        result = ResultMessage(
            subtype="result",
            duration_ms=100,
            duration_api_ms=80,
            is_error=False,
            num_turns=1,
            session_id="s1",
            result="A" * 400,  # 400 chars -> ~100 estimated tokens
        )

        async def mock_query(**kwargs):
            yield result

        with patch("dspy.lm.query", side_effect=mock_query):
            response = await lm.aforward(prompt="test")

        assert response.usage.completion_tokens == 100
        assert response.usage.total_tokens > 0


class TestClaudeAgentLMForward:
    """Tests for sync forward pass."""

    def test_forward_sync_wrapper(self):
        from claude_agent_sdk import ResultMessage

        lm = ClaudeAgentLM()

        result = ResultMessage(
            subtype="result",
            duration_ms=100,
            duration_api_ms=80,
            is_error=False,
            num_turns=1,
            session_id="sess-789",
            result="Sync response",
        )

        async def mock_query(**kwargs):
            yield result

        with patch("dspy.lm.query", side_effect=mock_query):
            response = lm.forward(prompt="test sync")

        assert response.choices[0].message.content == "Sync response"


class TestClaudeAgentLMOptions:
    """Tests for options construction and session management."""

    @pytest.mark.asyncio
    async def test_session_resume_passed_to_options(self):
        from claude_agent_sdk import ResultMessage

        lm = ClaudeAgentLM()
        lm._session_id = "previous-session"

        result = ResultMessage(
            subtype="result",
            duration_ms=100,
            duration_api_ms=80,
            is_error=False,
            num_turns=1,
            session_id="previous-session",
            result="Resumed",
        )

        captured_options = {}

        async def mock_query(**kwargs):
            captured_options.update(kwargs)
            yield result

        with patch("dspy.lm.query", side_effect=mock_query):
            await lm.aforward(prompt="continue")

        assert captured_options["options"].resume == "previous-session"

    @pytest.mark.asyncio
    async def test_no_resume_when_no_session(self):
        from claude_agent_sdk import ResultMessage

        lm = ClaudeAgentLM()
        assert lm._session_id is None

        result = ResultMessage(
            subtype="result",
            duration_ms=100,
            duration_api_ms=80,
            is_error=False,
            num_turns=1,
            session_id="new-session",
            result="Fresh",
        )

        captured_options = {}

        async def mock_query(**kwargs):
            captured_options.update(kwargs)
            yield result

        with patch("dspy.lm.query", side_effect=mock_query):
            await lm.aforward(prompt="first call")

        assert captured_options["options"].resume is None

    @pytest.mark.asyncio
    async def test_system_prompt_extracted(self):
        from claude_agent_sdk import ResultMessage

        lm = ClaudeAgentLM()

        result = ResultMessage(
            subtype="result",
            duration_ms=100,
            duration_api_ms=80,
            is_error=False,
            num_turns=1,
            session_id="s1",
            result="OK",
        )

        captured_options = {}

        async def mock_query(**kwargs):
            captured_options.update(kwargs)
            yield result

        with patch("dspy.lm.query", side_effect=mock_query):
            await lm.aforward(messages=[
                {"role": "system", "content": "Be concise."},
                {"role": "user", "content": "Hi"},
            ])

        assert captured_options["options"].system_prompt == "Be concise."
        assert "Hi" in captured_options["prompt"]

    @pytest.mark.asyncio
    async def test_multiple_system_messages_joined(self):
        from claude_agent_sdk import ResultMessage

        lm = ClaudeAgentLM()

        result = ResultMessage(
            subtype="result",
            duration_ms=100,
            duration_api_ms=80,
            is_error=False,
            num_turns=1,
            session_id="s1",
            result="OK",
        )

        captured_options = {}

        async def mock_query(**kwargs):
            captured_options.update(kwargs)
            yield result

        with patch("dspy.lm.query", side_effect=mock_query):
            await lm.aforward(messages=[
                {"role": "system", "content": "Rule 1."},
                {"role": "system", "content": "Rule 2."},
                {"role": "user", "content": "Go"},
            ])

        assert "Rule 1." in captured_options["options"].system_prompt
        assert "Rule 2." in captured_options["options"].system_prompt

    @pytest.mark.asyncio
    async def test_no_system_prompt_when_absent(self):
        from claude_agent_sdk import ResultMessage

        lm = ClaudeAgentLM()

        result = ResultMessage(
            subtype="result",
            duration_ms=100,
            duration_api_ms=80,
            is_error=False,
            num_turns=1,
            session_id="s1",
            result="OK",
        )

        captured_options = {}

        async def mock_query(**kwargs):
            captured_options.update(kwargs)
            yield result

        with patch("dspy.lm.query", side_effect=mock_query):
            await lm.aforward(messages=[
                {"role": "user", "content": "Hello"},
            ])

        assert captured_options["options"].system_prompt is None

    @pytest.mark.asyncio
    async def test_allowed_tools_empty(self):
        """Verify no tools are enabled -- pure LLM completion."""
        from claude_agent_sdk import ResultMessage

        lm = ClaudeAgentLM()

        result = ResultMessage(
            subtype="result",
            duration_ms=100,
            duration_api_ms=80,
            is_error=False,
            num_turns=1,
            session_id="s1",
            result="OK",
        )

        captured_options = {}

        async def mock_query(**kwargs):
            captured_options.update(kwargs)
            yield result

        with patch("dspy.lm.query", side_effect=mock_query):
            await lm.aforward(prompt="test")

        assert captured_options["options"].allowed_tools == []

    @pytest.mark.asyncio
    async def test_model_passed_to_options(self):
        from claude_agent_sdk import ResultMessage

        lm = ClaudeAgentLM(model="opus")

        result = ResultMessage(
            subtype="result",
            duration_ms=100,
            duration_api_ms=80,
            is_error=False,
            num_turns=1,
            session_id="s1",
            result="OK",
        )

        captured_options = {}

        async def mock_query(**kwargs):
            captured_options.update(kwargs)
            yield result

        with patch("dspy.lm.query", side_effect=mock_query):
            await lm.aforward(prompt="test")

        assert captured_options["options"].model == "opus"

    @pytest.mark.asyncio
    async def test_max_turns_passed_to_options(self):
        from claude_agent_sdk import ResultMessage

        lm = ClaudeAgentLM(max_turns=3)

        result = ResultMessage(
            subtype="result",
            duration_ms=100,
            duration_api_ms=80,
            is_error=False,
            num_turns=1,
            session_id="s1",
            result="OK",
        )

        captured_options = {}

        async def mock_query(**kwargs):
            captured_options.update(kwargs)
            yield result

        with patch("dspy.lm.query", side_effect=mock_query):
            await lm.aforward(prompt="test")

        assert captured_options["options"].max_turns == 3

    @pytest.mark.asyncio
    async def test_assistant_messages_formatted(self):
        """Test that assistant messages are properly formatted in prompt."""
        from claude_agent_sdk import ResultMessage

        lm = ClaudeAgentLM()

        result = ResultMessage(
            subtype="result",
            duration_ms=100,
            duration_api_ms=80,
            is_error=False,
            num_turns=1,
            session_id="s1",
            result="OK",
        )

        captured_options = {}

        async def mock_query(**kwargs):
            captured_options.update(kwargs)
            yield result

        with patch("dspy.lm.query", side_effect=mock_query):
            await lm.aforward(messages=[
                {"role": "user", "content": "What is 2+2?"},
                {"role": "assistant", "content": "4"},
                {"role": "user", "content": "And 3+3?"},
            ])

        prompt = captured_options["prompt"]
        assert "What is 2+2?" in prompt
        assert "[Previous assistant response]" in prompt
        assert "4" in prompt
        assert "And 3+3?" in prompt

"""ClaudeAgentLM -- DSPy BaseLM backend routing through Claude Agent SDK.

All LLM calls go through Claude Code Max subscription. Zero API spend.
"""
from __future__ import annotations

import asyncio
from typing import Any, Optional, List, Dict

import dspy  # Our proxy — ensures all DSPy classes share one settings instance

BaseLM = dspy.BaseLM

from litellm import ModelResponse

from claude_agent_sdk import (
    ClaudeAgentOptions,
    ResultMessage,
    SystemMessage,
    query,
)


class ClaudeAgentLM(BaseLM):
    """Routes DSPy LLM calls through Claude Agent SDK (Max subscription).

    Usage::

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
        # Allow kwargs to override our defaults
        base_kwargs = dict(
            temperature=0.0,
            max_tokens=8000,
        )
        base_kwargs.update(kwargs)
        super().__init__(
            model=f"claude-agent/{model}",
            model_type="chat",
            cache=False,
            **base_kwargs,
        )
        self.cli_model = model
        self.max_turns = max_turns
        self.timeout = timeout
        self._session_id: Optional[str] = None

    def forward(
        self,
        prompt: Optional[str] = None,
        messages: Optional[List[Dict[str, Any]]] = None,
        **kwargs: Any,
    ) -> ModelResponse:
        """Sync wrapper -- bridges DSPy's sync interface to Agent SDK's async API."""
        try:
            loop = asyncio.get_running_loop()
        except RuntimeError:
            loop = None

        if loop and loop.is_running():
            # Already in an async context -- run in a separate thread
            import concurrent.futures

            with concurrent.futures.ThreadPoolExecutor() as pool:
                future = pool.submit(
                    asyncio.run,
                    self.aforward(prompt=prompt, messages=messages, **kwargs),
                )
                return future.result(timeout=self.timeout)
        else:
            return asyncio.run(
                asyncio.wait_for(
                    self.aforward(prompt=prompt, messages=messages, **kwargs),
                    timeout=self.timeout,
                )
            )

    async def aforward(
        self,
        prompt: Optional[str] = None,
        messages: Optional[List[Dict[str, Any]]] = None,
        **kwargs: Any,
    ) -> ModelResponse:
        """Call Claude via Agent SDK and return a ModelResponse."""
        messages = messages or [{"role": "user", "content": prompt or ""}]

        # Split system prompt from conversation
        system_parts: List[str] = []
        conv_parts: List[str] = []
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
            allowed_tools=[],  # Pure LLM completion -- no tool use
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

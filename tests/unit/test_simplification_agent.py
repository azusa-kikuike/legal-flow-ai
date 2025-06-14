# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Unit tests for the simplification agent.
"""

import pytest
from app.sub_agents.simplification.agent import simplification_agent
from app.sub_agents.simplification.prompt import SIMPLIFICATION_AGENT_PROMPT


def test_simplification_agent_configuration():
    """Test that simplification agent is configured correctly."""
    assert simplification_agent.name == "simplification_agent"
    assert simplification_agent.model == "gemini-2.0-flash"
    assert simplification_agent.description == "Simplifies legal articles into plain language"
    assert simplification_agent.instruction == SIMPLIFICATION_AGENT_PROMPT


def test_simplification_agent_prompt_content():
    """Test that the prompt contains expected instructions."""
    assert "法令条文を平易な文章に訳す" in SIMPLIFICATION_AGENT_PROMPT
    assert "日本語の文章を返す" in SIMPLIFICATION_AGENT_PROMPT
    assert "各条文をそのまま訳す" in SIMPLIFICATION_AGENT_PROMPT
    assert "定義に記載されている各用語の意味を記載する" in SIMPLIFICATION_AGENT_PROMPT
    assert "legal_flow_agent" in SIMPLIFICATION_AGENT_PROMPT
    assert "転送" in SIMPLIFICATION_AGENT_PROMPT


def test_simplification_agent_prompt_not_empty():
    """Test that the prompt is not empty or None."""
    assert SIMPLIFICATION_AGENT_PROMPT is not None
    assert len(SIMPLIFICATION_AGENT_PROMPT.strip()) > 0
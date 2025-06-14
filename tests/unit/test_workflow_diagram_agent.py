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
Unit tests for the workflow diagram agent.
"""

import pytest
from app.sub_agents.workflow_diagram.agent import workflow_diagram_agent
from app.sub_agents.workflow_diagram.prompt import WORKFLOW_DIAGRAM_AGENT_PROMPT


def test_workflow_diagram_agent_configuration():
    """Test that workflow diagram agent is configured correctly."""
    assert workflow_diagram_agent.name == "workflow_diagram_agent"
    assert workflow_diagram_agent.model == "gemini-2.0-flash"
    assert workflow_diagram_agent.description == "Analyzes legal articles and creates business workflow diagrams"
    assert workflow_diagram_agent.instruction == WORKFLOW_DIAGRAM_AGENT_PROMPT


def test_workflow_diagram_agent_prompt_content():
    """Test that the prompt contains expected workflow analysis instructions."""
    assert "法令条文を解析して業務フロー図を作成しなさい" in WORKFLOW_DIAGRAM_AGENT_PROMPT
    assert "業務プロセスを分析する" in WORKFLOW_DIAGRAM_AGENT_PROMPT
    assert "関係者" in WORKFLOW_DIAGRAM_AGENT_PROMPT
    assert "時系列に沿った業務フロー" in WORKFLOW_DIAGRAM_AGENT_PROMPT
    assert "Mermaid記法" in WORKFLOW_DIAGRAM_AGENT_PROMPT
    assert "条件分岐や承認プロセス" in WORKFLOW_DIAGRAM_AGENT_PROMPT


def test_workflow_diagram_agent_prompt_not_empty():
    """Test that the prompt is not empty or None."""
    assert WORKFLOW_DIAGRAM_AGENT_PROMPT is not None
    assert len(WORKFLOW_DIAGRAM_AGENT_PROMPT.strip()) > 0


def test_workflow_diagram_agent_prompt_includes_mermaid():
    """Test that the prompt specifically mentions Mermaid syntax for diagram output."""
    assert "Mermaid" in WORKFLOW_DIAGRAM_AGENT_PROMPT


def test_workflow_diagram_agent_prompt_includes_stakeholders():
    """Test that the prompt mentions stakeholder identification."""
    assert "申請者" in WORKFLOW_DIAGRAM_AGENT_PROMPT
    assert "行政機関" in WORKFLOW_DIAGRAM_AGENT_PROMPT
    assert "事業者" in WORKFLOW_DIAGRAM_AGENT_PROMPT
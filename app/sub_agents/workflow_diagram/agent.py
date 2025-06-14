from google.adk.agents.llm_agent import Agent
from . import prompt

workflow_diagram_agent = Agent(
    name="workflow_diagram_agent",
    model='gemini-2.0-flash',
    description="Analyzes legal articles and creates business workflow diagrams",
    instruction=prompt.WORKFLOW_DIAGRAM_AGENT_PROMPT,
)
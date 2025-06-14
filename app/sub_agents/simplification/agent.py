from google.adk.agents.llm_agent import Agent
from . import prompt

simplification_agent = Agent(
    name="simplification_agent",
    model='gemini-2.0-flash',
    description="Simplifies legal articles into plain language",
    instruction=prompt.SIMPLIFICATION_AGENT_PROMPT,
)
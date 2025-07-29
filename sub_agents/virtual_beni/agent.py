"""Virtual_Beni_Agent for finding latest technology trends with a focus on trends in the aviation industry"""

from google.adk import Agent
from google.adk.tools import google_search

from . import prompt

MODEL = "gemini-2.5-pro"


virtual_beni_agent = Agent(
    model=MODEL,
    name="virtual_beni_agent",
    instruction=prompt.VIRTUAL_BENI_PROMPT,
    output_key="findings_beni",
    tools=[google_search],
)

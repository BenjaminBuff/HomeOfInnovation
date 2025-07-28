"""Virtual_Lukas_Agent for finding latest technology trends with a focus on trends in the aviation industry"""

from google.adk import Agent
from google.adk.tools import google_search

from . import prompt

MODEL = "gemini-2.5-pro"


current_destinations_agent = Agent(
    model=MODEL,
    name="virtual_lukas_agent",
    instruction=prompt.VIRTUAL_LUKAS_PROMPT,
    output_key="findings_lukas",
    tools=[google_search],
)

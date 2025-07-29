"""Selector: Select the most interesting topic that has the strongest and most compelling potential relation to the airline industry."""

from google.adk import Agent
from google.adk.tools import google_search

from . import prompt

MODEL = "gemini-2.5-pro"


selector_agent = Agent(
    model=MODEL,
    name="selector_agent",
    instruction=prompt.SELECTOR_PROMPT,
    output_key="selector",
)
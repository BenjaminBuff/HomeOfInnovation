"""Archiver:  Teams‑Post history keeper."""

from google.adk import Agent
from google.adk.tools import google_search

from . import prompt

MODEL = "gemini-2.5-pro"


archiver_agent = Agent(
    model=MODEL,
    name="archiver_agent",
    instruction=prompt.ARCHIVER_PROMPT,
    output_key="Archiver_results",
)
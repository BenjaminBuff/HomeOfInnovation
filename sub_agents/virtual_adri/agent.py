"""Virtual_Adi_Agent for finding latest technology trends with a focus on trends in the aviation industry"""

from google.adk import Agent
from google.adk.tools import google_search

from . import prompt

MODEL = "gemini-2.5-pro"


virtual_adri_agent = Agent(
    model=MODEL,
    name="virtual_adri_agent",
    instruction=prompt.VIRTUAL_ADRI_PROMPT,
    output_key="findings_adri",
    tools=[google_search],
)

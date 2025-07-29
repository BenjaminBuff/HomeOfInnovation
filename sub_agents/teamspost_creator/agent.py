"""Teamspost_Creator: Create a teams post for the home of innovation teams channel."""

from google.adk import Agent
from google.adk.tools import google_search
from ...tools.json_tools import send_email_with_yagmail

from . import prompt

MODEL = "gemini-2.5-pro"


teamspost_creator_agent = Agent(
    model=MODEL,
    name="teamspost_creator_agent",
    instruction=prompt.TEAMSPOST_CREATOR_PROMPT,
    output_key="teamspost",
    tools=[
        send_email_with_yagmail
    ],
)
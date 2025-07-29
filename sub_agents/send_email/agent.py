"""Teamspost_Creator: Create a teams post for the home of innovation teams channel."""

from google.adk import Agent
from ...tools.json_tools import send_email_with_yagmail

from . import prompt

MODEL = "gemini-2.5-pro"


send_email_agent = Agent(
    model=MODEL,
    name="send_email_agent",
    instruction=prompt.SEND_EMAIL_PROMPT,
    output_key="send_email",
    tools=[
        send_email_with_yagmail
    ],
)
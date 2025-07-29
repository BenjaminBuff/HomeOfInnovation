"""Home Of Innovation: Research for technology trends and innovation, discuss them with the team. Evaluate which trends could be helpful in an aviation field. Also create a teams post for the home of innovation teams channel."""

from google.adk.agents import LlmAgent
from google.adk.tools.agent_tool import AgentTool

from . import prompt
from .sub_agents.virtual_beni import virtual_beni_agent
from .sub_agents.virtual_adri import virtual_adri_agent
from .sub_agents.virtual_lukas import virtual_lukas_agent
from .sub_agents.virtual_edward import virtual_edward_agent
from .sub_agents.teamspost_creator import teamspost_creator_agent
from .sub_agents.selector import selector_agent
from .sub_agents.researcher import researcher_agent
<<<<<<< HEAD
from .sub_agents.send_email import send_email_agent
=======
from .sub_agents.archiver import archiver_agent
>>>>>>> fecc33b7da75282811c4d017357217c51f586d7e

MODEL = "gemini-2.5-pro"


Home_of_innovation = LlmAgent(
    name="home_of_innovation",
    model=MODEL,
    description=(
        "Research for technology trends and innovation, discuss them with the team. Evaluate which trends could be helpful in an aviation field. Also create a teams post for the home of innovation teams channel."
    ),
    instruction=prompt.ORCHESTRATOR_PROMPT,
    output_key="home_of_innovation",
    tools=[
        AgentTool(agent=virtual_beni_agent),
        AgentTool(agent=virtual_adri_agent),
        AgentTool(agent=virtual_lukas_agent),
        AgentTool(agent=virtual_edward_agent),
        AgentTool(agent=teamspost_creator_agent),
        AgentTool(agent=selector_agent),
        AgentTool(agent=researcher_agent),
<<<<<<< HEAD
        AgentTool(agent=send_email_agent)
=======
        AgentTool(agent=archiver_agent)
>>>>>>> fecc33b7da75282811c4d017357217c51f586d7e
    ],
)

root_agent = Home_of_innovation

import json, os
from google.adk.tools.function_tool import FunctionTool
from src.server import FastMCP

# Initialize the Gmail service
gmail_service = FastMCP("GMail")

BASE_DIR = os.path.dirname(os.path.dirname(__file__))  # Sports-Coach root
STATUS_PATH = os.path.join(BASE_DIR, "data", "processed", "training_status.json")
PLAN_PATH = os.path.join(BASE_DIR, "data", "processed", "current_training_plan.json")
# ---- READ STATUS ----
def send_email() -> dict:
   gmail_service.send_message(
    to='digitaladoption-and-innovation@swiss.com',
    subject='Test Email',
    message_text='Hello, this is a test email from an agent'
)


send_email_tool = FunctionTool(func=send_email)

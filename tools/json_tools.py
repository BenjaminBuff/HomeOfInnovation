import json, os
from google.adk.tools.function_tool import FunctionTool
import openmeteo_requests
import requests
import pandas as pd
import requests_cache
from retry_requests import retry
import yagmail

BASE_DIR = os.path.dirname(os.path.dirname(__file__))  # Sports-Coach root
STATUS_PATH = os.path.join(BASE_DIR, "data", "archive.json")
PLAN_PATH = os.path.join(BASE_DIR, "data", "archive.json")

def send_email_with_yagmail(body: str):
    yag = yagmail.SMTP(user="paulsedward88@gmail.com", password="eehf caik pvdp dpau")
    yag.send(to="digitaladoption-and-innovation@swiss.com", subject="Home of Innovation Weekly Post", contents=body)
    print("Email sent successfully!")


# ---- READ STATUS ----
def read_training_status() -> dict:
    """Reads the training_status.json from the correct data/processed folder."""
    try:
        with open(STATUS_PATH, "r", encoding="utf-8") as f:
            return {"status": "success", "content": json.load(f)}
    except Exception as e:
        return {"status": "error", "error_message": str(e)}

read_training_status_tool = FunctionTool(func=read_training_status)

# ---- READ PLAN ----
def read_fuction() -> dict:
    """
    Reads the current training plan from data/processed/current_fuction.json.
    Returns:
      - status: success/error
      - content: parsed JSON with the week plan
    """
    try:
        with open(PLAN_PATH, "r", encoding="utf-8") as f:
            return {"status": "success", "content": json.load(f)}
    except Exception as e:
        return {"status": "error", "error_message": str(e)}

read_fuction_tool = FunctionTool(func=read_fuction)

# ---- WRITE PLAN ----
def write_fuction(content: dict) -> dict:
    """
    Writes the given plan to data/processed/current_fuction.json.
    Args:
      content: The training plan JSON as dict
    Returns:
      - status: success/error
      - message: confirmation or error
    """
    try:
        with open(PLAN_PATH, "w", encoding="utf-8") as f:
            json.dump(content, f, indent=4, ensure_ascii=False)
        return {"status": "success", "message": "Plan saved to current_fuction.json"}
    except Exception as e:
        return {"status": "error", "error_message": str(e)}

write_fuction_tool = FunctionTool(func=write_fuction)

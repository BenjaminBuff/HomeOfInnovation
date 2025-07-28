import json, os
from google.adk.tools.function_tool import FunctionTool

BASE_DIR = os.path.dirname(os.path.dirname(__file__))  # Sports-Coach root
STATUS_PATH = os.path.join(BASE_DIR, "data", "processed", "training_status.json")
PLAN_PATH = os.path.join(BASE_DIR, "data", "processed", "current_training_plan.json")
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
def read_training_plan() -> dict:
    """
    Reads the current training plan from data/processed/current_training_plan.json.
    Returns:
      - status: success/error
      - content: parsed JSON with the week plan
    """
    try:
        with open(PLAN_PATH, "r", encoding="utf-8") as f:
            return {"status": "success", "content": json.load(f)}
    except Exception as e:
        return {"status": "error", "error_message": str(e)}

read_training_plan_tool = FunctionTool(func=read_training_plan)

# ---- WRITE PLAN ----
def write_training_plan(content: dict) -> dict:
    """
    Writes the given plan to data/processed/current_training_plan.json.
    Args:
      content: The training plan JSON as dict
    Returns:
      - status: success/error
      - message: confirmation or error
    """
    try:
        with open(PLAN_PATH, "w", encoding="utf-8") as f:
            json.dump(content, f, indent=4, ensure_ascii=False)
        return {"status": "success", "message": "Plan saved to current_training_plan.json"}
    except Exception as e:
        return {"status": "error", "error_message": str(e)}

write_training_plan_tool = FunctionTool(func=write_training_plan)

def fetch_weather_forecast(start_date: str, end_date: str) -> dict:
    """
    Fetches daily max precipitation probability for Basel, Switzerland.
    Args:
        start_date: YYYY-MM-DD
        end_date: YYYY-MM-DD
    Returns:
        A dict with {date: precipitation_probability_max}
    """
    latitude = 47.5584
    longitude = 7.5733
    timezone = "Europe%2FBerlin"
    url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={latitude}&longitude={longitude}&timezone={timezone}"
        f"&daily=precipitation_probability_max&start_date={start_date}&end_date={end_date}"
    )
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        dates = data["daily"]["time"]
        probs = data["daily"]["precipitation_probability_max"]
        return {
            "status": "success",
            "forecast": dict(zip(dates, probs))
        }
    except Exception as e:
        return {"status": "error", "error_message": str(e)}
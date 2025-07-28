from datetime import date, timedelta
from json_tools import fetch_weather_forecast

today = date.today()
start_date = today.strftime("%Y-%m-%d")
end_date = (today + timedelta(days=3)).strftime("%Y-%m-%d")

print(fetch_weather_forecast(start_date, end_date))
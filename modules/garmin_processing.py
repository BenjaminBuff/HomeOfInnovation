import pandas as pd
import json
import math

ACUTE_DAYS = 7
CHRONIC_DAYS = 28

def time_to_minutes(t):
    if isinstance(t, str):
        parts = t.split(":")
        if len(parts) == 3:  # HH:MM:SS
            return int(parts[0])*60 + int(parts[1]) + int(parts[2])/60
        elif len(parts) == 2:  # MM:SS
            return int(parts[0]) + int(parts[1])/60
    return None

def to_float(x):
    try:
        x = str(x).replace(",", ".").strip()
        return float(x) if x not in ["--", "", None] else None
    except:
        return None

def compute_load(row):
    if pd.notna(row["Avg_HR"]):
        intensity = row["Avg_HR"] / 150
        te_factor = row["Aerobic_TE"] if pd.notna(row["Aerobic_TE"]) else 1.0
        return row["Duration_min"] * intensity * te_factor
    else:
        # fallback: distance-based estimate
        return row["Distance_km"] * 10 if pd.notna(row["Distance_km"]) else 0.0

def fatigue_status_from_ratio(ratio):
    if ratio < 0.8:
        return "Fresh (underloaded)"
    elif 0.8 <= ratio <= 1.3:
        return "Optimal"
    else:
        return "Fatigued (overreaching)"

def workout_suggestion(fatigue_status):
    if "Fresh" in fatigue_status:
        return "You’re underloaded → Suggest a quality workout (tempo/intervals)."
    elif "Optimal" in fatigue_status:
        return "You’re in the sweet spot → Suggest a moderate Zone 2 endurance run (~12-15km)."
    else:
        return "You’re fatigued → Suggest easy recovery or full rest."

def clean_value(val):
    """Ensure all numbers are JSON-safe (replace NaN/Inf with None)."""
    if isinstance(val, float):
        if math.isnan(val) or math.isinf(val):
            return None
    return val

def clean_dict(obj):
    """Recursively clean dicts/lists for NaN/Inf values."""
    if isinstance(obj, dict):
        return {k: clean_dict(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [clean_dict(v) for v in obj]
    else:
        return clean_value(obj)

def process_garmin_csv(input_file, output_json):
    df = pd.read_csv(input_file)

    # Clean data
    df["Duration_min"] = df["Zeit"].apply(time_to_minutes)
    df["Avg_HR"] = df["Ø Herzfrequenz"].apply(to_float)
    df["Distance_km"] = df["Distanz"].apply(to_float)
    df["Aerobic_TE"] = df["Aerober TE"].apply(to_float)
    df["Training_Load"] = df.apply(compute_load, axis=1)
    df["Date"] = pd.to_datetime(df["Datum"]).dt.date

    # Group daily
    daily_loads = df.groupby("Date")["Training_Load"].sum().reset_index().sort_values("Date")
    daily_loads["Acute_Load_7d"] = daily_loads["Training_Load"].rolling(window=ACUTE_DAYS, min_periods=1).sum()
    daily_loads["Chronic_Load_28d"] = daily_loads["Training_Load"].rolling(window=CHRONIC_DAYS, min_periods=1).mean()

    # Latest metrics
    latest = daily_loads.iloc[-1]
    acute_load = latest["Acute_Load_7d"]
    chronic_load = latest["Chronic_Load_28d"]
    ratio = acute_load / chronic_load if chronic_load > 0 else 1.0

    fatigue_status = fatigue_status_from_ratio(ratio)
    suggestion = workout_suggestion(fatigue_status)

    # Per-day breakdown
    daily_records = []
    for d, day_df in df.groupby("Date"):
        activities = []
        for _, row in day_df.iterrows():
            activities.append({
                "type": row["Aktivitätstyp"],
                "distance_km": clean_value(row["Distance_km"]),
                "duration_min": clean_value(row["Duration_min"]),
                "avg_hr": clean_value(row["Avg_HR"]),
                "training_load": clean_value(round(row["Training_Load"], 1))
            })
        daily_records.append({
            "date": str(d),
            "daily_load": clean_value(round(day_df["Training_Load"].sum(), 1)),
            "activities": activities
        })

    result = {
        "summary": {
            "acute_load_7d": clean_value(round(float(acute_load), 1)),
            "chronic_load_28d": clean_value(round(float(chronic_load), 1)),
            "acute_chronic_ratio": clean_value(round(float(ratio), 2)),
            "fatigue_status": fatigue_status
        },
        "daily_activities": daily_records,
        "recommendation": suggestion
    }

    # Clean the entire dict once more to ensure JSON-safe
    result = clean_dict(result)

    with open(output_json, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=4, ensure_ascii=False)

    return result

import sys
import os
from modules.garmin_processing import process_garmin_csv

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python training_coach.py data/raw/Activities.csv")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = "data/processed/training_status.json"

    # Ensure processed folder exists
    os.makedirs("data/processed", exist_ok=True)

    result = process_garmin_csv(input_file, output_file)

    print("\n✅ Processed Garmin Data")
    print(f"7-day Acute Load: {result['summary']['acute_load_7d']}")
    print(f"28-day Chronic Load: {result['summary']['chronic_load_28d']}")
    print(f"Acute:Chronic Ratio: {result['summary']['acute_chronic_ratio']} → {result['summary']['fatigue_status']}")
    print(f"Tomorrow’s Suggestion: {result['recommendation']}")
    print(f"JSON saved to {output_file}")

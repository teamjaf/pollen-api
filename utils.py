import os
import httpx
import json
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GOOGLE_POLLEN_API_KEY")
LAT = 51.1657  # Germany latitude
LON = 10.4515  # Germany longitude

def fetch_and_save_pollen_last_5_days():
    url = "https://pollen.googleapis.com/v1/forecast:lookup"
    params = {
        "key": API_KEY,
        "location.latitude": LAT,
        "location.longitude": LON,
        "days": 5
    }

    try:
        response = httpx.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        os.makedirs("data", exist_ok=True)

        # Save each day's data separately using its date
        for entry in data.get("dailyInfo", []):
            date_obj = entry["date"]
            formatted_date = f"{date_obj['year']}-{date_obj['month']:02}-{date_obj['day']:02}"
            filename = f"data/pollen_{formatted_date}.json"

            with open(filename, "w", encoding="utf-8") as f:
                json.dump(entry, f, indent=2)

        print("✅ Saved daily pollen data files")

    except Exception as e:
        print(f"❌ Error fetching pollen data: {e}")

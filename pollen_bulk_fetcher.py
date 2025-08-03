import httpx
import datetime
import os
import json
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GOOGLE_POLLEN_API_KEY")
LAT = 51.1657  # Germany Latitude
LON = 10.4515  # Germany Longitude
DATA_DIR = "data"

def fetch_last_5_days_combined():
    """Fetches and saves combined data for the last 5 days with a filename based on the date range."""
    os.makedirs(DATA_DIR, exist_ok=True)
    combined_data = []

    start_date = datetime.date.today() - datetime.timedelta(days=4)
    end_date = datetime.date.today()

    for i in range(5):
        date = end_date - datetime.timedelta(days=i)
        params = {
            "key": API_KEY,
            "location.latitude": LAT,
            "location.longitude": LON,
            "days": 1
        }
        try:
            res = httpx.get("https://pollen.googleapis.com/v1/forecast:lookup", params=params)
            res.raise_for_status()
            data = res.json()
            data['fetched_date'] = str(date)
            combined_data.append(data)
        except Exception as e:
            combined_data.append({"fetched_date": str(date), "error": str(e)})

    filename = f"pollen_{start_date}_to_{end_date}.json"
    filepath = os.path.join(DATA_DIR, filename)

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(combined_data, f, indent=2)

    print(f"✅ Combined data saved to {filename}")
    return combined_data


def get_last_5_days_combined_data():
    """Only returns combined data for the last 5 days (without saving to disk)."""
    combined_data = []

    for i in range(5):
        date = datetime.date.today() - datetime.timedelta(days=i)
        params = {
            "key": API_KEY,
            "location.latitude": LAT,
            "location.longitude": LON,
            "days": 1
        }
        try:
            res = httpx.get("https://pollen.googleapis.com/v1/forecast:lookup", params=params)
            res.raise_for_status()
            data = res.json()
            data['fetched_date'] = str(date)
            combined_data.append(data)
        except Exception as e:
            combined_data.append({"fetched_date": str(date), "error": str(e)})

    return combined_data

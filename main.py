from fastapi import FastAPI
from scheduler import start_scheduler
import os
import json

from pollen_bulk_fetcher import fetch_last_5_days_combined, get_last_5_days_combined_data

app = FastAPI()
DATA_DIR = "data"

@app.on_event("startup")
async def startup_event():
    start_scheduler()

@app.get("/")
async def root():
    return {"message": "Pollen API running. Daily collection active."}

@app.get("/latest-json")
async def get_latest_json():
    """Return the latest JSON data."""
    files = sorted(
        [f for f in os.listdir(DATA_DIR) if f.endswith(".json")],
        reverse=True
    )
    if not files:
        return {"error": "No data found."}
    with open(os.path.join(DATA_DIR, files[0]), "r", encoding="utf-8") as f:
        data = json.load(f)
    return data

@app.get("/all-json")
async def get_all_json():
    """Return all JSON files as a list."""
    all_data = []
    files = sorted([f for f in os.listdir(DATA_DIR) if f.endswith(".json")])
    for filename in files:
        file_path = os.path.join(DATA_DIR, filename)
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            all_data.append(data)
    return {"data": all_data}

@app.get("/fetch-5-days-combined")
async def fetch_5_days_combined():
    """Save and return combined data from last 5 days."""
    combined_data = fetch_last_5_days_combined()
    return {"message": "Combined data for last 5 days saved.", "data": combined_data}

@app.get("/view-5-days-combined")
async def view_5_days_combined():
    """Only return combined data without saving."""
    combined_data = get_last_5_days_combined_data()
    return {"data": combined_data}

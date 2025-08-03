from apscheduler.schedulers.background import BackgroundScheduler
from utils import fetch_and_save_pollen_last_5_days
from pollen_bulk_fetcher import fetch_last_5_days_combined, get_last_5_days_combined_data

import os

def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(fetch_and_save_pollen_last_5_days)
    scheduler.add_job(fetch_last_5_days_combined)   
    # scheduler.add_job(fetch_and_save_pollen_last_5_days, "cron", hour=6)  # Every day at 6 AM
    scheduler.start()
    print("📅 Scheduler started.")

import json
import csv
import os

# Input and output file paths
INPUT_JSON = "data/pollen_2025-07-30_to_2025-08-03.json"  # Replace with your actual filename
OUTPUT_CSV = "data/pollen_2025-07-30_to_2025-08-03.csv"

def flatten_pollen_data(json_data):
    rows = []

    for day in json_data:
        date = day.get("fetched_date", "")
        region = day.get("regionCode", "")
        daily_info = day.get("dailyInfo", [])
        for info in daily_info:
            pollen_types = info.get("pollenTypeInfo", [])
            for pollen in pollen_types:
                row = {
                    "Date": date,
                    "Region": region,
                    "Pollen Type": pollen.get("displayName", ""),
                    "In Season": pollen.get("inSeason", ""),
                    "Category": pollen.get("indexInfo", {}).get("category", ""),
                    "Index Value": pollen.get("indexInfo", {}).get("value", ""),
                    "Index Description": pollen.get("indexInfo", {}).get("indexDescription", ""),
                    "Health Tips": "; ".join(pollen.get("healthRecommendations", []))
                }
                rows.append(row)
    return rows

def convert_json_to_csv(input_json_path, output_csv_path):
    with open(input_json_path, "r", encoding="utf-8") as json_file:
        data = json.load(json_file)

    rows = flatten_pollen_data(data)

    if not rows:
        print("❌ No data to write.")
        return

    fieldnames = rows[0].keys()

    with open(output_csv_path, "w", newline='', encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"✅ CSV saved to {output_csv_path}")


if __name__ == "__main__":
    convert_json_to_csv(INPUT_JSON, OUTPUT_CSV)

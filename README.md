# 🌿 Google Pollen API Forecast Collector

This project fetches and stores pollen forecast data using the Google Pollen API for locations in Germany. It supports automated daily fetches and provides REST API endpoints for accessing the latest and historical data.

---

## 📊 Pollen Data Structure

This section outlines the structure of the stored JSON data.

### 🔑 Top-Level Keys

| Key            | Description                                                  |
|----------------|--------------------------------------------------------------|
| `regionCode`   | Country/region code (e.g., `"DE"` for Germany)               |
| `fetched_date` | Date when data was retrieved (e.g., `"2025-08-03"`)          |
| `dailyInfo`    | List of daily pollen forecasts                               |

---

### 📅 Inside `dailyInfo` (Per Day)

#### `date`
- `year`: Forecast year  
- `month`: Forecast month  
- `day`: Forecast day  

#### `pollenTypeInfo` (Pollen Categories)

| Key                    | Description                                            |
|------------------------|--------------------------------------------------------|
| `code`                 | Pollen type (e.g., `"GRASS"`, `"TREE"`, `"WEED"`)      |
| `displayName`          | Human-readable name (e.g., `"Grass"`)                 |
| `inSeason`             | Boolean (`true`/`false`) - Is it currently active?     |
| `indexInfo`            | Pollen severity metrics:                               |
| - `code`               | Index type (e.g., `"UPI"` = Universal Pollen Index)    |
| - `value`              | Numeric severity (1 = Very Low, 2 = Low, etc.)         |
| - `category`           | Text label (e.g., `"Low"`)                             |
| - `indexDescription`   | Impact on allergy sufferers                            |
| - `color`              | RGB values for visualization                           |
| `healthRecommendations` | Suggested actions for allergic individuals           |

---

### 🌱 `plantInfo` (Specific Plants)

| Key                    | Description                                             |
|------------------------|---------------------------------------------------------|
| `code`                 | Plant ID (e.g., `"GRAMINALES"`)                         |
| `displayName`          | Common name (e.g., `"Grasses"`)                         |
| `inSeason`             | Boolean (`true`/`false`)                                |
| `indexInfo`            | Same as `pollenTypeInfo.indexInfo`                      |
| `plantDescription`     | Detailed metadata:                                      |
| - `type`               | GRASS / WEED / TREE, etc.                               |
| - `family`             | Plant family (e.g., `"Poaceae"`)                        |
| - `season`             | Typical pollination season                              |
| - `crossReaction`      | Related plant/food allergy links                        |
| - `picture`            | URL to plant image                                      |
| - `pictureCloseup`     | URL to close-up plant image                             |

---

## 🚀 Features

- 🔄 Daily automated pollen data collection
- 🌍 Country/location-specific support
- 🧪 JSON file-based storage
- 🔗 REST API to retrieve:
  - Latest data (`/latest-json`)
  - All collected data (`/all-json`)
  - Last 5 days combined (`/fetch-5-days-combined`)

---

## 🛠 Tech Stack

- [FastAPI](https://fastapi.tiangolo.com/)
- [httpx](https://www.python-httpx.org/)
- [dotenv](https://pypi.org/project/python-dotenv/)
- JSON for structured storage

---

## 📌 Notes

- Requires `GOOGLE_POLLEN_API_KEY` in `.env`
- Currently configured for Germany (`LAT = 51.1657`, `LON = 10.4515`)
- Extendable to support multiple regions or file formats (CSV, etc.)

---

## 📸 Screenshots - Response Visualiser from Postman
## 

![Postman Response](images/Screenshot_2025-08-03_163600.png)

![Data Structure](images/Screenshot_2025-08-03_163615.png)


## 📬 License

MIT License © 2025


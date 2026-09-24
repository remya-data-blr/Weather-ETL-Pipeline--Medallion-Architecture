# 🌦️ Weather ETL Pipeline - Medallion Architecture

Live weather data pipeline for 5 Indian cities using Open-Meteo free API.

## 📂 Architecture (Bronze -> Silver -> Gold)

**Bronze Layer:** Raw JSON from API stored as-is
- Source: https://open-meteo.com/
- 5 cities: Delhi, Mumbai, Bangalore, Kolkata, Chennai
- Files: `bronze/weather_{city}.json`

**Silver Layer:** Cleaned CSV
- Extracts: city, temperature_c, windspeed, weathercode
- File: `silver/weather_clean.csv`

**Gold Layer:** SQLite DB + Analytics
- DB: `weather.db` -> table `weather_data`
- Analytics Query: Find hottest city

## 🛠️ Tech Stack
- Python
- Requests (API extraction)
- Pandas (Transformation)
- SQLite (Gold layer)
- Medallion Architecture

## 🚀 How to Run
```bash
pip install requests pandas
python weather_pipeline.py
python run_sql.py
```


## 📊 Output - Gold Layer Analytics##
**Hottest City: Delhi 30.4°C**
**Average Temp: 27.0°C**

## 👩‍💻 Author
Remya | Aspiring Data Engineer | Bangalore

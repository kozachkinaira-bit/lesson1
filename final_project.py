import sqlite3
import requests

conn = sqlite3.connect("weather.sl3")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS weather (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    city TEXT NOT NULL,
    temperature REAL NOT NULL,
    wind_speed REAL NOT NULL
);
""")

with open("cities.txt", "r", encoding="utf-8") as cities_file:
    for line in cities_file:
        city = line.strip()
        if not city:
            continue

        # 1. Знаходимо координати міста за назвою
        geo_url = (
            f"https://geocoding-api.open-meteo.com/v1/search"
            f"?name={city}&count=1&language=uk"
        )
        geo_data = requests.get(geo_url, timeout=10).json()

        results = geo_data.get("results")
        if not results:
            print(f"Не знайдено координати для: {city}")
            continue

        lat = results[0]["latitude"]
        lon = results[0]["longitude"]

        # 2. Отримуємо погоду за знайденими координатами
        weather_url = (
            f"https://api.open-meteo.com/v1/forecast"
            f"?latitude={lat}&longitude={lon}&current=temperature_2m,wind_speed_10m"
        )
        weather_data = requests.get(weather_url, timeout=10).json()
        current = weather_data["current"]

        temp = float(current["temperature_2m"])
        wind = float(current["wind_speed_10m"])

        cursor.execute(
            "INSERT INTO weather (city, temperature, wind_speed) VALUES (?, ?, ?);",
            (city, temp, wind),
        )
        print(f"{city}: {temp}°C, вітер {wind} км/год")

conn.commit()
conn.close()
print("Готово! Дані збережено у weather.sl3")
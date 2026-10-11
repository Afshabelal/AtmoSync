import requests
import pandas as pd
import os

# --------------------------------------------------
# AtmoSync - Weather Data Collection
# --------------------------------------------------

# Bengaluru study locations
locations = {
    "Bengaluru Central": {
        "latitude": 12.9716,
        "longitude": 77.5946
    },
    "Whitefield": {
        "latitude": 12.9698,
        "longitude": 77.7500
    },
    "Electronic City": {
        "latitude": 12.8452,
        "longitude": 77.6602
    },
    "Yelahanka": {
        "latitude": 13.1007,
        "longitude": 77.5963
    },
    "Rajajinagar": {
        "latitude": 12.9916,
        "longitude": 77.5550
    },
    "Jayanagar": {
        "latitude": 12.9250,
        "longitude": 77.5938
    }
}

# Historical date range
start_date = "2025-09-01"
end_date = "2026-08-31"

# Open-Meteo historical weather API
api_url = "https://archive-api.open-meteo.com/v1/archive"

all_data = []

for location, coordinates in locations.items():

    print(f"Collecting data for: {location}")

    params = {
        "latitude": coordinates["latitude"],
        "longitude": coordinates["longitude"],
        "start_date": start_date,
        "end_date": end_date,
        "hourly": [
            "temperature_2m",
            "relative_humidity_2m",
            "precipitation",
            "wind_speed_10m",
            "surface_pressure"
        ],
        "timezone": "Asia/Kolkata",
        "temperature_unit": "celsius",
        "wind_speed_unit": "kmh",
        "precipitation_unit": "mm"
    }

    response = requests.get(api_url, params=params, timeout=60)

    if response.status_code != 200:
        print(f"Error collecting {location}: {response.status_code}")
        continue

    weather_data = response.json()

    hourly = weather_data["hourly"]

    df = pd.DataFrame(hourly)

    df["location"] = location
    df["latitude"] = coordinates["latitude"]
    df["longitude"] = coordinates["longitude"]

    all_data.append(df)

# Combine all locations
final_df = pd.concat(all_data, ignore_index=True)

# Rename columns
final_df = final_df.rename(columns={
    "time": "timestamp",
    "temperature_2m": "temperature_c",
    "relative_humidity_2m": "relative_humidity_pct",
    "wind_speed_10m": "wind_speed_kmh",
    "surface_pressure": "surface_pressure_hpa",
    "precipitation": "precipitation_mm"
})

# Create output directory if it doesn't exist
output_folder = "data/raw"
os.makedirs(output_folder, exist_ok=True)

# Save data
output_file = os.path.join(
    output_folder,
    "atmosync_weather_data.csv"
)

final_df.to_csv(output_file, index=False)

print("\n------------------------------------")
print("Data collection completed!")
print("------------------------------------")
print(f"Total records: {len(final_df):,}")
print(f"Locations: {final_df['location'].nunique()}")
print(f"Saved to: {output_file}")
print("------------------------------------")
import pandas as pd
import os

# AtmoSync - Exploratory Data Analysis

input_file = "data/processed/atmosync_feature_engineered.csv"
df = pd.read_csv(input_file)

print("=" * 50)
print("ATMOSYNC - EDA ANALYSIS")
print("=" * 50)

# 1. Overall weather statistics
print("\n1. OVERALL WEATHER STATISTICS")
print(df[[
    "temperature_c",
    "relative_humidity_pct",
    "precipitation_mm",
    "wind_speed_kmh",
    "surface_pressure_hpa"
]].describe().round(2))

# 2. Location-wise averages
print("\n2. LOCATION-WISE WEATHER AVERAGES")

location_summary = df.groupby("location").agg(
    avg_temperature_c=("temperature_c", "mean"),
    avg_humidity_pct=("relative_humidity_pct", "mean"),
    avg_rainfall_mm=("precipitation_mm", "mean"),
    avg_wind_speed_kmh=("wind_speed_kmh", "mean"),
    records=("timestamp", "count")
).round(2)

print(location_summary)

# 3. Hottest and coolest locations
print("\n3. HOTTEST LOCATION")
print(location_summary["avg_temperature_c"].idxmax())

print("\n4. COOLEST LOCATION")
print(location_summary["avg_temperature_c"].idxmin())

# 4. Monthly temperature analysis
df["timestamp"] = pd.to_datetime(df["timestamp"])
df["month_name"] = df["timestamp"].dt.strftime("%b")

monthly_summary = (
    df.groupby("month_name")
    .agg(
        avg_temperature_c=("temperature_c", "mean"),
        avg_humidity_pct=("relative_humidity_pct", "mean")
    )
    .round(2)
)

print("\n5. MONTHLY WEATHER SUMMARY")
print(monthly_summary)

# 5. Opportunity score summary
print("\n6. OPPORTUNITY SCORE SUMMARY")
print(df["opportunity_score"].describe().round(2))

print("\nRecords with opportunity flag:")
print(int(df["opportunity_flag"].astype(bool).sum()))

# 6. Save summaries
os.makedirs("data/output", exist_ok=True)

location_summary.to_csv(
    "data/output/location_summary.csv"
)

monthly_summary.to_csv(
    "data/output/monthly_summary.csv"
)

print("\n7. REPORT FILES SAVED")
print("data/output/location_summary.csv")
print("data/output/monthly_summary.csv")

print("\nEDA ANALYSIS COMPLETE")

import pandas as pd
import matplotlib.pyplot as plt
import os

# AtmoSync - Weather Visualization

df = pd.read_csv(
    "data/processed/atmosync_feature_engineered.csv"
)

os.makedirs("data/output", exist_ok=True)

# 1. Average temperature by location
location_temp = df.groupby("location")["temperature_c"].mean().sort_values()

plt.figure(figsize=(10, 6))
location_temp.plot(kind="bar")
plt.title("Average Temperature by Location")
plt.xlabel("Location")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=35, ha="right")
plt.tight_layout()
plt.savefig("data/output/average_temperature_by_location.png", dpi=300)
plt.close()

# 2. Average humidity by location
location_humidity = (
    df.groupby("location")["relative_humidity_pct"]
    .mean()
    .sort_values()
)

plt.figure(figsize=(10, 6))
location_humidity.plot(kind="bar")
plt.title("Average Humidity by Location")
plt.xlabel("Location")
plt.ylabel("Relative Humidity (%)")
plt.xticks(rotation=35, ha="right")
plt.tight_layout()
plt.savefig("data/output/average_humidity_by_location.png", dpi=300)
plt.close()

# 3. Monthly average temperature
df["timestamp"] = pd.to_datetime(df["timestamp"])

monthly_temp = (
    df.groupby(df["timestamp"].dt.to_period("M"))["temperature_c"]
    .mean()
)

monthly_temp.index = monthly_temp.index.astype(str)

plt.figure(figsize=(12, 6))
monthly_temp.plot(kind="line", marker="o")
plt.title("Monthly Average Temperature Trend")
plt.xlabel("Month")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("data/output/monthly_temperature_trend.png", dpi=300)
plt.close()

print("========== VISUALIZATION COMPLETE ==========")
print("1. data/output/average_temperature_by_location.png")
print("2. data/output/average_humidity_by_location.png")
print("3. data/output/monthly_temperature_trend.png")
print("============================================")
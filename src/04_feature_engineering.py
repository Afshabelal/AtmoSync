import pandas as pd

# ---------------------------------------------
# AtmoSync - Feature Engineering
# ---------------------------------------------

# Load cleaned data
input_file = "data/processed/atmosync_weather_cleaned.csv"
df = pd.read_csv(input_file)

# Convert timestamp
df["timestamp"] = pd.to_datetime(df["timestamp"])

# 1. Date and time features
df["date"] = df["timestamp"].dt.date
df["hour"] = df["timestamp"].dt.hour
df["day_of_week"] = df["timestamp"].dt.day_name()
df["month"] = df["timestamp"].dt.month
df["month_name"] = df["timestamp"].dt.month_name()

# 2. Temperature category
df["temperature_category"] = pd.cut(
    df["temperature_c"],
    bins=[-float("inf"), 18, 25, 30, float("inf")],
    labels=["Cool", "Comfortable", "Warm", "Hot"]
)

# 3. Humidity category
df["humidity_category"] = pd.cut(
    df["relative_humidity_pct"],
    bins=[-float("inf"), 40, 60, 80, float("inf")],
    labels=["Dry", "Comfortable", "Humid", "Very Humid"]
)

# 4. Calculate city-wide hourly averages
hourly_avg = (
    df.groupby("timestamp", as_index=False)
    .agg(
        avg_temperature_c=("temperature_c", "mean"),
        avg_humidity_pct=("relative_humidity_pct", "mean")
    )
)

# 5. Merge hourly averages back into dataset
df = df.merge(hourly_avg, on="timestamp", how="left")

# 6. Temperature and humidity gaps
df["temperature_gap_c"] = (
    df["temperature_c"] - df["avg_temperature_c"]
).abs()

df["humidity_gap_pct"] = (
    df["relative_humidity_pct"] - df["avg_humidity_pct"]
).abs()

# 7. Environmental opportunity score
# Temperature difference = 70%
# Humidity difference = 30%

df["opportunity_score"] = (
    (df["temperature_gap_c"] / df["temperature_gap_c"].max()) * 70
    +
    (df["humidity_gap_pct"] / df["humidity_gap_pct"].max()) * 30
)

# Round score
df["opportunity_score"] = df["opportunity_score"].round(2)

# 8. Opportunity flag
df["opportunity_flag"] = df["opportunity_score"] >= 60

# ---------------------------------------------
# Save engineered data
# ---------------------------------------------

output_file = "data/processed/atmosync_feature_engineered.csv"

df.to_csv(output_file, index=False)

# ---------------------------------------------
# Summary
# ---------------------------------------------

print("========== FEATURE ENGINEERING COMPLETE ==========")

print("\nRows:", len(df))
print("Columns:", len(df.columns))

print("\nNew columns:")
print([
    "date",
    "hour",
    "day_of_week",
    "month",
    "month_name",
    "temperature_category",
    "humidity_category",
    "avg_temperature_c",
    "avg_humidity_pct",
    "temperature_gap_c",
    "humidity_gap_pct",
    "opportunity_score",
    "opportunity_flag"
])

print("\nOpportunity records:")
print(df["opportunity_flag"].sum())

print("\nSaved to:")
print(output_file)

print("\n===================================================")
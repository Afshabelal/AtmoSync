import pandas as pd
import os

# ---------------------------------------------
# AtmoSync - Data Cleaning
# ---------------------------------------------

# Load raw data
input_file = "data/raw/atmosync_weather_data.csv"
df = pd.read_csv(input_file)

print("========== BEFORE CLEANING ==========")
print("Rows:", len(df))
print("Columns:", len(df.columns))

# 1. Convert timestamp to datetime
df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")

# 2. Convert weather columns to numeric
numeric_columns = [
    "temperature_c",
    "relative_humidity_pct",
    "precipitation_mm",
    "wind_speed_kmh",
    "surface_pressure_hpa",
    "latitude",
    "longitude"
]

for column in numeric_columns:
    df[column] = pd.to_numeric(df[column], errors="coerce")

# 3. Remove duplicate rows
duplicates_before = df.duplicated().sum()
df = df.drop_duplicates()

# 4. Remove rows with missing important values
important_columns = [
    "timestamp",
    "location",
    "temperature_c",
    "relative_humidity_pct"
]

missing_before = df[important_columns].isnull().any(axis=1).sum()

df = df.dropna(subset=important_columns)

# 5. Remove physically invalid values
df = df[
    (df["relative_humidity_pct"] >= 0) &
    (df["relative_humidity_pct"] <= 100) &
    (df["precipitation_mm"] >= 0) &
    (df["wind_speed_kmh"] >= 0) &
    (df["surface_pressure_hpa"] > 0)
]

# 6. Sort data
df = df.sort_values(["location", "timestamp"])

# 7. Create processed folder
output_folder = "data/processed"
os.makedirs(output_folder, exist_ok=True)

# 8. Save cleaned data
output_file = os.path.join(
    output_folder,
    "atmosync_weather_cleaned.csv"
)

df.to_csv(output_file, index=False)

# ---------------------------------------------
# Cleaning summary
# ---------------------------------------------

print("\n========== CLEANING SUMMARY ==========")
print("Duplicate rows found:", duplicates_before)
print("Rows with missing important values:", missing_before)
print("Rows after cleaning:", len(df))
print("Locations:", df["location"].nunique())
print("Saved to:", output_file)

print("\n========== CLEANING COMPLETE ==========")
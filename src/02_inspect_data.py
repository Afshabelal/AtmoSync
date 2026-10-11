import pandas as pd

# Load raw weather data
df = pd.read_csv("data/raw/atmosync_weather_data.csv")

print("========== ATMOSYNC DATA INSPECTION ==========")

print("\n1. Dataset Shape:")
print(df.shape)

print("\n2. Column Names:")
print(df.columns.tolist())

print("\n3. Data Types:")
print(df.dtypes)

print("\n4. Missing Values:")
print(df.isnull().sum())

print("\n5. Duplicate Rows:")
print(df.duplicated().sum())

print("\n6. Number of Locations:")
print(df["location"].nunique())

print("\n7. Locations:")
print(df["location"].unique())

print("\n8. Date Range:")
print(df["timestamp"].min())
print("to")
print(df["timestamp"].max())

print("\n9. Summary Statistics:")
print(df.describe())

print("\n========== INSPECTION COMPLETE ==========")

from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st

# Project paths
PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = (
    PROJECT_DIR
    / "data"
    / "processed"
    / "atmosync_feature_engineered.csv"
)

# Page setup
st.set_page_config(
    page_title="AtmoSync Dashboard",
    page_icon="🌦️",
    layout="wide",
)

st.title("🌦️ AtmoSync: Micro-Climate Analytics")
st.caption(
    "Weather comparison and environmental opportunity screening "
    "across Bengaluru locations"
)

# Load data
@st.cache_data
def load_data(file_path):
    data = pd.read_csv(file_path)
    data["timestamp"] = pd.to_datetime(
        data["timestamp"], errors="coerce"
    )
    return data


if not DATA_FILE.exists():
    st.error(f"Data file not found: {DATA_FILE}")
    st.info(
        "Please check that the feature-engineered CSV exists "
        "inside data/processed."
    )
    st.stop()

df = load_data(str(DATA_FILE))

required_columns = [
    "timestamp",
    "location",
    "temperature_c",
    "relative_humidity_pct",
    "opportunity_score",
    "opportunity_flag",
]

missing_columns = [
    col for col in required_columns if col not in df.columns
]

if missing_columns:
    st.error(f"Required columns missing: {missing_columns}")
    st.stop()

# Convert numeric fields safely
for col in [
    "temperature_c",
    "relative_humidity_pct",
    "opportunity_score",
    "precipitation_mm",
    "wind_speed_kmh",
]:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

# Normalize opportunity flag
df["opportunity_flag"] = (
    df["opportunity_flag"]
    .astype(str)
    .str.strip()
    .str.lower()
    .isin(["true", "1", "yes"])
)

# Sidebar filters
st.sidebar.header("Filter Weather Data")

locations = sorted(df["location"].dropna().unique().tolist())
selected_locations = st.sidebar.multiselect(
    "Select location(s)",
    options=locations,
    default=locations,
)

valid_dates = df["timestamp"].dropna()

if not valid_dates.empty:
    min_date = valid_dates.min().date()
    max_date = valid_dates.max().date()

    selected_dates = st.sidebar.date_input(
        "Select date range",
        value=(min_date, max_date),
        min_value=min_date,
        max_value=max_date,
    )
else:
    selected_dates = ()

# Apply filters
filtered = df[df["location"].isin(selected_locations)].copy()

if len(selected_dates) == 2:
    start_date, end_date = selected_dates
    filtered = filtered[
        filtered["timestamp"].dt.date.between(start_date, end_date)
    ]

if filtered.empty:
    st.warning("No records match the selected filters.")
    st.stop()

# Key metrics
total_records = len(filtered)
location_count = filtered["location"].nunique()
avg_temp = filtered["temperature_c"].mean()
avg_humidity = filtered["relative_humidity_pct"].mean()
flagged_count = int(filtered["opportunity_flag"].sum())

c1, c2, c3, c4, c5 = st.columns(5)

c1.metric("Weather Records", f"{total_records:,}")
c2.metric("Locations", location_count)
c3.metric(
    "Average Temperature",
    f"{avg_temp:.2f} °C" if pd.notna(avg_temp) else "N/A",
)
c4.metric(
    "Average Humidity",
    f"{avg_humidity:.2f}%" if pd.notna(avg_humidity) else "N/A",
)
c5.metric("Flagged Records", flagged_count)

st.divider()

# Location-wise summaries
st.subheader("📍 Location-wise Weather Summary")

summary_columns = {
    "temperature_c": "Average Temperature (°C)",
    "relative_humidity_pct": "Average Humidity (%)",
}

if "precipitation_mm" in filtered.columns:
    summary_columns["precipitation_mm"] = "Average Precipitation (mm)"

if "wind_speed_kmh" in filtered.columns:
    summary_columns["wind_speed_kmh"] = "Average Wind Speed (km/h)"

summary = (
    filtered.groupby("location", as_index=False)
    .agg({
        col: "mean" for col in summary_columns
    })
    .rename(columns=summary_columns)
    .round(2)
)

st.dataframe(summary, width="stretch", hide_index=True)

# Temperature chart
st.subheader("🌡️ Average Temperature by Location")

temp_chart = (
    filtered.groupby("location", as_index=False)["temperature_c"]
    .mean()
    .sort_values("temperature_c", ascending=False)
)

fig_temp = px.bar(
    temp_chart,
    x="location",
    y="temperature_c",
    color="temperature_c",
    labels={
        "location": "Location",
        "temperature_c": "Average Temperature (°C)",
    },
    title="Location-wise Average Temperature",
)
st.plotly_chart(fig_temp, width="stretch")

# Humidity chart
st.subheader("💧 Average Humidity by Location")

humidity_chart = (
    filtered.groupby("location", as_index=False)["relative_humidity_pct"]
    .mean()
    .sort_values("relative_humidity_pct", ascending=False)
)

fig_humidity = px.bar(
    humidity_chart,
    x="location",
    y="relative_humidity_pct",
    color="relative_humidity_pct",
    labels={
        "location": "Location",
        "relative_humidity_pct": "Average Humidity (%)",
    },
    title="Location-wise Average Relative Humidity",
)
st.plotly_chart(fig_humidity, use_container_width=True)

# Temperature trend over time
st.subheader("📈 Temperature Trend Over Time")

trend = (
    filtered.dropna(subset=["timestamp", "temperature_c"])
    .groupby(pd.Grouper(key="timestamp", freq="D"))["temperature_c"]
    .mean()
    .reset_index()
)

if not trend.empty:
    fig_trend = px.line(
        trend,
        x="timestamp",
        y="temperature_c",
        labels={
            "timestamp": "Date",
            "temperature_c": "Average Temperature (°C)",
        },
        title="Daily Average Temperature",
    )
    st.plotly_chart(fig_trend, use_container_width=True)
else:
    st.info("No valid temperature trend data is available.")

# Opportunity screening
st.subheader("🔎 Environmental Opportunity Screening")

st.caption(
    "The score is an analytical screening indicator based on "
    "environmental differences. It does not guarantee financial profit."
)

flagged = filtered[filtered["opportunity_flag"]].copy()

if flagged.empty:
    st.info("No records meet the configured opportunity threshold in this selection.")
else:
    display_columns = [
        col for col in [
            "timestamp",
            "location",
            "temperature_c",
            "relative_humidity_pct",
            "temperature_gap_c",
            "humidity_gap_pct",
            "opportunity_score",
        ]
        if col in flagged.columns
    ]

    flagged = flagged.sort_values(
        "opportunity_score", ascending=False
    )

    st.dataframe(
        flagged[display_columns],
        use_container_width=True,
        hide_index=True,
    )

# Download filtered data
st.subheader("⬇️ Download Filtered Data")

csv_data = filtered.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download filtered CSV",
    data=csv_data,
    file_name="atmosync_filtered_data.csv",
    mime="text/csv",
)

st.caption("AtmoSync | Data Analytics Internship Project")

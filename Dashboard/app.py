
from pathlib import Path

import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(
    page_title="AtmoSync: Micro-Climate Analytics",
    page_icon="🌦️",
    layout="wide"
)

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "data" / "processed" / "atmosync_feature_engineered.csv"

st.title("🌦️ AtmoSync: Micro-Climate Analytics")
st.write("Micro-climate data analysis across six Bengaluru locations.")

if not DATA_FILE.exists():
    st.error(f"Data file not found: {DATA_FILE}")
    st.stop()

df = pd.read_csv(DATA_FILE)

required_columns = [
    "temperature_c",
    "relative_humidity_pct",
    "location"
]

missing_columns = [col for col in required_columns if col not in df.columns]

if missing_columns:
    st.error(f"Missing columns: {', '.join(missing_columns)}")
    st.write("Available columns:", list(df.columns))
    st.stop()

df["temperature_c"] = pd.to_numeric(
    df["temperature_c"], errors="coerce"
)
df["relative_humidity_pct"] = pd.to_numeric(
    df["relative_humidity_pct"], errors="coerce"
)

st.sidebar.header("Filters")

locations = sorted(df["location"].dropna().unique().tolist())

selected_locations = st.sidebar.multiselect(
    "Select Locations",
    options=locations,
    default=locations
)

filtered = df[df["location"].isin(selected_locations)].copy()

if filtered.empty:
    st.warning("Please select at least one location.")
    st.stop()

col1, col2, col3 = st.columns(3)

col1.metric("Total Records", f"{len(filtered):,}")
col2.metric(
    "Average Temperature",
    f"{filtered['temperature_c'].mean():.2f} °C"
)
col3.metric(
    "Average Humidity",
    f"{filtered['relative_humidity_pct'].mean():.2f} %"
)

# Temperature chart
st.subheader("Average Temperature by Location")

temp_summary = (
    filtered.groupby("location", as_index=False)["temperature_c"]
    .mean()
)

fig_temp = px.bar(
    temp_summary,
    x="location",
    y="temperature_c",
    text_auto=".2f",
    title="Average Temperature by Location"
)

fig_temp.update_layout(
    xaxis_title="Location",
    yaxis_title="Temperature (°C)"
)

st.plotly_chart(fig_temp, width="stretch")

# Humidity chart
st.subheader("Average Humidity by Location")

humidity_summary = (
    filtered.groupby("location", as_index=False)["relative_humidity_pct"]
    .mean()
)

fig_humidity = px.bar(
    humidity_summary,
    x="location",
    y="relative_humidity_pct",
    text_auto=".2f",
    title="Average Humidity by Location"
)

fig_humidity.update_layout(
    xaxis_title="Location",
    yaxis_title="Humidity (%)"
)

st.plotly_chart(fig_humidity, width="stretch")

# Opportunity records
if "opportunity_flag" in filtered.columns:
    st.subheader("Micro-Climate Opportunity Records")

    opportunities = filtered[
        filtered["opportunity_flag"]
        .astype(str)
        .str.lower()
        .isin(["true", "1"])
    ]

    st.metric("Flagged Records", f"{len(opportunities):,}")

    if not opportunities.empty:
        display_columns = [
            col for col in [
                "timestamp",
                "location",
                "temperature_c",
                "relative_humidity_pct",
                "opportunity_score"
            ]
            if col in opportunities.columns
        ]

        st.dataframe(
            opportunities[display_columns],
            hide_index=True,
            width="stretch"
        )
    else:
        st.info("No opportunity records found for the selected locations.")

# Monthly temperature trend
if "month" in filtered.columns:
    filtered["month"] = pd.to_numeric(
        filtered["month"], errors="coerce"
    )

    month_names = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }

    monthly_summary = (
        filtered.dropna(subset=["month"])
        .groupby("month")["temperature_c"]
        .mean()
        .reset_index()
        .sort_values("month")
    )

    monthly_summary["month_name"] = (
        monthly_summary["month"].astype(int).map(month_names)
    )

    fig_month = px.line(
        monthly_summary,
        x="month_name",
        y="temperature_c",
        markers=True,
        category_orders={
            "month_name": [
                "January", "February", "March", "April",
                "May", "June", "July", "August",
                "September", "October", "November", "December"
            ]
        },
        title="Average Monthly Temperature"
    )

    fig_month.update_layout(
        xaxis_title="Month",
        yaxis_title="Temperature (°C)"
    )

    st.plotly_chart(fig_month, width="stretch")

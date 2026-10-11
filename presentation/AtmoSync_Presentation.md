# AtmoSync: Micro-Climate Arbitrage Analytics
### 10-Slide Project Presentation

## Slide 1: Title Slide

**AtmoSync: Micro-Climate Arbitrage Analytics**

- Organization: Infotact Solutions
- Role: Data Associate L1 Intern
- Domain: Data Analytics
- Project Duration: 1 Month

## Slide 2: Project Overview & Objectives

**Project Overview**

AtmoSync analyzes hourly weather observations across six Bengaluru locations to identify differences in temperature and humidity.

**Objectives**
- Collect and clean weather data.
- Perform feature engineering and exploratory data analysis.
- Compare environmental conditions across locations.
- Calculate an environmental opportunity score.
- Present insights through charts and an interactive dashboard.

## Slide 3: Dataset & Technology Stack

**Dataset**
- Total records: 52,560
- Locations: 6
- Observations: Hourly weather data
- Records per location: 8,760

**Locations**
Bengaluru Central, Electronic City, Jayanagar, Rajajinagar, Whitefield, and Yelahanka.

**Technologies**
Python, Pandas, NumPy, Matplotlib, Seaborn, Plotly, Streamlit, and VS Code.

## Slide 4: Project Workflow

1. Data Collection
2. Data Inspection
3. Data Cleaning
4. Feature Engineering
5. Exploratory Data Analysis
6. Data Visualization
7. Opportunity Screening
8. Dashboard and Reporting

**Outcome:** An end-to-end weather-data analytics workflow.

## Slide 5: Data Cleaning & Feature Engineering

**Data Validation**
- Missing values: 0
- Duplicate rows: 0
- Opportunity-flagged records: 2

**Features Created**
- Date, hour, day of week, and month
- Temperature and humidity categories
- Hourly average temperature and humidity
- Differences from hourly averages
- Opportunity score and opportunity flag

These features help compare local weather conditions with corresponding hourly averages.

## Slide 6: Location-Wise Analysis

**Average Temperature**
- Highest: Bengaluru Central and Rajajinagar — 23.76°C
- Lowest: Electronic City — 23.06°C

**Average Relative Humidity**
- Highest: Electronic City — 70.66%
- Lowest: Bengaluru Central and Rajajinagar — 66.55%

**Insert charts:**
- `avg_temp_by_location.png`
- `average_humidity_by_location.png`

*Insight: Average temperature and humidity vary across the six locations, although some locations have identical summary statistics that require further investigation.*

## Slide 7: Monthly Trends & Visualization

**Monthly Findings**
- Warmest month: April — 28.34°C average temperature
- Coolest month: December — 20.09°C
- Highest average humidity: October — 81.16%
- Lowest average humidity: April — 45.20%

**Insert chart:**
- `monthly_temperature_trend.png`

The monthly summaries help identify seasonal patterns in temperature and humidity.

## Slide 8: Opportunity Score & Key Results

**Scoring Method**
- Temperature difference: Up to 70 points
- Humidity difference: Up to 30 points
- Flagging threshold: Score ≥ 60

**Flagged Records**
- 18 March 2026, 16:00 — Yelahanka: 84.26
- 18 May 2026, 16:00 — Yelahanka: 100.00

Two records met the configured threshold and were selected for further investigation.

*The score is a custom analytical screening indicator, not a verified measure of financial profitability.*

## Slide 9: Limitations & Future Scope

**Limitations**
- Weather data source and provenance need verification.
- Similar statistics across some locations need investigation.
- Market prices, demand, and operating costs are not included.
- Actual financial profitability has not been established.

**Future Scope**
- Integrate verified weather data.
- Include market and business information.
- Validate the scoring methodology.
- Enhance dashboard filters and insights.
- Automate reporting and data quality checks.

## Slide 10: Conclusion & Thank You

**Conclusion**

AtmoSync demonstrates an end-to-end data analytics workflow, from weather-data collection and cleaning to feature engineering, visualization, and opportunity screening.

**Key Takeaway:** Environmental differences can help identify records worth investigating, but additional market and business evidence is necessary to establish actual arbitrage opportunities.

**Thank You!**

Questions & Discussion
# AtmoSync: Micro-Climate Arbitrage Analytics

## Final Project Report

**Organization:** Infotact Solutions
**Internship Role:** Data Associate L1 Intern
**Domain:** Data Analytics
**Project Duration:** 1 Month

---

## 1. Project Overview

AtmoSync is a micro-climate analytics project designed to analyze weather variations across multiple locations in Bengaluru. It processes hourly weather observations, identifies differences in environmental conditions, and generates analytical indicators that can help highlight locations with unusual temperature and humidity variations.

The project demonstrates a data analytics workflow, including data collection, inspection, cleaning, feature engineering, exploratory data analysis (EDA), and visualization.

## 2. Project Objectives

* Collect hourly weather data for multiple Bengaluru locations.
* Inspect the dataset and understand its structure and quality.
* Clean and prepare data for analysis.
* Create time-based and weather-related features.
* Compare temperature and humidity across locations.
* Calculate a screening score based on environmental differences.
* Generate summary tables and visualizations for insights.

## 3. Locations Covered

The dataset covers six locations:

1. Bengaluru Central
2. Electronic City
3. Jayanagar
4. Rajajinagar
5. Whitefield
6. Yelahanka

The collected dataset contains 52,560 records, representing 8,760 hourly records per location.

## 4. Tools and Technologies

* **Python:** Data processing and analysis
* **Pandas:** Data manipulation and aggregation
* **NumPy:** Numerical operations
* **Matplotlib:** Data visualization
* **Seaborn:** Statistical visualization support
* **Plotly:** Interactive visualization support
* **VS Code:** Development environment
* **CSV:** Data storage and exchange format

## 5. Project Workflow

### 5.1 Data Collection

The data collection script generates or retrieves the weather dataset used by the project. The resulting CSV file is stored at:

`data/raw/atmosync_weather_data.csv`

The dataset contains timestamps, weather measurements, location names, and geographical coordinates. The underlying data source should be documented separately if external data was used.

### 5.2 Data Inspection

The dataset was inspected to understand its columns, numerical ranges, and overall structure.

The weather measurements include temperature, relative humidity, precipitation, wind speed, and surface pressure.

### 5.3 Data Cleaning

The cleaning script prepares the dataset for analysis and saves the cleaned output at:

`data/processed/atmosync_weather_cleaned.csv`

The dataset was checked for missing values and duplicate rows. Validation output showed zero duplicate rows and zero missing values in the displayed humidity, precipitation, wind speed, surface pressure, location, latitude, and longitude columns.

### 5.4 Feature Engineering

Additional analytical features were created from the cleaned dataset, including:

* Date and hour
* Day of the week
* Month and month name
* Temperature category
* Humidity category
* Hourly average temperature and humidity across locations
* Absolute temperature difference from the hourly average
* Absolute humidity difference from the hourly average
* Opportunity score and opportunity flag

The engineered dataset is saved at:

`data/processed/atmosync_feature_engineered.csv`

### 5.5 Exploratory Data Analysis

The EDA process calculates location-wise weather summaries and monthly temperature and humidity summaries.

Generated files:

* `data/output/location_summary.csv`
* `data/output/monthly_summary.csv`

The analysis helps compare environmental conditions across locations and examine changes across months.

### 5.6 Data Visualization

The project generates the following charts:

* `data/output/average_temperature_by_location.png`
* `data/output/average_humidity_by_location.png`
* `data/output/monthly_temperature_trend.png`

These visualizations make it easier to compare locations and observe monthly temperature patterns.

## 6. Key Findings

### 6.1 Location-wise Temperature

The location summary shows average temperatures ranging from approximately 23.06°C to 23.76°C across the six locations.

Electronic City has the lowest reported average temperature at approximately 23.06°C. Bengaluru Central and Rajajinagar have reported average temperatures of approximately 23.76°C.

### 6.2 Location-wise Humidity

Average relative humidity ranges from approximately 66.55% to 70.66%.

Electronic City has the highest reported average humidity at approximately 70.66%, while Bengaluru Central and Rajajinagar have reported averages of approximately 66.55%.

### 6.3 Opportunity Screening

The analysis identified two records meeting the configured opportunity-score threshold:

* **18 March 2026, 16:00 — Yelahanka:** Score 84.26
* **18 May 2026, 16:00 — Yelahanka:** Score 100.00

These records indicate comparatively large temperature and humidity differences from the corresponding hourly averages in the analyzed dataset.

## 7. Opportunity Score Methodology

The opportunity score is a custom analytical indicator calculated using normalized temperature and humidity differences.

* Temperature difference contributes up to 70 points.
* Humidity difference contributes up to 30 points.
* The two normalized contributions are added to calculate the score.
* A record is flagged when its score is greater than or equal to 60.

The score is intended to prioritize records for further investigation. It does not independently measure market demand, financial returns, or profitability.

## 8. Project Limitations

* The analysis focuses on environmental measurements rather than actual market prices or business transactions.
* The opportunity score is a custom heuristic and has not been validated as a financial prediction model.
* The underlying weather data source and its reliability should be documented and verified.
* Similar summary statistics for some locations should be investigated to ensure the data represents genuine location-level variation.
* Additional market, demand, logistics, and cost data would be required to evaluate real arbitrage opportunities.

## 9. Future Enhancements

* Integrate verified weather data from a documented source.
* Add market prices and demand indicators for relevant goods or services.
* Investigate anomalies and validate the scoring methodology.
* Build an interactive dashboard with filters for location, date, and weather conditions.
* Add automated data validation and repeatable reporting.
* Evaluate candidate opportunities against actual business outcomes.

## 10. Conclusion

AtmoSync demonstrates an end-to-end data analytics workflow for comparing micro-climate conditions across multiple locations. The project combines data preparation, feature engineering, exploratory analysis, scoring, and visualization to identify environmental differences that merit further investigation.

The current opportunity score is an analytical screening indicator, not a guarantee of financial profit. Integrating reliable market and business data would be a necessary next step toward assessing practical arbitrage opportunities.

---

**End of Report**

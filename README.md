# AtmoSync: Micro-Climate Arbitrage Analytics

## Project Overview

AtmoSync is a data analytics project that compares environmental conditions across six Bengaluru locations. It analyzes hourly weather observations and identifies records with relatively large temperature and humidity differences.

The project demonstrates an end-to-end analytics workflow covering data collection, data cleaning, feature engineering, exploratory data analysis, visualization, and interactive dashboard development.

## Objectives

* Analyze weather conditions across six locations.
* Prepare and validate the weather dataset.
* Create time-based and environmental features.
* Compare location-wise and monthly weather patterns.
* Flag records for further environmental analysis.
* Present findings through charts and a dashboard.

## Technology Stack

* Python
* Pandas and NumPy
* Matplotlib and Seaborn
* Plotly
* Streamlit
* Visual Studio Code
* CSV datasets

## Locations

1. Bengaluru Central
2. Electronic City
3. Jayanagar
4. Rajajinagar
5. Whitefield
6. Yelahanka

## Project Structure

```text
AtmoSync/
├── Dashboard/
│   └── app.py
├── data/
│   ├── raw/
│   ├── processed/
│   └── output/
├── documentation/
│   └── project_charter.md
├── presentation/
│   └── AtmoSync_Presentation.md
├── reports/
│   └── AtmoSync_Final_Report.md
└── src/
    ├── 01_data_collection.py
    ├── 02_inspect_data.py
    ├── 03_clean_data.py
    ├── 04_feature_engineering.py
    ├── 05_eda_analysis.py
    └── 06_visualize_data.py
```

## Dataset and Validation

The feature-engineered dataset contains 52,560 records across six locations.

The final validation reported:

* Missing values: 0
* Duplicate rows: 0
* Opportunity-flagged records: 2

## Generated Outputs

The `data/output/` folder contains:

* `location_summary.csv`
* `monthly_summary.csv`
* `average_temperature_by_location.png`
* `average_humidity_by_location.png`
* `monthly_temperature_trend.png`

The processed datasets are stored in `data/processed/`.

## Run the Dashboard

Run the following command from the project root in PowerShell:

```powershell
.\.venv\Scripts\python.exe -m streamlit run .\Dashboard\app.py
```

Open the local URL displayed in the terminal to view the dashboard.

## Opportunity Score

The project calculates a custom screening score using normalized temperature and humidity differences from hourly averages. Temperature contributes up to 70 points and humidity contributes up to 30 points. Records scoring 60 or higher are flagged.

The score is an analytical screening indicator, not a verified measure of financial profitability.

## Limitations

* The underlying weather data source and provenance should be documented and verified.
* Similar summary statistics for some locations require further investigation.
* Market prices, demand, operating costs, and transaction data are not incorporated.
* Actual arbitrage profitability has not been established.

## Future Scope

* Integrate verified weather data.
* Incorporate market and business data.
* Validate the scoring approach.
* Enhance the dashboard with additional filters and insights.
* Automate data quality checks and reporting.

## Conclusion

AtmoSync demonstrates a complete weather-data analytics workflow, from raw data processing to visualization and interactive reporting. Its results can support further investigation of environmental differences, while real-world arbitrage assessment requires additional market and business evidence.

# Ford GoBike Performance Dashboard

A comprehensive data visualization dashboard analyzing Ford GoBike (now Bay Wheels) trip data using Python, Plotly, and Dash.

## 📊 Project Overview

This interactive dashboard provides insights into bike-sharing usage patterns across San Francisco, including:

- Trip volume and duration analysis
- User demographics (age, gender, user type)
- Temporal patterns (hourly usage)
- Station popularity rankings

## 🎯 Features

### Key Metrics

- **Total Trips**: 165,437
- **Average Duration**: 9.2 minutes
- **Active Users**: 4,597

### Visualizations

#### 1. Temporal Analysis

- Hourly trip distribution showing peak usage times
- Identifies rush hour patterns (8 AM and 5-6 PM peaks)

#### 2. Trip Duration Distribution

- Histogram showing most trips are under 15 minutes
- Right-skewed distribution indicating short commuter trips

#### 3. User Demographics

**Subscriber vs Customer Usage**

- 91.7% Subscribers (regular users)
- 8.3% Customers (casual/one-time users)

**Trips by Gender**

- Male: 74.9%
- Female: 23.1%
- Other: 2.0%

#### 4. Age Group Analysis

- 30-44 age group: Highest usage (~80k trips)
- 18-29 age group: Second highest (~62k trips)
- 45-59 age group: Moderate usage (~20k trips)
- 60-79 age group: Lowest usage

#### 5. Top Stations

| Rank | Station                          | Trips |
| ---- | -------------------------------- | ----- |
| 1    | Market St at 10th St             | 3,541 |
| 2    | San Francisco Caltrain Station 2 | 3,332 |
| 3    | Berry St at 4th St               | 2,854 |
| 4    | Montgomery St BART Station       | 2,606 |
| 5    | San Francisco Caltrain           | 2,517 |

## 🏗️ Project Structure

<p align="center">
  <img src="images/project structure.PNG" width="800">
</p>

    DATAANALYSISFINAL
    └── data-analysis-final-project/
    ├── .vscode/
    ├── dashboard/
    │   ├── pycache/
    │   ├── components/
    │   │   ├── pycache/
    │   │   ├── init.py
    │   │   ├── callbacks.py
    │   │   └── layout.py
    │   ├── plots/
    │   │   ├── pycache/
    │   │   ├── init.py
    │   │   ├── station_plots.py
    │   │   ├── time_plots.py
    │   │   └── user_plots.py
    │   ├── utils/
    │   │   └── init.py
    │   └── App.py
    ├── data/
    ├── material/
    ├── preprocessing/
    │   ├── pycache/
    │   ├── init.py
    │   ├── pipeline.py
    │   └── preprocessor.py
    └── README.md

## 📊 Dashboard – Part 1: KPIs & Filters

This section shows the interactive filters (User Type, Gender, Age Group) and key performance indicators.

<p align="center">
  <img src="images/one_part.PNG" width="900">
</p>

## 📈 Dashboard – Part 2: Usage Patterns

This section analyzes trip behavior by hour of day and trip duration distribution.

<p align="center">
  <img src="images/two_part.PNG" width="900">
</p>

## 🎥 Demo Video

<p align="center">
  ▶️ <a href="videos/APP.mp4">Watch the dashboard demo</a>
</p>

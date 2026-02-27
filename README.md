# Ford GoBike Performance Dashboard

A comprehensive data visualization dashboard analyzing Ford GoBike (now Bay Wheels) trip data using Python, Plotly, and Dash.

![Dashboard Overview](first%20part.PNG)

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

![Trips by Hour](first%20part.PNG)

- Hourly trip distribution showing peak usage times
- Identifies rush hour patterns (8 AM and 5-6 PM peaks)

#### 2. Trip Duration Distribution

![Duration Distribution](first%20part.PNG)

- Histogram showing most trips are under 15 minutes
- Right-skewed distribution indicating short commuter trips

#### 3. User Demographics

![User Type and Gender](second%20part.PNG)

**Subscriber vs Customer Usage**

- 91.7% Subscribers (regular users)
- 8.3% Customers (casual/one-time users)

**Trips by Gender**

- Male: 74.9%
- Female: 23.1%
- Other: 2.0%

#### 4. Age Group Analysis

![Age Groups](third%20part.PNG)

- 30-44 age group: Highest usage (~80k trips)
- 18-29 age group: Second highest (~62k trips)
- 45-59 age group: Moderate usage (~20k trips)
- 60-79 age group: Lowest usage

#### 5. Top Stations

![Top Stations](third%20part.PNG)
| Rank | Station | Trips |
|------|---------|-------|
| 1 | Market St at 10th St | 3,541 |
| 2 | San Francisco Caltrain Station 2 | 3,332 |
| 3 | Berry St at 4th St | 2,854 |
| 4 | Montgomery St BART Station | 2,606 |
| 5 | San Francisco Caltrain | 2,517 |

## 🏗️ Project Structure

<img src="images/project structure.png" width="800">

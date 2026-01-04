# COVID-19-Data-analysis-and-visualization-python-
# 🦠 COVID-19 Data Analysis and Visualization

## 📌 Project Objective
The objective of this project is to analyze the **spread of COVID-19 over time** by examining trends in confirmed cases and deaths across different countries. The project aims to provide meaningful insights into how the pandemic evolved over time using real-world data and visual representations.

This project demonstrates practical implementation of:
- Data manipulation using Pandas
- Time-series analysis
- Data visualization using Matplotlib and Seaborn

---

## ✨ Features and Functionalities

### 1. Data Collection
- Uses a real-world COVID-19 dataset sourced from **Our World in Data (OWID)**.
- Dataset contains country-wise and date-wise COVID-19 statistics.

### 2. Data Analysis
- Analyzes COVID-19 trends for multiple countries.
- Computes:
  - Total confirmed cases
  - Total deaths
- Performs time-based analysis to observe the spread over months.

### 3. Country-wise Comparison
- Allows comparison of COVID-19 impact across countries.
- Highlights differences in total cases using graphical comparison.

### 4. Data Visualization
The project generates the following visualizations:
- **Line Graph** – Total COVID-19 cases over time for each country
- **Line Graph** – Total deaths over time
- **Bar Chart** – Country-wise comparison of total cases on the latest date

These visualizations help in understanding pandemic trends clearly and intuitively.

---

## 🖥️ User Interface

This project uses a **Command Line Interface (CLI)** combined with **graphical plots**.

### CLI Interface:
- Displays dataset loading status
- Prints summary statistics for selected countries:
  - Total cases
  - Total deaths

### Graphical Interface:
- Interactive graphs displayed using:
  - Matplotlib
  - Seaborn

The interface is simple, readable, and suitable for academic demonstrations and viva examinations.

---

## 📂 Dataset Details

**Dataset Source:** Our World in Data (COVID-19 Dataset)

**File Name:** `owid_covid_data.csv`

**Important Columns Used:**
- `location` – Country name
- `date` – Date of observation (YYYY-MM-DD)
- `total_cases` – Cumulative confirmed cases
- `new_cases` – Daily new cases
- `total_deaths` – Cumulative deaths
- `new_deaths` – Daily deaths

The dataset represents real-world COVID-19 statistics collected from official health authorities.

---

## ⚙️ Project Requirements

### Software Requirements
- Python 3.x

### Python Libraries
- Pandas
- Matplotlib
- Seaborn

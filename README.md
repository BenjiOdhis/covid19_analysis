# 🦠 COVID-19 Global Data Tracker

## 📘 Description
A Python-based project that tracks and analyzes global COVID-19 trends. This script processes real-world data from [Our World in Data](https://ourworldindata.org/coronavirus), cleans it, and visualizes key metrics like infections, deaths, and vaccination progress across countries.

> Built using Python, pandas, matplotlib, and seaborn — run fully in VS Code.

---

## 🎯 Objectives
- Import and clean COVID-19 data
- Analyze trends over time (cases, deaths, vaccinations)
- Compare metrics across selected countries
- Visualize trends with charts
- Communicate findings through summary and saved plots

---

## 🛠️ Tools & Libraries
- Python 3
- `pandas`
- `matplotlib`
- `seaborn`
- VS Code (instead of Jupyter)

---

## 📂 Folder Structure
covid-tracker/
├── data/
│ └── owid-covid-data.csv
├── charts/
│ ├── total_cases_over_time.png
│ ├── daily_new_cases.png
│ ├── death_rate_over_time.png
│ ├── total_vaccinations_over_time.png
│ └── percent_vaccinated.png
├── covid_analysis.py
└── README.md

---

## ▶️ How to Run
1. Clone the repository
2. Ensure you have Python 3 installed
3. Install dependencies:
   ```bash
   pip install pandas matplotlib seaborn

import pandas as pd

# Load the dataset
try:
    df = pd.read_csv("data/owid-covid-data.csv")
    print("✅ Dataset loaded successfully.")
except FileNotFoundError:
    print("❌ File not found. Check the path.")
    exit()

# Preview the structure
print("\n📌 First 5 rows:")
print(df.head())

print("\n🧠 Columns available:")
print(df.columns)

print("\n🔍 Checking missing values:")
print(df.isnull().sum().head(15))  # Just showing the first 15 columns for now
# Convert 'date' column to datetime
df['date'] = pd.to_datetime(df['date'])

# Filter for selected countries
countries = ['Kenya', 'United States', 'India']
df_countries = df[df['location'].isin(countries)]

# Select relevant columns
columns = [
    'date', 'location', 'total_cases', 'new_cases',
    'total_deaths', 'new_deaths', 'total_vaccinations',
    'people_fully_vaccinated', 'population'
]
df_countries = df_countries[columns]

# Drop rows with missing date or location (very rare)
df_countries.dropna(subset=['date', 'location'], inplace=True)

# Optional: Fill missing numeric values with 0 for simplicity
df_countries.fillna(0, inplace=True)

# Confirm structure
print("\n✅ Filtered dataset (Kenya, USA, India):")
print(df_countries.head(10))

import matplotlib.pyplot as plt

# Create charts directory if it doesn't exist
import os
if not os.path.exists("charts"):
    os.makedirs("charts")

# Plot total cases over time by country
plt.figure(figsize=(10, 6))
for country in countries:
    subset = df_countries[df_countries['location'] == country]
    plt.plot(subset['date'], subset['total_cases'], label=country)

plt.title("📈 Total COVID-19 Cases Over Time")
plt.xlabel("Date")
plt.ylabel("Total Cases")
plt.legend()
plt.tight_layout()
plt.grid(True)
plt.savefig("charts/total_cases_over_time.png")
plt.show()

# 📊 Daily new cases comparison
plt.figure(figsize=(10, 6))
for country in countries:
    subset = df_countries[df_countries['location'] == country]
    plt.plot(subset['date'], subset['new_cases'], label=country)

plt.title("🦠 Daily New COVID-19 Cases")
plt.xlabel("Date")
plt.ylabel("New Cases")
plt.legend()
plt.tight_layout()
plt.grid(True)
plt.savefig("charts/daily_new_cases.png")
plt.show()

# 📈 Death Rate = total_deaths / total_cases
plt.figure(figsize=(10, 6))
for country in countries:
    subset = df_countries[df_countries['location'] == country].copy()
    subset['death_rate'] = subset['total_deaths'] / subset['total_cases']
    plt.plot(subset['date'], subset['death_rate'], label=country)

plt.title("☠️ COVID-19 Death Rate Over Time")
plt.xlabel("Date")
plt.ylabel("Death Rate")
plt.legend()
plt.tight_layout()
plt.grid(True)
plt.savefig("charts/death_rate_over_time.png")
plt.show()

# 💉 Total vaccinations over time
plt.figure(figsize=(10, 6))
for country in countries:
    subset = df_countries[df_countries['location'] == country]
    plt.plot(subset['date'], subset['total_vaccinations'], label=country)

plt.title("💉 Total COVID-19 Vaccinations Over Time")
plt.xlabel("Date")
plt.ylabel("Total Vaccinations")
plt.legend()
plt.tight_layout()
plt.grid(True)
plt.savefig("charts/total_vaccinations_over_time.png")
plt.show()

# ✅ Percent fully vaccinated
plt.figure(figsize=(10, 6))
for country in countries:
    subset = df_countries[df_countries['location'] == country].copy()
    subset['percent_vaccinated'] = (subset['people_fully_vaccinated'] / subset['population']) * 100
    plt.plot(subset['date'], subset['percent_vaccinated'], label=country)

plt.title("🧬 Percent of Population Fully Vaccinated")
plt.xlabel("Date")
plt.ylabel("Percent Vaccinated (%)")
plt.legend()
plt.tight_layout()
plt.grid(True)
plt.savefig("charts/percent_vaccinated.png")
plt.show()

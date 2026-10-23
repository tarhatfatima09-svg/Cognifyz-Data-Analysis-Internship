
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Set project paths
BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT_DIR = Path(__file__).resolve().parent / "outputs"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Load dataset
df = pd.read_csv(BASE_DIR / "Dataset .csv")

# Check required columns
print("Total restaurant records:", len(df))
print("Cities available:", df["City"].nunique())

# Task 1: City with the highest number of restaurants
restaurant_counts = df["City"].value_counts()

print("\nCITY WITH THE HIGHEST NUMBER OF RESTAURANTS")
print(restaurant_counts.head(1))

# Task 2: Average rating for each city
city_ratings = (
    df.dropna(subset=["City", "Aggregate rating"])
    .groupby("City")["Aggregate rating"]
    .mean()
    .sort_values(ascending=False)
)

print("\nAVERAGE RATING BY CITY (TOP 10)")
print(city_ratings.head(10).round(2))

# Task 3: City with the highest average rating
print("\nCITY WITH THE HIGHEST AVERAGE RATING")
print(city_ratings.head(1).round(2))

# Save restaurant counts and average ratings
summary = pd.concat(
    [
        restaurant_counts.rename("Restaurant Count"),
        city_ratings.rename("Average Rating")
    ],
    axis=1
)

summary.index.name = "City"
summary = summary.sort_values(
    "Restaurant Count", ascending=False
)

summary.to_csv(OUTPUT_DIR / "city_analysis_results.csv")

# Chart 1: Cities with the most restaurants
top_cities = restaurant_counts.head(10)

plt.figure(figsize=(11, 6))
bars = plt.bar(top_cities.index, top_cities.values)
plt.title("Top 10 Cities by Number of Restaurants")
plt.xlabel("City")
plt.ylabel("Number of Restaurants")
plt.xticks(rotation=45, ha="right")
plt.bar_label(bars, padding=2)
plt.tight_layout()
plt.savefig(
    OUTPUT_DIR / "city_restaurant_counts.png",
    dpi=300,
    bbox_inches="tight"
)
plt.show()

# Chart 2: Average ratings for the top 10 cities
top_rated_cities = city_ratings.head(10)

plt.figure(figsize=(11, 6))
bars = plt.bar(
    top_rated_cities.index,
    top_rated_cities.values
)
plt.title("10 Cities with the Highest Average Ratings")
plt.xlabel("City")
plt.ylabel("Average Rating")
plt.xticks(rotation=45, ha="right")
plt.bar_label(bars, fmt="%.2f", padding=2)
plt.tight_layout()
plt.savefig(
    OUTPUT_DIR / "city_average_ratings.png",
    dpi=300,
    bbox_inches="tight"
)
plt.show()

print("\nFiles saved successfully:")
print("city_analysis_results.csv")
print("city_restaurant_counts.png")
print("city_average_ratings.png")

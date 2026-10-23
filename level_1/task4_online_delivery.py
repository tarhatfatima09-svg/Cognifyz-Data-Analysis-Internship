
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Set project and output folders
BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT_DIR = Path(__file__).resolve().parent / "outputs"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Load the restaurant dataset
df = pd.read_csv(BASE_DIR / "Dataset .csv")

print("Total restaurant records:", len(df))

# Check delivery availability
print("\nOnline delivery values:")
print(df["Has Online delivery"].value_counts(dropna=False))

# Calculate delivery percentages
delivery_counts = df["Has Online delivery"].value_counts()
delivery_percentages = (
    delivery_counts / len(df) * 100
).round(2)

delivery_results = pd.DataFrame({
    "Online Delivery": delivery_counts.index,
    "Restaurant Count": delivery_counts.values,
    "Percentage (%)": delivery_percentages.values
})

print("\nONLINE DELIVERY DISTRIBUTION")
print("-" * 45)
print(delivery_results.to_string(index=False))

# Calculate average ratings for each delivery group
rating_results = (
    df.dropna(subset=["Aggregate rating"])
    .groupby("Has Online delivery")["Aggregate rating"]
    .agg(["mean", "count"])
    .reset_index()
)

rating_results["mean"] = rating_results["mean"].round(2)

rating_results = rating_results.rename(columns={
    "Has Online delivery": "Online Delivery",
    "mean": "Average Rating",
    "count": "Restaurants with Ratings"
})

print("\nAVERAGE RATINGS BY ONLINE DELIVERY")
print("-" * 45)
print(rating_results.to_string(index=False))

# Save results to CSV files
delivery_results.to_csv(
    OUTPUT_DIR / "online_delivery_distribution.csv",
    index=False
)

rating_results.to_csv(
    OUTPUT_DIR / "online_delivery_rating_comparison.csv",
    index=False
)

# Chart 1: Delivery availability
plt.figure(figsize=(8, 5))
bars = plt.bar(
    delivery_results["Online Delivery"].astype(str),
    delivery_results["Restaurant Count"]
)
plt.title("Restaurants Offering Online Delivery")
plt.xlabel("Online Delivery Available")
plt.ylabel("Number of Restaurants")
plt.bar_label(bars, padding=3)
plt.tight_layout()
plt.savefig(
    OUTPUT_DIR / "online_delivery_distribution.png",
    dpi=300,
    bbox_inches="tight"
)
plt.show()

# Chart 2: Average rating comparison
plt.figure(figsize=(8, 5))
bars = plt.bar(
    rating_results["Online Delivery"].astype(str),
    rating_results["Average Rating"]
)
plt.title("Average Rating With vs Without Online Delivery")
plt.xlabel("Online Delivery Available")
plt.ylabel("Average Aggregate Rating")
plt.bar_label(bars, fmt="%.2f", padding=3)
plt.tight_layout()
plt.savefig(
    OUTPUT_DIR / "online_delivery_rating_comparison.png",
    dpi=300,
    bbox_inches="tight"
)
plt.show()

print("\nFiles saved successfully:")
print("1. online_delivery_distribution.csv")
print("2. online_delivery_rating_comparison.csv")
print("3. online_delivery_distribution.png")
print("4. online_delivery_rating_comparison.png")
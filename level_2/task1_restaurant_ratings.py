
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Get the project folder and file paths
project_folder = Path(__file__).resolve().parent.parent
dataset_path = project_folder / "Dataset .csv"
output_folder = Path(__file__).resolve().parent / "outputs"

output_folder.mkdir(parents=True, exist_ok=True)

# Load the dataset
df = pd.read_csv(dataset_path)

# Select the required columns
ratings = df["Aggregate rating"]
votes = df["Votes"]

# Count restaurants with no rating
unrated_count = (ratings == 0).sum()

# Exclude zero ratings when analyzing actual rating ranges
rated_restaurants = ratings[ratings > 0]

# Define rating ranges
rating_bins = [1, 2, 3, 4, 5.01]
rating_labels = ["1.0–1.9", "2.0–2.9", "3.0–3.9", "4.0–5.0"]

rating_ranges = pd.cut(
    rated_restaurants,
    bins=rating_bins,
    labels=rating_labels,
    right=False,
    include_lowest=True
)

# Count restaurants in each rating range
rating_distribution = rating_ranges.value_counts(
    sort=False
)

# Add unrated restaurants as a separate category for visualization
chart_distribution = pd.concat([
    pd.Series({"0 (Unrated)": unrated_count}),
    rating_distribution
])

# Find the most common rating range among rated restaurants
most_common_range = rating_distribution.idxmax()
most_common_count = rating_distribution.max()

# Calculate average votes per restaurant
average_votes = votes.mean()

# Print results
print("========== RESTAURANT RATINGS ANALYSIS ==========")
print("Total restaurants:", len(df))
print("Restaurants with rating 0:", unrated_count)
print("\nRating distribution:")
print(chart_distribution)

print("\nMost common rating range:", most_common_range)
print("Restaurants in this range:", most_common_count)
print("Average votes per restaurant:", round(average_votes, 2))

# Save rating distribution to CSV
chart_distribution.rename("Restaurant Count").to_csv(
    output_folder / "rating_distribution.csv"
)

# Create and save the rating distribution chart
plt.figure(figsize=(9, 5))
chart_distribution.plot(kind="bar", edgecolor="black")

plt.title("Restaurant Rating Distribution")
plt.xlabel("Rating Range")
plt.ylabel("Number of Restaurants")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig(
    output_folder / "rating_distribution.png",
    dpi=300
)
plt.close()

# Save summary statistics
summary = pd.DataFrame({
    "Metric": [
        "Total restaurants",
        "Restaurants with rating 0",
        "Most common rating range",
        "Restaurants in most common range",
        "Average votes per restaurant"
    ],
    "Value": [
        len(df),
        unrated_count,
        str(most_common_range),
        most_common_count,
        round(average_votes, 2)
    ]
})

summary.to_csv(
    output_folder / "rating_analysis_summary.csv",
    index=False
)

print("\nFiles saved successfully in:", output_folder)

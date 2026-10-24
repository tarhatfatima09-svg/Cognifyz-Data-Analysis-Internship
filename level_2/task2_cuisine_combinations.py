
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Set file paths
project_folder = Path(__file__).resolve().parent.parent
dataset_path = project_folder / "Dataset .csv"
output_folder = Path(__file__).resolve().parent / "outputs"

output_folder.mkdir(parents=True, exist_ok=True)

# Load dataset
df = pd.read_csv(dataset_path)

# Clean cuisine names
df["Cuisines"] = df["Cuisines"].fillna("Unknown")
df["Cuisines"] = df["Cuisines"].astype(str).str.strip()

# Exclude blank cuisine entries
df = df[df["Cuisines"] != ""]

# Group restaurants by cuisine combination
cuisine_analysis = df.groupby("Cuisines").agg(
    Restaurant_Count=("Cuisines", "size"),
    Average_Rating=("Aggregate rating", lambda x: x[x > 0].mean()),
    Total_Votes=("Votes", "sum")
).reset_index()

# Sort by restaurant count
cuisine_analysis = cuisine_analysis.sort_values(
    by="Restaurant_Count",
    ascending=False
)

# Select top 10 cuisine combinations
top_10 = cuisine_analysis.head(10).copy()

# Round average ratings
top_10["Average_Rating"] = top_10["Average_Rating"].round(2)

# Display results
print("========== CUISINE COMBINATIONS ANALYSIS ==========")
print("Total cuisine combinations:", len(cuisine_analysis))

print("\nTop 10 cuisine combinations:")
print(top_10.to_string(index=False))

# Find combination with highest average rating
rated_combinations = cuisine_analysis.dropna(
    subset=["Average_Rating"]
)

if not rated_combinations.empty:
    highest_rated = rated_combinations.loc[
        rated_combinations["Average_Rating"].idxmax()
    ]

    print("\nHighest average-rated cuisine combination:")
    print("Cuisine:", highest_rated["Cuisines"])
    print("Average rating:", round(highest_rated["Average_Rating"], 2))

# Save complete analysis
cuisine_analysis["Average_Rating"] = (
    cuisine_analysis["Average_Rating"].round(2)
)

cuisine_analysis.to_csv(
    output_folder / "cuisine_combinations_results.csv",
    index=False
)

# Save top 10 results separately
top_10.to_csv(
    output_folder / "top_10_cuisine_combinations.csv",
    index=False
)

# Create chart showing the most common combinations
plt.figure(figsize=(12, 7))

plt.barh(
    top_10["Cuisines"][::-1],
    top_10["Restaurant_Count"][::-1],
    edgecolor="black"
)

plt.title("Top 10 Most Common Cuisine Combinations")
plt.xlabel("Number of Restaurants")
plt.ylabel("Cuisine Combination")
plt.tight_layout()

plt.savefig(
    output_folder / "top_10_cuisine_combinations.png",
    dpi=300
)

plt.close()

# Create chart comparing average ratings
rating_data = top_10.dropna(subset=["Average_Rating"]).sort_values(
    by="Average_Rating"
)

plt.figure(figsize=(12, 7))

plt.barh(
    rating_data["Cuisines"],
    rating_data["Average_Rating"],
    edgecolor="black"
)

plt.title("Average Ratings of Top 10 Cuisine Combinations")
plt.xlabel("Average Rating")
plt.ylabel("Cuisine Combination")
plt.xlim(0, 5)
plt.tight_layout()

plt.savefig(
    output_folder / "cuisine_combination_ratings.png",
    dpi=300
)

plt.close()

print("\nAnalysis completed successfully!")
print("Output folder:", output_folder)
print("Files generated:")
print("- cuisine_combinations_results.csv")
print("- top_10_cuisine_combinations.csv")
print("- top_10_cuisine_combinations.png")
print("- cuisine_combination_ratings.png")

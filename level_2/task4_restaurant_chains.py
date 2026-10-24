
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

# Check required columns
required_columns = [
    "Restaurant Name",
    "Aggregate rating",
    "Votes"
]

for column in required_columns:
    if column not in df.columns:
        raise ValueError(f"Required column not found: {column}")

# Clean restaurant names and numeric columns
df["Restaurant Name"] = (
    df["Restaurant Name"]
    .fillna("")
    .astype(str)
    .str.strip()
)

df["Aggregate rating"] = pd.to_numeric(
    df["Aggregate rating"], errors="coerce"
)

df["Votes"] = pd.to_numeric(
    df["Votes"], errors="coerce"
)

# Exclude records with missing restaurant names
df = df[df["Restaurant Name"] != ""].copy()

# Calculate statistics for each restaurant name
def average_positive_rating(values):
    positive_ratings = values[values > 0]
    return positive_ratings.mean()

chain_analysis = df.groupby("Restaurant Name").agg(
    Outlet_Count=("Restaurant Name", "size"),
    Average_Rating=("Aggregate rating", average_positive_rating),
    Total_Votes=("Votes", "sum")
).reset_index()

# Operational definition: names appearing in 2 or more records
chains = chain_analysis[
    chain_analysis["Outlet_Count"] >= 2
].copy()

# Sort by outlet count
chains = chains.sort_values(
    by=["Outlet_Count", "Average_Rating"],
    ascending=[False, False]
)

# Round average ratings
chains["Average_Rating"] = chains["Average_Rating"].round(2)

# Top 10 chains by number of records
top_10_chains = chains.head(10).copy()

# Print summary
print("========== RESTAURANT CHAINS ANALYSIS ==========")
print("Restaurant records analyzed:", len(df))
print("Unique restaurant names:", df["Restaurant Name"].nunique())
print("Names appearing in 2 or more records:", len(chains))

print("\nTop 10 restaurant names by outlet count:")
print(top_10_chains.to_string(index=False))

# Identify highest-rated chain among names appearing at least twice.
# Report the outlet count alongside the rating for context.
rated_chains = chains.dropna(subset=["Average_Rating"])

if not rated_chains.empty:
    highest_rated_chain = rated_chains.loc[
        rated_chains["Average_Rating"].idxmax()
    ]

    print("\nHighest average-rated chain (2+ records):")
    print("Restaurant:", highest_rated_chain["Restaurant Name"])
    print("Average rating:", highest_rated_chain["Average_Rating"])
    print("Number of records:", highest_rated_chain["Outlet_Count"])

# Save complete chain analysis
chains.to_csv(
    output_folder / "restaurant_chains_results.csv",
    index=False
)

# Save top 10 results
top_10_chains.to_csv(
    output_folder / "top_10_restaurant_chains.csv",
    index=False
)

# Chart 1: Top 10 by outlet count
plt.figure(figsize=(12, 7))

plt.barh(
    top_10_chains["Restaurant Name"][::-1],
    top_10_chains["Outlet_Count"][::-1],
    edgecolor="black"
)

plt.title("Top 10 Restaurant Names by Number of Records")
plt.xlabel("Number of Records")
plt.ylabel("Restaurant Name")
plt.tight_layout()

plt.savefig(
    output_folder / "top_10_restaurant_chains.png",
    dpi=300
)
plt.close()

# Chart 2: Average ratings for the top 10 chains
rating_data = top_10_chains.dropna(
    subset=["Average_Rating"]
).sort_values(by="Average_Rating")

plt.figure(figsize=(12, 7))

plt.barh(
    rating_data["Restaurant Name"],
    rating_data["Average_Rating"],
    edgecolor="black"
)

plt.title("Average Ratings of Top 10 Restaurant Names by Outlet Count")
plt.xlabel("Average Rating")
plt.ylabel("Restaurant Name")
plt.xlim(0, 5)
plt.tight_layout()

plt.savefig(
    output_folder / "restaurant_chain_ratings.png",
    dpi=300
)
plt.close()

print("\nAnalysis completed successfully!")
print("Output folder:", output_folder)
print("Files generated:")
print("- restaurant_chains_results.csv")
print("- top_10_restaurant_chains.csv")
print("- top_10_restaurant_chains.png")
print("- restaurant_chain_ratings.png")


import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# --------------------------------------------------
# 1. Set project paths
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent
DATASET_PATH = BASE_DIR.parent / "Dataset .csv"
OUTPUT_DIR = BASE_DIR / "outputs"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# --------------------------------------------------
# 2. Load dataset
# --------------------------------------------------

df = pd.read_csv(DATASET_PATH)

print("=" * 60)
print("LEVEL 2 - TASK 3: GEOGRAPHIC ANALYSIS")
print("=" * 60)

print("\nTotal restaurant records:", len(df))

# --------------------------------------------------
# 3. Check and clean geographic coordinates
# --------------------------------------------------

# Remove records with missing coordinates or (0, 0).
# The original dataset remains unchanged.
invalid_coordinates = (
    df["Latitude"].isna()
    | df["Longitude"].isna()
    | ((df["Latitude"] == 0) & (df["Longitude"] == 0))
)

geo_df = df.loc[~invalid_coordinates].copy()

excluded_count = int(invalid_coordinates.sum())

print("Records excluded due to missing/placeholder coordinates:",
      excluded_count)
print("Records used for geographic analysis:", len(geo_df))

if geo_df.empty:
    raise ValueError("No valid geographic coordinates remain.")

# Save the cleaned geographic dataset
geo_columns = [
    "Restaurant ID",
    "Restaurant Name",
    "City",
    "Locality",
    "Longitude",
    "Latitude",
    "Aggregate rating",
    "Votes"
]

geo_df[geo_columns].to_csv(
    OUTPUT_DIR / "geographic_restaurant_data.csv",
    index=False
)

# --------------------------------------------------
# 4. Display coordinate ranges
# --------------------------------------------------

print("\nLatitude range:")
print(geo_df["Latitude"].min(), "to", geo_df["Latitude"].max())

print("\nLongitude range:")
print(geo_df["Longitude"].min(), "to", geo_df["Longitude"].max())

# --------------------------------------------------
# 5. Approximate geographic clusters
# --------------------------------------------------

# Round coordinates to 2 decimal places to identify
# approximate areas, not exact geographic clusters.
geo_df["Latitude_Area"] = geo_df["Latitude"].round(2)
geo_df["Longitude_Area"] = geo_df["Longitude"].round(2)

clusters = (
    geo_df.groupby(["Latitude_Area", "Longitude_Area"])
    .size()
    .reset_index(name="Restaurant_Count")
    .sort_values("Restaurant_Count", ascending=False)
)

clusters.to_csv(
    OUTPUT_DIR / "geographic_cluster_results.csv",
    index=False
)

top_clusters = clusters.head(10).copy()

print("\nTop 10 approximate geographic areas:")
print(top_clusters.to_string(index=False))

# --------------------------------------------------
# 6. Chart: Geographic distribution
# --------------------------------------------------

plt.figure(figsize=(10, 7))

plt.scatter(
    geo_df["Longitude"],
    geo_df["Latitude"],
    alpha=0.45,
    s=12
)

plt.title("Geographic Distribution of Restaurants")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.grid(True, alpha=0.3)
plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "restaurant_geographic_distribution.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

# --------------------------------------------------
# 7. Chart: Top 10 approximate geographic areas
# --------------------------------------------------

top_clusters["Area"] = (
    top_clusters["Latitude_Area"].map(lambda x: f"{x:.2f}")
    + ", "
    + top_clusters["Longitude_Area"].map(lambda x: f"{x:.2f}")
)

plt.figure(figsize=(11, 6))

plt.bar(
    top_clusters["Area"],
    top_clusters["Restaurant_Count"]
)

plt.title("Top 10 Approximate Geographic Areas by Restaurant Count")
plt.xlabel("Latitude, Longitude")
plt.ylabel("Number of Restaurants")
plt.xticks(rotation=45, ha="right")
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "top_geographic_clusters.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

# --------------------------------------------------
# 8. Save a summary report as CSV
# --------------------------------------------------

summary = pd.DataFrame({
    "Metric": [
        "Total restaurant records",
        "Records excluded due to invalid coordinates",
        "Records used for geographic analysis",
        "Unique approximate geographic areas",
        "Minimum latitude",
        "Maximum latitude",
        "Minimum longitude",
        "Maximum longitude"
    ],
    "Value": [
        len(df),
        excluded_count,
        len(geo_df),
        len(clusters),
        geo_df["Latitude"].min(),
        geo_df["Latitude"].max(),
        geo_df["Longitude"].min(),
        geo_df["Longitude"].max()
    ]
})

summary.to_csv(
    OUTPUT_DIR / "geographic_analysis_summary.csv",
    index=False
)

# --------------------------------------------------
# 9. Completion message
# --------------------------------------------------

print("\nOutput files saved in:")
print(OUTPUT_DIR)

print("\nGenerated files:")
print("- geographic_restaurant_data.csv")
print("- geographic_cluster_results.csv")
print("- geographic_analysis_summary.csv")
print("- restaurant_geographic_distribution.png")
print("- top_geographic_clusters.png")

print("\nGeographic analysis completed successfully!")

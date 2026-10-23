
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Get the project folder paths
BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT_DIR = Path(__file__).resolve().parent / "outputs"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Load the dataset
file_path = BASE_DIR / "Dataset .csv"
df = pd.read_csv(file_path)

# Display basic information
print("Total restaurants:", len(df))
print("Missing cuisine values:", df["Cuisines"].isna().sum())

# Select the cuisine column and remove missing values
cuisine_data = df[["Restaurant ID", "Cuisines"]].dropna().copy()

# Split restaurants with multiple cuisines
cuisine_data["Cuisines"] = cuisine_data["Cuisines"].str.split(",")
cuisine_data = cuisine_data.explode("Cuisines")

# Remove extra spaces
cuisine_data["Cuisines"] = cuisine_data["Cuisines"].str.strip()

# Avoid counting the same restaurant twice for one cuisine
cuisine_data = cuisine_data.drop_duplicates(
    subset=["Restaurant ID", "Cuisines"]
)

# Count restaurants for each cuisine
cuisine_counts = cuisine_data["Cuisines"].value_counts()

# Get the top 3 cuisines
top_cuisines = cuisine_counts.head(3)

# Calculate percentages
results = pd.DataFrame({
    "Cuisine": top_cuisines.index,
    "Restaurant Count": top_cuisines.values
})

results["Percentage (%)"] = (
    results["Restaurant Count"] / len(df) * 100
).round(2)

# Display the results
print("\nTop 3 Most Common Cuisines")
print(results.to_string(index=False))

# Save the results
results.to_csv(
    OUTPUT_DIR / "top_cuisines_results.csv",
    index=False
)

# Create a bar chart
plt.figure(figsize=(9, 5))

bars = plt.bar(
    results["Cuisine"],
    results["Restaurant Count"]
)

plt.title("Top 3 Most Common Cuisines")
plt.xlabel("Cuisine")
plt.ylabel("Number of Restaurants")
plt.bar_label(bars, padding=3)
plt.tight_layout()

# Save the chart
plt.savefig(
    OUTPUT_DIR / "top_cuisines_chart.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("\nResults and chart saved in the outputs folder!")

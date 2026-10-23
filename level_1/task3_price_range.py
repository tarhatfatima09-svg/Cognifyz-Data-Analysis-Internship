
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Set project paths
BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT_DIR = Path(__file__).resolve().parent / "outputs"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Load the dataset
df = pd.read_csv(BASE_DIR / "Dataset .csv")

# Check dataset
print("Total restaurant records:", len(df))
print("Missing price range values:", df["Price range"].isna().sum())

# Remove rows with missing price range
price_data = df["Price range"].dropna()

# Count restaurants in each price range
price_counts = price_data.value_counts().sort_index()

# Calculate percentages
price_percentages = (
    price_counts / len(df) * 100
).round(2)

# Create results table
results = pd.DataFrame({
    "Price Range": price_counts.index,
    "Restaurant Count": price_counts.values,
    "Percentage (%)": price_percentages.values
})

# Display results
print("\nPRICE RANGE DISTRIBUTION")
print("-" * 45)
print(results.to_string(index=False))

# Save results to CSV
results.to_csv(
    OUTPUT_DIR / "price_range_results.csv",
    index=False
)

# Create bar chart
plt.figure(figsize=(9, 5))

bars = plt.bar(
    results["Price Range"].astype(str),
    results["Restaurant Count"]
)

plt.title("Distribution of Restaurants by Price Range")
plt.xlabel("Price Range Category")
plt.ylabel("Number of Restaurants")
plt.bar_label(bars, padding=3)
plt.tight_layout()

# Save chart
plt.savefig(
    OUTPUT_DIR / "price_range_distribution.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("\nFiles saved successfully:")
print("1. outputs/price_range_results.csv")
print("2. outputs/price_range_distribution.png")

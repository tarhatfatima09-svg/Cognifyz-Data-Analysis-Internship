# Cognifyz Technologies — Data Analysis Internship

## About the Project

This repository contains my work for the Cognifyz Technologies Data Analysis Internship. The project uses Python to analyze restaurant data, identify patterns, calculate statistics, and create visualizations.

## Technologies Used

- Python
- Pandas
- Matplotlib
- Visual Studio Code
- Git and GitHub

## Project Structure

```text
Cognifyz_Data_Analysis/
├── README.md
└── Level_1/
    ├── task1_top_cuisines.py
    ├── task2_city_analysis.py
    ├── task3_price_range.py
    └── task4_online_delivery.py
```

Each task generates CSV analysis results and PNG charts in the `Level_1/outputs/` directory.

## Level 1 — Completed Tasks

### Task 1: Top Cuisines
- Identified the three most common cuisines.
- Calculated restaurant counts and percentages.
- Created a bar chart of the top cuisines.

### Task 2: City Analysis
- Identified the city with the highest restaurant count.
- Calculated average ratings by city.
- Visualized restaurant counts and average ratings.

### Task 3: Price Range Distribution
- Analyzed restaurant counts across four price categories.
- Calculated the percentage in each category.
- Created a price range distribution chart.

### Task 4: Online Delivery Analysis
- Calculated the percentage of restaurants offering online delivery.
- Compared average ratings for restaurants with and without delivery.
- Created charts to visualize delivery availability and average ratings.

## Key Findings

- **Top cuisine:** North Indian, with 3,960 restaurant-cuisine records counted in the analysis.
- **City with the highest restaurant count:** New Delhi, with 5,473 restaurants.
- **Most common price range:** Price Range 1, representing 46.53% of the dataset.
- **Online delivery:** 25.66% of restaurants offer online delivery.
- **Average ratings:** Restaurants offering online delivery have an average rating of 3.25, compared with 2.47 for restaurants without delivery.

Percentages for individual cuisines may overlap because a restaurant can serve multiple cuisines.

## How to Run

1. Install Python.
2. Install the required libraries:

   ```bash
   py -m pip install pandas matplotlib
   ```

3. Place the permitted restaurant dataset in the project root using the filename expected by the scripts: `Dataset .csv`.
4. Open a terminal in the project folder.
5. Run a task, for example:

   ```bash
   py Level_1/task1_top_cuisines.py
   ```

   Replace the script name with any other task to run that analysis.

## Outputs

The analysis scripts generate CSV files containing results and PNG images containing charts. These are saved in `Level_1/outputs/`.

## Future Work

Level 2 analyses will be added after completion.

---

This repository is part of my learning journey in data analysis, data visualization, and Python-based exploratory data analysis.
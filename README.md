# 🍽️ Cognifyz Technologies — Data Analysis Internship

## 📌 Project Overview

This repository contains my work for the **Cognifyz Technologies Data Analysis Internship**. The project focuses on analyzing restaurant data using Python, Pandas, Matplotlib, and exploratory data analysis techniques.

The analysis explores restaurant ratings, cuisines, city-wise distribution, price ranges, online delivery, geographical patterns, and restaurant chains.

## 🎯 Objectives

- Analyze restaurant data to identify meaningful patterns and trends.
- Explore customer ratings, votes, cuisines, and pricing.
- Compare restaurant distribution across cities and geographical locations.
- Examine online delivery availability and restaurant chains.
- Create visualizations and reports to communicate findings.

## 🛠️ Tools and Technologies

- **Python**
- **Pandas** — data cleaning and analysis
- **Matplotlib** — data visualization
- **VS Code** — development environment
- **Git and GitHub** — version control and project hosting
- **CSV** — data storage and analysis outputs

## 📂 Project Structure

```text
Cognifyz_Data_Analysis/
│
├── README.md
├── .gitignore
│
├── level_1/
│   ├── Task 1 - Top Cuisines
│   ├── Task 2 - City Analysis
│   ├── Task 3 - Price Range Distribution
│   ├── Task 4 - Online Delivery Analysis
│   └── outputs/
│       ├── Charts
│       ├── CSV Results
│       └── Task Reports
│
└── level_2/
    ├── task1_restaurant_ratings.py
    ├── task2_cuisine_combinations.py
    ├── task3_geographic_analysis.py
    ├── task4_restaurant_chains.py
    ├── task1_report.txt
    ├── task2_report.txt
    ├── task3_report.txt
    ├── task4_report.txt
    ├── level2 summary.txt
    └── outputs/
        ├── Charts
        └── CSV Results
```

*Note: The folder structure above summarizes the main project components. The actual filenames inside `level_1/` may vary.*

## 📊 Level 1 — Exploratory Data Analysis

### Task 1: Restaurant Cuisines

- Identified the most frequently represented cuisines.
- Analyzed cuisine counts and percentages.
- Created a visualization of the top cuisines.

**Key findings:**
- North Indian: 3,960 records (41.46%)
- Chinese: 2,735 records (28.64%)
- Fast Food: 1,986 records (20.79%)

*Note: Cuisine percentages can overlap because a restaurant may offer multiple cuisines.*

### Task 2: City Analysis

- Analyzed restaurant distribution across cities.
- Compared restaurant counts and average ratings.
- Created city-wise visualizations.

**Key findings:**
- Total cities represented: 141
- New Delhi had the highest restaurant count, with 5,473 records.
- Inner City had the highest reported average rating at 4.90.

### Task 3: Price Range Distribution

- Examined the distribution of restaurants across price ranges.
- Checked for missing values.
- Created a price-range distribution chart.

**Key findings:**

| Price Range | Restaurants | Percentage |
|---|---:|---:|
| 1 | 4,444 | 46.53% |
| 2 | 3,113 | 32.59% |
| 3 | 1,408 | 14.74% |
| 4 | 586 | 6.14% |

No missing values were found in the price-range column.

### Task 4: Online Delivery Analysis

- Compared restaurants offering online delivery with those that do not.
- Analyzed restaurant counts and average ratings.

**Key findings:**
- Online delivery available: 2,451 restaurants (25.66%)
- Online delivery unavailable: 7,100 restaurants (74.34%)
- Average rating with online delivery: 3.25
- Average rating without online delivery: 2.47

These results show an association in the dataset; they do not establish that online delivery causes higher ratings.

## 📈 Level 2 — Advanced Data Analysis

### Task 1: Restaurant Ratings

- Analyzed restaurant rating distributions.
- Identified unrated restaurants and the most common rating range.
- Examined average votes per restaurant.

**Key findings:**
- Total restaurant records analyzed: 9,551
- Restaurants with a rating of 0: 2,148
- Most common rated range: 3.0–3.9, containing 4,590 restaurants
- Average votes per restaurant: 156.91

### Task 2: Cuisine Combinations

- Examined individual cuisines and cuisine combinations.
- Identified the most common combinations.
- Compared average ratings and votes.

**Key findings:**
- Total cuisine combinations: 1,826
- North Indian was the most frequent entry, with 936 records.
- North Indian and Chinese appeared together in 511 records.
- The highest average rating in the analyzed cuisine combinations was 4.9.

### Task 3: Geographic Analysis

- Examined the geographical distribution of restaurants.
- Analyzed latitude and longitude patterns.
- Identified areas with high concentrations of restaurant records.

**Key findings:**
- Original dataset: 9,551 records
- Records retained for geographical analysis: 9,054
- Records with `(0, 0)` coordinates were excluded from this analysis because they were likely placeholder coordinates.

The original dataset was retained; the exclusion applied only to the geographical analysis.

### Task 4: Restaurant Chains

- Identified restaurant names appearing in multiple records.
- Compared the number of records, average ratings, and votes.
- Created visualizations of frequently occurring restaurant names.

**Key findings:**
- Total restaurant records analyzed: 9,551
- Unique restaurant names: 7,446
- Names appearing in two or more records: 734
- Cafe Coffee Day appeared in 83 records.
- Domino's Pizza appeared in 79 records.
- Subway appeared in 63 records.

Repeated names are treated as potential chain indicators; they do not necessarily confirm distinct physical outlets.

## 📉 Visualizations and Outputs

The project includes charts and CSV outputs for:

- Top cuisines
- City-wise restaurant counts and average ratings
- Price-range distribution
- Online delivery comparisons
- Restaurant rating distribution
- Cuisine combinations and ratings
- Geographic restaurant distribution
- Restaurant chains and ratings

Task-specific text reports document the analysis and key findings.

## ▶️ How to Run the Project

1. Clone this repository:

   ```bash
   git clone https://github.com/tarhatfatima09-svg/Cognifyz-Data-Analysis-Internship.git
   ```

2. Open the project folder in VS Code.

3. Install the required Python libraries:

   ```bash
   py -m pip install pandas matplotlib
   ```

4. Place the source dataset in the project root directory, using the filename expected by the scripts.

5. Run a Level 2 task from the project root:

   ```bash
   py level_2/task1_restaurant_ratings.py
   ```

   Replace the script filename with the task you want to run.

**Important:** The dataset is excluded from Git tracking. You must obtain the dataset separately and place it in the expected location before running scripts that depend on it.

## 💡 Key Learnings

- Data cleaning and exploratory data analysis using Pandas.
- Grouping, aggregation, and percentage calculations.
- Analyzing restaurant ratings, cuisines, and votes.
- Comparing categorical data and identifying trends.
- Working with latitude and longitude data.
- Creating informative charts using Matplotlib.
- Organizing analysis scripts, outputs, and reports.
- Managing a data analysis project using Git and GitHub.

## 🏁 Conclusion

This project provided practical experience in analyzing real-world restaurant data, extracting meaningful insights, and communicating results through visualizations and reports.

Completing Level 1 and Level 2 strengthened my understanding of Python-based data analysis and established a foundation for more advanced analytical projects.

## 👩‍💻 Author

**Tarhat Fatima**

- GitHub: [tarhatfatima09-svg](https://github.com/tarhatfatima09-svg)
- Repository: [Cognifyz Data Analysis Internship](https://github.com/tarhatfatima09-svg/Cognifyz-Data-Analysis-Internship)

---

*Completed as part of the Cognifyz Technologies Data Analysis Internship.*

# Cognifyz Technologies – Data Analysis Internship

A Python-based data analysis project completed as part of the Cognifyz Technologies Data Analysis Internship. The project explores restaurant data through data cleaning, statistical analysis, aggregation, and visualization.

## Project Overview

- **Dataset:** Restaurant dataset (`Dataset .csv`)
- **Records:** 9,551 restaurant records
- **Language:** Python
- **Libraries:** Pandas, Matplotlib
- **Levels completed:** Level 1 and Level 2

## Project Structure

```text
Cognifyz_Data_Analysis/
├── level_1/
│   ├── outputs/
│   ├── task scripts
│   └── task reports
├── level_2/
│   ├── outputs/
│   ├── task1_restaurant_ratings.py
│   ├── task2_cuisine_combinations.py
│   ├── task3_geographic_analysis.py
│   ├── task4_restaurant_chains.py
│   ├── task1_report.txt
│   ├── task2_report.txt
│   ├── task3_report.txt
│   ├── task4_report.txt
│   └── level_2_summary_report.txt
├── .gitignore
└── README.md
```

## Level 1 – Data Analysis

### Task 1: Top Cuisines
- Identified the most common cuisine entries.
- North Indian appeared in 3,960 records.
- Chinese appeared in 2,735 records.
- Fast Food appeared in 1,986 records.
- Generated CSV results and a visualization.

*Note: Cuisine counts can overlap because a restaurant may serve multiple cuisines.*

### Task 2: City Analysis
- Analyzed restaurant counts and average ratings by city.
- New Delhi had the highest restaurant count, with 5,473 records.
- Generated city-level summaries and visualizations.

### Task 3: Price Range Analysis
- Analyzed restaurant distribution across price ranges.
- Price range 1 accounted for 46.53% of records.
- Price range 2 accounted for 32.59%.
- No missing values were found in the price range column.

### Task 4: Online Delivery Analysis
- Compared online delivery availability and average ratings.
- 2,451 records indicated online delivery availability.
- Average rating was 3.25 for delivery-enabled records and 2.47 for records without delivery.

*These results show an association in this dataset, not proof that online delivery causes higher ratings.*

## Level 2 – Advanced Analysis

### Task 1: Restaurant Ratings
- Examined rating distributions.
- The most common rating range was 3.0–3.9, with 4,590 records.
- Identified 2,148 records with a rating of 0 as unrated for this analysis.

### Task 2: Cuisine Combinations
- Analyzed 1,826 distinct cuisine combinations.
- North Indian was the most frequent cuisine entry, with 936 records.
- Compared restaurant counts, average ratings, and votes.

### Task 3: Geographic Analysis
- Examined latitude and longitude data.
- Excluded 497 records with missing or placeholder coordinates, including `(0, 0)`.
- Used 9,054 records for geographic analysis.
- Generated geographic distribution and approximate-area visualizations.

### Task 4: Restaurant Chains
- Identified repeated restaurant names and compared their records.
- Found 7,446 unique restaurant names.
- Identified 734 names appearing in two or more records.
- Cafe Coffee Day had the highest record count, with 83 records.

*Repeated names are treated as potential chain indicators; distinct physical outlets are not independently verified.*

## Technologies Used

- **Python:** Analysis and processing
- **Pandas:** Data manipulation and aggregation
- **Matplotlib:** Charts and visualizations
- **CSV:** Structured results and summaries

## Outputs

The `outputs` folders contain generated analysis results, CSV summaries, and PNG charts. Individual task reports and the Level 2 summary report document the objectives, methodology, findings, and conclusions.

## Running the Level 2 Scripts

Run these commands from the project root in the VS Code terminal:

```powershell
py level_2/task1_restaurant_ratings.py
py level_2/task2_cuisine_combinations.py
py level_2/task3_geographic_analysis.py
py level_2/task4_restaurant_chains.py
```

Make sure Python and the required libraries are installed. Keep the dataset in the project root for the scripts to locate it.

## Data and Repository Notes

The original dataset is excluded from version control through `.gitignore`. Place `Dataset .csv` in the project root locally before running the scripts.

## Conclusion

This project demonstrates practical skills in data analysis, data cleaning, aggregation, interpretation, and visualization using Python. It includes task-specific scripts, generated outputs, and reports documenting the analysis.

**Internship:** Cognifyz Technologies – Data Analysis Internship

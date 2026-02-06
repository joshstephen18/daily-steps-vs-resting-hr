![scatterplot](https://github.com/joshstephen18/daily-steps-vs-resting-hr/blob/main/plots/steps_vs_resting_hr.png)

# 🏃‍♂️ Daily Steps vs Resting Heart Rate Analysis

Project Description:
This project analyzes the relationship between average daily steps and resting heart rate for 14 individuals in a Fitbit dataset on Kaggle using Python.
It visualizes the correlation between the 2 variables with a scatterplot.

## 🛠️ Methods 
Data Processing: Loaded CSV files and converted timestamps to datetime objects.

Proxy Calculation: Extracted the minimum daily heart rate for subjects as a proxy for resting HR.

Aggregation: Values were averaged per user and merged with daily step counts via unique User IDs.

Statistics: Calculated a Pearson correlation coefficient ($r$) to quantify the relationship.

## 📉 Results 
The scatterplot shows a weak negative correlation (r = -0.23). 

The Trend: In general, more daily steps correlates with a slightly lower resting heart rate.

The Reality: High variability and outliers (like the 40 bpm data point) suggest that individual factors like age or baseline fitness play a massive role.


## ⚠️ Project Limitations
1. Small sample size - The analysis is only based on 14 individuals. While the analysis provides a snapshot, it is not a statistically significant representation of the general population. A larger dataset would help.

2. Lack of demographic context - Resting heart rate can be heavily influenced by variables not accounted for in this analysis such as age, medical conditions, current medications (e.g., beta-blockers), caffeine intake, sleep, etc.


## 💻 Libraries Used

  1. Pandas for data manipulation and analysis

  2. Matplotlib for creating the scatterplot and visualizing data


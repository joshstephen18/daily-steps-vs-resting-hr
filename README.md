![scatterplot](https://github.com/joshstephen18/daily-steps-vs-resting-hr/blob/main/plots/steps_vs_resting_hr.png)

Daily Steps vs Resting Heart Rate Analysis

Project Description:
This project analyzes the relationship between average daily steps and resting heart rate for 14 individuals in a Fitbit dataset on Kaggle using Python.
It visualizes the correlation between the 2 variables with a scatterplot.

Methods: The program first loads and reads uploaded CSV files. It then converts raw timestamps to datetime objects and extracts the minimum daily heart rate as a proxy for resting heart rate. These values are averaged per user and merged with average daily step counts via unique User IDs. A Pearson correlation coefficient is calculated, and the trend between the two variables can be visualized with a scatter plot. 


Results:
The scatterplot shows a weak negative correlation between average daily steps and resting heart rate, and it aligns with the resulting Pearson correlation coefficient of -0.23. 
In general, people who take more steps per day tend to have slighly lower resting heart rates.
However, there is a considerable amount of variability as well as outliers, suggesting that factors such as age or fitness level may influence resting heart rate.

Project Limitations:
1. Small sample size - The analysis is only based on 14 individuals. While the analysis provides a snapshot, it is not a statistically significant representation of the general population. A larger dataset would help.

2. Lack of demographic context - Resting heart rate can be heavily influenced by variables not accounted for in this analysis such as age, medical conditions, current medications (e.g., beta-blockers), caffeine intake, sleep, etc.


Libraries Used:

  1. Pandas for data manipulation and analysis

  2. Matplotlib for creating the scatterplot and visualizing data


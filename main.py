#step 1: import the libraries needed
import pandas as pd
import matplotlib.pyplot as plt

#step 2: load the csv files
hr_data = pd.read_csv ("data/heartrate_seconds_merged.csv")
activity_data = pd.read_csv ("data/dailyActivity_merged.csv")

#step 3: convert date columns to datetime
    #python treats dates as strings until we do the below
activity_data["ActivityDate"] = pd.to_datetime(activity_data["ActivityDate"])
hr_data ["Time"] = pd.to_datetime(hr_data["Time"])

#step 4: create a date only column
#we want to create a new column in each df titled "date" that doesn't include timestamps
activity_data["Date"] = activity_data["ActivityDate"].dt.date #.dt.date takes a full datetime and drops the time
hr_data["Date"] = hr_data["Time"].dt.date

#step 5: calculate daily resting hr per user (lowest hr per day for multiple days) then find average resting hr per user
daily_resting_hr = hr_data.groupby(["Id", "Date"])["Value"].min().reset_index()#.reset_index() meaning: By default, after grouping by "Date," pandas makes the date the "label" for the row. This function moves the date back into its own regular column
#in the above line, we are grouping by Id and Date, and then looking at HR

#find average resting hr per user
avg_resting_hr = daily_resting_hr.groupby("Id")["Value"].mean().reset_index()

#rename the only 2 columns we have in the df to something readable
avg_resting_hr.columns = ["Id", "AvgRestingHR"]

#step 6: calculate average daily steps per user. Here, we are grouping by Id only, and then looking at avg of the total steps
avg_steps = activity_data.groupby("Id")["TotalSteps"].mean().reset_index()

#change the column headers
avg_steps.columns = ["Id", "AvgDailySteps"]


#step 7: merge per-user steps and resting HR into a single df
merged_data = pd.merge(avg_steps, avg_resting_hr, on = "Id")

#drop missing values
merged_data.dropna(inplace=True)     #could also do merged_data = merged_data.dropna()

#step 8: calculate correlation between average resting hr and avg daily steps
correlation = merged_data["AvgDailySteps"].corr(merged_data["AvgRestingHR"])


#Summarize stats
print ("=====Results=====")
print ("Users Analyzed:", len(merged_data)) #returns the number of rows aka how many users I have data for
print("Average Daily Steps:", int(merged_data["AvgDailySteps"].mean()))
print("Average resting HR:", int(merged_data["AvgRestingHR"].mean()))
print ("The correlation between average daily steps and average resting heart rate is:", round(correlation, 2)) #round(value, decimal places)
print("=================")

#create a scatterplot to illustrate the relationship between average daily steps and average resting hr
#plt.scatter(x, y)
plt.scatter(
    merged_data["AvgDailySteps"],
    merged_data["AvgRestingHR"]
)

plt.title("Average Daily Steps vs Resting Heart Rate (Per User)")
plt.xlabel("Average Daily Steps")
plt.ylabel("Average Resting HR (bpm)")
plt.savefig("plots/steps_vs_resting_hr.png") #this line saves the scatterplot automatically to plots directory I created
plt.show()



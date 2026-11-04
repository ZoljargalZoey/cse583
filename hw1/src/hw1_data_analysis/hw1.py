#1
import pandas as pd
import matplotlib.pyplot as plt #added for task #6

df = pd.read_csv("bicycle_data.csv")
print(df.head())

#2
# Comment:
# The dataframe has 4 columns:
# Date: It should be a datetime, but pandas read it as text (str). I'll change it to datetime.
# The other three columns: These are floats.

print(df.dtypes)
df["Date"] = pd.to_datetime(df["Date"], format="%m/%d/%Y %I:%M:%S %p")
print(df.dtypes)

#3
df["Total"] = df["Fremont Bridge Sidewalks, south of N 34th St Cyclist East Sidewalk"] + df["Fremont Bridge Sidewalks, south of N 34th St Cyclist West Sidewalk"]
df["Hour"] = df["Date"].dt.hour
df["Year"] = df["Date"].dt.year
print(df.head())

#4
df_2016 = df[df["Year"] == 2016]
print(df_2016.head())

#5
print(df_2016.isna().sum())
print(df_2016[df_2016["Total"].isna()])
df_2016 = df_2016.dropna()
#Comment: There was one point with missing data and it's removed.

#6
counts_by_hour = df_2016.groupby("Hour")["Total"].mean()
print(counts_by_hour)
counts_by_hour.plot(kind="bar")
plt.title("Average Bicycle Count by Hour of the Day, Fremont Bridge, 2016")
plt.xlabel("Hour of the day (0 = midnight)")
plt.ylabel("Average number of bicycles (East + West)")
plt.tight_layout()
plt.savefig("counts_by_hour.png")

#7
busiest_hour = counts_by_hour.idxmax()
busiest_count = counts_by_hour.max()
print("Busiest hour:", busiest_hour)
#Comment: The busiest hour is 17.

 

import pandas as pd


#Path to my csv file containing all earthquake data
csv_path= "/home/mau/Documents/earthquake_project/Eartquakes-1990-2023.csv"


#Loads only the necessary columns
columns_needed=["date", "place", "magnitudo", "longitude", "latitude"]
df= pd.read_csv(csv_path, usecols=columns_needed)

#Renaming magnitudo to magnitude
df= df.rename(columns={"magnitudo": "magnitude"})

#Converting date to the datetime format for filtering
df["date"]= pd.to_datetime(df["date"], format="mixed", errors="coerce")

#Filtering for earthquakes in 2020 with magnitude
#7 or more
df_filtered= df[(df["date"].dt.year== 2020) & (df["magnitude"]>= 7)]

#Check if all years are 2020
print("Years in dataset:", df_filtered["date"].dt.year.unique())

#Check if all magnitudes are 7+
print("Minimum magnitude:", df_filtered["magnitude"].min())

#Check for missing values
print("Missing values:\n", df_filtered.isnull().sum())

#Saving the data to a csv file for future use
df_filtered.to_csv("filtered_earthquakes_2020.csv", index=False)
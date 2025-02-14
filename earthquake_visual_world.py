import folium as fol
import pandas as pd

csv_info=pd.read_csv("/home/mau/Documents/earthquake_project/filtered_earthquakes_2020.csv")


#Creates the world map
world_map=fol.Map(location=[20,0],zoom_start=2)

#Loops through the csv file, putting the data in the map
for index, row in csv_info.iterrows():
    fol.Marker(
        location=[row["latitude"], row["longitude"]],
        popup=row["magnitude"],
        tooltip=row["place"]
    ).add_to(world_map)
    

#Save the map to an html file to visualize.
world_map.save("World Map with Earthquakes for year 2020.html")
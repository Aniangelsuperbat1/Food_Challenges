import folium
from folium.plugins import MarkerCluster
import pandas as pd
import pdb

map = folium.Map(location=[38.954069, -95.254512], tiles="OpenStreetMap",
                 zoom_start=3, control_scale=True,)

# cluster = MarkerCluster().add_to(map)

# folium.Marker(location=[48.86762, 2.3624], popup="text").add_to(cluster)
# folium.Marker(location=[48.86762, 2.3625], popup="text1").add_to(cluster)
# folium.Marker(location=[48.86762, 2.3626], popup="text2 + <br> + text5 + <br> + text6").add_to(cluster)

# folium.Marker(location=[48.86762, 2.3624], popup="text").add_to(map)
df = pd.read_csv('restaurants_geodata.csv')
# print(df)

count = 0

cluster = MarkerCluster().add_to(map)

for point, row in df.iterrows():
    Latitude = df.at[point, "latitude"]
    Longitude = df.at[point, "longitude"]

    popup = str(df.at[point, "Location name"]) + "<br>" + \
        str(df.at[point, "Challenge name"]) + "<br>" + \
        str(df.at[point, "Restaurant address"])

    popup = popup.replace("`", "'")

    folium.Marker(location=[Latitude, Longitude], popup=popup).add_to(cluster)

map.save("index.html")

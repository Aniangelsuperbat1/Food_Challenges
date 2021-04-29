import pandas as pd
import requests
import json
import config

df = pd.read_csv("food_challenge_location.csv")
# print(df)

for i, row in df.iterrows():
    address = str(df.at[i,"Restaurant address"])
    
    parameters = {
        "key" : api_key,
        "location" : address

    }
    geodata = requests.get("http://www.mapquestapi.com/geocoding/v1/address", params = parameters)

    data = json.loads(geodata.text)["results"]

    latitude = data[0]["locations"][0]["latLng"]["lat"]
    longitude = data[0]["locations"][0]["latLng"]["lng"]
    
    df.at[i,"latitude"] = latitude
    df.at[i,"longitude"] = longitude
    
df.to_csv("restaurants_geodata.csv")





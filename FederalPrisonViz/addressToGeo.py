from geopy.geocoders import Nominatim      
import pandas as pd

geolocator = Nominatim(user_agent="myGeocoder")
# prison_data = pd.read_csv("test2.csv")
prison_data = pd.read_csv('UpdatedPrisonData.csv')

cities = prison_data['City'].tolist()
state = prison_data['State'].tolist()

lats = []
lons = []

for c, s in zip(cities, state):
    location = geolocator.geocode(c + ", " + s + ", " + "United States")
    if hasattr(location, "latitude"):
        # print(c + ", " + s + ", " + str(location.latitude) + ", " + str(location.longitude))
        lats.append(location.latitude)
        lons.append(location.longitude)

    else:
        print(c + ", " + s + ", " + str(39.997349) + ", " + str(-74.613007))
        # lats.append(39.997349)
        # lons.append(-74.613007)

prison_data['Latitude'] = lats
prison_data['Longitude'] = lons
# print (prison_data)
# prison_data.to_csv('PrisonDataWithGeo.csv', index=False)


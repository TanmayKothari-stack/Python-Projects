"""import geocoder

location = geocoder.ip('me')

print("Latitude: ", location.lat)
print("Longitude: ", location.lng)"""

"""import requests

response = requests.get("https://ipinfo.io/json")

data = response.json()

latitude, longitude = map(float,data["loc"].split(","))

print("Latitude: ", latitude)
print("Longitude: ", longitude)"""

from geopy.geocoders import Nominatim
import geocoder

location = geocoder.osm("me")

print("Latitude: ", location.lat)
print("Longitude: ", location.lng)

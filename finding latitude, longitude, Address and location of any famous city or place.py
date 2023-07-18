import pandas as pd
from geopandas.tools import geocode
from geopy.geocoders import Nominatim
import folium
import webbrowser

inp = input("Enter the place or city: ")   # mahapura
                                           # taj mahal
information = geocode(inp, provider="nominatim", user_agent="xyz", timeout=5)
lat = information.geometry.loc[0].y
lon = information.geometry.loc[0].x
geolocator = Nominatim(user_agent="my_app")

# Reverse geocode the coordinates to obtain the address
location = geolocator.reverse(f"{lat}, {lon}")

# printing latitude and longitude
print("Its latitude is  :", lat)
print("Its longitude is :", lon)
print("")

# printing the address of the latitude and longitude
print("Its Address is:", location.address)

# Create a new map centered on the location
map = folium.Map(location=[lat, lon], zoom_start=13)

# Add a marker for the location with a popup
popup_text = location.address
marker = folium.Marker(location=[lat, lon], popup=popup_text)
marker.add_to(map)

# Save the map as an HTML file
map.save("map.html")

# Open the map in the default web browser

webbrowser.open("map.html")

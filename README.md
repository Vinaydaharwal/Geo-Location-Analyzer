# City Geolocation and Mapping

## Overview
This Python script utilizes geocoding and mapping libraries to find the latitude, longitude, and address of a given place or city. It then displays a map centered on the location with a marker indicating the place.

## Requirements
- Python 3.x
- Pandas
- Geopandas
- Geopy
- Folium

## Installation
1. Make sure you have Python 3.x installed on your system. If not, download it from the official Python website: [python.org](https://www.python.org/).

2. Install the required Python libraries using pip:

```bash
pip install pandas geopandas geopy folium
```

## How to Use
1. Clone this repository to your local machine or download the script directly.

2. Open your terminal or command prompt and navigate to the directory containing the script.

3. Run the script:
```bash
python find_location.py

```
4. When prompted, enter the name of the place or city for which you want to find the geolocation and mapping.

5. The script will display the latitude, longitude, and address of the location in the terminal.

6. A new tab will open in your default web browser showing the map centered on the location with a marker.

## Example 
```bash
python geolocation_mapping.py
```
```bash
Enter the place or city: mahapura 
Its latitude is  : 26.8457738
Its longitude is : 75.66841

Its Address is: Mahapura, Sanganer Tehsil, Jaipur District, Rajasthan, 302013, India
```
```bash
Enter the place or city: taj mahal
Its latitude is  : 27.1750075
Its longitude is : 78.04210126365584

Its Address is: Taj Mahal, Taj East Gate Road, Taj Ganj, Agra, Agra District, Uttar Pradesh, 282006, India

```
## Acknowledgments
The script uses the Nominatim geocoding service from OpenStreetMap through the Geopy library.
The mapping is achieved using Folium, a Python wrapper for Leaflet.js.vbnet

## About this file
This is the markdown file created using [readme.so](https://readme.so/) and [ChatGPT](https://chat.openai.com/)

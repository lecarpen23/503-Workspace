import streamlit as st
from OSMPythonTools.nominatim import Nominatim

option = st.selectbox('Which city would you like to focus on? ', ('Washington DC', 'New York City'))
st.write(option)
city = option
if city == 'Washington DC':
    city = 'Washington, District of Columbia, United States'
elif city == 'New York City':
    city = 'New York, United States'

nominatim = Nominatim()
if city == 'Washington, District of Columbia, United States':
    area_id = nominatim.query(city).areaId()
elif city == 'New York, United States':
    area_id = nominatim.query(city).areaId()



option2 = st.selectbox('What would you like to find?', ('University', 'Cafe', 'Bar'))
st.write(option2)
amenity = option2
amenity = amenity.lower()

st.write('User input (city): ' + city)
st.write('User input (amenity): ' + amenity)

#create a map with foliumn with the selected options
import folium
from OSMPythonTools.api import Api
from OSMPythonTools.nominatim import Nominatim
from OSMPythonTools.overpass import overpassQueryBuilder, Overpass
api = Api()
nominatim = Nominatim()
overpass = Overpass()

location = nominatim.query(city).toJSON()[0]
lat, lon = location['lat'], location['lon']
st.write('lat: ' + lat)
st.write('lon: ' + lon)

query = overpassQueryBuilder(area=area_id, elementType='node', selector=f'amenity={amenity}')
results = overpass.query(query)
result = results.elements()

import random
max_results = 150
if len(result) > max_results:
    result = random.sample(result, max_results)
else:
    result = result

st.write('Number of results: ' + str(len(result)))

map = folium.Map(location=[lat, lon], zoom_start=13)

for element in result:
    if element.type() == 'node':
        popup = element.tag('name') if element.tag('name') else element.tag('amenity')
        folium.Marker([element.lat(), element.lon()], popup=popup).add_to(map)

from streamlit_folium import folium_static
folium_static(map)
import streamlit as st

option = st.selectbox('Which city would you like to focus on? ', ('Washington DC', 'New York City'))
st.write(option)
city = option
if city == 'Washington DC':
    city = 'Washington, District of Columbia, United States'
elif city == 'New York City':
    city = 'New York, United States'



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

query = overpassQueryBuilder(area=city, elementType='node', selector=f'amenity={amenity}', out='body')
result = overpass.query(query, timeout=1000)

#create a map from the query result with folium
map = folium.Map(location=[result.elements()[0].lat(), result.elements()[0].lon()], zoom_start=15)
for element in result.elements():
    folium.Marker([element.lat(), element.lon()], popup=element.tags()).add_to(map)
map.save('map.html')
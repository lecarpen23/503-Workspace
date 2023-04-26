import streamlit as st

option = st.selectbox('Which city would you like to focus on? ', ('Washington DC', 'New York City'))
st.write(option)
city = option

option2 = st.selectbox('What would you like to find?', ('University', 'Cafe', 'Bar'))
st.write(option2)
amenity = option2

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
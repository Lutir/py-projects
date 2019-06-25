import pandas
import folium
from folium.plugins import MarkerCluster


data = pandas.read_csv('health.csv')

name = list(data['Facility Name'])
lat = list()
lon = list()

for x in data['Location']:
    x = x[x.find('('):][1:-1].replace(' ', '').split(',')
    lat.append(x[0])
    lon.append(x[1])

map = folium.Map(location = [37.773972, -122.431297], zoom_start=13)

fg_h = folium.FeatureGroup(name = "Medical Facilities")
marker_cluster = MarkerCluster().add_to(map)

for lt, ln, name in zip(lat, lon, name):
    #fg_h.add_child(folium.Marker(location = [lt,ln], popup=name, fillColor="orange", fill_opacity=0.8))
    (folium.Marker(location = [lt,ln], popup=name, fillColor="orange", fill_opacity=0.8)).add_to(marker_cluster)

#map.add_child(fg_h)

map.add_child(folium.LayerControl())

map.save('index.html')

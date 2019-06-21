'''
Project 2: Make a Web Map and plot data from Datasets!
WHat is it?
The following is a representation of Volcanoes in USA and Countries based on their population on a world map.

Libraries Used:
    Folium & leaflet.js
    Pandas
    and lots of awesomeness!

'''

#importing Libraries
import folium
import pandas

#defining a function which takes volcano elevation as input and returns a color
def color_prod(elev):
    if elev < 1000:
        return "green"
    elif (elev >= 1000) and (elev <3000):
        return "orange"
    else:
        return "red"

#reading data of Volcanoes from a txt file and getting their requires params
data = pandas.read_csv("http://pythonhow.com/data/Volcanoes_USA.txt")
lat = list(data['LAT'])
lon = list(data['LON'])
name = list(data['NAME'])
elev = list(data['ELEV'])

#folium.Map = Used to create a map object. location = start point of the map & tiles = different varients of maps!
map = folium.Map(location = [38.58, -99.09], tiles = "Stamen Terrain")

#A FeatureGroup is more like a layer which we add upon the base map
fg_volcano = folium.FeatureGroup(name = "Volcanoes!")

for lt, ln, nm, el in zip(lat, lon, name, elev):
    # add_child() - this adds "things" to the feature group. We are adding markers using folium.CircleMarker (you can also use folium.Marker) and are providing the neccessary params
    fg_volcano.add_child(folium.CircleMarker(location = [lt, ln], popup = nm , fill_color = color_prod(el), color = "grey", fill_opacity = 0.7))

# Create a new feature group for Population!
fg_pop = folium.FeatureGroup(name="Population")

# folium.GeoJson is another amazing function which takes the input of a geojson and helps to plot - "POLYGONS" in our base map.
# the style_function param in GeoJson is used to modify the POLYGON according to its properties (We need to pass a Lambda function to it)
fg_pop.add_child(folium.GeoJson(data = (open("world.json", "r", encoding = "utf-8-sig").read()),
style_function = lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 1000000 else "blue" if x['properties']['POP2005'] < 10000000 else "red"}))

# Adding features to the base Map
map.add_child(fg_volcano)
map.add_child(fg_pop)

# Adding LayerControl to toggle Features in Map!
map.add_child(folium.LayerControl())

# Saving the output in a file called map.html
map.save("map.html")

# Ta-da!

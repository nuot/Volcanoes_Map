import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else: return 'red'

map = folium.Map(location = [38.58, -99.09], zoom_start = 6, titles ='Stamen Terrain')

fg_v = folium.FeatureGroup(name = "Volcanoes")

for lt,ln, el in zip(lat, lon, elev):
    pop = folium.Popup(str(el) + " m", parse_html = True)
    fg_v.add_child(folium.CircleMarker(location = [lt,ln], radius = 7, popup = pop, fill_color=color_producer(el), color = 'grey', fill = True, fill_opacity = 0.7))

fg_p = folium.FeatureGroup(name = "Population")

fg_p.add_child(folium.GeoJson(data = open('world.json','r', encoding = 'utf-8-sig').read(),
style_function = lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))


map.add_child(fg_v)
map.add_child(fg_p)
map.add_child(folium.LayerControl())

map.save("Map1.html")


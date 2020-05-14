import folium
import pandas

data = pandas.read_excel("volcanoes.xlsx")

lon = list(data["LONGITUDE"])
lat = list(data["LATITUDE"])
elev = list(data["ELEVATION"])

def color_producer(elevation):
    if elevation < 1000:
        return 'black'
    elif 1000 <= elevation > 3000:
        return 'red'
    else:
        return 'orange'


map = folium.Map(location=[29.35, 76.72], tiles="OpenStreetMap")
fg = folium.FeatureGroup(name= "My Map")

for lt, ln, el in zip(lat, lon, elev):
    fg.add_child(folium.CircleMarker(location=[lt, ln], radius=6, popup=str(el)+" mtrs.",
    fill_color=color_producer(el), color = 'grey' ,fill_opacity=0.7
     ))


fg.add_child(folium.GeoJson(data=open('world.json','r', encoding='utf-8-sig').read(),
style_function= lambda x: {'fillColor':'red' if x['properties']['POP2005'] < 10000000 else 'orange' if 10000000 <= x['properties']
['POP2005'] < 20000000 else 'red' }))

map.add_child(fg)


map.save("Map1.html")

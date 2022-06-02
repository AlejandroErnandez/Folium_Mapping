import folium
import pandas
import volcano_module as vm

data = pandas.read_csv("Volcanoes.txt")
name = list(data["NAME"])
location = list(data["LOCATION"])
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

view_map = folium.Map(location=[41.79962657386727, -109.77566102320047],
                      zoom_start=5,
                      tiles="Stamen Terrain")

fg_v = folium.FeatureGroup(name="Volcanoes")
for nm, loc, lt, ln, el in zip(name, location, lat, lon, elev):
    fg_v.add_child(folium.CircleMarker(location=[lt, ln],
                                       radius=10,
                                       popup=f"{nm},\n {loc},\n {el} meters",
                                       fill_color=vm.icon_color(el),
                                       color='grey',
                                       fill_opacity=0.9))

fg_p = folium.FeatureGroup(name="Populations")
fg_p.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
                              style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000
                              else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

view_map.add_child(fg_p)
view_map.add_child(fg_v)
view_map.add_child(folium.LayerControl())
view_map.save("map.html")

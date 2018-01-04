import folium
import pandas as pd
import numpy as np
import requests
import json

d = json.loads(requests.get("http://opendata.iprpraha.cz/CUR/DOP/DOP_PID_VSTUPY_B/S_JTSK/DOP_PID_VSTUPY_B.json").text)
coors = pd.DataFrame([[d["features"][x]['geometry']['coordinates'],d["features"][x]['properties']['VSTUPY_POPIS']] for x in range(356)], columns = ['souradnice','popisek'])
coors = coors.iloc[0:20]
lat = list(coors['souradnice'][x][0] for x in range(len(coors)))
lng = list(coors['souradnice'][x][1] for x in range(len(coors)))
description = list(coors['popisek'][x] for x in range(len(coors)))


map = folium.Map(location=[25, 10], zoom_start=3, tiles="Mapbox Bright")

stations = folium.FeatureGroup(name="Station exits")

for lt, ln, desc in zip(lat, lng, description):
    stations.add_child(folium.CircleMarker(location=[lt, ln], radius = 5, popup=str(desc),
    fill_color="yellow", fill=True,  color = 'grey', fill_opacity=0.7))

map.add_child(stations)

map.add_child(folium.LayerControl())

map.save("Map1.html")

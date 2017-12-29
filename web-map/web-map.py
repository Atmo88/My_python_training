import folium
import pandas

data_cities = pandas.read_csv("simplemaps-worldcities-basic.csv")
data_cities = data_cities.ix[data_cities["pop"]>1000000.0]
clat = list(data_cities["lat"])
clng = list(data_cities["lng"])
cpop = list(data_cities["pop"])
cname = list(data_cities["city"])

categories = {"Minor cities" : "green", "Big cities" : "yellow", "Megacities" : "red"}

def category_producer(population):
    if population < 3000000:
        info = {
            "category" : "Minor cities",
            "color" : "green",
            "radius" : 4,
        }
    elif population < 5000000:
        info = {
            "category" : "Big cities",
            "color" : "yellow",
            "radius" : 6,
        }
    else:
        info = {
            "category" : "Megacities",
            "color" : "red",
            "radius" : 8,
        }
    return info

map = folium.Map(location=[25, 10], zoom_start=3, tiles="Mapbox Bright")

fgs = {}
for category in categories:
    fgs[category] = folium.FeatureGroup(name=category)

for lt, ln, pop, name in zip(clat, clng, cpop, cname):
    fgs[category_producer(pop)["category"]].add_child(folium.CircleMarker(location=[lt, ln], radius = category_producer(pop)["radius"], popup=name + " " + str("{:,}".format(int(pop))),
    fill_color=category_producer(pop)["color"], fill=True,  color = 'grey', fill_opacity=0.7))

for fg in fgs:
    map.add_child(fgs[fg])

map.add_child(folium.LayerControl())

map.save("Map1.html")

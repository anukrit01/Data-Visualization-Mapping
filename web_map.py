import folium
import pandas
import io

data = pandas.read_csv('E:/Volcanoes_USA.txt')
lon = list(data['LON'])
lat = list(data['LAT'])
elev= list(data['ELEV'])
def color_producer(elev):
    if(elev<1000):
        return('green')
    elif(1000<=elev<3000):
        return('orange')
    else:
        return('red')

#Using Folium
map = folium.Map(location=[32.58, -99.09], zoom_start= 6, tiles='Mapbox Bright')
fgv = folium.FeatureGroup(name='Volcanoes')

for lt, ln, el in zip(lat, lon, elev):
    fgv.add_child(folium.Marker(location=[lt,ln], popup= str(el)+'m', icon= folium.Icon(color= color_producer(el))))

fgp = folium.FeatureGroup(name= 'Population')

fgp.add_child(folium.GeoJson(data=io.open('world.json','r', encoding='utf-8-sig').read(),
                style_function=lambda x:{'fillColor':'green' if x['properties']['POP2005']<10000000
                else 'orange' if 10000000<= x['properties']['POP2005']<20000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save('Map.html')
import folium
import pandas
import datetime

def mapaLeaflet():
    df=pandas.read_csv("Maps/coordenadas.txt")
    map=folium.Map(location=[df['LAT'].mean(),df['LON'].mean()],zoom_start=6,tiles='Mapbox bright')
    fg=folium.FeatureGroup(name="HACKEO MASIVO")
    for lat,lon,name in zip(df['LAT'],df['LON'],df['NAME']):
        #twitter_tag = folium.Html(name,script=True)
        #name = folium.Popup(twitter_tag)
        #fg.add_child(folium.Marker(location=[lat,lon],popup=(folium.Popup(name)),icon=folium.Icon(color=color(elev),icon_color='green')))
	fg.add_child(folium.Marker(location=[lat,lon],popup=name,icon=folium.Icon(color="blue",icon_color='white')))
    	map.add_child(fg)
	map.add_child(folium.GeoJson(data=open('Maps/world_geojson_from_ogr.json').read(), name="Population", style_function=lambda x: 
{'fillColor':'green' if x['properties']['POP2005'] <= 10000000 else 'orange' if 10000000 < x['properties']['POP2005'] < 20000000 else 'red'}))
	map.add_child(folium.LayerControl())
    	now = datetime.datetime.now()
    	namefile = now.isoformat()
    	map.save(outfile='Maps/MapsHTML/'+ namefile + ".html")

import pandas as pd  # pip install pandas
import gmplot # pip install gmplot

url = "http://api.open-notify.org/iss-now.json"
df= pd.read_json(url)

print(df)

lat=df.loc['latitude','iss_position']
lon=df.loc['longitude','iss_position']
gmap1 = gmplot.GoogleMapPlotter(lat,lon, 7 )
gmap1.marker(lat, lon, "red", title="ISS")

gmap1.draw("C:\\Users\\ashwa\\Desktop\\map.html") // change the file location according to your choice

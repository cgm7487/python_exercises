from flask import Flask, g, render_template, request
import gpsreader
from gmplot import gmplot

app = Flask(__name__)

def generateMapHtml(lat, lon, myMap):

    # Place Map
    gmap = gmplot.GoogleMapPlotter(lat,lon,13)
    # Marker
    gmap.marker(lat, lon, 'cornflowerblue')

    # Draw
    gmap.draw(myMap)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/map')
def showMap():
    gpsAll = gpsreader.get_gps_data('/dev/ttyUSB0', 4800)
    if gpsAll != 'NODATA':
        gpsList = gpsAll.split(',')
        lat = float(gpsList[2])/100 if gpsList[3] == 'N' else -1 * float(gpsList[2])/100
        lon = float(gpsList[4])/100 if gpsList[5] == 'E' else -1 * float(gpsList[4])/100
        myMap = 'templates/map.html'
        generateMapHtml(lat,lon,myMap)
        return render_template(myMap)

    return "No GPS Data"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=17487, debug=True)
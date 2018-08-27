from flask import Flask, g, render_template, request
from gmplot import gmplot
import gpsreader
import math

app = Flask(__name__)

def generateMapHtml(lat, lon, myMap):

    # Place Map
    gmap = gmplot.GoogleMapPlotter(lat,lon,20)

    # Marker
    gmap.marker(lat, lon, 'cornflowerblue')

    # Draw
    gmap.draw('templates/'+myMap)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/map')
def showMap():
    gpsAll = gpsreader.get_gps_data('/dev/ttyUSB0', 4800)

    print(gpsAll)

    if gpsAll != 'NODATA':
        gpsList = gpsAll.split(',')

        if int(gpsList[6]) == 0:
            return "NO GPS Data"

        latTemp = math.modf(float(gpsList[2])/100)
        latNoDir = latTemp[1]+(latTemp[0]*100.0/60.0)
        lat = latNoDir if gpsList[3] == 'N' else -1 * latNoDir

        lonTemp = math.modf(float(gpsList[4])/100)
        lonNoDir = lonTemp[1]+(lonTemp[0]*100.0/60.0)
        lon = lonNoDir if gpsList[5] == 'E' else -1 * lonNoDir

        myMap = 'map.html'
        generateMapHtml(lat,lon,myMap)
        return render_template(myMap)

    return "No GPS Data"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=17487, debug=True)

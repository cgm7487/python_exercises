import serial
import math

def get_gps_raw_data(serialInterface, baudrate):
    with serial.Serial( serialInterface,
                        baudrate,
                        timeout = None) as gpsSer:
        gpsData = gpsSer.readline()

        return gpsData

def get_gps_data(serialInterface, baudrate):

    try:
        with serial.Serial( serialInterface,
                            baudrate,
                            timeout = None) as gpsSer:

            try:
                gpsData = gpsSer.readline().decode('ascii')
            except:
                return "NODATA"

            if gpsData[1:6] != "GPGGA":
                return "NODATA"

            return gpsData
    except:
        return "NODATA"

def get_gps_pos_data(serialInterface, baudrate):

    gpsData = get_gps_data(serialInterface, baudrate)
    if gpsData == 'NODATA':
        return None

    gpsList = gpsData.split(',')

    if int(gpsList[6]) == 0:
        return None

    latTemp = math.modf(float(gpsList[2])/100)
    latNoDir = latTemp[1]+(latTemp[0]*100.0/60.0)
    lat = latNoDir if gpsList[3] == 'N' else -1 * latNoDir

    lonTemp = math.modf(float(gpsList[4])/100)
    lonNoDir = lonTemp[1]+(lonTemp[0]*100.0/60.0)
    lon = lonNoDir if gpsList[5] == 'E' else -1 * lonNoDir

    alt = float(gpsList[9])

    return '{"lat":%f,"lng":%f,"alt":%f}'%(lat,lon,alt)

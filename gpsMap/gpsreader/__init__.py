import serial

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


def get_gps_raw_data(serialInterface, baudrate):
    with serial.Serial( serialInterface,
                        baudrate,
                        timeout = None) as gpsSer:
        gpsData = gpsSer.readline()

        return gpsData

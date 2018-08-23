import serial

def get_gps_data(serialInterface, baudrate):
    with serial.Serial( serialInterface,
                        baudrate,
                        timeout = None) as gpsSer:
        gpsData = gpsSer.readline()

        if gpsData[1:6] != "GPGGA":
            return "NODATA"

        return gpsData

get_gps_data("/dev/ttyS0", 4800)
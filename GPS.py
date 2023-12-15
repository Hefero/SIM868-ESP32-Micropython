def  _isValidRMC(rmc_sentence):
    is_valid = 0;
    rmc_vector = rmc_sentence.split(',')
    if rmc_vector[0] == '$GNRMC':
        is_valid = 1
        
    return is_valid


def _nmeaToDecimalLatitude(nmea_latitude):
    degrees = float(nmea_latitude[:2])
    minutes = float(nmea_latitude[2:])
    decimal_latitude = degrees + minutes / 60.0

    return decimal_latitude


def _nmeaToDecimalLongitude(nmea_longitude):
    degrees = float(nmea_longitude[:3])
    minutes = float(nmea_longitude[3:])
    decimal_longitude = degrees + minutes / 60.0

    return decimal_longitude


class GPS:
    def __init__(self):
        self.Latitude = 0
        self.Longitude = 0
        self.Speed = 0
        self.UTC = 0
        
    def SetRMC(self, rmc_sentence):
        success = 0
        if(_isValidRMC(rmc_sentence)):
            rmc_vector = rmc_sentence.split(',')
            
            self.Latitude = _nmeaToDecimalLatitude(rmc_vector[3])
            if(rmc_vector[4] == 'S'):
                self.Latitude = self.Latitude * -1
                
            self.Longitude = _nmeaToDecimalLongitude(rmc_vector[5])
            if(rmc_vector[6] == 'W'):
                self.Longitude = self.Longitude * -1
                
            self.Speed = float(rmc_vector[7])
            
            success = 1
        return success


    def GetCoordinates(self):
        return self.Latitude, self.Longitude

    def GetSpeed(self):
        return self.Speed
        


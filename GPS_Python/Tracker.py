from machine import UART
from GPS import GPS
import time


class Tracker:
    def __init__(self):
        self.gps = GPS()
        
        self.uart = UART(2)
        self.uart.init(115200, bits=8, parity=None, stop=1)
        
        self.uart.write("AT+CGATT=1")
        time.sleep_ms(500)
        
        
        self.uart.write('AT+CGDCONT=1,"IP","CMNET"')
        time.sleep_ms(500)
        
        
        self.uart.write("AT+CGACT=1,1")
        time.sleep_ms(500)
        
        
        self.uart.write("AT+GPS=1")
        time.sleep_ms(500)
        
        
        self.uart.write("AT+GPSRD=60")
        time.sleep_ms(500)
        
        
    def loop(self):
        while(1):
            
            read_flag = 0
            
            while(self.uart.any()):
                data = self.uart.readline()
                if data is not None:
                    read_string = data.decode()
                if(self.gps.SetRMC(read_string)):
                    read_flag = 1
                    
            if(read_flag == 1):
                
                Latitude, Longitude = self.gps.GetCoordinates()
                
                self.uart.write('AT+HTTPGET=\"https://api.thingspeak.com/update?api_key=FRHNMS2Y95UJ92FU&field3={latitude}&field4={latitude}\r\n"'.format(latitude=Latitude, longitude=Longitude))
                    
                                
        

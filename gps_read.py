# main.py -- put your code here!
from machine import UART
import time

       
def gps_read(uart):
    uart.write("AT+CGNSINF\n")
    timeout = time.time() + 2   # 5 secs from now
    string = ""    
    while True:        
        if time.time() > timeout:
            break
        data = uart.readline()
        if data is not None:            
            string += data.decode()
    print(string)
    gps = string.replace('+CGNSINF: ','').split(',')
    print(gps)
    for x in range(len(gps)):            
        if gps[x] == '':
            gps[x] = '0'
    print(gps[x])
    gps = {
        'Power':int(gps[0]),
        'Fix':int(gps[1]),
        'Time':gps[2],
        'Latitude':float(gps[3]),
        'Longitude':float(gps[4]),
        'Altitude':float(gps[5]),
        'Speed':float(gps[6]),
        'Course':float(gps[7]),
        'Fix Mode':float(gps[8])
        }
    return gps


uart = UART(2)
uart.init(115200, bits=8, parity=None, stop=1)
read = gps_read(uart)
print(read['Latitude'])
print(read['Longitude'])

import network
import time
import sys
from machine import Pin
from machine import UART
import dht
#utilizaremos a versao “robusta” do cliente umqtt em vez da “simple”
from umqtt.robust import MQTTClient

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

try:
    uart.write("AT+CGNSPWR=1\n")
    print("try")
except Exception as e:
    print(e)
try:
    read = gps_read(uart)
    print(read)
except Exception as e:
    print(e)
try:
    read = gps_read(uart)
    print(read)
except Exception as e:
    print(e)

# MQTT Server Parameters
MQTT_CLIENT_ID = "CCcXLC8oOBoYIyQrJCsnERs"
MQTT_BROKER = "mqtt3.thingspeak.com"
MQTT_USER = "CCcXLC8oOBoYIyQrJCsnERs"
MQTT_PASSWORD = "1oF+gsHDXpIHzMyXQqeYaP7u"
MQTT_PUB_TOPIC = "channels/2253753/publish"

#WIFI parameters
WIFI_SSID  ="Offline_Connection_2_4G"
WIFI_PASSWD = "oliver@15oliver@15"

#Create a WLAN network interface object. STA_IF = station aka client, connects to upstream WiFi access points
print("Connecting to WiFi", end="")
nic = network.WLAN(network.STA_IF)
nic.active(True)
nic.connect(WIFI_SSID, WIFI_PASSWD)
while not nic.isconnected():  
    print(".", end="")  
    time.sleep(0.1)
print(" Connected!")

#conexão com broker Thingspeak
print("Connecting to MQTT server... ", end="")
client = MQTTClient (MQTT_CLIENT_ID, MQTT_BROKER, user = MQTT_USER, password = MQTT_PASSWORD, ssl=False)

try:            
    client.connect()
except Exception as e:
    print('could not connect to MQTT server {}{}'.format(type(e).__name__, e))
    sys.exit() 
print("Connected!")

message="field1={latitude}&field2={longitude}&status=MQTTPUBLISH".format(latitude=read['Latitude'],longitude=read['Longitude'])
print("Reporting to MQTT topic {}: {}".format(MQTT_PUB_TOPIC, message))
client.publish(MQTT_PUB_TOPIC, message)



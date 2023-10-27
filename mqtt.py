import network
import time
import sys
from machine import Pin
import dht
#utilizaremos a versao “robusta” do cliente umqtt em vez da “simple”
from umqtt.robust import MQTTClient

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

message="field1={temp}&field2={hum}&status=MQTTPUBLISH".format(temp=33,hum=34)
print("Reporting to MQTT topic {}: {}".format(MQTT_PUB_TOPIC, message))
client.publish(MQTT_PUB_TOPIC, message)

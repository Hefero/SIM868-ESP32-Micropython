# RP2040 SIM868 Micropython Library


- __SIM868L.py__: a pure-MicroPython driver for the SIM868 GPRS module with both HTTP(S) GET and POST support. Works out of the box on the [RP2040-SIM868](https://www.robotics.org.za/#). 

Example usage of HTTP is in the example_SIM868.py script, just set the APN and change the pins if needed, then run the "example_usage" function.

Example usage of GPS is in the gps_example.py script, run the "example_usage" function.

## How to use

- [Tutorial on getting started with the RP2040 and MicroPython](https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico/2) from **Install Thonny** to **Blink the onboard LED** is the most relavant.
- Save/upload the SIM868.py file to the [RP2040-SIM868](https://www.robotics.org.za/#).
- Save/upload one of the example file or create your own script.

## Credit
This is a modified fork from [Pythings](https://github.com/pythings/Drivers) SIM800L HAL Driver. There driver significantly speeded up development of [RP2040-SIM868](https://www.robotics.org.za/#) HAL driver.

## Methodes

``` python
Modem(uart=None, MODEM_PWKEY_PIN=None, MODEM_RST_PIN=None, MODEM_POWER_ON_PIN=None, MODEM_TX_PIN=None, MODEM_RX_PIN=None)
```
### Brief
Initialize a class of Modem.

### Params
- **uart**: Hardware uart number to use
- **MODEM_PWKEY_PIN**: Pin that the power key is attaced too. N/A for the RP2040-SIM868.
- **MODEM_RST_PIN**: Pin that the Reset on the SIM868 is attaced too. N/A for the RP2040-SIM868.
- **MODEM_POWER_ON_PIN**: Pin that the Power on/off on the SIM868 is attaced too. PIN 3 on the RP2040-SIM868.
- **MODEM_TX_PIN**: Pin that the TX on the SIM868 is attaced too. PIN 5 on the RP2040-SIM868.
- **MODEM_TX_PIN**: Pin that the RX on the SIM868 is attaced too. PIN 4 on the RP2040-SIM868.
---
``` python
Modem.initialize()
```
### Brief
Power on the modem and initialize the uart driver.

---
``` python
Modem.connect( apn, user='', pwd='')
```
### Brief
Connect to the GPRS network.
### Note
Set the APN to `internet` with no username or password. Otherwise please contact your service provider to get these settings.
### Params
- **apn**: Set SIM868 APN.
- **user**: SIM868 APN USERNAME.
- **pwd**: SIM868 APN PASSWORD.
 
---
``` python
Modem.disconnect(url, mode='GET', data=None, content_type='application/json')
```
### Brief
Disconnect from the GPRS network.

---
``` python
Modem.http_request(url, mode='GET', data=None, content_type='application/json')
```
### Brief
Send a HTTP request via the GPRS network.
### Note
Only support for GET and POST method at this time.
### Params
- **url**: URL to send the HTTP Request too.
- **mode**: HTTP method to use.
- **data**: Data to be sent on the network via HTTP.
- **content_type**: Set the HTTP contentype header.
### Returns
HTTP Response.

---
``` python
Modem.gps_on()
```
### Brief
Turn on the GPS.

---
``` python
Modem.gps_off()
```
### Brief
Turn off the GPS.

---
``` python
Modem.gps_read()
```
### Brief
Request GPS data from the SIM868.
### Returns
GPS data as a dictonary.

---
``` python
Modem.send_sms(number=None,msg='')
```
### Brief
Send a SMS message. (untested)
## Note
The number must lead with you international code eg. +27xxxxxxxxx
### Params
- **number**: Number to send the SMS too.
- **msg**: SMS message.

---
---
``` python
Modem.get_info()
```
### Brief
Get information about the modem
### Returns
Modem information.

---

## Untested or Undocumented 

``` python
Modem.battery_status()
```

---
``` python
Modem.scan_networks()
```

---
``` python
Modem.get_current_network()
```

---
``` python
Modem.get_signal_strength()
```

---
``` python
Modem.get_ip_addr()
```

---
``` python
Modem.get_ip_addr()
```

---

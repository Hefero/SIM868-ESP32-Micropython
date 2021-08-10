# ---------------------
# SIM800L example usage
# ---------------------

from SIM868 import Modem
from machine import Timer
import json

modem = Modem(MODEM_PWKEY_PIN    = None,
                MODEM_RST_PIN      = None,
                MODEM_POWER_ON_PIN = 3,
                MODEM_TX_PIN       = 5,
                MODEM_RX_PIN       = 4)

def ping_gps(timer):
    global modem
    print(modem.gps_read())

def example_usage():
    global modem
    print('Starting up...')

    # Initialize the modem
    
    modem.initialize()
	print('init')
    modem.gps_on()
    tim = Timer()
    tim.init(freq=1, mode=Timer.PERIODIC, callback=ping_gps)
     
if __name__ == '__main__':
    example_usage();

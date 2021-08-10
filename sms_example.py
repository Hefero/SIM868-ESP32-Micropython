# ---------------------
# SIM800L example usage
# ---------------------

from SIM868 import Modem

modem = Modem(MODEM_PWKEY_PIN    = None,
                MODEM_RST_PIN      = None,
                MODEM_POWER_ON_PIN = 3,
                MODEM_TX_PIN       = 5,
                MODEM_RX_PIN       = 4)

def example_usage():
    global modem
    print('Starting up...')

    # Initialize the modem
    
    modem.initialize()
	modem.send_sms('+27xxxxxxxxx','Hello from RP2040-SIM868')

     
if __name__ == '__main__':
    example_usage();
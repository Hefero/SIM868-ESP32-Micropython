# main.py -- put your code here!
from machine import UART

uart = UART(2)
uart.init(115200, bits=8, parity=None, stop=1)
uart.write("AT\n")
#try:
uart.write("AT+CGNSPWR=1\n")
uart.write("AT+CGNSINF\n")

while True:
    data = uart.read()

    if data is not None:       
        print(data)
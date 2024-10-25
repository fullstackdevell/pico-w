# hw
# all the way to the left, read 100, all the way to the right read 0

import machine
from time import sleep

analogInput = 28
potentiometer = machine.ADC(analogInput)

while True:
    potentiometerVal = potentiometer.read_u16()
    voltage = (3.3 / 65535) * potentiometerVal
    percentage = 100 * (1 - voltage / 3.3)
    print(int(percentage))
    sleep(0.5)
import machine
from time import sleep

analogInput = 28
# analog pin
potentiometer = machine.ADC(analogInput)
# potentiometer object 
# ADC - analog to digital converter

while True:
    potentiometerVal = potentiometer.read_u16()
    voltage = (3.3 / 65535) * potentiometerVal 
    print(voltage)
    sleep(.5)
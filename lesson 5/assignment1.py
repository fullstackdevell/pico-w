import machine
from time import sleep

analogInput = 28
# analog pin where the potentiometer is connected
# it will be used to read the voltage from the potentiometer

potentiometer = machine.ADC(analogInput)
# ADC - analog to digital converter
# potentiometer object
# it allows to read analog values from the potentiometer


while True:
    potentiometerVal = potentiometer.read_u16()
    # read the current value from the potentiometer as a 16-bit unsigned integer (0 to 65535)
    voltage = (3.3 / 65535) * potentiometerVal 
    # convert the raw ADC value to voltage (in volts) based on a 3.3V reference
    print(voltage)
    sleep(.5)
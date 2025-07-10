# build a circuit that has a potentiometer, 3 leds, red, yellow, green, 3 resistors. when potentiometer all the way to the left, 
# value should be 0, when all the way to the right it should be 100, if value between 0 and 79, green, between 80 and 94, yellow, 
# from 95 to 100, red

import machine
from machine import Pin
from time import sleep

ledRed = Pin(15, Pin.OUT)
ledYellow = Pin(14, Pin.OUT)
ledGreen = Pin(13, Pin.OUT)

analogInput = 28
potentiometer = machine.ADC(analogInput)

while True:
    potentiometerVal = potentiometer.read_u16()
    voltage = (3.3 / 65535) * potentiometerVal
    percentage = 100 * (1 - voltage / 3.3)
    if 0 <= percentage <= 79:
        ledGreen.value(1)
        ledYellow.value(0)
        ledRed.value(0)
    if 80 <= percentage <= 94:
        ledYellow.value(1)
        ledRed.value(0)
        ledGreen.value(0)
    if 95 <= percentage <= 100:
        ledRed.value(1)
        ledYellow.value(0)
        ledGreen.value(0)

    sleep(0.5)
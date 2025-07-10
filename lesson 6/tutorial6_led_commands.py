from machine import Pin
import time
led = Pin(15, Pin.OUT)
while True:
    CMD = input('What is Your Command? (On/Off/Toggle)')
    if CMD == 'On':
        led.value(1)
    if CMD == 'Off':
        led.value(0)
    if CMD == 'Toggle':
        led.toggle()
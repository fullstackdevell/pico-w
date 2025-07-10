from machine import Pin
from time import sleep
redLed = Pin(15, Pin.OUT)
while True:
    redLed.value(1)
    sleep(1)
    redLed.value(0)
    sleep(2)
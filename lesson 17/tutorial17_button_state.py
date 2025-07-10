from machine import Pin
from time import sleep

butPin = 14
myButton = Pin(butPin, Pin.IN, Pin.PULL_UP)
while True:
    butState = myButton.value()
    print(butState)
    sleep(.1)
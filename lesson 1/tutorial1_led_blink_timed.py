from machine import Pin
from time import sleep
myLed = Pin('LED', Pin.OUT)
while True:
    myLed.value(1)
    sleep(.1)
    myLed.value(0)
    sleep(2)
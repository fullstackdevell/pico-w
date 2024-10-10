from machine import Pin
from time import sleep
myLed = Pin('LED', Pin.OUT)
while True:
    myLed.toggle()
    sleep(.1)
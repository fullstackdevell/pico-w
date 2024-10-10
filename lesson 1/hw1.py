# how quickly can you make this thing blink before you can't see it anymore

from machine import Pin
from time import sleep
myLed = Pin('LED', Pin.OUT)
while True:
    myLed.toggle()
    sleep(0.01)
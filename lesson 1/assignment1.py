from machine import Pin
myLed = Pin('LED', Pin.OUT)
myLed.value(1)
myLed.value(0)
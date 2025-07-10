from machine import Pin
redLed = Pin(15, Pin.OUT)
redLed.value(1)
redLed.value(0)
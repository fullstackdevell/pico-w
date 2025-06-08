# on off switch with button and led, press button, led on, press button, led off

from machine import Pin
from time import sleep

LEDPin = 15
myLED = Pin(LEDPin, Pin.OUT)
butPin = 14
myButton = Pin(butPin, Pin.IN, Pin.PULL_UP)
butStateNow = 1
butStateOld = 1
LEDState = False
while True:
    butStateNow = myButton.value()
    if butStateNow == 1 and butStateOld == 0:
        LEDState = not LEDState
        myLED.value(LEDState)
    print(LEDState, butStateNow)
    butStateOld = butStateNow
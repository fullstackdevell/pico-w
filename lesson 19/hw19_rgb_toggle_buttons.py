from machine import Pin
from time import sleep

# define GPIO pins
redLEDPin = 17
greenLEDPin = 18
blueLEDPin = 19

redLED = Pin(redLEDPin, Pin.OUT)
greenLED = Pin(greenLEDPin, Pin.OUT)
blueLED = Pin(blueLEDPin, Pin.OUT)

redButPin = 13
greenButPin = 8
blueButPin = 3

redButton = Pin(redButPin, Pin.IN, Pin.PULL_UP)
greenButton = Pin(greenButPin, Pin.IN, Pin.PULL_UP)
blueButton = Pin(blueButPin, Pin.IN, Pin.PULL_UP)

redButStateNow = 1
greenButStateNow = 1
blueButStateNow = 1

redButStateOld = 1
greenButStateOld = 1
blueButStateOld = 1

redLEDState = False
greenLEDState = False
blueLEDState = False


while True:
    redButStateNow = redButton.value()
    greenButStateNow = greenButton.value()
    blueButStateNow = blueButton.value()
    # print(redButStateNow, greenButStateNow, blueButStateNow)
    # sleep(.1)

    if redButStateOld == 0 and redButStateNow == 1:
        redLEDState = not redLEDState
        redLED.value(redLEDState)
    redButStateOld = redButStateNow

    if greenButStateOld == 0 and greenButStateNow == 1:
        greenLEDState = not greenLEDState
        greenLED.value(greenLEDState)
    greenButStateOld = greenButStateNow

    if blueButStateOld == 0 and blueButStateNow == 1:
        blueLEDState = not blueLEDState
        blueLED.value(blueLEDState)
    blueButStateOld = blueButStateNow
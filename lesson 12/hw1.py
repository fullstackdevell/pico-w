# hw ask user what color he wants, red, green, blue, cyan, magenta, yellow, orange, white, whatever user specifies
# as the color, the led should display that color

from machine import Pin, PWM
from time import sleep

# define GPIO pins
redPin = 13
greenPin = 14
bluePin = 15

# create PWM objects for each LED color
redLED = PWM(Pin(redPin))
greenLED = PWM(Pin(greenPin))
blueLED = PWM(Pin(bluePin))

# set PWM frequency and initial bridghtness
redLED.freq(1000)
redLED.duty_u16(0)
greenLED.freq(1000)
greenLED.duty_u16(0)
blueLED.freq(1000)
blueLED.duty_u16(0)

# default bridghtness
redBrightness = 0
greenBrightness = 0
blueBrightness = 0

while True:
    CMD = input('What color should the LED display? (red, green, blue, cyan, magenta, yellow, orange, white)')
    if CMD == 'red':
        redBrightness = 65535
        greenBrightness = 0
        blueBrightness = 0
    elif CMD == 'green':
        redBrightness = 0
        greenBrightness = 65535
        blueBrightness = 0
    elif CMD == 'blue':
        redBrightness = 0
        greenBrightness = 0
        blueBrightness = 65535
    elif CMD == 'cyan':
        redBrightness = 0
        greenBrightness = 65535
        blueBrightness = 65535
    elif CMD == 'magenta':
        redBrightness = 65535
        greenBrightness = 0
        blueBrightness = 65535
    elif CMD == 'yellow':
        redBrightness = 65535
        greenBrightness = 65535
        blueBrightness = 0
    elif CMD == 'orange':
        redBrightness = 65535
        greenBrightness = 42432
        blueBrightness = 0
    elif CMD == 'white':
        redBrightness = 65535
        greenBrightness = 65535
        blueBrightness = 65535
    else:
        print("Invalid color. Please choose from red, green, blue, cyan, magenta, yellow, orange, white")

    redLED.duty_u16(redBrightness)
    greenLED.duty_u16(greenBrightness)
    blueLED.duty_u16(blueBrightness)

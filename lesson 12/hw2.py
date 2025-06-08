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

colorArray = []
numColors = int(input('How many colors in your sequence?'))

for i in range(0, numColors, 1):
    myColor = input('Enter your color')
    myColor=myColor.lower()
    colorArray.append(myColor)
    print(colorArray)
while True:
    for color in colorArray:
        if color == 'red':
            redLED.duty_u16(65535)
            greenLED.duty_u16(0)
            blueLED.duty_u16(0)
            sleep(1)
        elif color == 'green':
            redLED.duty_u16(0)
            greenLED.duty_u16(65535)
            blueLED.duty_u16(0)
            sleep(1)
        elif color == 'blue':
            redLED.duty_u16(0)
            greenLED.duty_u16(0)
            blueLED.duty_u16(65535)
            sleep(1)
        elif color == 'cyan':
            redLED.duty_u16(0)
            greenLED.duty_u16(65535)
            blueLED.duty_u16(65535)
            sleep(1)
        elif color == 'magenta':
            redLED.duty_u16(65535)
            greenLED.duty_u16(0)
            blueLED.duty_u16(65535)
            sleep(1)
        elif color == 'yellow':
            redLED.duty_u16(65535)
            greenLED.duty_u16(65535)
            blueLED.duty_u16(0)
            sleep(1)
        elif color == 'orange':
            redLED.duty_u16(65535)
            greenLED.duty_u16(42432)
            blueLED.duty_u16(0)
            sleep(1)
        elif color == 'white':
            redLED.duty_u16(65535)
            greenLED.duty_u16(65535)
            blueLED.duty_u16(65535)
            sleep(1)
        elif color == 'off':
            redLED.duty_u16(0)
            greenLED.duty_u16(0)
            blueLED.duty_u16(0)
            sleep(1)
        else:
            print("Invalid color. Please choose from red, green, blue, cyan, magenta, yellow, orange, white")
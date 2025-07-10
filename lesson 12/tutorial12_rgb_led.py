from machine import Pin, PWM
from time import sleep

# define the GPIO (General Purpose Input Output) pins connected to the red, green, and blue LEDs legs
redPin = 13
greenPin = 14
bluePin = 15

# create PWM (Pulse Width Modulation) objects for each LED color. The PWM(Pin(...)) sets up PWM on the specified pins. This allows to control the brightness of the LEDs by varying the duty cycle of the PWM signal.

redLED = PWM(Pin(redPin))
greenLED = PWM(Pin(greenPin))
blueLED = PWM(Pin(bluePin))

# set the frequency of the PWM signal for each LED to 1000 Hz. The frequency determines how fast the LED is pulsed on and off.
# set the initial brightness of the LEDs to 0 (off). The duty_u16() function takes a value from 0 to 65535, where 0 means the LED is off, and 65535 means the LED is fully on.
redLED.freq(1000)
redLED.duty_u16(0)
greenLED.freq(1000)
greenLED.duty_u16(0)
blueLED.freq(1000)
blueLED.duty_u16(0)

while True:
    redBrightness = 6000
    greenBrightness = 1000
    blueBrightness = 3000

    redLED.duty_u16(redBrightness)
    greenLED.duty_u16(greenBrightness)
    blueLED.duty_u16(blueBrightness)
    sleep(.1)
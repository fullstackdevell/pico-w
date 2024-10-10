# create a circuit with an external Led that blinks sos

# s - 3 short
# o - 3 long
# s - 3 short

from machine import Pin
from time import sleep
redLed = Pin(15, Pin.OUT)
while True:

    # S part: 3 short blinks
    for _ in range(3):
        redLed.value(1)  # LED on
        sleep(0.3)       # Short blink
        redLed.value(0)  # LED off
        sleep(0.3)       # Short pause

    # O part: 3 long blinks
    for _ in range(3):
        redLed.value(1)  # LED on
        sleep(0.6)       # Long blink
        redLed.value(0)  # LED off
        sleep(0.6)       # Short pause

    # S part: 3 short blinks
    for _ in range(3):
        redLed.value(1)  # LED on
        sleep(0.3)       # Short blink
        redLed.value(0)  # LED off
        sleep(0.3)       # Short pause

    # Wait before repeating the entire SOS signal
    sleep(2)
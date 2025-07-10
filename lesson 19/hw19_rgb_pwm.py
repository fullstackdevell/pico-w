# This script controls the brightness of Red, Green, and Blue (RGB) LEDs
# using Pulse Width Modulation (PWM) based on button presses.
# Pressing and holding a button will smoothly increase the brightness of
# the corresponding LED. Releasing and pressing the button again will
# smoothly decrease its brightness.

from machine import Pin, PWM
from time import sleep


RED_LED_PIN = 17
GREEN_LED_PIN = 18
BLUE_LED_PIN = 19

RED_BUTTON_PIN = 13
GREEN_BUTTON_PIN = 8
BLUE_BUTTON_PIN = 3

# A higher frequency results in
# smoother dimming
PWM_FREQUENCY = 1000

# Duty cycle determines the brightness: 0 is off, 1023 (for 10-bit resolution) is full brightness.
MIN_DUTY = 0
MAX_DUTY = 65535

BRIGHTNESS_STEP = 20

TRANSITION_DELAY_MS = 5

red_led = PWM(Pin(RED_LED_PIN), freq=PWM_FREQUENCY)
green_led = PWM(Pin(GREEN_LED_PIN), freq=PWM_FREQUENCY)
blue_led = PWM(Pin(BLUE_LED_PIN), freq=PWM_FREQUENCY)

red_button = Pin(RED_BUTTON_PIN, Pin.IN, Pin.PULL_UP)
green_button = Pin(GREEN_BUTTON_PIN, Pin.IN, Pin.PULL_UP)
blue_button = Pin(BLUE_BUTTON_PIN, Pin.IN, Pin.PULL_UP)

current_red_brightness = MIN_DUTY
current_green_brightness = MIN_DUTY
current_blue_brightness = MIN_DUTY

# Store the direction of brightness change for each LED (True for increasing, False for decreasing).
red_brightness_increasing = False
green_brightness_increasing = False
blue_brightness_increasing = False

# Store the previous state of each button to detect presses
prev_red_button_state = True # True means released (PULL_UP state)
prev_green_button_state = True
prev_blue_button_state = True

def smooth_brightness_transition(led_pwm_object, current_brightness, increasing_direction):
    if increasing_direction:
        # Increase brightness, but don't exceed MAX_DUTY
        current_brightness = min(current_brightness + BRIGHTNESS_STEP, MAX_DUTY)
    else:
        # Decrease brightness, but don't go below MIN_DUTY
        current_brightness = max(current_brightness - BRIGHTNESS_STEP, MIN_DUTY)

    led_pwm_object.duty_u16(current_brightness) # Set the new duty cycle
    return current_brightness

while True:
    # Read the current state of each button
    current_red_button_state = red_button.value()
    current_green_button_state = green_button.value()
    current_blue_button_state = blue_button.value()

    # Check for a button press
    if prev_red_button_state and not current_red_button_state:
        # Toggle the brightness direction (increase/decrease) on press
        red_brightness_increasing = not red_brightness_increasing

    # If the button is currently held down
    if not current_red_button_state:
        current_red_brightness = smooth_brightness_transition(
            red_led, current_red_brightness, red_brightness_increasing
        )
        sleep(TRANSITION_DELAY_MS / 1000)

    # Update the previous button state for the next loop iteration
    prev_red_button_state = current_red_button_state

    if prev_green_button_state and not current_green_button_state:
        green_brightness_increasing = not green_brightness_increasing

    if not current_green_button_state:
        current_green_brightness = smooth_brightness_transition(
            green_led, current_green_brightness, green_brightness_increasing
        )
        sleep(TRANSITION_DELAY_MS / 1000)

    prev_green_button_state = current_green_button_state

    if prev_blue_button_state and not current_blue_button_state:
        blue_brightness_increasing = not blue_brightness_increasing

    if not current_blue_button_state:
        current_blue_brightness = smooth_brightness_transition(
            blue_led, current_blue_brightness, blue_brightness_increasing
        )
        sleep(TRANSITION_DELAY_MS / 1000)

    prev_blue_button_state = current_blue_button_state
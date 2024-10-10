# import machine
# led = machine.Pin("LED", machine.Pin.OUT)
# led.off()
# led.on()
# led.off()

# import machine
# import time

# # Initialize the onboard LED (Pin "LED" on Pico W)
# led = machine.Pin("LED", machine.Pin.OUT)

# # Blink the LED in a loop
# while True:
#     led.on()   # Turn the LED on
#     time.sleep(0.1)  # Wait for 1 second
#     led.off()  # Turn the LED off
#     time.sleep(0.1)  # Wait for 1 second

# import machine
# import time

# # Initialize the onboard LED (Pin "LED" on Pico W)
# led = machine.Pin("LED", machine.Pin.OUT)

# # Set the number of blinks
# blink_count = 5

# # Blink 5 times, then stop
# for _ in range(blink_count):
#     led.on()    # Turn the LED on
#     time.sleep(1)  # Wait for 1 second
#     led.off()   # Turn the LED off
#     time.sleep(1)  # Wait for 1 second

# # Ensure the LED is turned off after blinking
# led.off()

# # Print message to indicate blinking has stopped
# print("Blinking stopped and LED is off.")
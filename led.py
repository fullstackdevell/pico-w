# import machine
# led = machine.Pin("LED", machine.Pin.OUT)
# led.off()
# led.on()
# led.off()



# from machine import Pin

# led = Pin(15, Pin.OUT)
# led.value(1)
# led.value(0)




# from machine import Pin, Timer
# led = Pin(15, Pin.OUT)
# timer = Timer()

# def blink(timer):
#     led.toggle()

# timer.init(freq=2, mode=Timer.PERIODIC, callback=blink)



# from machine import Pin
# import time

# # Set up LED
# led = Pin(15, Pin.OUT)

# # Define intervals
# short_blink = 0.25  # 200 ms for individual blinks
# fast_blink = 0.1   # 100 ms for quick blinks

# while True:
#     # Blink twice
#     led.value(1)
#     time.sleep(short_blink)
#     led.value(0)
#     time.sleep(short_blink)
    
#     led.value(1)
#     time.sleep(short_blink)
#     led.value(0)
#     time.sleep(short_blink)

#     # Three quick blinks
#     led.value(1)
#     time.sleep(fast_blink)
#     led.value(0)
#     time.sleep(fast_blink)
    
#     led.value(1)
#     time.sleep(fast_blink)
#     led.value(0)
#     time.sleep(fast_blink)
    
#     led.value(1)
#     time.sleep(fast_blink)
#     led.value(0)

#     # One blick
#     led.value(1)
#     time.sleep(short_blink)
#     led.value(0)
#     time.sleep(short_blink)



# from machine import Pin
# from utime import sleep

# # Initialize LEDs
# led1 = Pin(16, Pin.OUT)
# led2 = Pin(17, Pin.OUT)
# led3 = Pin(18, Pin.OUT)
# led4 = Pin(19, Pin.OUT)
# led5 = Pin(20, Pin.OUT)
# led6 = Pin(21, Pin.OUT)

# while True:
#     # Sequence for LEDs
#     led1.value(1)
#     sleep(0.3)
#     led1.value(0)
    
#     led2.value(1)
#     sleep(0.3)
#     led2.value(0)
    
#     led3.value(1)
#     sleep(0.3)
#     led3.value(0)
    
#     led4.value(1)
#     sleep(0.3)
#     led4.value(0)
    
#     led5.value(1)
#     sleep(0.3)
#     led5.value(0)
    
#     led6.value(1)
#     sleep(0.3)
#     led6.value(0)
    
#     # Repeat sequence with some variations
#     led1.value(1)
#     sleep(0.3)
#     led1.value(0)
    
#     led2.value(1)
#     sleep(0.3)
#     led2.value(0)
    
#     led3.value(1)
#     sleep(0.3)
#     led3.value(0)
    
#     led4.value(1)
#     sleep(0.3)
#     led4.value(0)
    
#     led5.value(1)
#     sleep(0.3)
#     led5.value(0)
    
#     led6.value(1)
#     sleep(0.3)
#     led6.value(0)
    
#     # More complex pattern
#     led1.value(1)
#     sleep(0.3)
#     led1.value(0)
    
#     led2.value(1)
#     sleep(0.3)
#     led2.value(0)
    
#     led3.value(1)
#     sleep(0.3)
#     led3.value(0)
    
#     led4.value(1)
#     sleep(0.3)
#     led4.value(0)
    
#     led5.value(1)
#     sleep(0.3)
#     led5.value(0)
    
#     led6.value(1)
#     sleep(0.3)
#     led6.value(0)
    
#     # Turn off all LEDs and wai




# from machine import Pin
# from utime import sleep

# # Initialize LEDs
# led1 = Pin(16, Pin.OUT)
# led2 = Pin(17, Pin.OUT)
# led3 = Pin(18, Pin.OUT)
# led4 = Pin(19, Pin.OUT)
# led5 = Pin(20, Pin.OUT)
# led6 = Pin(21, Pin.OUT)

# while True:
#     # Turn on LEDs 1, 3, and 5; Turn off LEDs 2, 4, and 6
#     led2.value(0)
#     led4.value(0)
#     led6.value(0)
#     led1.value(1)
#     led3.value(1)
#     led5.value(1)
#     sleep(0.2)
    
#     # Turn off LEDs 1, 3, and 5; Turn on LEDs 2, 4, and 6
#     led1.value(0)
#     led3.value(0)
#     led5.value(0)
#     led2.value(1)
#     led4.value(1)
#     led6.value(1)
#     sleep(0.2)


# from machine import Pin
# import time

# # Set up LEDs (4 LEDs)
# leds = [Pin(16, Pin.OUT), Pin(17, Pin.OUT), Pin(18, Pin.OUT), Pin(19, Pin.OUT)]

# # Define intervals
# short_blink = 0.3  # 300 ms for individual blinks
# long_blink = 0.5   # 500 ms for longer on times
# chase_delay = 0.1  # 100 ms for chase effect

# def blink_leds_pattern():
#     # All LEDs on
#     for led in leds:
#         led.value(1)
#     time.sleep(long_blink)
#     for led in leds:
#         led.value(0)
#     time.sleep(0.1)
    
#     # Sequence blink (1 to 4)
#     for i in range(4):
#         leds[i].value(1)
#         time.sleep(short_blink)
#         leds[i].value(0)
#         time.sleep(0.1)
    
#     # Reverse sequence blink (4 to 1)
#     for i in range(3, -1, -1):
#         leds[i].value(1)
#         time.sleep(short_blink)
#         leds[i].value(0)
#         time.sleep(0.1)
    
#     # Chase pattern
#     for _ in range(3):  # Repeat the chase pattern 3 times
#         for i in range(4):
#             leds[i].value(1)
#             time.sleep(chase_delay)
#             leds[i].value(0)
#         time.sleep(0.2)  # Brief pause before repeating chase

# while True:
#     blink_leds_pattern()

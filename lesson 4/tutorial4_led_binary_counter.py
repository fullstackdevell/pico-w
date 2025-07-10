from machine import Pin
from time import sleep
# green
led1 = Pin(19, Pin.OUT)
# yellow
led2 = Pin(18, Pin.OUT)
# red
led3 = Pin(17, Pin.OUT)
# blue
led4 = Pin(16, Pin.OUT)



while True:
    #  0
    led1.value(0)
    led2.value(0)
    led3.value(0)
    led4.value(0)
    sleep(0.5)

    # 1  = 0001
    led1.value(0)
    led2.value(0)
    led3.value(0)
    led4.value(1)
    sleep(0.5)

    # 2  = 0010
    led1.value(0)
    led2.value(0)
    led3.value(1)
    led4.value(0)
    sleep(0.5)

    # 3  = 0011
    led1.value(0)
    led2.value(0)
    led3.value(1)
    led4.value(1)
    sleep(0.5)

    # 4  = 0100
    led1.value(0)
    led2.value(1)
    led3.value(0)
    led4.value(0)
    sleep(0.5)

    # 5  = 0101
    led1.value(0)
    led2.value(1)
    led3.value(0)
    led4.value(1)
    sleep(0.5)

    # 6  = 0110
    led1.value(0)
    led2.value(1)
    led3.value(1)
    led4.value(0)
    sleep(0.5)

    # 7  = 0111
    led1.value(0)
    led2.value(1)
    led3.value(1)
    led4.value(1)
    sleep(0.5)

    # 8  = 1000
    led1.value(1)
    led2.value(0)
    led3.value(0)
    led4.value(0)
    sleep(0.5)

    # 9  = 1001
    led1.value(1)
    led2.value(0)
    led3.value(0)
    led4.value(1)
    sleep(0.5)

    # 10 = 1010
    led1.value(1)
    led2.value(0)
    led3.value(1)
    led4.value(0)
    sleep(0.5)

    # 11 = 1011
    led1.value(1)
    led2.value(0)
    led3.value(1)
    led4.value(1)
    sleep(0.5)

    # 12 = 1100
    led1.value(1)
    led2.value(1)
    led3.value(0)
    led4.value(0)
    sleep(0.5)

    # 13 = 1101
    led1.value(1)
    led2.value(1)
    led3.value(0)
    led4.value(1)
    sleep(0.5)

    # 14 = 1110
    led1.value(1)
    led2.value(1)
    led3.value(1)
    led4.value(0)
    sleep(0.5)

    # 15 = 1111
    led1.value(1)
    led2.value(1)
    led3.value(1)
    led4.value(1)
    sleep(0.5)
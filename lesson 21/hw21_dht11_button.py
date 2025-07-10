# add a button to the circuit that will toggle between reporting the temperature in Celsius and Fahrenheit

from machine import Pin
import utime as time
from dht import DHT11

dataPin = 16
myPin = Pin(dataPin)
sensor = DHT11(myPin)

butPin = 15
myButton = Pin(butPin, Pin.IN, Pin.PULL_UP)
butStateNow = 1
butStateOld = 1

tempUnitC = True

while True:
    butStateNow = myButton.value()
    if butStateNow == 1 and butStateOld == 0:
        tempUnitC = not tempUnitC

    butStateOld = butStateNow

    try:
        sensor.measure()
        tempC = sensor.temperature()
        tempF = (tempC * 9/5) + 32
        humidity = sensor.humidity()
    
        if tempUnitC == True:
            print("\rtemperature = ", tempC, chr(176) + "C", "humidity = ", humidity, "%", end="")
        else:
            print("\rtemperature = ", tempF, chr(176) + "F", "humidity = ", humidity, "%", end="")
    except OSError as e:
        print("\r", "Sensor error:", e, end='')
    time.sleep(0.5)
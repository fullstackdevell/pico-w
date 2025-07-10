# displayd tempF, tempC, humidity on LCD

from machine import Pin
from lcd1602 import LCD
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

lcd = LCD()
lcd.clear()

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
        lcd.clear()
    
        if tempUnitC == True:
            lcd.write(0, 0, "temp: " + str(tempC) + "\xDF" + "C")
            lcd.write(0, 1, "humidity: " + str(humidity) + "%")
        else:
            lcd.write(0, 0, "temp: " + str(tempF) + "\xDF" + "F")
            lcd.write(0, 1, "humidity: " + str(humidity) + "%")
    except OSError as e:
        print("\r", "Sensor error:", e, end='')
    time.sleep(0.5)
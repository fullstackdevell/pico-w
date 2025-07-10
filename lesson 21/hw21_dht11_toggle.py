# add more toggle activity, tempF, tempC, humidity

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

displayMode = 0  # 0 = C, 1 = F, 2 = humidity

while True:
    butStateNow = myButton.value()
    if butStateNow == 1 and butStateOld == 0:
        displayMode = (displayMode + 1) % 3
    butStateOld = butStateNow

    try:
        sensor.measure()
        tempC = sensor.temperature()
        tempF = (tempC * 9/5) + 32
        humidity = sensor.humidity()
    
        if displayMode == 0:
            print("\rTemperature = ", tempC, chr(176) + "C", end="")
        elif displayMode == 1:
            print("\rTemperature = ", tempF, chr(176) + "F", end="")
        else:
            print("\rHumidity = ", humidity, "%", end="")
            
    except OSError as e:
        print("\r", "Sensor error:", e, end='')
    time.sleep(0.5)
# displayd tempF, tempC, humidity on LCD

from machine import Pin
import utime as time
from dht import DHT11
from lcd1602 import LCD

lcd=LCD()
 
dataPin = 16
myPin = Pin(dataPin,Pin.OUT,Pin.PULL_DOWN)
sensor = DHT11(myPin)
 
butPin = 15
myButton = Pin(butPin,Pin.IN,Pin.PULL_UP)

tempUnitC = True
buttonState = 1
buttonStateOld = 1

while True:
    buttonState = myButton.value()
    if buttonStateOld == 0 and buttonState == 1:
        tempUnitC = not tempUnitC
    try:
        sensor.measure()
    except:
        pass

    tempC = sensor.temperature()
    tempF = tempC * 9/5 + 32
    hum = sensor.humidity()

    if tempUnitC == True:
        lcd.write(0,0,'Temp: '+str(tempC)+'\xDF'+'C  ')
        lcd.write(0,1,"Humidity: "+str(hum)+'%')
    if tempUnitC == False:
        lcd.write(0,0,'Temp: '+str(tempF)+'\xDF'+'F')
        lcd.write(0,1,"Humidity: "+str(hum)+'%')
    time.sleep(.1)
    buttonStateOld = buttonState
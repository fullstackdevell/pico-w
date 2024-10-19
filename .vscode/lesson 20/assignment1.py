from machine import Pin
import utime as time
from dht import DHT11

dataPin = 16

myPin = Pin(dataPin, Pin.OUT, Pin.PULL_DOWN)
sensor = DHT11(myPin)
time.sleep(2)

while True:
    sensor.measure()
    tempC = sensor.temperature()
    hum = sensor.humidity()
    print("\r", 'temperature = ', tempC, chr(176)+'C ', 'humidity = ', hum, '%', end='')
    time.sleep(1)
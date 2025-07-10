from lcd1602 import LCD
import utime as time

lcd = LCD()
while True:
    myName = input("Enter your name: ")
    greeting1 = "Hello, " + myName
    greeting2 = "Welcome"
    lcd.clear()
    lcd.write(0, 0, greeting1)
    lcd.write(0, 1, greeting2)

    time.sleep(2)  # give time to read

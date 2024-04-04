from machine import Pin
import utime

fan = Pin(15, Pin.OUT)

while True:
    fan.toggle()
    utime.sleep(0.5)
    
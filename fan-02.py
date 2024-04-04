from machine import Pin
from time import sleep

fan = machine.Pin(16, machine.Pin.IN)

while True:
    fan.value(1)
    sleep(1)
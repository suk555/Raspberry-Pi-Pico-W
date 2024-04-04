import machine
import utime

INTERVAL = 500

# led = machine.Pin("LED", machine.Pin.OUT)
led = machine.Pin(16, machine.Pin.OUT)
while True:
    led.value(1)
    utime.sleep_ms(INTERVAL)
    led.value(0)
    utime.sleep_ms(INTERVAL)

from machine import Pin, PWM
import utime

pwm = PWM(Pin(16))

pwm.freq(1000)

while True:
    for duty in range(65536):
        pwm.duty_u16(duty)
        utime.sleep_us(1)

    for duty in range(65534, 0, -1):
        pwm.duty_u16(duty)
        utime.sleep_us(1)

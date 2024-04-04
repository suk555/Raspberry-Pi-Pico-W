import time
from machine import Pin, PWM, ADC, Timer

level_input = ADC(0)
pwm_output = PWM(Pin(27))
timer = Timer()

# 25 KHz
pwm_output.freq(25000)

def update_pwm(timer):
    """ Update PWM duty cycle based on ADC input """
    duty = level_input.read_u16()
    pwm_output.duty_u16(duty)

# Start with 50% duty cycle for 2 seconds (to start fan)
pwm_output.duty_u16(32768)
time.sleep(2)

# Update from ADC input after that
timer.init(mode=Timer.PERIODIC, period=100, callback=update_pwm)
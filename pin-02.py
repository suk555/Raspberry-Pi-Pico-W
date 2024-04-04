from picozero import RGBLED
from time import sleep

rgb = RGBLED(red = 1, green = 2, blue = 3)

while True:
    rgb.color = (255, 0, 0)
    sleep(0.5)
    rgb.color = (0, 255, 0)
    sleep(0.5)
    rgb.color = (0, 0, 255)
    sleep(0.5)
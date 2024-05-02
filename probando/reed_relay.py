import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)
gpio.setup(31,gpio.OUT)

while(True):
    gpio.output(31, True)
    time.sleep(2)
    gpio.output(31, False)
    time.sleep(2)



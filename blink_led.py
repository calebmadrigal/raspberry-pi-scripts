import RPi.GPIO as GPIO
from time import sleep

GPIO_PIN = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_PIN, GPIO.OUT)
for i in xrange(32):
    GPIO.output(GPIO_PIN, True)
    sleep(0.05)
    GPIO.output(GPIO_PIN, False)
    sleep(0.05)


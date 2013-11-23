import RPi.GPIO as GPIO
from time import sleep

# Note: they all work for output

# Rev 1
r1_pins = [0, 1, 4, 17, 21, 22, 10, 9, 11, 18, 23, 24, 25, 8, 7]

# Rev 2
r2_pins = [2, 3, 4, 17, 27, 22, 10, 9, 11, 18, 23, 24, 25, 8, 7, 15, 14]

GPIO.setmode(GPIO.BCM)
for pin in r2_pins:
    GPIO.setup(pin, GPIO.OUT)

def pulse_pins(pins):
    for pin in pins:
        print "Pulsing pin", pin
        GPIO.output(pin, True)
    sleep(0.5)
    for pin in pins:
        GPIO.output(pin, False)
    sleep(0.5)

for i in xrange(10000):
    pulse_pins(r2_pins)


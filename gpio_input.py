import RPi.GPIO as GPIO
from time import sleep
import sys

# Work for output: 0, 1, 4, 17, 21, 22, 10, 9, 11, 18, 23, 24, 25, 8, 7
#                                   27?
# Work for input: Everything except 2 and 3 (rev 2 board) 

input_pin = int(sys.argv[1])

GPIO.setmode(GPIO.BCM)
GPIO.setup(input_pin, GPIO.IN)
#GPIO.setup(input_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#GPIO.setup(input_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def input_callback(channel):
    print "HIT"

GPIO.add_event_detect(input_pin, GPIO.RISING, callback=input_callback, bouncetime=200)

print "Input on pin", input_pin
raw_input("Hit ENTER to exit...\n\n")

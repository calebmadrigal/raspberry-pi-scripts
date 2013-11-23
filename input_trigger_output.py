import RPi.GPIO as GPIO
from time import sleep
import sys

input_pin = 7
output_pin = 17
alarm_time_on = 5 #seconds
bounce_time = alarm_time_on * 1000 # milliseconds
triggered = False

def input_callback(channel):
    global triggered
    triggered = True

def pulse_pin(pin, pulse_time_in_secs=1):
    GPIO.output(pin, True)
    print "\tOutput: on"
    sleep(pulse_time_in_secs)
    GPIO.output(pin, False)
    print "\tOutput: off"

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(input_pin, GPIO.IN)
GPIO.setup(output_pin, GPIO.OUT)

GPIO.add_event_detect(input_pin, GPIO.RISING, callback=input_callback, bouncetime=bounce_time)
GPIO.output(output_pin, False)

print "Input pin:", input_pin
print "Ouput pin:", output_pin

while 1:
    if triggered:
        triggered = False
        print "Alarm triggered!"
        pulse_pin(output_pin, alarm_time_on)
    else:
        sleep(0.1)


import RPi.GPIO as GPIO
from time import sleep

on_pins = [9, 1, 7]
off_pins = [11, 0, 8]

GPIO.setmode(GPIO.BCM)

# Set pins to output mode
for pin in on_pins + off_pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, False)

def pulse_pin(pin):
    GPIO.output(pin, True)
    sleep(1)
    GPIO.output(pin, False)

while 1:
    command = raw_input("[switch number (1, 2, or 3)] [on or off (1 or 0)] > ")
    if command == 'exit':
        break
    else:
        try:
            (switch_num, onoff) = command.split(' ')
        except ValueError:
            continue
        if onoff == '1': # on
            print "Turning on switch", switch_num
            pulse_pin(on_pins[int(switch_num)-1])
        else: # off
            print "Turning off switch", switch_num
            pulse_pin(off_pins[int(switch_num)-1])


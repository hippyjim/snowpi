#!/usr/bin/python

# Import required libraries
import RPi.GPIO as GPIO

# Tell GPIO library to use GPIO references
GPIO.setmode(GPIO.BCM)

# Don't display a warning if we didn't clean up properly in our last script
GPIO.setwarnings(False)

LEDs = [7,8,9,22,18,17,23,24,25]
# Setup LED pins as outputs
for x in range(9):
    GPIO.setup(LEDs[x], GPIO.OUT)
    GPIO.output(LEDs[x], False)
# Turn off all LEDs
for x in range(9):
    GPIO.output(LEDs[x], False)

# Reset GPIO settings
GPIO.cleanup()

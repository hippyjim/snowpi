#!/usr/bin/python

# Import required libraries
import RPi.GPIO as GPIO

# Tell GPIO library to use GPIO references
GPIO.setmode(GPIO.BCM)

LEDs = [7,8,9,22,18,17,23,24,25]
# Setup LED pins as outputs
for x in range(8):
    GPIO.setup(LEDs[x], GPIO.OUT)
    GPIO.output(LEDs[x], True)
# Light all LEDs
for x in range(8):
    GPIO.output(LEDs[x], False)

# Reset GPIO settings
GPIO.cleanup()

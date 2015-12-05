#!/usr/bin/python
# Import required libraries
import RPi.GPIO as GPIO
import time

# Tell GPIO library to use GPIO references
GPIO.setmode(GPIO.BCM)

LEDs = [7,8,9,22,18,17,23,24,25]
# Setup LED pins as outputs
for x in range(9):
    GPIO.setup(LEDs[x], GPIO.OUT)
    GPIO.output(LEDs[x], False)
# Light all LEDs
for x in range(9):
    GPIO.output(LEDs[x], True)

print("Press CTRL-C to exit")

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\nExiting")
    GPIO.cleanup()

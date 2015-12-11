#!/usr/bin/python
# Import required libraries
import RPi.GPIO as GPIO
import time

# Tell GPIO library to use GPIO references
GPIO.setmode(GPIO.BCM)

eyeLeft = 23
eyeRight = 24
nose = 25
buttonTopLeft = 7
buttonMiddleLeft = 8
buttonBottomLeft = 9
buttonTopRight = 17
buttonMiddleRight = 18
buttonBottomRight = 22

LEDs = [7,8,9,22,18,17,23,24,25]
# Setup LED pins as outputs
for x in range(9):
    GPIO.setup(LEDs[x], GPIO.OUT)
    GPIO.output(LEDs[x], False)


print("Press CTRL-C to exit")

try:
    GPIO.output(nose, True)
    time.sleep(1)
    GPIO.output(eyeLeft, True)
    GPIO.output(eyeRight, True)
    time.sleep(1)
    GPIO.output(buttonTopLeft, True)
    time.sleep(1)
    GPIO.output(buttonTopRight, True)
    time.sleep(1)
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\nExiting")
    GPIO.cleanup()
#!/usr/bin/python
# Tony Goodhew 19 November 2015
# Uses SnowPi and switch with 10K Ohm pull up on GPIO #16
# PWM brightness control of nose
 
# Import required libraries
import RPi.GPIO as GPIO
import time
import random
random.seed()
 
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


freq = 200  # PWM frequency - 200 times /sec
dutyCycle = 0  # percentage of time on - range 0 to 100
GPIO.setup(nose, GPIO.OUT)
GPIO.setup(eyeLeft, GPIO.OUT)
GPIO.setup(eyeRight, GPIO.OUT)
GPIO.setup(buttonTopLeft, GPIO.OUT)
GPIO.setup(buttonMiddleLeft, GPIO.OUT)
GPIO.setup(buttonBottomLeft, GPIO.OUT)
GPIO.setup(buttonTopRight, GPIO.OUT)
GPIO.setup(buttonMiddleRight, GPIO.OUT)
GPIO.setup(buttonBottomRight, GPIO.OUT)

pwmNose = GPIO.PWM(nose, freq)
pwmEyeLeft = GPIO.PWM(eyeLeft, freq)
pwmEyeRight = GPIO.PWM(eyeRight, freq)
pwmButtonTopLeft = GPIO.PWM(buttonTopLeft, freq)
pwmButtonMiddleLeft = GPIO.PWM(buttonMiddleLeft, freq)
pwmButtonBottomLeft = GPIO.PWM(buttonBottomLeft, freq)
pwmButtonTopRight = GPIO.PWM(buttonTopRight, freq)
pwmButtonMiddleRight = GPIO.PWM(buttonMiddleRight, freq)
pwmButtonBottomRight = GPIO.PWM(buttonBottomRight, freq)

pwmNose.start(0)
pwmEyeLeft.start(0)
pwmEyeRight.start(0)
pwmButtonTopLeft.start(0)
pwmButtonMiddleLeft.start(0)
pwmButtonBottomLeft.start(0)
pwmButtonTopRight.start(0)
pwmButtonMiddleRight.start(0)
pwmButtonBottomRight.start(0)

# ==== Main begins ====
pwmNose.ChangeDutyCycle(100)  # Nose full brightness

try:
    while True:
        for brite in range(0,100,1):
            pwmNose.ChangeDutyCycle(brite)
            pwmEyeLeft.ChangeDutyCycle(100 - brite)
            pwmEyeRight.ChangeDutyCycle(100 - brite)
            pwmButtonTopLeft.ChangeDutyCycle(brite)
            pwmButtonMiddleLeft.ChangeDutyCycle(100 - brite)
            pwmButtonBottomLeft.ChangeDutyCycle(brite)
            pwmButtonTopRight.ChangeDutyCycle(brite)
            pwmButtonMiddleRight.ChangeDutyCycle(100 - brite)
            pwmButtonBottomRight.ChangeDutyCycle(brite)
            time.sleep(0.01)
        time.sleep(0.1)
        for brite in range(100,0,-1):
            pwmNose.ChangeDutyCycle(brite)
            pwmEyeLeft.ChangeDutyCycle(100 - brite)
            pwmEyeRight.ChangeDutyCycle(100 - brite)
            pwmButtonTopLeft.ChangeDutyCycle(brite)
            pwmButtonMiddleLeft.ChangeDutyCycle(100 - brite)
            pwmButtonBottomLeft.ChangeDutyCycle(brite)
            pwmButtonTopRight.ChangeDutyCycle(brite)
            pwmButtonMiddleRight.ChangeDutyCycle(100 - brite)
            pwmButtonBottomRight.ChangeDutyCycle(brite)
            time.sleep(0.01)
except KeyboardInterrupt:
    print("\nExiting")
    GPIO.cleanup()
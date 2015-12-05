#SnowPi Test Code - requires GPIOZero library to be installed
import random
import time
from gpiozero import LED
#Setup all the LEDs
 
buttonTopLeft = LED(7)
buttonMiddleLeft = LED(8)
buttonBottomLeft = LED(9)
buttonTopRight = LED(17)
buttonMiddleRight = LED(18)
buttonBottomRight = LED(22)
eyeLeft = LED(23)
eyeRight = LED(24)
nose = LED(25)
 
buttonTopLeft.off()
buttonMiddleLeft.off()
buttonBottomLeft.off()
buttonTopRight.off()
buttonMiddleRight.off()
buttonBottomRight.off()
eyeLeft.off()
eyeRight.off()
nose.off()
 
while True:
    buttonTopLeft.toggle()
    time.sleep(1)
    buttonMiddleLeft.toggle()
    time.sleep(1)
    buttonBottomLeft.toggle()
    time.sleep(1)
    buttonTopRight.toggle()
    time.sleep(1)
    buttonMiddleRight.toggle()
    time.sleep(1)
    buttonBottomRight.toggle()
    time.sleep(1)
    eyeLeft.toggle()
    time.sleep(1)
    eyeRight.toggle()
    time.sleep(1)
    nose.toggle()
    time.sleep(1)

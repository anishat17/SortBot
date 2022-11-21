# Use this file to communicate with the RaspberryPi and Arduino
import RPi.GPIO as GPIO
from time import sleep
from signal import pause

blinkerPin = 18
indicateLeftLED = 18
indicateRightLED = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(blinkerPin, GPIO.OUT)

# Set pin to ON or OFF depdning on newState=bool
def lightBlinkTest(newState):
    if newState:
        print("LED on")
        GPIO.output(blinkerPin, GPIO.HIGH)
    else:
        print("LED off")
        GPIO.output(blinkerPin, GPIO.LOW)

# Visual inidcation functions for Lab 7 demo. Light up corresponding
#  LED for the direction camera needs to turn to center target
def indicateTurnLeft():
    GPIO.output(indicateRightLED, GPIO.LOW)
    GPIO.output(indicateLeftLED, GPIO.HIGH)

def indicateTurnRight():
    GPIO.output(indicateLeftLED, GPIO.LOW)
    GPIO.output(indicateRightLED, GPIO.HIGH)

def turnLeft( degrees ):
    return None

def lowerCrane():
    return None

def turnOnMagnet():
    return None

def returnCraneToCenter():
    return None

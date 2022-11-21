# Use this file to communicate with the RaspberryPi and Arduino
import RPi.GPIO as GPIO
from time import sleep
from signal import pause

blinkerPin = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(blinkerPin, GPIO.out)

# Set pin to ON or OFF depdning on newState=bool
def lightBlinkTest(newState):
    if newState:
        print("LED on")
        GPIO.output(blinkerPin, GPIO.HIGH)
    else:
        print("LED off")
        GPIO.output(blinkerPin, GPIO.LOW)


def turnLeft( degrees ):
    return None

def lowerCrane():
    return None

def turnOnMagnet():
    return None

def returnCraneToCenter():
    return None

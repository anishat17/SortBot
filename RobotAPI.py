# Use this file to communicate with the RaspberryPi and Arduino
import RPi.GPIO as GPIO
from time import sleep
from signal import pause
from adafruit_servokit import ServoKit
import time

kit = ServoKit(channels = 16)

blinkerPin = 18
indicateLeftLED = 18
indicateRightLED = 17

servo1Angle = 90
servo2Angle = 90

GPIO.setmode(GPIO.BCM)
GPIO.setup(blinkerPin, GPIO.OUT)
GPIO.setup(indicateLeftLED, GPIO.OUT)
GPIO.setup(indicateRightLED, GPIO.OUT)

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

def turnRight( degrees ):
    global servo1Angle
    turnAngle = servo1Angle - degrees
    print (turnAngle)
    if (0<=turnAngle<=180):
        kit.servo[15].angle = turnAngle
        servo1Angle = turnAngle
    time.sleep(2)

    return None
def turnLeft( degrees ):
    global servo1Angle
    turnAngle = servo1Angle + degrees
    print (turnAngle)
    if (0<=turnAngle<=180):
        kit.servo[15].angle = turnAngle
        servo1Angle = turnAngle
    time.sleep(2)

    return None

def lowerCrane():
    kit.servo[14].angle = 9
    print("blow")
    time.sleep(2)
    returnCraneToCenter()
    time.sleep(2)

    return None

def turnOnMagnet():
    return None

def returnCraneToCenter():
    global servo1Angle 

    servo1Angle = 90
    print("flow")

    kit.servo[15].angle = 90
    kit.servo[14].angle = 90
    return None

if __name__ == "__main__":
    turnLeft(30)
    sleep(2)
    turnRight(30)
    sleep(1)
    #returnCraneToCenter()
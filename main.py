# Main loop here

import CameraInput
import RobotFunctions
import RobotAPI

import time


print("Running main.py")

CameraInput.testprint()

i = 0
while (1):
    i += 1
    print(i)
    # Alternate BlinkTest input between TRUE/FALSE
    RobotAPI.lightBlinkTest( i%2 == 0 )
    time.sleep(1)

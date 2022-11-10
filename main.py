# Main loop here

import CameraInput
import RobotFunctions
import RobotUI

import time


print("Running main.py")

CameraInput.testprint()

i = 0
while (1):
    i += 1
    print(i)
    CameraInput.printTowelAlternating(i)
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
#sudo apt-get install build-essential cmake pkg-config libjpeg-dev libtiff5-dev libjasper-dev libpng-dev libavcodec-dev libavformat-dev libswscale-dev libv4l-dev libxvidcore-dev libx264-dev libfontconfig1-dev libcairo2-dev libgdk-pixbuf2.0-dev libpango1.0-dev libgtk2.0-dev libgtk-3-dev libatlas-base-dev gfortran libhdf5-dev libhdf5-serial-dev libhdf5-103 python3-pyqt5 python3-dev -y

# Main loop here

import time

import CameraInput
#import RobotAPI
import RobotFunctions

print("Running main.py")

CameraInput.testprint()

centerX, centerY = CameraInput.getCameraCenterCoordinate()
for i in CameraInput.trackObject():
    print(i, ";", centerX, end=' ')
    if (i[0] >= centerX):
        print("Camera looking too far left! Must turn towards right...")
        #RobotAPI.indicateTurnLeft()
    else:
        print("Camera looking too far right! Must turn towards left...")
        #RobotAPI.indicateTurnRight()


import cv2
import numpy as np

large = cv2.imread('1.jpg')

small = cv2.cvtColor(large, cv2.COLOR_BGR2GRAY)

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
grad = cv2.morphologyEx(small, cv2.MORPH_GRADIENT, kernel)

_, bw = cv2.threshold(grad, 0.0, 255.0, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 1))
connected = cv2.morphologyEx(bw, cv2.MORPH_CLOSE, kernel)

contours, hierarchy = cv2.findContours(connected.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

mask = np.zeros(bw.shape, dtype=np.uint8)

with open("coords.txt","w+") as file:
    for idx in range(len(contours)):
        x, y, w, h = cv2.boundingRect(contours[idx])
        mask[y:y+h, x:x+w] = 0
        file.write("Box {0}: ({1},{2}), ({3},{4}), ({5},{6}), ({7},{8})".format(idx,x,y,x+w,y,x+w,y+h,x,y+h))
        cv2.drawContours(mask, contours, idx, (255, 255, 255), -1)
        r = float(cv2.countNonZero(mask[y:y+h, x:x+w])) / (w * h)

# Handle all camera input and processing here then pass to main.py

import cv2

def testprint():
    print("Calling testprint() from CameraInput.py")


def printTowel():
    print("Loading Start Window:")
    image = cv2.imread("towel.jpeg")
    cv2.imshow("Start window", image)
    # waitKey will close the window upon any keypress with delay=0 ms
    #   (Window MUST be selected first)
    cv2.waitKey(0)
    print("Start Window closed")


def printTowelAlternating(i):
    print("Loading Start Window:")
    i += 1
    if i % 2 == 0:
        image = cv2.imread("towel.jpeg")
    else:
        image = cv2.imread("towels.jpeg")
    cv2.imshow("Start window", image)
    # waitKey will close the window upon any keypress with delay=0 ms
    #   (Window MUST be selected first)
    cv2.waitKey(0)
    print("Start Window closed")

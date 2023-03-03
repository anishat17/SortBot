import threading
import CameraInput
import RobotFunctions
import time
from collections import deque

margin =50
turnAngle= 45

print("Running MainThreaded.py")
y = 0
centerX, centerY = CameraInput.getCameraCenterCoordinate()
frameBuffer = deque(maxlen=10)
globalImageVar = [None]

def queueFrames(dequeObject):
    for img in CameraInput.frameGenerator():
        dequeObject.append(img)

def analyzeFrame(dequeObject, outImage):
    hsvClassifier = CameraInput.HSVClassifier()
    while True:
        if len(dequeObject) > 0:
            img = dequeObject.popleft()
            outImage[0] = hsvClassifier.label(img, still_image=False)


t1 = threading.Thread(target=queueFrames, args=(frameBuffer,))
t2 = threading.Thread(target=analyzeFrame, args=(frameBuffer, globalImageVar))


t1.start()
t2.start()

while True:
    if globalImageVar[0] is not None:
        CameraInput.cv2.imshow("Labeled feed", globalImageVar[0])
        if CameraInput.cv2.waitKey(10) & 0xFF == ord('q'):
            break
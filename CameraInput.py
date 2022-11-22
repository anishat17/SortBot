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


#run a FOREVER loop. shows camera feed and draws bounding box around
# object of interest, and also YIELDS the x,y of the box to caller func
def trackObject():
    imcap = cv2.VideoCapture(0)

    imcap.set(3, 640) # Set field 3 (width) to 640
    imcap.set(4, 480) # Set field 4 (Height) 480

    # import cascade (OpenCV pre-trained HAAR classifier)
    faceCascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

    while True:
        success, img = imcap.read() # capture frame from video
        # converting image from color to grayscale 
        imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Getting corners around the face
        # 1.3 = scale factor, 5 = minimum neighbor can be detected
        faces = faceCascade.detectMultiScale(imgGray, 1.3, 5)  

        # drawing bounding box around face
        for (x, y, w, h) in faces:
            img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255,   0), 3)
            yield (x + w/2),(y + h/2) # Yield coordinate of center of box
        # displaying image with bounding box
        cv2.imshow('face_detect', img)
        # loop will be broken when 'q' is pressed on the keyboard
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
    imcap.release()
    cv2.destroyWindow('face_detect')
    

# Returns (x,y) coordinate that is CENTER of current videoCapture device
def getCameraCenterCoordinate():
    imcap = cv2.VideoCapture(0)
    x = imcap.get(cv2.CAP_PROP_FRAME_WIDTH)
    y = imcap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    imcap.release()
    return x/2,y/2

#script 
#from picamera import PiCamera

#camera = PiCamera()
#camera.resolution = (1280,720)
#camera.vflip = True
#camera.contrast = 50

#time.sleep(2)


#camera.capture("/home/pi/Pictures/img.jpg")
#print("Done.")



#-----------------------------------------------------------------------


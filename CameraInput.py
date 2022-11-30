# Handle all camera input and processing here then pass to main.py

import cv2
import imutils
import ShapeDetector

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
def trackFace():
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

#script. Test if picamera is functional or not idk what this is for
# Instantiates pi's camera, takes a picture, and saves to below directory 
def savePiPhoto():
    from picamera import PiCamera
    import time

    camera = PiCamera()
    camera.resolution = (1280,720)
    camera.vflip = True
    camera.contrast = 50

    time.sleep(2)

    camera.capture("/home/pi/Pictures/img.jpg")
    print("Done.")


#run a FOREVER loop. shows camera feed and draws contours around
# shapes, and also YIELDS the x,y of the contour to caller func
def trackShapes():
	# load the camera and resize it to a smaller factor so that
	# the shapes can be approximated better
    imcap = cv2.VideoCapture(0)

    imcap.set(3, 640) # Set field 3 (width) to 640
    imcap.set(4, 480) # Set field 4 (Height) 480
    
    while True:
        success, img = imcap.read() # capture frame from video
        resized = imutils.resize(img, width=300)
        ratio = img.shape[0] / float(resized.shape[0])
        # converting image from color to grayscale, blur, and threshold
        blurred = cv2.GaussianBlur(resized, (5, 5), 0)
        imgGray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)
        lab = cv2.cvtColor(blurred, cv2.COLOR_BGR2LAB)
        thresh = cv2.threshold(imgGray, 60, 255, cv2.THRESH_BINARY)[1]

        # Find contours in thresholded image and init ShapeDetector
        contours = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE)
        contours = imutils.grab_contours(contours)

        sd = ShapeDetector.ShapeDetector()
        cl = ShapeDetector.ColorLabeler()


        # drawing bounding box around face
        for c in contours:
            # compute the center of the contour, then detect the name of the
            # shape using only the contour
            M = cv2.moments(c)
            if ( M["m00"] != 0 ):
                cX = int((M["m10"] / M["m00"]) * ratio)
                cY = int((M["m01"] / M["m00"]) * ratio)
            else:
                # For some reason M["m00"] can be 0 which causes Div-0 error
                cX = 0
                cY = 0
            shape = sd.detect(c)
            color = cl.label(lab, c)

            # multiply the contour (x, y)-coordinates by the resize ratio,
            # then draw the contours and the name of the shape on the image
            c = c.astype("float")
            c = c.astype("int")
            cv2.drawContours(img, [c], -1, (0, 255, 0), 2)
            text = "{} {}".format(color, shape)
            cv2.putText(img, text, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX,
                0.5, (255, 255, 255), 2)

            yield (cX),(cY) # Yield coordinate of center of box
        # displaying image with bounding box
        cv2.imshow('shape_detect', img)
        # loop will be broken when 'q' is pressed on the keyboard
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
    imcap.release()
    cv2.destroyWindow('face_detect')


if __name__ == "__main__":
    import time
    import RobotFunctions

    print("Running CameraInput.py")

    testprint()

    centerX, centerY = getCameraCenterCoordinate()
    frameCounter = 0
    for i in trackShapes():
        print(frameCounter, i, ";", centerX, end=' ')
        if (i[0] >= centerX):
            print("Camera looking too far left! Must turn towards right...")
            #RobotAPI.indicateTurnLeft()
        else:
            print("Camera looking too far right! Must turn towards left...")
            #RobotAPI.indicateTurnRight()
        frameCounter += 1

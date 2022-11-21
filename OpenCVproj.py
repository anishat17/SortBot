#OpenCV and TensorFlow demo
import cv2


print("Now running OpenCVproj...")




# Demo 2 Snippet: I forgot what this demo was about
#  This demo snippet is just to make sure the script is 
#  importing and running OpenCV (cv2) correctly. Accesses
#  a single image (towel.jpeg) (provided in same folder)
#  and shows the image (cv2.imshow()) in a new window.
#

print("Loading Start Window:")
image = cv2.imread("towel.jpeg")
cv2.imshow("Start window", image)
# waitKey will close the window upon any keypress with delay=0 ms
#   (Window MUST be selected first)
cv2.waitKey(0)
print("Start Window closed")






# Demo 1: Real time object detection
# https://towardsdatascience.com/
#  how-to-detect-objects-in-real-time-using-opencv-and-python-c1ba0c2c69c0
#
# This demo will take in webcam's video-capture and draw a bounding-
#  box around the specified target class in each frame (human face)
#

# '0' for default built-in web-cam. '+/-1' for external cam
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
        print("face detected at:", x, y)
    # displaying image with bounding box
    cv2.imshow('face_detect', img)
    # loop will be broken when 'q' is pressed on the keyboard
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
imcap.release()
cv2.destroyWindow('face_detect')

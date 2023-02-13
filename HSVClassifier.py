import cv2
import numpy as np
import imutils
from collections import OrderedDict

# Alternative object identifier because the ones in ShapeDetector are lackin
class HSVClassifier:

    # Pre-defined "Color Ranges" (clrRng) as numpy arrays
    # TODO: (maybe) Add more color entries IF we have more OBJECTS OF INTEREST
    clrRng = OrderedDict({
        "red" : (np.array([0,100,100]), np.array([7,255,255])),
        "yellow" : (np.array([25,100,100]), np.array([30,255,255])),
        "green" : (np.array([40,70,80]), np.array([70,255,255])),
        "blue" : (np.array([90,60,0]), np.array([121,255,255]))
    })

    def __init__(self):
        pass

    # Given an img, finds all objects that fall within a pre-defined clr range
    #  and labels the image with labels of the color
    """
        img : Image to read and rewrite over with labels. Modified and returned
        min/maxSize : Size check for all objects. Object ignored if outside bounds
        still_image : Bool on whether this method is being called on a still image
                        rather than a live video capture.
                        Can ALSO be used to go frame-by-frame in a video
        verbose : Debugging tool. Displays extra information like obj size and
                    (TODO:) the object's HSV value
    """
    def label(self, img, minSize=250, maxSize=1000, still_image=False, verbose=False):
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        # For every color defined in Classifier's 'clrRng'...
        for searchColor in HSVClassifier.clrRng.items():
            # Mask regions that fall in range
            inRangeRegion = cv2.inRange(hsv, searchColor[1][0], searchColor[1][1])
            # then find the contour of those regions
            contours=cv2.findContours(inRangeRegion,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
            contours = imutils.grab_contours(contours)
            for c in contours:
                perimeterLength = cv2.arcLength(c, True)
                if minSize < perimeterLength < maxSize: # contour size filter
                    cv2.drawContours(img, [c], -1, (0,255,0), 2)
                    # Compute center of contour
                    M = cv2.moments(c)
                    if M["m00"] != 0:
                        cX = int(M["m10"] / M["m00"])
                        cY = int(M["m01"] / M["m00"])
                    else:
                        cX, cY = 0, 0
                    cv2.circle(img, (cX, cY), 7, (255, 255, 255), 1) # Mark center of c
                    text = searchColor[0]
                    if verbose:
                        text += " " + str(int(perimeterLength))
                        # TODO: Append HSV value to text
                    cv2.putText(img, text, (cX - 20, cY - 20),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 1)
        if still_image:
            cv2.imshow("still_image",img)
            k = cv2.waitKey(0)
        return img




if __name__=="__main__":
    image = cv2.imread("ColorWheel.png")
    hsvClassifier = HSVClassifier()
    hsvClassifier.label(image)
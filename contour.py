import cv2 
import numpy as np 
import sys
from matplotlib import pyplot as plt

THRESHOLD_MIN = 100
THRESHOLD_MAX = 150

def input():
    if len(sys.argv) != 2:
        print ("Usage")
        print ("python contour.py <image_file>")
        sys.exit(0)
    else:
        imageFile = sys.argv[1]
    return imageFile 

if __name__ == "__main__":
    #1. Input
    imageFile = input()

    #2. Preprocessing
    img = cv2.imread(imageFile)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #3. Apply threshold or canny to convert to binary image
    #_, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    binary = cv2.Canny(gray, THRESHOLD_MIN, THRESHOLD_MAX)

    #4. Classify shape by finding contours
    # TODO: Get the degree of corner to distinguish between diamond and triangle
    _, contours, _ = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    shape = "Undefined"
    for contour in contours:
        perimeter = cv2.arcLength(contour, True)
        epsilon = 0.02 * perimeter # in the range of 0.01peri - 0.05peri
        approx = cv2.approxPolyDP(contour, epsilon, True)
        numVertices = len(approx)
        if numVertices == 3:
            shape = "Triangle"
        elif numVertices == 4:
            _, _, w, h = cv2.boundingRect(contour)
            ratio = float(w) / h
            if ratio >= 0.9 and ratio <= 1.1:
                shape = "Square"
            else:
                shape = "Rectangle"
        elif numVertices == 5:
            shape = "Pentagon"
        elif numVertices > 5:
            shape = "Circle"

        # Detect the centroid of the shape
        if numVertices >= 3:
            M = cv2.moments(contour)
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])

            # Classify the shape
            cv2.putText(img, shape, (cx, cy), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 2)

    cv2.imshow('img',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
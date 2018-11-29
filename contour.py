import cv2 
import numpy as np 
from matplotlib import pyplot as plt

IMAGE_FILE = 'shape.png'

img = cv2.imread(IMAGE_FILE)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply threshold or canny to convert to binary image
_, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

_, contours, _ = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for contour in contours:
    perimeter = cv2.arcLength(contour, True)
    epsilon = 0.02 * perimeter
    approx = cv2.approxPolyDP(contour, epsilon, True)
    if len(approx) == 3:
        print ('Triangle')
        cv2.drawContours(img, [contour], 0, (0,0,255), 2) # Red
    elif len(approx) == 4:
        print ('Rectangle')
        cv2.drawContours(img, [contour], 0, (0,255,0), 2) # Green
    else:
        print ('Circle', len(approx))
        cv2.drawContours(img, [contour], 0, (255,0,0), 2) # Blue

# cv2.drawContours(img, contours, -1, (0,0,255), 3)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
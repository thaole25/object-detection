import cv2
import numpy as np
from matplotlib import pyplot as plt

IMAGE_FILE = 'shape-black.png'
THRESHOLD_MIN = 100
THRESHOLD_MAX = 200
RHO = 1 
THETA = np.pi/180
MIN_VOTE_LINE = 100 

def houghLine(binaryImg):
    lines = cv2.HoughLines(binaryImg, RHO, THETA, MIN_VOTE_LINE)
    for rho,theta in lines[0]:
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a*rho
        y0 = b*rho
        x1 = int(x0 + 1000*(-b))
        y1 = int(y0 + 1000*(a))
        x2 = int(x0 - 1000*(-b))
        y2 = int(y0 - 1000*(a))
        cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)

def houghCircle(grayImg):
    circles = cv2.HoughCircles(grayImg,cv2.HOUGH_GRADIENT,1,10,param1=50,param2=30,minRadius=0,maxRadius=0)
    circles = np.uint16(np.around(circles))
    for i in circles[0,:]:
        # draw the outer circle
        cv2.circle(grayImg,(i[0],i[1]),i[2],(0,255,0),2)
        # draw the center of the circle
        cv2.circle(grayImg,(i[0],i[1]),2,(0,0,255),3)


if __name__ == "__main__":
    # Preprocessing
    img = cv2.imread(IMAGE_FILE)
    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Canny algorithm
    edges = cv2.Canny(grayImg, THRESHOLD_MIN, THRESHOLD_MAX)

    # Plot the results
    plt.subplot(121),plt.imshow(edges,cmap = 'gray')
    plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

    plt.subplot(122),plt.imshow(grayImg,cmap = 'gray')
    plt.title('Circle Image') , plt.xticks([]), plt.yticks([])
    plt.show()
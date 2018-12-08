# object-detection
Reference: https://www.pyimagesearch.com/2016/02/08/opencv-shape-detection/

Detect rectangle, square, round, triangle and diamond shape objects

Usage: python contour.py <image_file>

Step-by-step
1. Preprocessing: convert BGR image to Binary image (may use canny algorithm in this step)
2. Find contours. Use contour approximation to get the number of vertices of each shape
3. Classify the shape based on the number of vertices
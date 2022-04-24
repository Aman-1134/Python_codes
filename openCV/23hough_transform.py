import cv2
import numpy as np

img = cv2.imread('D:\opencv-master\samples\data\sudoku.png')
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(imgray, 0, 150, apertureSize=3)
cv2.imshow('Canny', edges)
# # -------------------- Hough Line Transform ----------------- #
# lines = cv2.HoughLines(edges, 1, np.pi/180, 200)
#
# for line in lines:
#     rho, theta = line[0]          # lines return two values
#     a = np.cos(theta)
#     b = np.sin(theta)
#     x0 = a * rho
#     y0 = b * rho
#
#     x1 = int(x0 + 1000 * (-b))
#     y1 = int(y0 + 1000 * a)
#
#     x2 = int(x0 - 1000 * (-b))
#     y2 = int(y0 - 1000 * a)
#     cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
# # --------------------------------------------------------- #

# -------------------- Probabilistic Hough Transform ----------------- #
lines = cv2.HoughLinesP(edges, 1, np.pi/180, 200, maxLineGap=10, minLineLength=100)
for line in lines:
    x1, y1, x2, y2 = line[0]              # here line returns 4 values
    cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
# -------------------------------------------------------------------- #
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
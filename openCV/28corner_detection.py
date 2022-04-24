# --------------- Harris Corner Detection ------------- #
# -------------------------- Steps -------------------- #
# 1.Determine which window produce very large variation in intensity when moved in both x and y direction
# 2.With each such window found, a score R is computed
# 3.After applying threshold to this score, important corners are selected and marked

#             Harris Not Working           #

import numpy as np
import cv2

img = cv2.imread('D:\opencv-master\samples\data\\pic1.png')
cv2.imshow('Original Image', img)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gray = np.float32(gray)
dst = cv2.cornerHarris(gray, 2, 3, 0.04)         # takes the image in float32 format
dst = cv2.dilate(dst, None)

img[dst > 0.01 * dst.max()] = [0, 0, 255]
cv2.imshow('Harris', dst)

# -------------- Shi Tomasi Corner Detection --------------- #
# This is modified form of Harris Corner detection and detects corner in a better way

img = cv2.imread('D:\opencv-master\samples\data\\pic1.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(gray, 50, 0.01, 10)
corners = np.int0(corners)

for i in corners:
    x, y = i.ravel()
    cv2.circle(img, (x, y), 3, 255, 3)

cv2.imshow('Tomasi', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
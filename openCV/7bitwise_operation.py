import numpy as np
import cv2

img1 = np.zeros((250, 500, 3))               # a complete black image
img1 = cv2.rectangle(img1, (200, 0), (300, 100), (255, 255, 255), -1)
img2 = np.zeros((250, 500, 3))               # complete black image is made half white
img2 = cv2.rectangle(img2, (250, 0), (500, 250), (255, 255, 255), -1)

bitAnd = cv2.bitwise_and(img1, img2)         # and operation on both images
# change 'and' with other logical operators
# ie or, and, xor, not
cv2.imshow('Image1', img1)
cv2.imshow('Image2', img2)
cv2.imshow('Result', bitAnd)

cv2.waitKey(0)
cv2.destroyAllWindows()
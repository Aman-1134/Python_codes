# template matching is a process of finding a certain template<part> in a larger image

import cv2
import numpy as np

img = cv2.imread('D:\opencv-master\samples\data\messi5.jpg')
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
tempelate = cv2.imread('messi_face.png', 0)
w, h = tempelate.shape[::-1]

# res = cv2.matchTemplate(imgray, tempelate, cv2.TM_CCORR_NORMED)        # use threshold = 0.99 for this
res = cv2.matchTemplate(imgray, tempelate, cv2.TM_CCOEFF_NORMED)
print(res)

threshold = 0.95
loc = np.where(res >= threshold)
print(loc)

for pt in zip(*loc[::-1]):
    cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (255, 255, 0), 2)

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
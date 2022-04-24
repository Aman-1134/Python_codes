import numpy as np
import cv2
import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')
plt.grid(color='m', linewidth=0.5, linestyle=':')
img = cv2.imread('D:\opencv-master\samples\data\\lena.jpg', 0)
# img = np.zeros((200, 200), np.uint8)
# cv2.rectangle(img, (0, 100), (200, 200), (255), -1)
# cv2.rectangle(img, (0, 50), (100, 100), (127), -1)

# b, g, r = cv2.split(img)
#
# cv2.imshow('b', b)
# cv2.imshow('g', g)
# cv2.imshow('r', r)

# plt.hist(b.ravel(), 256, [0, 256], color='b')
# plt.hist(g.ravel(), 256, [0, 256], color='g')
# plt.hist(r.ravel(), 256, [0, 256], color='r')

hist = cv2.calcHist([img], [0], None, [256], [0, 256])
plt.plot(hist)
plt.xlabel('Intensity of Pixels')
plt.ylabel('Number of pixels')
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()

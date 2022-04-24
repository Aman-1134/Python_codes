import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('D:\opencv-master\samples\data\smarties.png', cv2.IMREAD_GRAYSCALE)
_, mask = cv2.threshold(img, 220, 250, cv2.THRESH_BINARY_INV)

kernel = np.ones((2, 2), np.uint8)                   # draws a 2*2 white square in the dots in figures

# kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
# array([[1, 1, 1, 1, 1],
#        [1, 1, 1, 1, 1],
#        [1, 1, 1, 1, 1],
#        [1, 1, 1, 1, 1],
#        [1, 1, 1, 1, 1]], dtype=uint8)
# # Elliptical Kernel
# kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
# array([[0, 0, 1, 0, 0],
#        [1, 1, 1, 1, 1],
#        [1, 1, 1, 1, 1],
#        [1, 1, 1, 1, 1],
#        [0, 0, 1, 0, 0]], dtype=uint8)
# # Cross-shaped Kernel
# kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5))
# array([[0, 0, 1, 0, 0],
#        [0, 0, 1, 0, 0],
#        [1, 1, 1, 1, 1],
#        [0, 0, 1, 0, 0],
#        [0, 0, 1, 0, 0]], dtype=uint8)

dilation = cv2.dilate(mask, kernel, iterations=3)    # it removes the spots but size of balls increase
erosion = cv2.erode(dilation, kernel, iterations=1)
# erosion = 1 if all pixels surrounding a pixel is 1, else 0
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
# opening = erosion followed by dilation
closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
# closing = dilation followed by erosion
mg = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernel)
# difference between dilation and erosion of image
th = cv2.morphologyEx(mask, cv2.MORPH_TOPHAT, kernel)
# diff between input image and opening of an image
# Black Hat = difference between the closing of the input image and input image

titles = ['Image', 'mask', 'dilation', 'erosion', 'opening', 'closing', 'morph-gradient', 'Tophat']
image = [img, mask, dilation, erosion, opening, closing, mg, th]

for i in range(8):
    plt.subplot(2, 4, i+1), plt.imshow(image[i], 'gray')
    plt.title(titles[i])
    plt.axis('off')

plt.show()
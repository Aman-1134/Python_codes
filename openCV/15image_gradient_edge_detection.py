# image gradient is the directional change in the intensity or color
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('D:\opencv-master\samples\data\lena.jpg', 0)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

lap = cv2.Laplacian(img, cv2.CV_64F, ksize=1)           # all edges are detected
lap = np.uint8(np.absolute(lap))               # image has float pixels value, changing them to int

sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0)      # 1 and 0 are for order of dx and dy
sobelX = np.uint8(np.absolute(sobelX))

sobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1)
sobelY = np.uint8(np.absolute(sobelY))

sobelCombined = cv2.bitwise_or(sobelX, sobelY)

# canny edge detection method
canny = cv2.Canny(img, 100, 200)                    # produces least noise images

#_______________________- Canny Edge Detection Steps -_____________________#
# 1.Noise Reduction
# 2.Gradient Calculation
# 3.Non-Maximum Suppression
# 4.Double Threshold
# 5.Edge Tracking by Hysteresis

titles = ['Image', 'Laplacian Gradient', 'SobelX', 'SobelY', 'Sobel Combined', 'Canny']
images = [img, lap, sobelX, sobelY, sobelCombined, canny]

for i in range(6):
    plt.subplot(2, 3, i+1), plt.imshow(images[i])
    plt.axis('off')
    plt.title(titles[i])

plt.show()
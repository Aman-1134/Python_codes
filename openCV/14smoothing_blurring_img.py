import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('D:\opencv-master\samples\data\opencv-logo.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# img1 = cv2.imread('D:\opencv-master\samples\data\Noise_salt_and_pepper.png')
# img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)

kernel = np.ones((5, 5), np.float64) / 25     # k =1/(k_width * k_height)

dst = cv2.filter2D(img, -1, kernel)
blur = cv2.blur(img, (5, 5))                    # cv2.boxFilter()
# It simply takes the average of all the pixels under kernel area and replaces the central element with
# this average

gblur = cv2.GaussianBlur(img, (5, 5), 0)        # removes the high frequency noise from image
mblur = cv2.medianBlur(img, 3)                  # great for salt and pepper noise in image
# computes the median of all the pixels under the kernel window and the central pixel is replaced with
# this median value
# ksize in median filter is always a odd number starting from 3
bfil = cv2.bilateralFilter(img, 9, 75, 75)      # effective in preserving edges
titles = ['Logo', '2D Convolution', 'Blurred', 'Gaussian Blur', 'Median Blur', 'Bilateral Filter']
images = [img, dst, blur, gblur, mblur, bfil]

for i in range(6):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.axis('off')

plt.show()
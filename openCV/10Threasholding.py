import cv2
import matplotlib.pyplot as plt

# Thresholding is the process of converting an image to binary image. Processes may differ but main
# concept is that a range is given in which if pixels value is less than given, it is completely blacked
# and that greater than the value, it is completely made white

img = cv2.imread('D:\opencv-master\samples\data\gradient.png')
_, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
_, th2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
_, th3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
_, th4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)      # pixel value < 127 = 0
_, th5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)
titles = ['Original Image', 'Binary', 'Binary Inv', 'Trunc', 'Tozero', 'Tozero Inv']
images = [img, th1, th2, th3, th4, th5]

for i in range(6):
    plt.subplot(2, 3, i+1), plt.imshow(images[i])
    plt.title(titles[i])
    plt.axis('off')

plt.show()


# cv2.imshow('Image', img)
# cv2.imshow('th1', th1)
# cv2.imshow('th2', th2)
# cv2.imshow('th3', th3)
# cv2.imshow('th4', th4)       # pixels upto 127 remains the same and then pixels of 127 is given beyond

# cv2.waitKey(0)
# cv2.destroyAllWindows()
import cv2
import numpy as np

img = cv2.imread('D:\opencv-master\samples\data\lena.jpg')
layer = img.copy()
# ------------------ Gaussian Pyramid --------------------- #
# lr1 = cv2.pyrDown(img)
# lr2 = cv2.pyrDown(lr1)
# lh1 = cv2.pyrUp(lr1)
# # print(np.shape(img))
# # print(np.shape(lr))
# cv2.imshow('Original Image', img)
# cv2.imshow('Pyramid Down1', lr1)
# cv2.imshow('Pyramid Down2', lr2)
# cv2.imshow('Pyramid Up1', lh1)

gp = [layer]

for i in range(5):
    layer = cv2.pyrDown(layer)
    gp.append(layer)
    # cv2.imshow(str(i), layer)
# ----------------------------------------------------------- #

# --------------------- Laplacian Pyramid ------------------- #
# Laplacian pyramid are useful to blend and reconstruct the images
# Output is similar to edge detection
layer = gp[4]
cv2.imshow('Upper Gaussian Pyramid', layer)
lp = [layer]

for i in range(4, 0, -1):
    gaussian_extended = cv2.pyrUp(gp[i])
    laplacian = cv2.subtract(gp[i-1], gaussian_extended)
    cv2.imshow(str(i), laplacian)
# ----------------------------------------------------------- #


cv2.waitKey(0)
cv2.destroyAllWindows()
# ---------------------- Steps to Blend Images ----------------- #
# 1.Load two images (eg. apple and orange)
# 2.Find Gaussian Pyramid of both images
# 3.From Gaussian Pyramid, find their Laplacian pyramid
# 4.Now join the left half of 1st image and right half of second image in each levels of Laplacian Pyramid
# 5.From this joint image pyramid, reconstruct the original image

import cv2
import numpy as np

apple = cv2.imread('D:\opencv-master\samples\data\\apple.jpg')
orange = cv2.imread('D:\opencv-master\samples\data\orange.jpg')
apple_orange = np.hstack((apple[:, :256], orange[:, 256:]))

# app = apple[0: 256]
# oran = orange[256: 512]
# apple_orange = np.vstack((app, oran))

# Generating Gaussian Pyramid for Apple
apple_copy = apple.copy()
gp_apple = [apple_copy]

for i in range(6):
    apple_copy = cv2.pyrDown(apple_copy)
    gp_apple.append(apple_copy)

# Grnerating Gaussian Pyramid for Orange
orange_copy = orange.copy()
gp_orange = [orange_copy]

for i in range(6):
    orange_copy = cv2.pyrDown(orange_copy)
    gp_orange.append(orange_copy)

# Generating Laplacian Pyramid for Apple
apple_copy = gp_apple[5]
lp_apple = [apple_copy]

for i in range(5, 0, -1):
    gaussian_extended = cv2.pyrUp(gp_apple[i])
    laplacian = cv2.subtract(gp_apple[i-1], gaussian_extended)
    lp_apple.append(laplacian)

# Generating Laplacian Pyramid for orange
orange_copy = gp_orange[5]
lp_orange = [orange_copy]

for i in range(5, 0, -1):
    gaussian_extended = cv2.pyrUp(gp_orange[i])
    laplacian = cv2.subtract(gp_orange[i-1], gaussian_extended)
    lp_orange.append(laplacian)

# Adding left half and right half of both images
apple_orange_pyramid = []
n = 0
for apple_lap, orange_lap in zip(lp_apple, lp_orange):
    n += 1
    cols, rows, ch = apple_lap.shape
    laplacian = np.hstack((apple_lap[:, 0:int(cols/2)], orange_lap[:, int(cols/2):]))
    apple_orange_pyramid.append(laplacian)

# Reconstructing Image
apple_orange_reconstruct = apple_orange_pyramid[0]
for i in range(1, 6):
    apple_orange_reconstruct = cv2.pyrUp(apple_orange_reconstruct)
    apple_orange_reconstruct = cv2.add(apple_orange_pyramid[i], apple_orange_reconstruct)

cv2.imshow('Apple', apple)
cv2.imshow('Orange', orange)
cv2.imshow('Blend', apple_orange)
cv2.imshow('apple_orange_reconstruct', apple_orange_reconstruct)

cv2.waitKey(0)
cv2.destroyAllWindows()
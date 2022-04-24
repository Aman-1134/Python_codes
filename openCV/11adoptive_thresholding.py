import cv2

img = cv2.imread('D:\opencv-master\samples\data\lena.jpg', 0)
img1 = cv2.imread('D:\opencv-master\samples\data\lena.jpg')
_, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_TRIANGLE)
th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 6)
th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 6)
mblur = cv2.medianBlur(th3, 3)             # removing salt and pepper noise in th3

cv2.imshow('Image', img1)
cv2.imshow('th1', th1)
cv2.imshow('th2', th2)
cv2.imshow('blur', mblur)
cv2.waitKey(0)
cv2.destroyAllWindows()



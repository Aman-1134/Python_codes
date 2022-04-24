import cv2

img = cv2.imread('D:\opencv-master\samples\data\opencv-logo.png')
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(imgray, 127, 255, 0)
contour, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

print('Number of contours = ', str(len(contour)))
cv2.drawContours(img, contour, -1, (0, 255, 0), 3)     # -1 shows all contours in img, to get a particilar contor, use indexes as 1, 2, 3 etc

cv2.imshow('Image', img)
cv2.imshow('Gray Image', imgray)

cv2.waitKey(0)
cv2.destroyAllWindows()
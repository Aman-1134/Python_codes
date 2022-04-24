import cv2
import numpy as np

img = cv2.imread('D:\opencv-master\samples\data\lena.jpg', 1)

# img = np.zeros((512, 512, 3))                    # creating an image using numpy
# img = cv2.line(img, (0, 0), (255, 255), (255, 0, 0), 2)
# cv2.line(name<variable> of image, starting point, end point, color, thickness)
# img = cv2.arrowedLine(img, (0, 255), (255, 255), (0, 255, 0), 2)

cv2.rectangle(img, (150, 150), (400, 400), (0, 255, 0), 2)
# cv2.rectangle(img, (150, 150), (400, 400), (0, 255, 0), -1)     # -1 fills whole rectangle with color provided
cv2.circle(img, (280, 280), 100, (0, 0, 255), 2)
font = cv2.FONT_ITALIC
cv2.putText(img, 'OpenCV', (150, 500), font, 2, (255, 255, 255), 4, cv2.LINE_AA)

cv2.imshow('Lena', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
import cv2 as cv
import numpy as np

# HSV = hue<color>, saturation<light to dark color>, value<brightness>
def nothing(x):
    pass

cap = cv.VideoCapture(0)
cv.namedWindow('Track')
cv.createTrackbar('LH', 'Track', 0, 255, nothing)
cv.createTrackbar('LS', 'Track', 0, 255, nothing)
cv.createTrackbar('LV', 'Track', 0, 255, nothing)
cv.createTrackbar('UH', 'Track', 255, 255, nothing)
cv.createTrackbar('US', 'Track', 255, 255, nothing)
cv.createTrackbar('UV', 'Track', 255, 255, nothing)

while (1):
    # frame = cv.imread('D:\opencv-master\samples\data\smarties.png')
    ret, frame = cap.read()

    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    l_h = cv.getTrackbarPos('LH', 'Track')
    l_s = cv.getTrackbarPos('LS', 'Track')
    l_v = cv.getTrackbarPos('LV', 'Track')

    u_h = cv.getTrackbarPos('UH', 'Track')
    u_s = cv.getTrackbarPos('US', 'Track')
    u_v = cv.getTrackbarPos('UV', 'Track')

    l_b = np.array([l_h, l_s, l_v])
    u_b = np.array([u_h, u_s, u_v])

    # l_b = np.array([100, 50, 50])
    # u_b = np.array([130, 255, 255])

    mask = cv.inRange(hsv, l_b, u_b)
    res = cv.bitwise_and(frame, frame, mask=mask)

    cv.imshow('frame', frame)
    cv.imshow('mask', mask)
    cv.imshow('res', res)
    k = cv.waitKey(1)
    if k == 27:
        break

cap.release()
cv.destroyAllWindows()
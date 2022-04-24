import numpy as np
import cv2

# events = [i for i in dir(cv2) if 'EVENT' in i]
# print(events)

def click_event(event, x, y, param, flags):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, ', ', y)

        font = cv2.FONT_ITALIC
        strXY = str(x) + ', ' + str(y)
        cv2.putText(img, strXY, (x, y), font, 0.5, (255, 255, 255), 1, cv2.LINE_AA)
        cv2.imshow('Image', img)

    if event == cv2.EVENT_RBUTTONDOWN:
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        font = cv2.FONT_ITALIC
        strBGR = str(blue) + ', ' + str(green) + ', ' + str(red)
        cv2.putText(img, strBGR, (x, y), font, 0.5, (0, 255, 255), 1, cv2.LINE_AA)
        cv2.imshow('Image', img)

    # if event == cv2.EVENT_LBUTTONDOWN:
    #     cv2.circle(img, (x, y), 3, (255, 255, 255), -1)
    #     point.append((x, y))
    #     if len(point) >= 2:
    #         cv2.line(img, point[-1], point[-2], (255, 255, 255), 1)
    #     cv2.imshow('Image', img)

    # if event == cv2.EVENT_LBUTTONDOWN:
    #     blue = img[y, x, 0]
    #     green = img[y, x, 1]
    #     red = img[y, x, 2]
    #     print(blue, ' ', green, ' ', red)
    #     cv2.circle(img, (x, y), 3, (0, 0, 255), -1)
    #     mycolorImage = np.ones((512, 512, 3))
    #     mycolorImage[:] = [blue, green, red]
    #     cv2.imshow('color', mycolorImage)

img = cv2.imread('D:\opencv-master\samples\data\messi5.jpg', 1)
cv2.imshow('Image', img)

point = []
cv2.setMouseCallback('Image', click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()
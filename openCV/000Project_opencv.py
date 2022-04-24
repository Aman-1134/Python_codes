import cv2
import numpy as np

def menu():
    print("List Of operations that can be done.")
    print("1.Get Coordinates of position of mouse")
    print("2.Detect Certain Color")

def click_event(event, x, y, param, flags):

    if event == cv2.EVENT_LBUTTONDOWN:
        print('Coordinates are::')
        print(x, ', ', y)

        text = str(x) + ', ' + str(y)
        cv2.putText(img, text, (x, y), cv2.FONT_HERSHEY_DUPLEX, 0.5, (255, 255, 255), 1)
        cv2.imshow('Image', img)

    if event == cv2.EVENT_RBUTTONDOWN:
        print('RGB color values are::')
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        print(str(red) + ', ' + str(green) + ', ' + str(blue))

        text = str(red) + ', ' + str(green) + ', ' + str(blue)
        cv2.putText(img, text, (x, y), cv2.FONT_ITALIC, 0.5, (255, 255, 0), 1)
        cv2.imshow('Image', img)

def nothing(x):
    pass


class Edit:
    def __init__(self, image):
        self.image = image

    def get_mouse_position_coordinates(self):
        print('Left click to get coordinate and right click to get rgb values')
        cv2.imshow('Image', self.image)
        cv2.setMouseCallback('Image', click_event)

    def detect(self):
        cv2.namedWindow('Track')
        cv2.createTrackbar('LH', 'Track', 0, 255, nothing)
        cv2.createTrackbar('LS', 'Track', 0, 255, nothing)
        cv2.createTrackbar('LV', 'Track', 0, 255, nothing)

        cv2.createTrackbar('UH', 'Track', 255, 255, nothing)
        cv2.createTrackbar('US', 'Track', 255, 255, nothing)
        cv2.createTrackbar('UV', 'Track', 255, 255, nothing)

        while (1):
            hsv = cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV)

            lh = cv2.getTrackbarPos('LH', 'Track')
            ls = cv2.getTrackbarPos('LS', 'Track')
            lv = cv2.getTrackbarPos('LV', 'Track')

            uh = cv2.getTrackbarPos('UH', 'Track')
            us = cv2.getTrackbarPos('US', 'Track')
            uv = cv2.getTrackbarPos('UV', 'Track')

            l_b = np.array([lh, ls, lv])
            u_b = np.array([uh, us, uv])

            mask = cv2.inRange(hsv, l_b, u_b)
            res = cv2.bitwise_and(self.image, self.image, mask)

            cv2.imshow('Result', res)


img = cv2.imread('D:\opencv-master\samples\data\messi5.jpg')
menu()

oper = int(input('Enter your operation::'))

if oper == 1:
    oper1 = Edit(img)
    oper1.get_mouse_position_coordinates()

if oper == 2:
    oper1 = Edit(img)
    oper1.detect()

cv2.waitKey(0)
cv2.destroyAllWindows()
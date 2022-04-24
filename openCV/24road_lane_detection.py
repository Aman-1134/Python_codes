import matplotlib.pyplot as plt
import numpy as np
import cv2

def region_of_interest(img, vertices):
    mask = np.zeros_like(img)                          # creates a array with all elements 0 of order same as image
    # channel_count = img.shape[2]                     # counts rgb channel ie 3
    # match_mask_color = (255,) * channel_count        # creates a tuple of 3 elements ie 255
    match_mask_color = 255                             # for gray scale image
    cv2.fillPoly(mask, vertices, match_mask_color)     # gives a black image with white portion inside vertices
    masked_image = cv2.bitwise_and(img, mask)          # to get an image within vertices only
    return masked_image

def draw_lines(img, lines):
    img = np.copy(img)
    blank_image = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)
    for line in lines:
        for x1, y1, x2, y2 in line:
            cv2.line(blank_image, (x1, y1), (x2, y2), (0, 255, 0), 3)

    img = cv2.addWeighted(img, 0.8, blank_image, 1, 0)
    return img

img = cv2.imread('D:\opencv-master\samples\data\\road.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

print(img.shape)           # (547, 978, 3)
height = img.shape[0]
width = img.shape[1]
region_of_interest_vertices = [
    (0, height),
    (width/2, height/2),
    (width, height)
]
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
canny_image = cv2.Canny(gray_image, 100, 200)
cropped_image = region_of_interest(canny_image, np.array([region_of_interest_vertices], np.int32))

lines = cv2.HoughLinesP(cropped_image, 6, np.pi/60, 160, lines=np.array([]), minLineLength=40,
                        maxLineGap=25)

img_with_lines = draw_lines(img, lines)

plt.imshow(img_with_lines)
plt.show()

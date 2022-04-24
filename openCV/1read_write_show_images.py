import cv2

img = cv2.imread('D:\opencv-master\samples\data\lena.jpg', 1)
# second opt is for flags, if flag = 1, color image is loaded, if 0, greyscale and
# color with alpha channel if -1
# print(img)               # prints the pixel value of image

cv2.imshow('Lena', img)     # image name and image to be shown
k = cv2.waitKey(0) & 0xFF         # if not used images is shown for very small time
                            # for 64 bit os, or in some case use mask

if k == 27:                            # if time = 0, image wont disappear until it is closed
    cv2.destroyAllWindows()            # to destroy window shown

elif k == ord('s'):
    cv2.imwrite('1Lena_copy.png', img)

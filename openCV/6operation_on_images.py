import cv2

img = cv2.imread('D:\opencv-master\samples\data\messi5.jpg')
img2 = cv2.imread('D:\opencv-master\samples\data\opencv-logo.png')

# print(img.shape)
# print(img.size)
# print(img.dtype)
# print(img.ndim)
b, g, r = cv2.split(img)                 # split colors
img = cv2.merge((g, r, b))               # mix colors and show again
ball = img[280:340, 330:390]             # roi<region of interest> is ball
img[273:333, 100:160] = ball             # copying ball to another location
# messi_face = img[80:135, 220:260]
# cv2.imwrite('messi_face.png', messi_face)
# ball = img[325:285, 400:334]
# img[180:140, 255:181] = ball
cv2.imshow('Messi', img)
# ________________ Resizing Images ___________________ #
img = cv2.resize(img, (512, 512))            # adding two images can occur only if both images have same size
img2 = cv2.resize(img2, (512, 512))          # so img and img2 are given sizes 512*512 each
dex = cv2.add(img, img2)
dex = cv2.addWeighted(img, 0.7, img2, 0.5, 0.1)   # adding with different opacity
cv2.imshow('Added Image', dex)
cv2.waitKey(0)
cv2.destroyAllWindows()
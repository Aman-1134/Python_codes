import cv2
import matplotlib.pyplot as plt

img = cv2.imread('D:\opencv-master\samples\data\lena.jpg')
cv2.imshow('OpenCV', img)

# b, g, r = cv2.split(img)
# img = cv2.merge((r, g, b))

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)         # opencv reads an image in BGR format and matplotlib in RGB
plt.axis('off')           # or use plt.xticks([]), plt.yticks([])f
plt.imshow(img)
plt.show()


cv2.waitKey(0)
cv2.destroyAllWindows()
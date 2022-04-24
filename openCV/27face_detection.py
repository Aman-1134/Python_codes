# Face detection is done by machine learning approach using Haar Feature Based Cascade Classifier
# Here the machine is trained by giving it many positive and negative examples
# Positive examples are those that contain the object we want to detect
# Negative images do not contain the object that is to be detected
# get pre trained xml files at https://github.com/opencv/opencv/tree/master/data/haarcascades

import cv2

face_cascade = cv2.CascadeClassifier('27haarcascade_frontalface_default.xml')
# eye_cascade = cv2.CascadeClassifier('27haarcascade_eye_tree_eyeglasses.xml')
# img = cv2.imread('D:\opencv-master\samples\data\messi5.jpg')
vid = cv2.VideoCapture(0)

# address = "http://192.168.1.64:8080/video"      # if connecting to smart phone via ip_webcam
# vid.open(address)

# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# out = cv2.VideoWriter('27Face_detect.avi', fourcc, 20.0, (640, 480))

while vid.isOpened():
    _, img = vid.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 255), 3)
        # roi_gray = gray[y:y+h, x:x+w]
        # roi_color = img[y:y+h, x:x+w]
        # eye = eye_cascade.detectMultiScale(roi_gray)
        #
        # for (ex, ey, ew, eh) in eye:
        #     cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 255), 3)

    # out.write(img)

    cv2.imshow('Image', img)
    if cv2.waitKey(1) == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()

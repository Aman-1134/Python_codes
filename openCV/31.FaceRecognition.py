import cv2
import face_recognition

i = 0

def encode_func(gray):
    encode = face_recognition.face_encodings(gray)
    print(encode)
    for i in range(7):
        if encodings[i] == 0:
            encodings[i] = encode  # gives the index of the current encoding
            break


cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()

    if ret == True:
        cv2.imshow('frame', frame)
        k = cv2.waitKey(1) & 0xFF

        if k == ord('q'):
            break

        elif k == ord('s'):
            encoding_image = cv2.imwrite('D:\\LOAD\\laod_pic' + str(i) + '.png', frame)
            i += 1
            encode_func(encoding_image)
            continue

    else:
        break

cap.release()
cv2.destroyAllWindows()


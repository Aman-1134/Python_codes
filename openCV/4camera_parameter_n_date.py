import cv2
import datetime

cap = cv2.VideoCapture(0)
print(cap.get(3))        # print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(4))        # print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

cap.set(3, 1000)
cap.set(4, 600)

print(cap.get(3))
print(cap.get(4))
while cap.isOpened():
    ret, frame = cap.read()

    if ret == True:
        font = cv2.FONT_ITALIC
        dt = str(datetime.datetime.now())
        text = 'Width:' + str(cap.get(3)) + ' ' + 'Height:' + str(cap.get(4))
        frame = cv2.putText(frame, dt, (100, 500), font, 0.5, (210, 155, 155),
                            1, cv2.LINE_AA)
        frame = cv2.putText(frame, text, (100, 50), font, 0.5, (20, 255, 0),
                            1, cv2.LINE_8)
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    else:
        break

cap.release()
cv2.destroyAllWindows()
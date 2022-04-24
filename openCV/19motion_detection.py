import cv2

vid = cv2.VideoCapture('D:\opencv-master\samples\data\\vtest.avi')

ret, frame1 = vid.read()
ret, frame2 = vid.read()

while vid.isOpened():
    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=3)
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2)

    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)
        if cv2.contourArea(contour) < 900:
            continue

        cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame1, 'Status: {}'.format('Movement'), (10, 50), cv2.FONT_HERSHEY_DUPLEX, 1,
                    (0, 0, 255), 2)

    cv2.imshow('Feed', frame1)
    cv2.imshow('Dilated', dilated)

    frame1 = frame2
    ret, frame2 = vid.read()

    if cv2.waitKey(40) == 27 or cv2.waitKey(40) == ord('q'):
            break


cv2.destroyAllWindows()
vid.release()
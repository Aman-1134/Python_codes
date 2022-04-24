import cv2

cap = cv2.VideoCapture(0)          # provide name and extension to view a video from file
# In case you want to capture video using an external device (camera) provide the device index
# In case 0 does not work, use -1, if more than one device is used try 1, 2, 3

# _________________________ Write Videos _____________________ #
fourcc = cv2.VideoWriter_fourcc(*'XVID')
# FOURCC is short for "four character code" - an identifier for a video codec,
# compression format, color or pixel format used in media files.

out = cv2.VideoWriter('2Output.avi', fourcc, 20.0, (640, 480))
# cv2.Videowriter(name of file, fourcc code, frames per s, size of frame)
# ______________________________________________________________ #

while cap.isOpened():          # can use while True: cap.isOpened returns true when the video file is opened
    # print(cap.isOpened())
    ret, frame = cap.read()
    # Ret will store true if frame is available else false. frame will store the frame captured

    if ret == True:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))   # to print height and width of frame
        # print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

        out.write(frame)                              # write in RGB format

        cv2.imshow('frame', frame)               # to show the frames(videos) in gray
        if cv2.waitKey(1) & 0xFF == ord('q'):    # exit process if q is pressed
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()

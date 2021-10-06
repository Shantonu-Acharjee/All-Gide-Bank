import numpy as np
import cv2
video_path = r'Video//1.mp4'

cap = cv2.VideoCapture(video_path)

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        image = cv2.resize(frame, (600,400))
        cv2.imshow('Video',image)

        if cv2.waitKey(25) & 0xff == ord('q'):
            break

    else: 
        break


cap.release()
cv2.destroyAllWindows()

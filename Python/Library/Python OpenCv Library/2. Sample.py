from re import T
import cv2
cap = cv2.VideoCapture(0)

print('Is Camera is Open : ', cap.isOpened())
while True:
    ret, frame = cap.read()


    FrameWidth = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    FrameHight = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

    print(f'Frame Width is : {FrameWidth} & Frame Hight is : {FrameHight}')


    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Frame', frame)
    cv2.imshow('Gray', gray)

    if cv2.waitKey(1) == ord('q'):
        break





cap.release()
cv2.destroyAllWindows()


# Video 43:00 minute done
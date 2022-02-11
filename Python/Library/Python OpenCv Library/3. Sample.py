from re import T
import cv2
cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('Video\Output.avi', fourcc, 20.0, (640, 480))

print('Is Camera is Open : ', cap.isOpened())
while True:
    ret, frame = cap.read()
    if ret == True:

        FrameWidth = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        FrameHight = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        print(f'Frame Width is : {FrameWidth} & Frame Hight is : {FrameHight}')

        out.write(frame)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('Frame', frame)
        cv2.imshow('Gray', gray)

        if cv2.waitKey(1) == ord('q'):
            break


    else:
        break



cap.release()
out.release()
cv2.destroyAllWindows()

# Vidoe 48:40 Minute Done



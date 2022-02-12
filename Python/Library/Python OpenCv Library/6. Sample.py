import cv2
import datetime
cap = cv2.VideoCapture(0)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))


cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1000)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1000)

while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        cv2.putText(frame, f'With : {cap.get(cv2.CAP_PROP_FRAME_WIDTH)} and Hight : {cap.get(cv2.CAP_PROP_FRAME_HEIGHT)}', (70, 50), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 3)
        cv2.putText(frame, f'Date Time : {str(datetime.datetime.now())}' , (0, 100), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 0), 3)
        





        cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


cap.release()
cv2.destroyAllWindows()









# Video 1:17:10 Done
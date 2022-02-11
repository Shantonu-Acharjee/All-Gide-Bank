import numpy as np
import cv2

img = cv2.imread('Photo\lena.jpg', -1)
img = cv2.line(img, (0, 0), (255, 255), (255, 0, 0), 3)
img = cv2.arrowedLine(img, (0, 100), (255, 355), (0, 255, 0), 3)
img = cv2.rectangle(img, (0, 300), (400, 400), (0, 0, 255), 3)
img = cv2.rectangle(img, (0, 0), (100, 100), (255, 0, 255), -1)
img = cv2.circle(img, (450, 450), 30, (255, 255, 0), 3)
img = cv2.putText(img, 'Shantonu', (10, 500), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 3)

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Video 1:02:46 Minute Done
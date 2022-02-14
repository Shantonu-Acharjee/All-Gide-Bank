import re
import numpy as np
import cv2


img = cv2.imread('Photo\lena.jpg')


def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:

        blue = img[x, y, 0]
        green = img[x, y, 1]
        red = img[x, y, 2]

        # img[:] = [red, green, blue]
        cv2.circle(img, (x, y), 10, (int(blue), int(green), int(red)), -1)
        cv2.imshow('Image', img)

    

    '''elif event == cv2.EVENT_RBUTTONDOWN:
        img[:] = cv2.imread('Photo\lena.jpg')
        cv2.imshow('Image', img)
'''



cv2.imshow('Image', img)
cv2.setMouseCallback('Image', click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Video 1:46:0 minute done
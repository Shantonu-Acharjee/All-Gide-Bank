import cv2
# print(cv2.__version__)

img = cv2.imread('Photo\lena.jpg', -1)
cv2.imshow('Image', img)
k = cv2.waitKey(0) & 0xFF

if k == ord('q'):
    cv2.destroyAllWindows()

cv2.imwrite('Photo\lena_copy.png', img)
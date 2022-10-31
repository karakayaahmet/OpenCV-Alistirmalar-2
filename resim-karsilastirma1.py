import cv2
import numpy as np

img1 = cv2.imread("aircraft.jpg")
img1 = cv2.resize(img1, (640,480))

img2 = cv2.imread("aircraft.jpg")
img2 = cv2.resize(img2, (640,480))

if img1.shape == img2.shape:
    print("same size")

else:
    print("not same")

cv2.imshow("img", img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
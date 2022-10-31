import cv2
import numpy as np

img = cv2.imread("starwars.jpg")
img2 = cv2.imread("starwars2.jpg")

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

w,h = gray_img2.shape[::-1]

result = cv2.matchTemplate(gray_img, gray_img2, cv2.TM_CCOEFF_NORMED)
location = np.where(result >= 0.7)

for point in zip(*location[::-1]):
    cv2.rectangle(img, point, (point[0]+w,point[1]+h), (255,0,0), 2)

cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
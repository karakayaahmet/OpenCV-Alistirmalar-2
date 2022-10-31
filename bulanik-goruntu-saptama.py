import cv2

img = cv2.imread("starwars.jpg")

blur_img = cv2.medianBlur(img, 5)

laplacian = cv2.Laplacian(img, cv2.CV_64F).var()

laplacian1 = cv2.Laplacian(blur_img, cv2.CV_64F).var()

if laplacian1 < laplacian:
    print("blurry image")

else:
    print("not blurry image")


cv2.imshow("img", img)
cv2.imshow("blur", blur_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
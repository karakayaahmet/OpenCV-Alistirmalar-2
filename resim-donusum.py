import cv2

def nothing(x):
    pass

img1 = cv2.imread("aircraft.jpg")
img1 = cv2.resize(img1, (640,480))

img2 = cv2.imread("balls.jpg")
img2 = cv2.resize(img2, (640,480))

output = cv2.addWeighted(img1, 0.5, img2, 0.5, 0)
name = "Transition"
cv2.namedWindow(name)

cv2.createTrackbar("alfa-beta", name, 0, 1000, nothing)

while True:
    cv2.imshow(name, output)
    alfa = cv2.getTrackbarPos("alfa-beta", name)/1000
    beta = 1-alfa

    output = cv2.addWeighted(img1, alfa, img2, beta, 0)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


cv2.destroyAllWindows()
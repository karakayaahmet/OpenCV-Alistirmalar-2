import cv2

name = "Webcam"
cv2.namedWindow(name)

cap = cv2.VideoCapture(0)
print("width: ", str(cap.get(3)))
print("height: ", str(cap.get(4)))

cap.set(3, 1280)
cap.set(4, 720)

print("width* : ", str(cap.get(3)))
print("height* : ", str(cap.get(4)))

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)

    if ret is False:
        break

    cv2.imshow(name, frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
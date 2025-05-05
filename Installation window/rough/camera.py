import cv2

capture = cv2.VideoCapture(0)
while True:
    ret, frame = capture.read()
    if frame is not None:
        cv2.imshow('Camera', frame)
    quit = cv2.waitKey(1)
    if (quit == ord("Q") or quit == ord("q")):
        break
cv2.destroyAllWindows()

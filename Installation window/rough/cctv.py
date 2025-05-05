import cv2
url = 'http://10.63.22.187:8080/video'
#url = 'http://100.103.22.16:8080/video'
capture = cv2.VideoCapture(url)
while True:
    ret, frame = capture.read()
    if frame is not None:
        cv2.imshow('CCTV Footage', frame)
    quit = cv2.waitKey(1)
    if (quit == ord("Q") or quit == ord("q")):
        break
cv2.destroyAllWindows()

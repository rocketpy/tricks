import cv2


capture = cv2.VideoCapture(0)

if not video_capture.isOpened():
    raise Exception("Not open")

ret, frame = capture.read()

capture.release()



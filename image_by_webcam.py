import cv2


# by first cam
img = cv2.VideoCapture(0)
ret, frame = img.read()
cv2.imwrite('file_name.jpg', frame)  # or .png
img.release()

# by second cam , if two cams
img_sec = cv2.VideoCapture(1)
ret, frame = img_sec.read()
cv2.imwrite('file_name.jpg', frame)  # or .png
img_sec.release()

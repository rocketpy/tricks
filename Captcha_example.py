import cv2
import pytesseract
from PIL import Image
from pdf2image import convert_from_path, convert_from_bytes


# image = Image.open('captcha.jpg')  # using PIL
image = cv2.imread('captcha.jpg')  # using cv2

"""
path = ("https://captcha_url")
file = open('captcha.jpg', 'wb')
file.write(urllib.urlopen(path).read())
file.close()
"""

# image = convert_from_path('/home/belval/example.pdf')  # using pdf2image
# image = convert_from_bytes(open('/home/belval/example.pdf', 'rb').read())

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
# gray = cv2.medianBlur(gray, 3)

filename = "{}.png".format("file_name")
cv2.imwrite(filename, gray)
text = pytesseract.image_to_string(Image.open('file_name.png'))

print(text)

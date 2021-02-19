import cv2
import pytesseract
from PIL import Image
from pdf2image import convert_from_path


#img = Image.open('captcha.jpg')
image = cv2.imread('captcha.jpg')

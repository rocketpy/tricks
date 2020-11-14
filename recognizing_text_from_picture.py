import pytesseract
from PIL import Image


#  Download tesseract on Windows:  https://tesseract-ocr.github.io/tessdoc/4.0-with-LSTM
#  DOCS: https://pypi.org/project/pytesseract/
#  Config options:  https://help.ubuntu.ru/wiki/tesseract
#  Dictionaries: https://github.com/tesseract-ocr/tessdata

img = Image.open("file_name.png")  #  .jpg

# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # for Windows need use !!!

file_name = img.filename  # take name of file
file_name = file_name.split(".")[0]

# custom_config = r'--oem 3 --psm 13'
custom_config = r'--oem 3 --psm 6'

result = pytesseract.image_to_string(img, lang='rus', config=custom_config)  # lang='eng'
# print(result)

with open(f'{file_name}.txt', 'w') as text_file:  # save result to text file
    text_file.write(result)

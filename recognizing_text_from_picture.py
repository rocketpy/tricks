import pytesseract
from PIL import Image


#  DOCS: https://pypi.org/project/pytesseract/

img = Image.open("file_name.png")  #  .jpg

# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

file_name = img.filename
file_name = file_name.split(".")[0]

# custom_config = r'--oem 3 --psm 13'
custom_config = r'--oem 3 --psm 6'

result = pytesseract.image_to_string(img, lang='rus', config=custom_config)
print(result)

with open(f'{file_name}.txt', 'w') as text_file:
    text_file.write(result)

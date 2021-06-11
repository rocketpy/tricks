#  Convert JPEG to PNG and Save to other directory.
import Image


im = Image.open('/current/directory/file_name.jpg')
im.save('/other/directory/file_name.png')

# or
from glob import glob                                                           
import cv2 


pngs = glob('./*.png')

for i in pngs:
    img = cv2.imread(i)
    cv2.imwrite(i[:-3] + 'jpg', img)


# or
from PIL import Image


im = Image.open('file_name.jpg')
im.save('file_name.png')


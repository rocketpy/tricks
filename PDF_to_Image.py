#  convert PDF to a PIL Image object

# PyPi:  https://pypi.org/project/pdf2image/

# pip install pdf2image

from pdf2image import convert_from_path, convert_from_bytes
from pdf2image.exceptions import (PDFInfoNotInstalledError,
                                  PDFPageCountError,
                                  PDFSyntaxError
                                 )

images = convert_from_path('/home/belval/example.pdf')
# OR
images = convert_from_bytes(open('/home/belval/example.pdf', 'rb').read())

# OR better yet
import tempfile


with tempfile.TemporaryDirectory() as path:
    images_from_path = convert_from_path('/home/belval/example.pdf', output_folder=path)
    # Do something here


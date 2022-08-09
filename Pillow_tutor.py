# Install

# Windows:
# python -m venv venv
# .\venv\Scripts\activate
# (venv) PS> python -m pip install Pillow

# Linux+macOS:
# $ python -m venv venv
# $ source venv/bin/activate
# (venv) $ python -m pip install Pillow


# Working with image
from PIL import Image

img_name = "file_name.jpg"
with Image.open(img_name) as img:
    img.load()

# useful methods:

# img.show()
# type(img)
# img.format
# img.size
# img.mode
# isinstance(img, Image.Image)

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


# crop and resize image
cropped_img = img.crop((250, 100, 500, 900))
# cropped_img.size
# cropped_img.show()

low_res_img = cropped_img.resize((cropped_img.width // 4, cropped_img.height // 4))
low_res_img.show()
# or
# low_res_img = cropped_img.reduce(4)

# method thumbnail() changes the image object but does not return a new object !!!

# method save():
cropped_img.save("cropped_image.jpg")
low_res_img.save("low_resolution_cropped_image.png")

# Rotate Image
converted_img = img.transpose(Image.FLIP_TOP_BOTTOM)
converted_img.show()

# image.FLIP_LEFT_RIGHT
# image.ROTATE_90
# image.TRANSPOSE
# image.TRANSVERSE

rotated_img = img.rotate(45)
rotated_img.show()

rotated_img = img.rotate(45, expand=True)
rotated_img.show()


# Gradations and modes

filename = "file_name.jpg"
with Image.open(filename) as img:
    img.load()

cmyk_img = img.convert("CMYK")
gray_img = img.convert("L")  # Grayscale

cmyk_img.show()
gray_img.show()

img.getbands()
# ('R', 'G', 'B')

cmyk_img.getbands()
# ('C', 'M', 'Y', 'K')

gray_img.getbands()
# ('L',)


# To create three new images
zeroed_band = red.point(lambda _: 0)

red_merge = Image.merge(
    "RGB", (red, zeroed_band, zeroed_band))

green_merge = Image.merge(
    "RGB", (zeroed_band, green, zeroed_band))

blue_merge = Image.merge(
    "RGB", (zeroed_band, zeroed_band, blue))

# red_merge.show()
# green_merge.show()
# blue_merge.show()


# Creating a common image from several
from PIL import Image


def common_image(*images, vertical=False):
    width, height = images[0].width, images[0].height
    size = (
        (width, height * len(images))
        if vertical
        else (width * len(images), height))
    new_img = Image.new(images[0].mode, size)
    row, col = 0, 0
    for image in images:
        new_img.paste(image, (row, col))
        if vertical:
            col += height
        else:
            row += width

    return new_img

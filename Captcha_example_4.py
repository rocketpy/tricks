from PIL import Image


image = Image.open("file_name")
cropped_image = image.crop((left, upper, right, lower))

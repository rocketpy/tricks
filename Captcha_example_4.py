from PIL import Image


image = Image.open("file_name")
cropped_image = image.crop((left, upper, right, lower))

#  cropped image from image source
image = Image.open("captcha.png").convert("L") # Grayscale conversion
cropped_image = image.crop((0, 0, 25, 35))
cropped_image.save("cropped_image.png")

# remove from captcha some black lines
pixel_matrix = cropped_image.load()
for col in range(0, cropped_image.height):
    for row in range(0, cropped_image.width):
        if pixel_matrix[row, col] != 0:
            pixel_matrix[row, col] = 255
image.save("thresholded_image.png")

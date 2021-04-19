from PIL import Image


# open an some image
pic = Image.open("img_name.jpg")
print(pic.size)


# get a smaller image
x, y = pic.size
x //= 10
y //= 10
smaller = pic.resize((x, y))
print(smaller)

#  border detection
from PIL import ImageFilter

edges = smaller.filter(ImageFilter.FIND_EDGES)
print(edges)

# sharp lines
bands = edges.split()
bands[0]

# inverting the colors
outline = bands[0].point(lambda x: 255 if x<100 else 0)
print(outline)

# crop image
outline.crop((10, 200, 300, 400))

# save image to file
outline.save("file_name.pdf")


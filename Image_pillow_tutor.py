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




# pip install Pillow

import os
from PIL import Image


# print the file size
def get_size_format(b, factor=1024, suffix="B"):
    for unit in ["", "K", "M", "G", "T", "P", "E", "Z"]:
        if b < factor:
            return f"{b:.2f}{unit}{suffix}"
        b /= factor
    return f"{b:.2f}Y{suffix}"

# main function for compressing images
def compress_img(image_name, new_size_ratio=0.9, quality=90, width=None, height=None, to_jpg=True):
    img = Image.open(image_name)
    print("[*] Image shape:", img.size)
    image_size = os.path.getsize(image_name)
    print("[*] Size before compression:", get_size_format(image_size))
    if new_size_ratio < 1.0:
        img = img.resize((int(img.size[0] * new_size_ratio), int(img.size[1] * new_size_ratio)), Image.ANTIALIAS)
        print("[+] New Image shape:", img.size)
    elif width and height:
        img = img.resize((width, height), Image.ANTIALIAS)
        print("[+] New Image shape:", img.size)
    filename, ext = os.path.splitext(image_name)
    if to_jpg:
        new_filename = f"{filename}_compressed.jpg"
    else:
        new_filename = f"{filename}_compressed{ext}"
    try:
        img.save(new_filename, quality=quality, optimize=True)
    except OSError:
        img = img.convert("RGB")
        img.save(new_filename, quality=quality, optimize=True)
    print("[+] New file saved:", new_filename)
    new_image_size = os.path.getsize(new_filename)
    print("[+] Size after compression:", get_size_format(new_image_size))
    saving_diff = new_image_size - image_size
    print(f"[+] Image size change: {saving_diff/image_size*100:.2f}% of the original image size.")

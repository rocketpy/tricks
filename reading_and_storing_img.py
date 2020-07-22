from PIL import Image
import csv
#  reading from disk 

#  read a single image and its meta from a .png and .csv file
def read_single_disk(image_id):
    img = np.array(Image.open(disk_dir / f"{image_id}.png"))
    with open(disk_dir / f"{image_id}.csv", "r") as csvfile:
        reader = csv.reader(csvfile, delimiter=" ", quotechar="|", quoting=csv.QUOTE_MINIMAL)
        label = int(next(reader)[0])
    return img, label


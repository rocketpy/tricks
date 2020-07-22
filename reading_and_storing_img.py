from PIL import Image
import csv

#  reading from disk 
#  read a single image and meta from a .png and .csv file
def read_single_image(image_id):
    img = np.array(Image.open(disk_dir / f"{image_id}.png"))
    with open(disk_dir / f"{image_id}.csv", "r") as csvfile:
        reader = csv.reader(csvfile, delimiter=" ", quotechar="|", quoting=csv.QUOTE_MINIMAL)
        label = int(next(reader)[0])
    return img, label


#  storing to disk
from PIL import Image
import csv


def store_single_image(image, image_id, label):
    Image.fromarray(image).save(disk_dir / f"{image_id}.png")
    with open(disk_dir / f"{image_id}.csv", "wt") as csvfile:
        writer = csv.writer(csvfile, delimiter=" ", quotechar="|", quoting=csv.QUOTE_MINIMAL)
        writer.writerow([label])

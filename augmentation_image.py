#  Albumentations is a fast and flexible image augmentation library.

#  Docs:  https://albumentations.ai/docs/
#  Github:  https://github.com/albumentations-team/albumentations

#  pip install -U albumentations

#  simple example
import cv2
import albumentations as A


transform = A.Compose([A.RandomCrop(width=256, height=256),
                       A.HorizontalFlip(p=0.5),
                       A.RandomBrightnessContrast(p=0.2),
                      ])

# Read an image with OpenCV and convert it to the RGB colorspace
image = cv2.imread("image.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Augment an image
transformed = transform(image=image)
transformed_image = transformed["image"]

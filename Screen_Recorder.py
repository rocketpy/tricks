import cv2
import datetime
import numpy as np
from PIL import ImageGrab
from win32api import GetSystemMetrics


width = GetSystemMetrics(0)
height = GetSystemMetrics(1)

time_stamp = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
file_name = f'{time_stamp}.mp4'

four_c = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')

captured_video = cv2.VideoWriter(file_name, four_c, 20.0, (width, height))

webcam = cv2.VideoCapture(1)


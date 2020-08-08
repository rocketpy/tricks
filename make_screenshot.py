#  docs: https://pypi.org/project/PyAutoGUI/
#  pip install pyautogui

import pyautogui


img = pyautogui.screenshot()
img.save('my_img.png')
# or
img_2 = pyautogui.screenshot('my_img_2.png')

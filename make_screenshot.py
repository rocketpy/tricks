#  docs: https://pypi.org/project/PyAutoGUI/
#  pip install pyautogui

import pyautogui


img = pyautogui.screenshot()
img.save('my_img.png')
# or
img_2 = pyautogui.screenshot('my_img_2.png')


#  for locate where an image is on the screen
button7location = pyautogui.locateOnScreen('button.png') # returns (left, top, width, height) of matching region
#  button7location  #(1416, 562, 50, 41)
buttonx, buttony = pyautogui.center(button7location)
#  buttonx, buttony  # (1441, 582)
pyautogui.click(buttonx, buttony)

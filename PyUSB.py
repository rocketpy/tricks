#  Python USB access module

# PyPi:https://pypi.org/project/pyusb/
# Github - Tutorial: https://github.com/pyusb/pyusb/blob/master/docs/tutorial.rst

# pip install pyusb

import usb.core


dev = usb.core.find()

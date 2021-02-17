#  Python USB access module

# PyPi:https://pypi.org/project/pyusb/
# Github - Tutorial: https://github.com/pyusb/pyusb/blob/master/docs/tutorial.rst

# pip install pyusb

"""
Where are you?

The find() function in the core module is used to find and enumerate devices connected to the system. 

import usb.core

dev = usb.core.find(idVendor=0xfffe, idProduct=0x0001)
if dev is None:
    raise ValueError('Our device is not connected')
"""

import usb.core
import usb.util


dev = usb.core.find()

# find our device
dev = usb.core.find(idVendor=0xfffe, idProduct=0x0001)

# was it found?
if dev is None:
    raise ValueError('Device not found')

# set the active configuration. With no arguments, the first
# configuration will be the active one
dev.set_configuration()

# get an endpoint instance
cfg = dev.get_active_configuration()
intf = cfg[(0,0)]

ep = usb.util.find_descriptor(
    intf,
    # match the first OUT endpoint
    custom_match = \
    lambda e: \
        usb.util.endpoint_direction(e.bEndpointAddress) == \
        usb.util.ENDPOINT_OUT)

assert ep is not None

# write the data
ep.write('test')


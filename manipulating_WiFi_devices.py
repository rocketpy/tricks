# pywifi - A cross-platform module for manipulating WiFi devices.

# https://pypi.org/project/pywifi/
# https://github.com/awkman/pywifi

# pip install pywifi


import pywifi

wifi = pywifi.PyWiFi()
iface = wifi.interfaces()[0]
iface.disconnect()
time.sleep(1)
assert iface.status() in\
    [const.IFACE_DISCONNECTED, const.IFACE_INACTIVE]

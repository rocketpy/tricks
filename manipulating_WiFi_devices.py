# pywifi - A cross-platform module for manipulating WiFi devices.

# https://pypi.org/project/pywifi/
# https://github.com/awkman/pywifi

# pip install pywifi


# Example:

import pywifi

profile = pywifi.Profile()
profile.ssid = 'testap'
profile.auth = const.AUTH_ALG_OPEN
profile.akm.append(const.AKM_TYPE_WPA2PSK)
profile.cipher = const.CIPHER_TYPE_CCMP
profile.key = '12345678'

wifi = pywifi.PyWiFi()
iface = wifi.interfaces()[0]
profile = iface.add_network_profile(profile)
iface.connect(profile)


import pywifi

wifi = pywifi.PyWiFi()
iface = wifi.interfaces()[0]
iface.disconnect()
time.sleep(1)
assert iface.status() in\
    [const.IFACE_DISCONNECTED, const.IFACE_INACTIVE]

profile = pywifi.Profile()
profile.ssid = 'testap'
profile.auth = const.AUTH_ALG_OPEN
profile.akm.append(const.AKM_TYPE_WPA2PSK)
profile.cipher = const.CIPHER_TYPE_CCMP
profile.key = '12345678'

iface.remove_all_network_profiles()
tmp_profile = iface.add_network_profile(profile)

iface.connect(tmp_profile)
time.sleep(30)
assert iface.status() == const.IFACE_CONNECTED

iface.disconnect()
time.sleep(1)
assert iface.status() in\
[const.IFACE_DISCONNECTED, const.IFACE_INACTIVE]

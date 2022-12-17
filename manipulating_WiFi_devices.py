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

profile = pywifi.Profile()
profile.ssid = 'testap'
profile.auth = const.AUTH_ALG_OPEN
profile.akm.append(const.AKM_TYPE_WPA2PSK)
profile.cipher = const.CIPHER_TYPE_CCMP
profile.key = '12345678'

iface.remove_all_network_profiles()
tmp_profile = iface.add_network_profile(profile)
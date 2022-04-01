# uPnP client library for Python 3.

# https://github.com/flyte/upnpclient
# pip install upnpclient


import upnpclient

devices = upnpclient.discover()
print(devices)

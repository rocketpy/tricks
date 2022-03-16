# get the users ip address
import socket
import urllib

print(socket.gethostbyname(socket.gethostname()))
response = urllib.urlopen('http://api.hostip.info/get_html.php?   ip=xxx&position=true').read()
print(response)

# update
ip = socket.gethostbyname(socket.gethostname())
url = "http://api.hostip.info/get_html.php?ip=" + ip + "&position=true"
url = "http://api.hostip.info/get_html.php?ip=%s&position=true" % ip
url = "http://api.hostip.info/get_html.php?ip=xxx&position=true".replace("xxx", ip)
url = "http://api.hostip.info/get_html.php?ip={}&position=true".format(ip)


# or 
from geoip import geolite2

match = geolite2.lookup('10.10.10.10')
print('Country: '+ match.country)
print('timezone: '+ match.timezone)


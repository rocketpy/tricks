# get the users ip address
import socket
import urllib

print(socket.gethostbyname(socket.gethostname()))
response = urllib.urlopen('http://api.hostip.info/get_html.php?   ip=xxx&position=true').read()
print(response)


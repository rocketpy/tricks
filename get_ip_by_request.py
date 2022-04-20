# Get location with IP address
import requests

response = requests.get("https://geolocation-db.com/json/29.100.135.73&position=true").json()

  
# by curl
# $ curl 'https://api.ipify.org?format=json'


# get local ip
hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)

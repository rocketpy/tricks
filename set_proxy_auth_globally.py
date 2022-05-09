import re
import urllib2
import requests
from requests.auth import HTTPProxyAuth

s = requests.Session()

proxies = {"http": "http://121.132.195.201:8000",
           "https": "https://134.171.191.202:8000"}

auth = HTTPProxyAuth("...", "...")

s.proxies = proxies

# set auth params globally
s.auth = auth
ext_ip = s.get('http://checkip.dyndns.org')

# print(ext_ip.text)


#  Apply proxy with auth using http.client for API

# If use urlib2 or requests
# HTTPS_PROXY = https://user:pass@host:port


# or
import requests


proxies = {'http':  f"http://username:pwd@webproxy.subdomain.website.com:8080", 
           'https': f"https://username:pwd@webproxy.subdomain.website.com:8080"}

url = 'https://api...'
params = 'mkt=' + 'en-US' + '&q=' + urllib.parse.quote (query)
headers = {'Key': subscriptionKey}
session = requests.Session()
session.proxies = proxies
req = session.get(url, params=params, headers=headers)


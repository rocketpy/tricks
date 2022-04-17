import re
import urllib2
import requests
from requests.auth import HTTPProxyAuth

s = requests.Session()

proxies = {"http": "http://121.132.195.201:8000",
           "https": "https://134.171.191.202:8000"}

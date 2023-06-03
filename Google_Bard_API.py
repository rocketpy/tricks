# Google Bard API

# https://github.com/dsdanielpark/Bard-API
# https://pypi.org/project/bardapi/
# pip install bardapi

# development version from Github:
# pip install git+https://github.com/dsdanielpark/Bard-API.git

# Simple Usage
from bardapi import Bard

token = 'xxxxxxxxxx'
bard = Bard(token=token)
bard.get_answer(".....")['content']


# Or use this
from bardapi import Bard
import os

os.environ['_BARD_API_KEY']="xxxxxxxx"
Bard().get_answer(".....")['content']


# To get reponse dictionary
import bardapi
import os

# set your __Secure-1PSID value to key
token = 'xxxxxxxxxx'


# Behind a proxy
from bardapi import Bard
import os

# Change 'http://proxy.example.com:8080' to your http proxy
# timeout in seconds
proxies = {
    'http': 'http://proxy.example.com:8080',
    'https': 'https://proxy.example.com:8080'
}

bard = Bard(token='xxxxxxxxxx', proxies=proxies, timeout=30)
bard.get_answer("....")['content']


# Reusable session object
import os
import requests
from bardapi import Bard

os.environ['_BARD_API_KEY'] = 'xxxxxxxxxxx'
# token='xxxxxxxxxxx'

session = requests.Session()
session.headers = {
            "Host": "bard.google.com",
            "X-Same-Domain": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
            "Origin": "https://bard.google.com",
            "Referer": "https://bard.google.com/",
        }
session.cookies.set("__Secure-1PSID", os.getenv("_BARD_API_KEY")) 
# session.cookies.set("__Secure-1PSID", token) 

bard = Bard(token=token, session=session, timeout=30)
bard.get_answer(".....")['content']

# Continued conversation without set new session
bard.get_answer("What is my last prompt??")['content']


# installation required
# pip install git+https://github.com/dsdanielpark/Bard-API.git

# Multi-language Bard API
# GitHub Dev version only.

from bardapi import Bard

bard = Bard(token='xxxxxxxx', language='chinese (simplified)')
res = bard.get_answer("你好。")
print(res['content'])

# or

from bardapi import Bard
import os

os.environ["_BARD_API_LANG"] = 'chinese (simplified)'
os.environ["_BARD_API_KEY"] = 'xxxxxxxx'

res = Bard().get_answer("你好。")
print(res['content'])


# Get image links
# GitHub Dev version only.
from bardapi import Bard

bard = Bard(token='xxxxxxxxxxx')
res = bard.get_answer("Find me an image of the main entrance of Stanford University.")
res['links'] # Get image links (list)
res['images'] # Get images (set)


# ChatBard
from bardapi import ChatBard
    
chat = ChatBard()
chat.start()

# or
from bardapi import ChatBard
import os

os.environ["_BARD_API_KEY"] = 'xxxxxx'   # Requird
os.environ["_BARD_API_LANG"] = Arabic    # Optional, Default to English
os.environ["_BARD_API_TIMEOUT"] = 30     # Optional, Session Timeout
 
chat = ChatBard()
chat.start()

# or
from bardapi import Bard, SESSION_HEADERS
import os
import requests

token='xxxxxxxxxxx'
session = requests.Session()
session.headers = SESSION_HEADERS
session.cookies.set("__Secure-1PSID", token) 
proxies = {
    'http': 'http://proxy.example.com:8080',
    'https': 'https://proxy.example.com:8080'
}
    
ChatBard(token=token, session=session, proxies=proxies, timeout=40, language="chinese (simplified)").start()


# Executing Python code received as a response from Bard
# GitHub Dev version only!!!
from bardapi import Bard
    
bard = Bard(token="xxxxxxxxx", run_code=True)
bard.get_answer("code a pie chart in python for this data={'blue':25, 'red':30, 'green':30, 'purple':15}")


# Using Bard asynchronously
# GitHub Dev version only!!!
from bardapi import BardAsync 
    
bard = BardAsync(token="xxxxxxxxx")
await bard.get_answer("What is ...?")


# Bard which can get Cookies
# GitHub Dev version only.
from bardapi import BardCookies

cookie_dict = {
    "__Secure-1PSID": "xxxxxxxxx",
    "__Secure-1PSIDTS": "xxxxxxxxx",
    # Any cookie values you want to pass session object.
}

bard = BardCookies(cookie_dict=cookie_dict)

print(bard.get_answer("....."))

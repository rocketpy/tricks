# Google Bard API

# https://github.com/dsdanielpark/Bard-API
# pip install bardapi

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


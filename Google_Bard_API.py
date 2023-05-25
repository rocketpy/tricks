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

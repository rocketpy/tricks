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

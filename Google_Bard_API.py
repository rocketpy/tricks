# Google Bard API

# https://github.com/dsdanielpark/Bard-API
# pip install bardapi

# Simple Usage
from bardapi import Bard

token = 'xxxxxxxxxx'
bard = Bard(token=token)
bard.get_answer(".....")['content']

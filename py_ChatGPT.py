# pyChatGPT - An unofficial Python wrapper for OpenAI's ChatGPT API

# https://pypi.org/project/pyChatGPT/
# https://github.com/terry3041/pyChatGPT

# https://github.com/acheong08/ChatGPT - official API
# Get API key from https://platform.openai.com/account/api-keys
# python -m pip install --upgrade revChatGPT

# Basic example
from revChatGPT.V3 import Chatbot

chatbot = Chatbot(api_key="<api_key>")
chatbot.ask("Hello world")

# pip install pyChatGPT

"""
Features:
 Cloudflare's anti-bot protection bypass using undetected_chromedriver
 OpenAI / Google / Microsoft login support (experimental)
 Captcha solvers support (2Captcha, PyPasser)
 Headless machines support
 Proxy support (only without basic auth)
"""

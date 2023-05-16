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

# Interactive mode
# python3 -m pyChatGPT

from pyChatGPT import ChatGPT

session_token = 'abc123'  # `__Secure-next-auth.session-token` cookie from https://chat.openai.com/chat
api = ChatGPT(session_token)  # auth with session token
api = ChatGPT(session_token, conversation_id='some-random-uuid')  # specify conversation id
api = ChatGPT(session_token, proxy='https://proxy.example.com:8080')  # specify proxy
api = ChatGPT(session_token, chrome_args=['--window-size=1920,768'])  # specify chrome args
api = ChatGPT(session_token, moderation=False)  # disable moderation
api = ChatGPT(session_token, verbose=True)  # verbose mode (print debug messages)

# auth with google login
api = ChatGPT(auth_type='google', email='example@gmail.com', password='password')

# auth with microsoft login
api = ChatGPT(auth_type='microsoft', email='example@gmail.com', password='password')

# auth with openai login (captcha solving using speech-to-text engine)
api = ChatGPT(auth_type='openai', email='example@gmail.com', password='password')

# auth with openai login (manual captcha solving)
api = ChatGPT(auth_type='openai', captcha_solver=None, 
              email='example@gmail.com', password='password')

# auth with openai login (2captcha for captcha solving)
api = ChatGPT(auth_type='openai', captcha_solver='2captcha', solver_apikey='abc', 
              email='example@gmail.com', password='password')

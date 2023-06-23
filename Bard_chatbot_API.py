# Google's Bard chatbot API

# https://github.com/acheong08/Bard

# Authentication
# Go to https://bard.google.com/

# pip3 install --upgrade GoogleBard


# Usage
"""
$ python3 -m Bard -h
usage: Bard.py [-h] --session SESSION
options:
  -h, --help         show this help message and exit
  --session SESSION  __Secure-1PSID cookie.
"""

# Quick mode
# $ export BARD_QUICK="true"
# $ export BARD_SESSION="<__Secure-1PSID>"
# $ python3 -m Bard

# Example bash shortcut:
# USAGE1: bard QUESTION
# USAGE2: echo "QUESTION" | bard
bard () {
	export BARD_QUICK=true
	export BARD_SESSION=<REDACTED>.
	python3 -m Bard "${@:-$(</dev/stdin)}" | tail -n+7
}


# Developer Documentation
from os import environ
from Bard import Chatbot

token = environ.get("BARD_TOKEN")

chatbot = Chatbot(token)

chatbot.ask("Hello, how are you?")

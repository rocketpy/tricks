#  Arsenic - Asynchronous WebDriver client

# PyPi - https://pypi.org/project/arsenic/21.8/
# Github - https://github.com/HDE/arsenic
# Docs - https://arsenic.readthedocs.io/en/latest/

# pip install arsenic==21.8

# VeryImportant
"""
Warning !!!

While this library is asynchronous, web drivers are not. You must call the APIs in sequence.
The purpose of this library is to allow you to control multiple web drivers asynchronously or
to use a web driver in the same thread as an asynchronous web server.
"""

#  Quickstart

# To run a local Firefox instance.

from arsenic import get_session
from arsenic.browsers import Firefox
from arsenic.services import Geckodriver


async def example():
    # Runs geckodriver and starts a firefox session
    async with get_session(Geckodriver(), Firefox()) as session:
        # go to example.com
        await session.get('http://example.com')
        # wait up to 5 seconds to get the h1 element from the page
        h1 = await session.wait_for_element(5, 'h1')
        # print the text of the h1 element
        print(await h1.get_text())


#  Creating a virtual env

# create a virtual env to install arsenic:
# python3.6 -m venv env

# env/bin/pip install --upgrade pip

# install arsenic:

# env/bin/pip install --pre arsenic

# create a file named cats.py and insert the following code:

import asyncio
import sys

from arsenic import get_session, keys, browsers, services


if sys.platform.startswith('win'):
    GECKODRIVER = './geckodriver.exe'
else:
    GECKODRIVER = './geckodriver'


async def hello_world():
    service = services.Geckodriver(binary=GECKODRIVER)
    browser = browsers.Firefox()
    async with get_session(service, browser) as session:
        await session.get('https://images.google.com/')
        search_box = await session.wait_for_element(5, 'input[name=q]')
        await search_box.send_keys('Cats')
        await search_box.send_keys(keys.ENTER)
        await asyncio.sleep(10)


def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(hello_world())


if __name__ == '__main__':
    main()

# Save it and in the terminal, run python cats.py


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


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

# urllib3 - urllib3 is a powerful, user-friendly HTTP client for Python.

# Installing
# urllib3 can be installed with pip

# python -m pip install urllib3

# from GitHub:

# git clone git://github.com/urllib3/urllib3.git
# pip install .


# easy to use:
import urllib3

http = urllib3.PoolManager()
r = http.request('GET', 'http://httpbin.org/robots.txt')
r.status
r.data

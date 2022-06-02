# urllib3 - urllib3 is a powerful, user-friendly HTTP client for Python.


# easy to use:
import urllib3

http = urllib3.PoolManager()
r = http.request('GET', 'http://httpbin.org/robots.txt')
r.status
r.data

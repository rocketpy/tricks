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
print(r.status)
print(r.data)


# Response Content
# The HTTPResponse object provides status, data, and headers attributes:
import urllib3

# Making the request (The request function returns HTTPResponse object)
resp = urllib3.request("GET", "https://httpbin.org/ip")

print(resp.status)
# 200

print(resp.data)
# b"{\n  "origin": "104.232.115.37"\n}\n"

print(resp.headers)
# HTTPHeaderDict({"Content-Length": "32", ...})


# JSON Content
# JSON content can be loaded by json() method of the response:

resp = urllib3.request("GET", "https://httpbin.org/ip")

print(resp.json())
# {"origin": "127.0.0.1"}


# Alternatively, Custom JSON libraries such as orjson can be used to encode data,
# retrieve data by decoding and deserializing the data attribute of the request:
import orjson
import urllib3

encoded_data = orjson.dumps({"attribute": "value"})
resp = urllib3.request(method="POST", url="http://httpbin.org/post", body=encoded_data)

print(orjson.loads(resp.data)["json"])
# {'attribute': 'value'}


# Binary Content
# The data attribute of the response is always set to a byte string representing the response content:
import urllib3

resp = urllib3.request("GET", "https://httpbin.org/bytes/8")

print(resp.data)
# b"\xaa\xa5H?\x95\xe9\x9b\x11"


# Using io Wrappers with Response Content
import io
import urllib3

resp = urllib3.request("GET", "https://example.com", preload_content=False)
resp.auto_close = False

for line in io.TextIOWrapper(resp):
    print(line)


# Request Data
# Headers

import urllib3

resp = urllib3.request(
    "GET",
    "https://httpbin.org/headers",
    headers={
        "X-Something": "value"
    }
)

print(resp.json()["headers"])
# {"X-Something": "value", ...}


# Or you can use the HTTPHeaderDict class to create multi-valued HTTP headers:
import urllib3

# Create an HTTPHeaderDict and add headers
headers = urllib3.HTTPHeaderDict()
headers.add("Accept", "application/json")
headers.add("Accept", "text/plain")

# Make the request using the headers
resp = urllib3.request(
    "GET",
    "https://httpbin.org/headers",
    headers=headers
)

print(resp.json()["headers"])
# {"Accept": "application/json, text/plain", ...}


# Cookies:
# Cookies are specified using the Cookie header with a string containing the ; delimited key-value pairs:
import urllib3

resp = urllib3.request(
    "GET",
    "https://httpbin.org/cookies",
    headers={
        "Cookie": "session=f3efe9db; id=30"
    }
)

print(resp.json())
# {"cookies": {"id": "30", "session": "f3efe9db"}}


# Query Parameters:
# For GET, HEAD, and DELETE requests, you can simply pass the arguments as a dictionary in the fields argument to request():
import urllib3

resp = urllib3.request("GET",
                       "https://httpbin.org/get",
                       fields={"arg": "value"})

print(resp.json()["args"])
# {"arg": "value"}



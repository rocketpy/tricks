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



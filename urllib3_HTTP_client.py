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
# http = urllib3.PoolManager(num_pools=50)
# or
http = urllib3.PoolManager(maxsize=10)
# Alternatively
pool = urllib3.HTTPConnectionPool("google.com", maxsize=10)
# or
http = urllib3.PoolManager(maxsize=10, block=True)

# Alternatively
pool = urllib3.HTTPConnectionPool("google.com", maxsize=10, block=True)

r = http.request('GET', 'http://httpbin.org/robots.txt')
print(r.status)
print(r.data)


# Proxies
# use ProxyManager to tunnel requests through an HTTP proxy:

import urllib3

proxy = urllib3.ProxyManager("https://localhost:3128/")
proxy.request("GET", "https://google.com/")
"""
The usage of ProxyManager is the same as PoolManager.
You can connect to a proxy using HTTP, HTTPS or SOCKS.
urllib3’s behavior will be different depending on the type of proxy you selected and the destination you’re contacting.
"""

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


# For POST and PUT requests, you need to manually encode query parameters in the URL:
from urllib.parse import urlencode
import urllib3

# Encode the args into url grammar.
encoded_args = urlencode({"arg": "value"})

# Create a URL with args encoded.
url = "https://httpbin.org/post?" + encoded_args
resp = urllib3.request("POST", url)

print(resp.json()["args"])
# {"arg": "value"}


# Form Data
# For PUT and POST requests, urllib3 will automatically form-encode the dictionary in the fields argument provided to request():
import urllib3

resp = urllib3.request(
    "POST",
    "https://httpbin.org/post",
    fields={"field": "value"}
)

print(resp.json()["form"])
# {"field": "value"}


# JSON
"""
You can send a JSON request by specifying the data as json argument,
urllib3 automatically encodes data using json module with UTF-8 encoding.
Also by default "Content-Type" in headers is set to "application/json" if not specified when calling request():
"""
import urllib3

data = {"attribute": "value"}
resp = urllib3.request(
    "POST",
    "https://httpbin.org/post",
    body=data,
    headers={"Content-Type": "application/json"}
)

print(resp.json())
# {"attribute": "value"}


# Files & Binary Data
"""
For uploading files using multipart/form-data encoding you can use the same approach as Form Data and
specify the file field as a tuple of (file_name, file_data):
"""
import urllib3

# Reading the text file from local storage.
with open("example.txt") as fp:
    file_data = fp.read()

# Sending the request.
resp = urllib3.request(
    "POST",
    "https://httpbin.org/post",
    fields={
       "filefield": ("example.txt", file_data),
    }
)

print(resp.json()["files"])
# {"filefield": "..."}

"""
While specifying the filename is not strictly required, it’s recommended in order to match browser behavior.
You can also pass a third item in the tuple to specify the file’s MIME type explicitly:
"""
resp = urllib3.request(
    "POST",
    "https://httpbin.org/post",
    fields={
        "filefield": ("example.txt", file_data, "text/plain"),
    }
)


# For sending raw binary data simply specify the body argument. It’s also recommended to set the Content-Type header:
import urllib3

with open("/home/samad/example.jpg", "rb") as fp:
    binary_data = fp.read()

resp = urllib3.request(
    "POST",
    "https://httpbin.org/post",
    body=binary_data,
    headers={"Content-Type": "image/jpeg"}
)

print(resp.json()["data"])


# Certificate Verification

# python -m pip install certifi

# using the secure extra:
# python -m pip install urllib3[secure]

# Once you have certificates, you can create a PoolManager that verifies certificates when making requests:

import certifi
import urllib3

http = urllib3.PoolManager(
    cert_reqs="CERT_REQUIRED",
    ca_certs=certifi.where()
)


# The PoolManager will automatically handle certificate verification and will raise SSLError if verification fails:
import certifi
import urllib3

http = urllib3.PoolManager(
    cert_reqs="CERT_REQUIRED",
    ca_certs=certifi.where()
)

http.request("GET", "https://httpbin.org/")
# (No exception)
http.request("GET", "https://expired.badssl.com")


# Using Timeouts:
"""
Timeouts allow you to control how long (in seconds) requests are allowed to run before being aborted.
In simple cases, you can specify a timeout as a float to request():
"""
import urllib3

resp = urllib3.request(
    "GET",
    "https://httpbin.org/delay/3",
    timeout=4.0
)

print(type(resp))
# <class "urllib3.response.HTTPResponse">

# This request will take more time to process than timeout.
urllib3.request(
    "GET",
    "https://httpbin.org/delay/3",
    timeout=2.5
)
# MaxRetryError caused by ReadTimeoutError


# For more granular control you can use a Timeout instance which lets you specify separate connect and read timeouts:
import urllib3

resp = urllib3.request(
    "GET",
    "https://httpbin.org/delay/3",
    timeout=urllib3.Timeout(connect=1.0)
)

print(type(resp))
# <urllib3.response.HTTPResponse>

urllib3.request(
    "GET",
    "https://httpbin.org/delay/3",
    timeout=urllib3.Timeout(connect=1.0, read=2.0)
)
# MaxRetryError caused by ReadTimeoutError


# If you want all requests to be subject to the same timeout, you can specify the timeout at the PoolManager level:
import urllib3

http = urllib3.PoolManager(timeout=3.0)

http = urllib3.PoolManager(
    timeout=urllib3.Timeout(connect=1.0, read=2.0)
)


#  Retrying Requests

# To change the number of retries just specify an integer:
import urllib3

urllib3.request("GET", "https://httpbin.org/ip", retries=10)


# To disable all retry and redirect logic specify retries=False:
import urllib3

urllib3.request(
    "GET",
    "https://nxdomain.example.com",
    retries=False
)
# NewConnectionError

resp = urllib3.request(
    "GET",
    "https://httpbin.org/redirect/1",
    retries=False
)

print(resp.status)
# 302


# To disable redirects but keep the retrying logic, specify redirect=False:
resp = urllib3.request(
    "GET",
    "https://httpbin.org/redirect/1",
    redirect=False
)

print(resp.status)
# 302


# For more granular control you can use a Retry instance. This class allows you far greater control of how requests are retried.
# For example, to do a total of 3 retries, but limit to only 2 redirects:

urllib3.request(
    "GET",
    "https://httpbin.org/redirect/3",
    retries=urllib3.Retry(3, redirect=2)
)
# MaxRetryError


# disable exceptions for too many redirects and just return the 302 response:
resp = urllib3.request(
    "GET",
    "https://httpbin.org/redirect/3",
    retries=urllib3.Retry(
        redirect=2,
        raise_on_redirect=False
    )
)
print(resp.status)
# 302


# all requests to be subject to the same retry policy, you can specify the retry at the PoolManager level:
import urllib3

http = urllib3.PoolManager(retries=False)

http = urllib3.PoolManager(
    retries=urllib3.Retry(5, redirect=2)
)


# Errors & Exceptions

# urllib3 wraps lower-level exceptions, for example:

import urllib3

try:
    urllib3.request("GET","https://nx.example.com", retries=False)

except urllib3.exceptions.NewConnectionError:
    print("Connection failed.")
# Connection failed.


# Logging

# If you are using the standard library logging module urllib3 will emit several logs.
# In some cases this can be undesirable. You can use the standard logger interface to change the log level for urllib3’s logger:

logging.getLogger("urllib3").setLevel(logging.WARNING)


# If you’re receiving the ProxyError and it mentions your proxy only speaks HTTP and not HTTPS here’s what to do to solve your issue:
# If you’re using urllib3 directly, make sure the URL you’re passing into urllib3.
# ProxyManager starts with http:// instead of https://:

# Do this:
http = urllib3.ProxyManager("http://...")

# Not this:
http = urllib3.ProxyManager("https://...")


# Ensure that the values for all of these environment variables starts with http:// and not https://:
# Check your existing environment variables in bash

$ env | grep "_PROXY"
HTTP_PROXY=http://127.0.0.1:8888
HTTPS_PROXY=https://127.0.0.1:8888  # <--- This setting is the problem!

# Make the fix in your current session and test your script
$ export HTTPS_PROXY="http://127.0.0.1:8888"
$ python test-proxy.py  # This should now pass.

# Persist your change in your shell 'profile' (~/.bashrc, ~/.profile, ~/.bash_profile, etc)
# You may need to logout and log back in to ensure this works across all programs.
$ vim ~/.bashrc


# If you’re on Windows or macOS your proxy may be getting set at a system level.
# To check this first ensure that the above environment variables aren’t set then run the following:

$ python -c 'import urllib.request; print(urllib.request.getproxies())'

# If the output of the above command isn’t empty and looks like this:

{
  "http": "http://127.0.0.1:8888",
  "https": "https://127.0.0.1:8888"  # <--- This setting is the problem!
}

# Search how to configure proxies on your operating system and change the https://... URL into http://.
# After you make the change the return value of urllib.request.getproxies() should be:

{  # Everything is good here! :)
  "http": "http://127.0.0.1:8888",
  "https": "http://127.0.0.1:8888"
}


# SOCKS Proxies

# For SOCKS, you can use SOCKSProxyManager to connect to SOCKS4 or SOCKS5 proxies.
# In order to use SOCKS proxies you will need to install PySocks or install urllib3 with the socks extra:

python -m pip install urllib3[socks]

# Once PySocks is installed, you can use SOCKSProxyManager:
from urllib3.contrib.socks import SOCKSProxyManager

proxy = SOCKSProxyManager("socks5h://localhost:8889/")
proxy.request("GET", "https://google.com/")



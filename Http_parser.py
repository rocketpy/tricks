# http request/response parser

# PyPI: https://pypi.org/project/http-parser/
# Github: https://github.com/benoitc/http-parser/

# pip install http-parser

import socket

from http_parser.http import HttpStream
from http_parser.reader import SocketReader


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect(('gunicorn.org', 80))
        s.send("GET / HTTP/1.1\r\nHost: gunicorn.org\r\n\r\n")
        r = SocketReader(s)
        p = HttpStream(r)
        print p.headers()
        print p.body_file().read()
    finally:
        s.close()

if __name__ == "__main__":
    main()

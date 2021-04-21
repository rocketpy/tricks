# PyJWT - JSON Web Token implementation in Python

# Github - https://github.com/jpadilla/pyjwt
# pip install PyJWT

import jwt


encoded = jwt.encode({"some": "payload"}, "secret", algorithm="HS256")
print(encoded)

#  Decoding a payload on the server
jwt.decode(encoded, 'secret', algorithms=['HS256'])
# {'some': 'payload'}

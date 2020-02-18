import os
os.urandom(12)
# '\xf0?a\x9a\\\xff\xd4;\x0c\xcbHi'

import uuid
uuid.uuid4().hex
# '3d6f45a5fc12445dbac2f59c3b6c7cb1'

import secrets
secrets.token_urlsafe(16)
# 'Drmhze6EPcv0fN_81Bj-nA'

import os
os.urandom(12).hex()
# 'f3cfe9ed8fae309f02079dbf'

#  Set secret key in Flask
#Method 1:
app.secret_key = 'the random string'

Method 2: Use app.config:
app.config['SECRET_KEY'] = 'the random string' 

Method 3: Put it in your config file:
SECRET_KEY = 'the random string'

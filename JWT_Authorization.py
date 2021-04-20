#  All code here:  https://steelkiwi.com/blog/jwt-authorization-python-part-1-practise/

#  create a wrapper for aiohttp.web.Response
import json
from aiohttp import web


def json_response(body='', **kwargs):
    kwargs['body'] = json.dumps(body or kwargs['body']).encode('utf-8')
    kwargs['content_type'] = 'text/json'
    return web.Response(**kwargs)


#  get and create users in the memory
from models import User

User.objects.create(email='user@email.com', password='password')  


#  create a handler to allow the client to login
from datetime import datetime, timedelta
import jwt

JWT_SECRET = 'secret'
JWT_ALGORITHM = 'HS256'
JWT_EXP_DELTA_SECONDS = 20

async def login(request):
    post_data = await request.post()

    try:
        user = User.objects.get(email=post_data['email'])
        user.match_password(post_data['password'])
    except (User.DoesNotExist, User.PasswordDoesNotMatch):
        return json_response({'message': 'Wrong credentials'}, status=400)

    payload = {
        'user_id': user.id,
        'exp': datetime.utcnow() + timedelta(seconds=JWT_EXP_DELTA_SECONDS)
    }
    jwt_token = jwt.encode(payload, JWT_SECRET, JWT_ALGORITHM)
    return json_response({'token': jwt_token.decode('utf-8')})

app = web.Application()
app.router.add_route('POST', '/login', login)

  

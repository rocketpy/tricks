# python-facebook-api - A simple Python wrapper around the Facebook Graph API
# Now we can use base class GraphApi to get data.

# Github: https://github.com/sns-sdks/python-facebook

# pip install python-facebook-api

#  Usage:

# GraphAPI
# We can use GraphApi class to communicate with Facebook Graph Api.
# We can initial GraphApi with three different methods.

# if already have an access token:
from pyfacebook import GraphAPI

api = GraphAPI(access_token="token")


# use app credentials to generate app token:
from pyfacebook import GraphAPI

api = GraphAPI(app_id="id", app_secret="secret", application_only_auth=True)


#  to perform an authorization process to a user:

from pyfacebook import GraphAPI

api = GraphAPI(app_id="id", app_secret="secret", oauth_flow=True)
api.get_authorization_url()
# ('https://www.facebook.com/dialog/oauth?response_type=code&client_id=id&redirect_uri=https%3A%2F%2Flocalhost%2F&scope=public_profile&state=PyFacebook',
# 'PyFacebook')
# let user to do oauth at the browser opened by link.
# then get the response url

api.exchange_user_access_token(response="url redirected")
# Now the api will get the user access token.


# Get object data:
api.get_object(object_id="20531316728")
# {'name': 'Facebook App', 'id': '20531316728'}


# Initial methods same with GraphAPI.
# Get user data:
fb.user.get_info(user_id="413140042878187")
# User(id='413140042878187', name='Kun Liu')

# Get page data:
fb.page.get_info(page_id="20531316728")
Page(id='20531316728', name='Facebook App')




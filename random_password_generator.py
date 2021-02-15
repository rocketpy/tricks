import string
import random


#  size: default=8
#  chars: default=A-Za-z0-9 


def password_generator(size=8, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for i in range(size))
 

import string
import random


#  size: default=8
#  chars: default=A-Za-z0-9 


def password_generator(size=8, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for i in range(size))
 

    
"""
import string
import random


def password_generator():
    lower_case_letter = random.choice(string.ascii_lowercase)
    upper_case_letter = random.choice(string.ascii_uppercase)
    number = random.choice(string.digits)
    other_characters = [random.choice(string.ascii_letters + string.digits)
                       for index in range(random.randint(3, 17))
                       ]

"""
    
    

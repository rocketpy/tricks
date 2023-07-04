# Python version of Google's common library for parsing, formatting, storing and validating international phone numbers.

# https://pypi.org/project/phonenumbers/
# https://github.com/daviddrysdale/python-phonenumbers

# pip install phonenumbers


import phonenumbers
from phonenumbers import geocoder, carrier

ph = phonenumbers.parse('+.......')

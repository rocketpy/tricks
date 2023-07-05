# Python version of Google's common library for parsing, formatting, storing and validating international phone numbers.

# https://pypi.org/project/phonenumbers/
# https://github.com/daviddrysdale/python-phonenumbers

# pip install phonenumbers


import phonenumbers
from phonenumbers import geocoder, carrier

ph = phonenumbers.parse('+.......')

# x = phonenumbers.parse("+442083661177", None)

# Country Code: 44 National Number: 2083661177 Leading Zero: False
# type(x)

y = phonenumbers.parse("020 8366 1177", "GB")

# Country Code: 44 National Number: 2083661177 Leading Zero: False
# x == y
# True

z = phonenumbers.parse("00 1 650 253 2222", "GB")  # as dialled from GB, not a GB number

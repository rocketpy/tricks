# Phone Gen - International phone number generation, for generating test data.

# https://pypi.org/project/phone-gen/

# pip install phone-gen


from phone_gen import PhoneNumber

phone_number = PhoneNumber("GB")  # ISO 3166-2
# or
phone_number = PhoneNumber("GBR")  # ISO 3166-3
# or
phone_number = PhoneNumber("Great Britain")  # Country name

# Get a phone number
number = phone_number.get_number()
# +442908124840

# Get a country code
country_code = phone_number.get_code()
# 44

# Get a phone number without a country code
number = phone_number.get_number(full=False)
# 183782623

# Get a mobile phone number
number = phone_number.get_mobile()
# +447911899521

# Get a national phone number
number = phone_number.get_national()
# +442408055065


# PYTEST FIXTURE
import pytest
from phone_gen import PhoneNumber


@pytest.fixture
def phone_number():
    def wrap(code):
        return PhoneNumber(code).get_number()
    yield wrap

def test_one(phone_number):
    number = phone_number("DE")


"""
Using the CLI
usage: phone-gen [-h] [-v] [-n] country [country ...]

International phone number generation

positional arguments:
  country         Country code or country name. Example: "GB" or "GBR" or "Great Britain"

optional arguments:
  -h, --help      show this help message and exit
  -v, --version   show program's version number and exit
  -f, --not-full  Get a phone number without a country code
  -m, --mobile    Get mobile phone number
  -n, --national  Get national phone number
"""

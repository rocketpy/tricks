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
z = phonenumbers.parse("+120012301", None)
phonenumbers.is_possible_number(z)  # too few digits for USA
phonenumbers.is_valid_number(z)
z = phonenumbers.parse("+12001230101", None)
# phonenumbers.is_possible_number(z)
# phonenumbers.is_valid_number(z)  # NPA 200 not used

z = phonenumbers.parse("02081234567", None)  # no region, no + => unparseable

phonenumbers.format_number(x, phonenumbers.PhoneNumberFormat.NATIONAL)
phonenumbers.format_number(x, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
phonenumbers.format_number(x, phonenumbers.PhoneNumberFormat.E164)

# The AsYouTypeFormatter object allows this.
formatter = phonenumbers.AsYouTypeFormatter("US")
formatter.input_digit("6")
formatter.input_digit("5")

# Each of these match objects holds a PhoneNumber object together with information about where the match occurred in the original string.
text = "Call me at 510-748-8230 if it's before 9:30, or on 703-4800500 after 10am."
for match in phonenumbers.PhoneNumberMatcher(text, "US"):
    print(match)

# PhoneNumberMatch [11,23) 510-748-8230
# PhoneNumberMatch [51,62) 703-4800500

# get some information about the location that corresponds to a phone number
geocoder.area_description_for_number()


from phonenumbers import geocoder

ch_number = phonenumbers.parse("0431234567", "CH")
geocoder.description_for_number(ch_number, "de")
geocoder.description_for_number(ch_number, "en")
# 'Zurich'


from phonenumbers import carrier

ro_number = phonenumbers.parse("+40721234567", "RO")
carrier.name_for_number(ro_number, "en")


from phonenumbers import timezone

gb_number = phonenumbers.parse("+447986123456", "GB")
timezone.time_zones_for_number(gb_number)

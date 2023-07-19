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

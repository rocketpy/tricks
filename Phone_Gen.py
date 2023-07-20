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

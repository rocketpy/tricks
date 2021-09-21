# Mimesis: fake data generator.

# PyPi: https://pypi.org/project/mimesis/
# Github: https://github.com/lk-geimfari/mimesis

# pip install mimesis


# Usage

# This library is really easy to use and everything you need is just import an object,
# which represents a type of data you need (we call such object a Provider).

# In the example below we import provider Person, which represents data related to personal information, such as name, surname, email and etc:

from mimesis import Person
from mimesis.locales import Locale


person = Person(Locale.EN)

person.full_name()
# 'Brande Sears'

person.email(domains=['example.com'])
# 'roccelline1878@example.com'

person.email(domains=['mimesis.name'], unique=True)
# 'f272a05d39ec46fdac5be4ac7be45f3f@mimesis.name'

person.telephone(mask='1-4##-8##-5##3')
# '1-436-896-5213'


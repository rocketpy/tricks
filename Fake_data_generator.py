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


# Locales

# Mimesis currently includes support for 34 different locales. You can specify a locale when creating providers and
# they will return data that is appropriate for the language or country associated with that locale.

from mimesis import Person
from mimesis.enums import Gender


de = Person('de')
en = Person('en')

de.full_name(gender=Gender.FEMALE)
# 'Sabrina Gutermuth'

en.full_name(gender=Gender.MALE)
# 'Layne Gallagher'


"""
# Generating structured data

# You can generate dictionaries which can be easily converted to any the format you want (JSON/XML/YAML etc.) with any structure you want.

from flask import Flask, jsonify, request
from mimesis.schema import Field, Schema
from mimesis.enums import Gender


app = Flask(__name__)


@app.route('/apps', methods=('GET',))
def apps_view():
    locale = request.args.get('locale', default='en', type=str)
    count = request.args.get('count', default=1, type=int)

    _ = Field(locale)

    schema = Schema(schema=lambda: {
        'id': _('uuid'),
        'name': _('text.word'),
        'version': _('version', pre_release=True),
        'timestamp': _('timestamp', posix=False),
        'owner': {
            'email': _('person.email', domains=['test.com'], key=str.lower),
            'token': _('token_hex'),
            'creator': _('full_name', gender=Gender.FEMALE)},
    })
    data = schema.create(iterations=count)
    return jsonify(data)


"""




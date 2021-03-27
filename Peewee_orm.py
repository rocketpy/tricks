#  Peewee - a little orm

# PyPi: https://pypi.org/project/peewee/
# Docs: http://docs.peewee-orm.com/en/latest/peewee/quickstart.html#quickstart

# pip install peewee

from peewee import *


# Set database
db = SqliteDatabase('customers.db')  # 'db/database.db'

class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    username = CharField(unique=True)

class Tweet(BaseModel):
    user = ForeignKeyField(User, backref='tweets')
    message = TextField()
    created_date = DateTimeField(default=datetime.datetime.now)
    is_published = BooleanField(default=True)
  
  
# Connect to the database and create tables

db.connect()
db.create_tables([User, Tweet])

db.commit()
db.close()


# Create a few rows

charlie = User.create(username='charlie')
huey = User(username='huey')
huey.save()

# No need to set `is_published` or `created_date` since they
# will just use the default values we specified.
Tweet.create(user=charlie, message='My first tweet')

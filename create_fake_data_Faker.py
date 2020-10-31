#  Docs:  https://faker.readthedocs.io/en/latest/index.html
#  Using the Faker Class :  https://faker.readthedocs.io/en/latest/fakerclass.html

#  pip install Faker

from faker import Faker


fake = Faker()

fake.name()
# 'Lucy Cechtelar'

fake.address()
# '426 Jordy Lodge
#  Cartwrightshire, SC 88120-6700'

fake.text()
#  Aut molestias et maxime. Fugit autem facilis quos vero. Eius quibusdam possimus est.
#  Ea quaerat et quisquam. Deleniti sunt quam. Adipisci consequatur id in occaecati.
#  Et sint et. Ut ducimus quod nemo ab voluptatum.'

# Celery is  Distributed Task Queue !
# pip install celery

# https://docs.celeryproject.org/en/latest/getting-started/first-steps-with-celery.html  - First Steps with Celery
# https://docs.celeryproject.org/en/latest/getting-started/next-steps.html  -  Next Steps

#  Simple example ( ... taked from https://pypi.org/project/celery/ )
from celery import Celery

app = Celery('hello', broker='amqp://guest@localhost//')

@app.task
def hello():
    return 'hello world'
  

#  Useful celery config.
"""
app = Celery('tasks',
             broker='redis://localhost:6379',
             backend='redis://localhost:6379')

app.conf.update(
    CELERY_TASK_RESULT_EXPIRES=3600,
    CELERY_QUEUES=(
        Queue('default', routing_key='tasks.#'),
        Queue('hipri', routing_key='tasks.#'),
    ),
    CELERY_ROUTES={
        'tasks.tasks.add': {'queue': 'hipri'},
    }
)

"""
celery -A tasks worker --loglevel=info  # run the worker

celery worker --help  # list command-line options available

celery multi start w1 -A proj -l info  # start one or more workers in the background

celery multi restart w1 -A proj -l info  # restart workers

celery multi stop w1 -A proj -l info  # stop workers aynchronously

celery multi stopwait w1 -A proj -l info  # stop after executing tasks are completed

celery multi start w1 -A proj -l info --pidfile=/var/run/celery/%n.pid --logfile=/var/log/celery/%n%I.log  # create pid and log files in the current directory

celery -A proj inspect active  # control and inspect workers at runtime
celery -A proj inspect active --destination=celery@w1.computer

celery -A proj inspect scheduled # list scheduled ETA tasks.

celery -A proj control cancel_consumer  # Force all worker to cancel consuming from a queue
celery -A proj control cancel_consumer foo -d worker1.local  # Force an specified worker to cancel consuming from a queue

celery -A proj inspect active_queues  # Get a list of queues that workers consume
celery -A proj inspect active_queues -d celery@worker1  # Get a list of queues that a worker consumes

celery -A proj inspect stats  # show worker statistics.

celery shell -I  # Drop into IPython console.

celery -A tasks result -t tasks.add dbc53a54-bd97-4d72-908c-937827009736  # See the result of a task.

# Control workers
i = app.control.inspect()
i = app.control.inspect(['worker1.example.com', 'worker2.example.com'])
i.registered()  // Show registred tasks for specified workers
i.active()  // Get a list of active tasks
i.scheduled  // Get a list of tasks waiting to be scheduled
i.reserved() # Get a list of tasks that has been received, but are still waiting to be executed

app.control.broadcast('shutdown')  # shutdown all workers
app.control.broadcast('shutdown', destination=['celer@worker'])

app.control.ping()
app.control.ping(['celer@worker'])

# Inspecting queues in Redis
redis-cli -h HOST -p PORT -n DATABASE_NUMBER llen QUEUE_NAME
LRANGE queue_name 0 10  # Redis client

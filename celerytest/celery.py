from __future__ import absolute_import, unicode_literals
import os

from celery import Celery, states
from celery.exceptions import Ignore
from django.conf import settings
from .paramiko_lib import paramiko_remoteshell

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celerytest.settings')

app = Celery('celerytest')
app.conf.enable_utc = False
app.conf.update(timezone='America/New_York')
app.config_from_object('django.conf:settings', namespace='CELERY')

#celery beat settings
app.conf.beat_schedule = {

}

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')

@app.task
def print_hello(a, b):
    print('Hello from function' + a+ b )

@app.task(bind=True)
def run_remotescript(self, host, script):
    # paramiko_remoteshell('skytech-ubuntu', './test.sh')
    ret = paramiko_remoteshell(host , script)
    # raise Exception("Sorry, no numbers below zero")
    # self.update_state(state=states.FAILURE, meta={'info': ex})
    return ret


@app.task
def add(x, y):
    z = x + y
    print(z)
from __future__ import absolute_import, unicode_literals
import os
import django
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')  # Settings for your own project
django.setup()

app = Celery('server')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
app.conf.broker_connection_retry_on_startup = True

app.conf.beat_schedule = {
    'every-60-seconds': {
        'task': 'todo.tasks.send_email_task',
        'schedule': 60.0,
    }
}
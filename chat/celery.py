import os
from celery import Celery

from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chat.settings')

app = Celery('chat')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


# do a task at a given time interval
app.conf.beat_schedule = {
    'send-messaga': {
        'task': 'main.tasks.time_check',
        'schedule': 59.0,
    },
}

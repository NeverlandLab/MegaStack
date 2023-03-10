import os
from datetime import timedelta

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MegaStack.settings')
app = Celery('MegaStack')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


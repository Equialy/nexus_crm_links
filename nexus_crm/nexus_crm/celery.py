import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nexus_crm.settings')

app = Celery('nexus_crm')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
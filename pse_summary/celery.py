from __future__ import absolute_import, unicode_literals
import os

from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pse_summary.settings')

app = Celery('pse_summary')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
app.conf.update(
    worker_max_tasks_per_child=1,
    broker_pool_limit=None
)

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

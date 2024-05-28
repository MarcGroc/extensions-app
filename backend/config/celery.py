import os

from celery import Celery

env = "config.settings.development"

os.environ.setdefault("DJANGO_SETTINGS_MODULE", env)

celery_app = Celery("backend")
celery_app.config_from_object("django.conf:settings", namespace="CELERY")
celery_app.autodiscover_tasks()

celery_app.conf.beat_schedule = {
    # "test-task-every-30-seconds": {
    #     "task": "contact.tasks.test_task",
    #     "schedule": 30.0,
    # },
}

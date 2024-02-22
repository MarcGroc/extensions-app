import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.config.settings.development")

celery_app = Celery("backend")
celery_app.config_from_object("django.conf:settings", namespace="CELERY")
celery_app.autodiscover_tasks()

celery_app.conf.beat_schedule = {
    "task-every-30-seconds": {
        "task": "users.tasks.get_users_count",
        "schedule": 30.0,
    },
}

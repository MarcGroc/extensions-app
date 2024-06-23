from celery import Celery

from config.helper_functions import settings_loader

settings_loader()

celery_app = Celery("backend")
celery_app.config_from_object("django.conf:settings", namespace="CELERY")
celery_app.autodiscover_tasks()

celery_app.conf.beat_schedule = {}

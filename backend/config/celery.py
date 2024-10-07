from celery import Celery
from celery.schedules import crontab
from config.helper_functions import settings_loader

settings_loader()

celery_app = Celery("backend")
celery_app.config_from_object("django.conf:settings", namespace="CELERY")
celery_app.autodiscover_tasks()

celery_app.conf.beat_schedule = {
    "get_jobs_postings": {
        "task": "scraper.tasks.get_jobs_postings",
        "schedule": crontab(hour='0', minute='0'), },  # every day at midnight

}

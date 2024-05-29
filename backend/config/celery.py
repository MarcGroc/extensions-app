from celery import Celery

from config.load_settings import loader_settings

loader_settings()

celery_app = Celery("backend")
celery_app.config_from_object("django.conf:settings", namespace="CELERY")
celery_app.autodiscover_tasks()

celery_app.conf.beat_schedule = {
    # "test-task-every-30-seconds": {
    #     "task": "users.tasks.get_users_count",
    #     "schedule": 30.0,
    # },
}

from config import celery_app
from django.contrib.auth import get_user_model

User = get_user_model()


@celery_app.task()
def get_users_count():
    """test task"""
    return User.objects.count()

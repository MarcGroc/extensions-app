from django.apps import AppConfig
from django.core.management import call_command
from loguru import logger


class UsersConfig(AppConfig):
    name = "users"
    default_auto_field = "django.db.models.BigAutoField"

    def ready(self):
        try:
            return call_command("check_db")
        except Exception as e:
            logger.exception(e)

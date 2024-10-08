from django.apps import AppConfig
from django.core.management import call_command
from loguru import logger


class UsersConfig(AppConfig):
    name = "users"
    default_auto_field = "django.db.models.BigAutoField"

    def ready(self) -> None:
        import users.signals  # noqa: F401

        try:
            call_command("check_db")
        except Exception as e:
            logger.exception(e)

        try:
            call_command("check_or_create_user")
        except Exception as e:
            logger.exception(e)

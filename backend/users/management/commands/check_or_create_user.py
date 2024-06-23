import environ
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.core.management.base import BaseCommand
from django.db import IntegrityError
from loguru import logger


class Command(BaseCommand):
    help = "Django command to check if user exists in db or create new one"

    def handle(self, *args, **options) -> None:
        if not settings.DEBUG:
            return
        logger.info("Checking if user exists...")
        env = environ.Env()
        env.read_env(str(settings.BASE_DIR / ".env/.env.dev"))
        username = env("ADMIN_NAME", default="admin")
        email = env("ADMIN_EMAIL", default="admin@example.com")
        password = env("ADMIN_PASSWORD", default="adminpass")

        User_model = get_user_model()

        try:
            if not User_model.objects.filter(username=username).exists():
                User_model.objects.create_superuser(username, email, password)
                logger.info("Superuser created.")
            else:
                logger.info("Superuser already exists.")
        except (ValidationError, IntegrityError) as e:
            logger.exception(f"Error creating superuser: {e}")

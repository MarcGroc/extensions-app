import os
import time

from django.core.management.base import BaseCommand
from django.db import connection
from django.db.utils import OperationalError
from loguru import logger

from config.settings.base import CONNECTION_ATTEMPTS, DELAY_BETWEEN_ATTEMPTS
from config.settings.development import DATABASES

class Command(BaseCommand):
    help = "Django command to check database connection"

    def handle(self, *args, **options) -> None:
        if os.getenv("GITHUB_ACTIONS") == "true":
            logger.info("Skipping database check in GitHub Actions")
            return
        logger.info("Connecting to database...")
        is_db_available = False
        connection_attempt_count = 0
        while not is_db_available and connection_attempt_count < CONNECTION_ATTEMPTS:
            try:
                connection.ensure_connection()
                is_db_available = True
            except OperationalError:
                logger.warning(f"Database unavailable, waiting {DELAY_BETWEEN_ATTEMPTS} seconds to try again...")
                time.sleep(DELAY_BETWEEN_ATTEMPTS)
                connection_attempt_count += 1

        if is_db_available:
            logger.success(f"Database {DATABASES['default']['NAME']} available, and connection is established!")
        else:
            logger.critical(
                f"After {CONNECTION_ATTEMPTS} tries, database is still unavailable."
                f"Please check your database connection settings or database host."
                f"Aborting..."
            )

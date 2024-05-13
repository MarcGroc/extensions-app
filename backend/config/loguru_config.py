import logging

from loguru import logger


class InterceptHandler(logging.Handler):
    """Intercept loguru logs and send them to Logstash"""

    def emit(self, record) -> None:
        # Get corresponding Loguru level if it exists
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno

        # Find caller from where originated the logged message
        frame, depth = logging.currentframe(), 2
        while frame.f_code.co_filename == logging.__file__:
            frame = frame.f_back
            depth += 1

        logger.opt(depth=depth, exception=record.exc_info).log(level, record.getMessage())


logging.basicConfig(handlers=[InterceptHandler()], level=0)

logger.add(
    "logs/loguru-errors.log",
    level="ERROR",
    retention="7 days",
    rotation="1 day",
    enqueue=True,
    backtrace=True,
    diagnose=True,
)
logger.add(
    "logs/loguru-critical.log",
    level="CRITICAL",
    retention="7 days",
    rotation="1 day",
    enqueue=True,
    backtrace=True,
    diagnose=True,
)

import logging
import sys
from pathlib import Path


from loguru import logger


from app.settings import settings


class InterceptHandler(logging.Handler):
    loglevel_mapping = {
        50: "CRITICAL",
        40: "ERROR",
        30: "WARNING",
        25: "SUCCESS",
        20: "INFO",
        10: "DEBUG",
        0: "NOTSET",
    }

    def emit(self, record):
        try:
            level = logger.level(record.levelname).name
        except AttributeError:
            level = self.loglevel_mapping[record.levelno]

            frame, depth = logging.currentframe(), 2
        while frame.f_code.co_filename == logging.__file__:
            frame = frame.f_back
            depth += 1

            log = logger.bind(request_id="app")
            log.opt(depth=depth, exception=record.exc_info).log(
                level, record.getMessage())


class CustomizeLogger:
    @classmethod
    def make_logger(cls):

        config_path = Path(settings.path_log_predict)

        logger = cls.customize_logging(
            config_path, level="info", format=settings.log_format
        )
        return logger

    @classmethod
    def customize_logging(cls, filepath: Path, level: str, format: str):

        logger.remove()
        logger.add(
            sys.stdout,
            enqueue=True,
            backtrace=True,
            level=level.upper(),
            format=format
        )
        logger.add(
            str(filepath),
            rotation=settings.rotation,
            retention=settings.retention,
            compression=settings.compression,
            enqueue=True,
            backtrace=True,
            level=level.upper(),
            format=format,
        )
        logging.basicConfig(handlers=[InterceptHandler()], level=0)
        logging.getLogger("uvicorn.access").handlers = [InterceptHandler()]
        for _log in ["uvicorn", "uvicorn.error", "fastapi"]:
            _logger = logging.getLogger(_log)
            _logger.handlers = [InterceptHandler()]

        return logger.bind(request_id=None, method=None)

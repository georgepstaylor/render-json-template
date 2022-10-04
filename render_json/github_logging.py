import logging
import logging.config


class GitHubLoggingFilter(logging.Filter):
    def __init__(self, name):
        super().__init__(name)
        self.github_level = None

    def filter(self, record: logging.LogRecord):
        super().filter(record)
        match record.levelname:
            case logging.INFO:
                self.github_level = "notice"
            case logging.WARNING:
                self.github_level = "warning"
            case logging.ERROR:
                self.github_level = "error"
            case _:
                self.github_level = "debug"


LOGGING = {
    "version": 1,
    "disable_existing_loggers": True,
    "filters": {
        "github_filter": {
            "()": GitHubLoggingFilter,
        }
    },
    "formatters": {
        "default": {
            "format": "::%(github_level)s::%(message)s",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "filters": ["github_filter"]
        }
    }
}


def config():
    logging.config.dictConfig(LOGGING)
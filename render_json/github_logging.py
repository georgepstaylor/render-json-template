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


def config(name: str):
    logging.config.dictConfig(
        {
            "version": 1,
            "disable_existing_loggers": True,
            "filters": {
                "github_filter": {
                    "()": GitHubLoggingFilter,
                    "name": name,
                }
            },
            "formatters": {
                "default": {
                    "format": "::%(github_level)s::%(message)s",
                },
            },
            "handlers": {
                "stdout": {
                    "class": "logging.StreamHandler",
                    "stream": "ext://sys.stdout",
                    "filters": ["github_filter"],
                }
            },
            "loggers": {
                "": {
                    "handlers": None,
                },
                "render_json": {
                    "handlers": ["stdout"],
                    "level": "DEBUG",
                    "propagate": True,
                }
            }
        }
    )

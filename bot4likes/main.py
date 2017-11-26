import logging

from bot4likes.config import log_fmt, log_level
from bot4likes.longpoll import LongPoll


def configure_logger():
    logger = logging.getLogger()
    handler = logging.StreamHandler()
    formatter = logging.Formatter(log_fmt)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(log_level)


if __name__ == '__main__':
    configure_logger()
    LongPoll().handle()

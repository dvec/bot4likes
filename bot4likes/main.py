import logging

from bot4likes.config import log_fmt, log_level, log_file
from bot4likes.longpoll import LongPoll


def configure_logger():
    logging.basicConfig(filename=log_file, filemode='w', format=log_fmt, level=log_level)


if __name__ == '__main__':
    configure_logger()
    LongPoll().handle()

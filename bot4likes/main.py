import os
import logging

from bot4likes.config import log_fmt, log_level, log_file, log_dir
from bot4likes.longpoll import LongPoll


def configure_logger():
    try:
        os.makedirs(log_dir)
    except FileExistsError:
        pass

    logging.basicConfig(filename=log_file, filemode='w+', format=log_fmt, level=log_level)


if __name__ == '__main__':
    configure_logger()
    LongPoll().handle()

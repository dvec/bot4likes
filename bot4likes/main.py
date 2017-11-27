from bot4likes.config import configure_logger
from bot4likes.longpoll import LongPoll

if __name__ == '__main__':
    configure_logger()
    LongPoll().handle()

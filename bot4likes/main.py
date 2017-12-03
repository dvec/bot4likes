from bot4likes.config import api_group_token, api_user_login, api_user_password
from bot4likes.longpoll import LongPoll

if __name__ == '__main__':
    LongPoll(group_token=api_group_token, user_login=api_user_login, user_password=api_user_password).handle()

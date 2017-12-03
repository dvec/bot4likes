import threading
from time import sleep

from peewee import fn
from vk_api import VkApi, ApiError
from vk_api.longpoll import VkLongPoll, VkEventType

from bot4likes.commands.command_manager import CommandManager
from bot4likes.config import *
from bot4likes.domain.database import database
from bot4likes.domain.task import Task
from bot4likes.domain.user import User


class LongPoll:
    logger = logging.getLogger()

    def __init__(self):
        self.group_sess = VkApi(token=api_group_token)
        self.group_api = self.group_sess.get_api()

        self.user_sess = VkApi(login=api_user_login, password=api_user_password)
        self.user_sess.auth()
        self.user_api = self.user_sess.get_api()

        self.long_poll = self.__get__long_poll()
        self.command_manager = CommandManager()

    def __handle_message(self, event):
        self.logger.info("Performing message: {}".format(event.text))

        try:
            result = self.command_manager.process(self.__get_current_user(event.user_id), self.user_api, event)
        except Exception as e:
            self.logger.exception(e)
            result = 'Произошла внутренняя ошибка. Повторите попытку позже'

        if result == '':
            result = 'Готово'

        while 1:
            try:
                self.group_api.messages.send(user_id=event.user_id, message=result)
            except Exception as e:
                self.logger.exception(e)
                sleep(10)
            else:
                logging.info("Send answer: {}".format(result.replace('\n', ' ')))
                break

    def __get_current_user(self, user_id):
        try:
            return User.get(user_id=user_id)
        except User.DoesNotExist:
            user_info = self.user_api.users.get(user_ids=[user_id], fields='photo_id')[0]
            with database.transaction():
                Task().create(customer_id=user_id, item_id=user_info['photo_id'].split('_')[1],
                              owner_id=user_id, content_type='photo', type=Task.LIKE_TYPE,
                              reward=Task().select(fn.avg(Task.reward) + 1).where(Task.type == Task.LIKE_TYPE))

                return User.create(user_id=user_id, photo=user_info['photo_id'],
                                   first_name=user_info['first_name'],
                                   last_name=user_info['last_name'], scores=0, tasks_done=[], send_ads=True)

    def __get__long_poll(self):
        while 1:
            try:
                return VkLongPoll(self.group_sess)
            except ApiError as e:
                self.logger.exception(e)
                sleep(10)

    def __listen_long_poll(self):
        while True:
            try:
                events = self.long_poll.listen()
                for event in events:
                    yield event
            except Exception as e:
                logging.exception(e)
                self.long_poll.update_longpoll_server()

    def handle(self):
        for event in self.__listen_long_poll():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                threading.Thread(target=self.__handle_message, args=[event]).start()

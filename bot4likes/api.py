import queue

from vk_api import VkApiError, AuthError, VkApi
from logging import getLogger


class Api:
    def __init__(self, auth_data):
        self._apis = queue.Queue()
        for login, password in auth_data:
            api = VkApi(login=login, password=password)
            try:
                api.auth()
            except AuthError:
                getLogger().warning('Failed to get api key for login {}'.format(login))
            else:
                self._apis.put_nowait(api)

    def call(self, name, **kwargs):
        for i in range(self._apis.qsize()):
            api = self._apis.get_nowait()
            self._apis.put(api)

            try:
                api.call(name, **kwargs)
            except VkApiError:
                pass
            else:
                break
        else:
            getLogger().warning('Failed to call method. Please add new accounts')

import queue
from logging import getLogger

from vk_api import VkApiError, AuthError, VkApi


class AccountsBannedError(Exception):
    pass


# TODO REWRITE WITH ASYNC
class ApiAllocator:
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

    def method(self, name, **kwargs):
        for i in range(self._apis.qsize()):
            api = self._apis.get_nowait()
            self._apis.put(api)

            try:
                return api.method(name, kwargs)
            except VkApiError:
                pass
        else:
            raise AccountsBannedError('Failed to call method. Please add new accounts')

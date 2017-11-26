from abc import abstractmethod, ABCMeta


class Command:
    __metaclass__ = ABCMeta

    names = []
    description = 'нет описания'
    pattern = '^$'
    help = 'нет страницы помощи'

    @staticmethod
    @abstractmethod
    def process(user, parsed, api, attachments):
        pass

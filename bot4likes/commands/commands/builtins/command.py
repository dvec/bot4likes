from abc import ABCMeta


class Command:
    __metaclass__ = ABCMeta

    names = []
    description = 'нет описания'
    pattern = '^$'
    ignore = False
    help = 'нет страницы помощи'

    @staticmethod
    def process(user, parsed, api, attachments):
        pass

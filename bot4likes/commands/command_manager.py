import re

import os

from bot4likes.commands.command import Command


class CommandManager:
    methods = None

    @classmethod
    def __init__(cls):
        path = os.path.dirname(__file__)
        for root, _, files in os.walk(path):
            for f in files:
                if f.endswith('.py') and not f.startswith('__'):
                    pp = os.environ.get('PYTHONPATH')
                    if root.startswith(pp):
                        root = root.replace(pp, '', 1)

                    exec('import {}.{}'.format(root.replace(os.sep, '.')[1:], os.path.splitext(f)[0]))

        cls.methods = Command.__subclasses__()

    @classmethod
    def get_possible_methods(cls, name):
        possible_methods = []
        for method in cls.methods:
            if name in method.names:
                possible_methods.append(method)
        return possible_methods

    @classmethod
    def get_aliases(cls, name):
        for method in cls.methods:
            alias = method.aliases.get(name)
            if alias:
                return alias

    @classmethod
    def process(cls, user, api, event):
        text = event.text.lower()
        command = text.split(' ')[0]
        msg = ' '.join(text.split(' ')[1:])
        possible_methods = cls.get_possible_methods(command)

        if not possible_methods:
            return 'Нет такой команды. Для того, чтобы получить их список, введите: "помощь"'

        for method in possible_methods:
            if re.match(method.pattern, msg):
                return method.process(user, re.findall(method.pattern, msg)[0], api, event.attachments)

        return 'Параметры команды некорректны'

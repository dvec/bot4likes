from bot4likes.commands.command_manager import CommandManager
from bot4likes.commands.commands.builtins.command import Command
from bot4likes.config import bot_guide


class HelpCommand(Command):
    description = 'получить список команд'
    names = ['п', 'помощь']

    @staticmethod
    def process(user, parsed, api, attachments):
        commands = '\n'.join(['{}. {}: {}'
                             .format(i + 1, ' или '.join(map('"{}"'.format, m.names)), m.description) for i, m in
                              enumerate(filter(lambda x: not x.ignore, CommandManager.methods))])

        return 'Список команд: \n{}. \nГайд по использованию бота: {}'.format(commands, bot_guide)

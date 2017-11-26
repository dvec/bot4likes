from bot4likes.commands.command import Command
from bot4likes.commands.command_manager import CommandManager


class HelpCommand(Command):
    description = 'получить список команд'
    names = ['помощь']

    @staticmethod
    def process(user, parsed, api, attachments):
        return 'Список команд: \n{}'.format(
            '\n'.join(['{}. {}: {}'
                      .format(i + 1, '|'.join(m.names), m.description) for i, m in enumerate(CommandManager.methods)]))

from bot4likes.commands.commands.builtins.command import Command


class ScoreCommand(Command):
    names = ['счет']
    description = 'показать счет'

    @staticmethod
    def process(user, parsed, api, attachments):
        return 'Ваш счет: {}'.format(user.scores)

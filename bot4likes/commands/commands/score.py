from bot4likes.commands.command import Command


class ScoreCommand(Command):
    names = ['счет']
    description = 'выводит ваш счет'

    @staticmethod
    def process(user, parsed, api, attachments):
        return 'Ваш счет: {}'.format(user.scores)

from bot4likes.commands.commands.builtins.command import Command
from bot4likes.domain.database import database


class SkipCommand(Command):
    names = ['пр', 'пропустить']
    description = 'пропустить данное задание'

    @staticmethod
    def process(user, parsed, api, attachments):
        if user.current_task:
            with database.transaction():
                user.tasks_done.append(user.current_task)
                user.current_task = None
                user.save()
        else:
            return 'У вас еще нет таска'

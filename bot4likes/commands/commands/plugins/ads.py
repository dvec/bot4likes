from bot4likes.commands.commands.builtins.command import Command
from bot4likes.domain.database import database


class TasksCommands(Command):
    names = ['р', 'реклама']
    description = 'включить/выключить рекламу'
    ignore = True
    pattern = '^$'

    @staticmethod
    def process(user, parsed, api, attachments):
        with database.transaction():
            user.send_ads = not user.send_ads
            user.save()
        if user.send_ads:
            return 'Реклама включена'
        else:
            return 'Реклама выключена'

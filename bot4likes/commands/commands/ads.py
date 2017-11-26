from bot4likes.commands.command import Command
from bot4likes.domain.database import database


class TasksCommands(Command):
    names = ['реклама']
    description = 'включает или выключает рекламу'
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

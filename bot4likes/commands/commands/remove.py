from bot4likes.commands.command import Command
from bot4likes.domain.database import database
from bot4likes.domain.task import Task


class TasksCommands(Command):
    names = ['убрать']
    description = 'убирает ваш таск'
    pattern = '^(\d+)$'

    @staticmethod
    def process(user, parsed, api, attachments):
        task_id = int(parsed)
        with database.transaction():
            try:
                task = Task().get((Task.id == task_id) & (Task.customer_id == user.user_id))
            except Task.DoesNotExist:
                return 'У вас нет таска с таким ID'
            else:
                task.delete_instance()
                task.save()
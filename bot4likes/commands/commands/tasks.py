from bot4likes.commands.command import Command
from bot4likes.config import vk_url
from bot4likes.domain.task import Task, STR_TYPES


class TasksCommands(Command):
    names = ['таски']
    description = 'показать список всех заданий'

    @staticmethod
    def process(user, parsed, api, attachments):
        tasks = Task().select().where(Task.customer_id == user.user_id)
        tasks = ['{}. {} {}{}{}_{} за {}'.format(t.id, STR_TYPES[t.type], vk_url, t.content_type,
                                                 t.owner_id, t.item_id, t.reward) for t in tasks]
        return '\n'.join(tasks) if len(tasks) != 0 else 'У вас нет тасков'

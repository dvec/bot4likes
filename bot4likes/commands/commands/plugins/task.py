from bot4likes.commands.commands.builtins.command import Command
from bot4likes.domain.database import database
from bot4likes.domain.task import Task, ID_TYPES
from bot4likes.domain.user import User


class TaskCommand(Command):
    names = ['таск']
    description = 'получить задание'
    pattern = '^(\w*)$'

    @staticmethod
    def get_action(task):
        return {
            Task.LIKE_TYPE: 'Лайкните',
            Task.REPOST_TYPE: 'Репостните'
        }[task.type]

    @staticmethod
    def get_filter(task):
        return {
            Task.LIKE_TYPE: 'likes',
            Task.REPOST_TYPE: 'copies'
        }[task.type]

    @staticmethod
    def is_liked(user, api, task, api_filter):
        content_type = {
            'wall': 'post'
        }.get(task.content_type, task.content_type)

        likes = api.likes.get_list(type=content_type,
                                   owner_id=task.owner_id,
                                   item_id=task.item_id,
                                   filter=[api_filter])['items']
        return user.user_id in likes

    @staticmethod
    def process(user, parsed, api, attachments):
        added = None
        if user.current_task is not None:
            task = Task().get(Task.id == user.current_task)
            client = User.get(User.id == task.customer_id)
            if client.scores < task.reward:
                user.current_task = None
            elif TaskCommand.is_liked(user, api, task, [task.type]):
                client = User.get(User.id == task.customer_id)
                with database.transaction():
                    user.scores += task.reward
                    user.current_task = None
                    user.tasks_done += [task.id]
                    client.scores -= task.reward
                    user.save()
                    client.save()
                    added = task.reward

        if parsed:
            task_type = ID_TYPES.get(parsed)
            if task_type is None:
                return 'Неизвестный тип задания'
            else:
                task_type_condition = (Task.type == task_type)
        else:
            task_type_condition = True

        task = (Task()
                .select()
                .join(User, on=(User.id == Task.customer_id))
                .where(~(Task.id << user.tasks_done) &
                       (Task.customer_id != user.id) &
                       (User.scores >= Task.reward) &
                       task_type_condition)
                .order_by(Task.reward)
                .first())

        prefix = ''
        if added is not None:
            prefix = 'На ваш счет добавлено {} баллов. '.format(added)

        if task is None:
            return prefix + 'Таски закончились :(. Немного подождите, прежде чем появятся новые'

        with database.transaction():
            user.current_task = task.id
            user.save()

        return prefix + '{} {}\nНапишите "таск", когда вы выполните задание'\
            .format(TaskCommand.get_action(task), task.url)

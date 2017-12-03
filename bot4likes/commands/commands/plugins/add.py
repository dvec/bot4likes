from bot4likes.commands.commands.builtins.command import Command
from bot4likes.domain.database import database
from bot4likes.domain.task import Task, STR_TYPES, ID_TYPES


class TaskAddCommand(Command):
    names = ['добавить']
    description = 'добавить свое задание'
    pattern = '(\w*) (\d+)'

    @staticmethod
    def process(user, parsed, api, attachments):
        task_type, reward = parsed
        reward = int(reward)

        if reward > user.scores:
            return 'Вы не можете предложить больше баллов, чем у вас есть сейчас'
        if len(attachments) != 2:
            return 'Вы должны репостнуть одно фото или пост'

        owner_id, item_id = attachments['attach1'].split('_')
        attach_type = attachments['attach1_type']

        if task_type and task_type not in STR_TYPES.values():
            return 'Неизвестный тип'
        elif attach_type == STR_TYPES[Task.LIKE_TYPE]:
            if ID_TYPES[task_type] == Task.REPOST_TYPE:
                return 'Невозможно репостнуть фото'
            task_type = Task.LIKE_TYPE
        else:
            return 'Вы должны указать тип таска (лайк или репост)'

        with database.transaction():
            task = Task.create(customer_id=user.id, item_id=item_id, owner_id=owner_id,
                               content_type=attach_type, type=ID_TYPES[task_type], reward=reward)
            task.save()
        return 'Таск добавлен. ID: {}'.format(task.id)

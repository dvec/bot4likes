from bot4likes.commands.command import Command
from bot4likes.domain.task import Task, STR_TYPES, ID_TYPES


class TaskAddCommand(Command):
    names = ['добавить']
    description = 'добавляет таск'
    pattern = '(\w+) (\d+)'

    @staticmethod
    def process(user, parsed, api, attachments):
        task_type, reward = parsed
        reward = int(reward)

        if reward > user.scores:
            return 'Вы не можете предложить больше баллов, чем у вас есть сейчас'
        if len(attachments) != 2:
            return 'Вы должны репостнуть одно фото или пост'

        if task_type not in STR_TYPES.values():
            return 'Неизвестный тип'

        owner_id, item_id = attachments['attach1'].split('_')
        attach_type = attachments['attach1_type']
        if task_type == Task.REPOST_TYPE and attach_type != 'wall':
            return 'Репостить можно только посты'

        task = Task.create(customer_id=user.user_id, item_id=item_id, owner_id=owner_id,
                           content_type=attach_type, type=ID_TYPES[task_type], reward=reward)
        task.save()
        return 'Таск добавлен. ID: {}'.format(task.id)

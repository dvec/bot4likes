from bot4likes.commands.command import Command
from bot4likes.config import vk_url
from bot4likes.domain.database import database
from bot4likes.domain.user import User


class TransferCommand(Command):
    names = ['перевод']
    description = 'перевести свои баллы другому участнику'
    ignore = True
    pattern = '^{}(\w*) (\d)$'.format(vk_url)

    @staticmethod
    def process(user, parsed, api, attachments):
        to, scores = parsed
        if user.scores < int(scores):
            return 'На вашем счете недостаточно баллов'
        user_info = api.users.get(user_ids=[to])[0]
        user_to = User.get(User.user_id == user_info['id'])
        if user_to.user_id == user.user_id:
            return 'Вы не можете перевести деньги самому себе'
        with database.transaction():
            user.scores -= int(scores)
            user_to.scores += int(scores)
            user.save()
            user_to.save()
        return 'Готово'

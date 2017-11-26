from bot4likes.commands.command import Command
from bot4likes.config import bot_top_size
from bot4likes.domain.user import User


class TopCommand(Command):
    names = ['топ']
    description = 'выводит 10 игроков с самым большим кол-вом баллов'

    @staticmethod
    def process(user, parsed, api, attachments):
        top = User().select().order_by(User.scores.desc()).limit(bot_top_size)
        return '\n'.join(['{}. [id{}|{} {}] - {}'.format(
            i + 1, u.user_id, u.first_name, u.last_name, u.scores) for i, u in enumerate(top)])

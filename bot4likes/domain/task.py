from peewee import Model, IntegerField, CharField

from bot4likes.config import vk_url
from bot4likes.domain.database import database


# noinspection PyTypeChecker
class Task(Model):
    LIKE_TYPE = 0
    REPOST_TYPE = 1

    type = IntegerField()
    reward = IntegerField()
    item_id = IntegerField()
    owner_id = IntegerField()
    content_type = CharField()
    customer_id = IntegerField()

    @property
    def url(self):
        return '{}{}{}_{}'.format(vk_url, self.content_type, self.owner_id, self.item_id)

    class Meta:
        database = database


STR_TYPES = {
    Task.LIKE_TYPE: 'лайк',
    Task.REPOST_TYPE: 'репост'
}

ID_TYPES = dict(zip(STR_TYPES.values(), STR_TYPES.keys()))

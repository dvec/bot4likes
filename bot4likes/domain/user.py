from playhouse.postgres_ext import *

from bot4likes.domain.database import database


class User(Model):
    user_id = IntegerField()
    photo = CharField()
    first_name = CharField()
    last_name = CharField()
    scores = IntegerField()
    current_task = CharField(null=True)
    tasks_done = ArrayField(IntegerField)
    send_ads = BooleanField()

    class Meta:
        database = database

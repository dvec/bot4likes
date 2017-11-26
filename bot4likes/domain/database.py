from playhouse.postgres_ext import PostgresqlDatabase

from bot4likes.config import db_database, db_user, db_password, db_host

database = PostgresqlDatabase(db_database, user=db_user, password=db_password, host=db_host)

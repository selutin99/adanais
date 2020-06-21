from flask_script import Command
from sqlalchemy_utils import database_exists, drop_database, create_database

from config.database import DB_URL


class DatabaseCreateCommand(Command):
    """ Create the database."""

    def run(self):
        self.reset_db()

    @staticmethod
    def reset_db():
        if database_exists(DB_URL):
            drop_database(DB_URL)

        if not database_exists(DB_URL):
            create_database(DB_URL)
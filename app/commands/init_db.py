from flask_script import Command

from app import alchemy_db


class DatabaseInitCommand(Command):
    """ Initialize the database."""

    def run(self):
        self.init_db()

    @staticmethod
    def init_db():
        alchemy_db.drop_all()
        alchemy_db.create_all()

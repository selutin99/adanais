from flask_script import Command

from app import db


class DatabaseInitCommand(Command):
    """ Initialize the database."""

    def run(self):
        self.init_db()

    @staticmethod
    def init_db():
        db.drop_all()
        db.create_all()

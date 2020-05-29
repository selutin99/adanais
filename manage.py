from flask_migrate import MigrateCommand
from flask_script import Manager

from app.commands import DatabaseInitCommand, DatabaseCreateCommand

# Setup Flask-Script with command line commands
from app import create_app

manager = Manager(create_app())

# For automatic database migration
# python manage.py db init
# python manage.py db migrate
# python manage.py db upgrade
# python manage.py db --help
manager.add_command('db', MigrateCommand)
# For manual database migration
# python manage.py create_db
# python manage.py init_db
manager.add_command('create_db', DatabaseCreateCommand)
manager.add_command('init_db', DatabaseInitCommand)

if __name__ == "__main__":
    # python manage.py                      # shows available commands
    # python manage.py runserver --help     # shows available runserver options
    manager.run()

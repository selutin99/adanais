import os
from logging import Formatter, INFO
from logging.handlers import RotatingFileHandler
from os import listdir
from os.path import isfile, join

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config.constants import CONFIGURATION_DIRECTORY
from config.settings import LOGGING_FORMAT, LOGGING_DATE_FORMAT, LOGGING_PATH
from utils.db_utils.pymysql_db_provider import PyMySQLProvider


app = Flask(__name__, instance_relative_config=True)
# Database connect providers
db = SQLAlchemy()
pymysql_db = PyMySQLProvider()
# End database connect providers


def create_app():
    init_config()
    logging_initialize()
    return app


def init_config():
    [app.config.from_pyfile(os.path.abspath(CONFIGURATION_DIRECTORY) + os.path.sep + file)
     for file in listdir(CONFIGURATION_DIRECTORY)
     if isfile(join(CONFIGURATION_DIRECTORY, file)) and file.endswith('.py')]


def logging_initialize():
    log = app.logger
    formatter = Formatter(fmt=LOGGING_FORMAT, datefmt=LOGGING_DATE_FORMAT)

    handler = RotatingFileHandler(LOGGING_PATH, maxBytes=10000, backupCount=1)
    handler.setLevel(INFO)
    handler.setFormatter(formatter)

    log.addHandler(handler)

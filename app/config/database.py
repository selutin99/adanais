MYSQL_USER = 'root'
MYSQL_PASSWORD = '75297529S'
MYSQL_URL = 'localhost'
MYSQL_DB = 'adanais'

DB_URL = 'mysql://{user}:{pw}@{url}/{db}'.format(user=MYSQL_USER,
                                                 pw=MYSQL_PASSWORD,
                                                 url=MYSQL_URL,
                                                 db=MYSQL_DB)

SQLALCHEMY_DATABASE_URI = DB_URL
SQLALCHEMY_TRACK_MODIFICATIONS = False

SESSION_TYPE = 'sqlalchemy'

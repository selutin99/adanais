import pymysql.cursors

from app.config.database import MYSQL_URL, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DB


class PyMySQLProvider:

    def __init__(self):
        self.connection = pymysql.connect(host=MYSQL_URL,
                                          user=MYSQL_USER,
                                          password=MYSQL_PASSWORD,
                                          database=MYSQL_DB,
                                          cursorclass=pymysql.cursors.DictCursor)

    def get_query(self, query, params=()):
        with self.connection.cursor() as cursor:
            # Read a record
            sql = query
            cursor.execute(sql, params)
            result = cursor.fetchall()
            print('Get result from PyMySQL provider')
            self.connection.commit()
            return result

    def upsert_query(self, query, params=()):
        with self.connection.cursor() as cursor:
            sql = query
            cursor.execute(sql, params)
        print('Commit changes to PyMySQL provider')
        self.connection.commit()

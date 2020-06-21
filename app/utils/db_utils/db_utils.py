from app import alchemy_db, pymysql_db


def sync_commit():
    # Function required to maintain database consistency
    alchemy_db.session.commit()
    pymysql_db.connection.commit()

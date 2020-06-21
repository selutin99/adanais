from app import db, pymysql_db


def sync_commit():
    # Function required to maintain database consistency
    db.session.commit()
    pymysql_db.connection.commit()

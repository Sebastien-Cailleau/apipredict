import pymysql
from app.settings import settings
from app.utilities import logger


class DBConnection(object):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self):
        """Initialize the database connection"""
        self._connect = pymysql.connect(
            host=settings.dns_db_host,
            user=settings.dns_db_user,
            password=settings.dns_db_password,
            db=settings.dns_db,
            charset="utf8mb4",
            cursorclass=pymysql.cursors.DictCursor,
        )
        self._cursor = self._connect.cursor()
        logger.info("Connection with the database, done")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor()
        self.close()

    def commit(self):
        logger.info("Commit, done")
        return self._connect.commit()

    def cursor(self):
        logger.info("Cursor, closed")
        return self._cursor.close()

    def close(self):
        logger.info("Connection with the database, closed")
        return self._connect.close()

    def execute(self, request, params=None):
        logger.info("Execute request, done")
        return self._cursor.execute(request, params or ())

    def fetchall(self):
        logger.info("Fetch all datas, done")
        return self._cursor.fetchall()

    def fetchone(self):
        logger.info("Fetch one data, done")
        return self._cursor.fetchone()

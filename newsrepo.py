import sqlite3
from log import logger


class NewsRepository(object):

    def __init__(self, db_name):
        self._db_name = db_name
        self._cursor = None

    def add(self, parser):
        connection = None
        try:
            connection = sqlite3.connect(self._db_name)
            self._cursor = connection.cursor()
            for n in parser.news:
                self._create_entry(n, parser.id)
            connection.commit()
        except sqlite3.Error as error:
            if connection:
                connection.rollback()
            logger.inform("Database error: {0}".format(error.args[0]))
        finally:
            if connection:
                connection.close()

    def _create_entry(self, new, web_site_id):
        try:
            self._cursor.execute("""
                insert into News(Contents, WebSiteId, PostDate)
                values ('{0}', {1}, datetime('now', 'localtime'))
                """.format(new, web_site_id))
        except sqlite3.Error as error:
            logger.inform("Database error: {0}".format(error.args[0]))

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
            logger.inform("Database error [{0}]: {1}".format(
                type(error), error.args[0]))
        finally:
            if connection:
                connection.close()

    def _create_entry(self, new, web_site_id):
        try:
            self._cursor.execute("""
                insert into News(Contents, WebSiteId, PostDate)
                values ('{0}', {1}, date('now'))
                """.format(new.replace("'", "-"), web_site_id))
        except sqlite3.IntegrityError:
            # The news already in database
            pass
        except sqlite3.OperationalError as error:
            logger.inform("Syntax error[{0}]: {1} on new:\n{2}".format(
                type(error), error, new))
        except sqlite3.Error as error:
            logger.inform("Database error [{0}]: {1}".format(
                type(error), error))

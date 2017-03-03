import sqlite3
from log.logger import Logger


class NewsRepository(object):

    def __init__(self, db_name):
        self._db_name = db_name
        self._logger = Logger()
        self._cursor = None

    def add(self, parser):
        connection = None
        try:
            connection = sqlite3.connect(self._db_name)
            self._cursor = connection.cursor()
            web_site_id = self._get_web_site_id(parser.url)
            for item in parser.news:
                if not self._is_exists(item):
                    self._add_new_in_database(item, web_site_id)
            connection.commit()
            self._logger.inform("Information stored in the database")
        except sqlite3.Error, e:
            if connection:
                connection.rollback()
            self._logger.inform("Database error: {0}".format(e.args[0]))
        finally:
            if connection:
                connection.close()

    def _get_web_site_id(self, web_site_name):
        if not self._cursor:
            return
        self._cursor.execute("""
                       select Id from WebSites
                       where Name='{0}'
                       """.format(web_site_name))
        return self._cursor.fetchone()[0]

    def _is_exists(self, news):
        if not self._cursor:
            return
        self._cursor.execute("""
                             select exists (
                             select Contents from News
                             where Contents='{0}'
                             )
                             """.format(news))
        return self._cursor.fetchone()[0]

    def _add_new_in_database(self, new, web_site_id):
        if not self._cursor:
            return
        self._cursor.execute("""
                             insert into News(Contents, WebSiteId, DateTime)
                             values ('{0}', {1}, datetime('now', 'localtime'))
                             """.format(new, web_site_id))

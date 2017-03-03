import sqlite3
from log.logger import Logger


class NewsRepository(object):

    def __init__(self, db_name):
        self._db_name = db_name
        self._logger = Logger("log/log.txt")

    def add(self, parser):
        connection = None
        try:
            connection = sqlite3.connect(self._db_name)
            cursor = connection.cursor()
            cursor.execute("""
                           select Id from WebSites
                           where Name='{0}'
                           """.format(parser.url))
            web_site_id_entry = cursor.fetchone()
            if not web_site_id_entry:
                cursor.execute("""
                               insert into WebSites(Name)
                               values ('{0}')
                               """.format(parser.url))
                cursor.execute("""
                               select Id from WebSites
                               where Name='{0}'
                               """.format(parser.url))
                web_site_id_entry = cursor.fetchone()
            web_site_id = web_site_id_entry[0]
            for item in parser.news:
                cursor.execute("""
                               select exists (
                               select Contents from News
                               where Contents='{0}'
                               )
                               """.format(item))
                item_in_database = cursor.fetchone()[0]
                if not item_in_database:
                    cursor.execute("""
                                   insert into News(Contents, WebSiteId, DateTime)
                                   values ('{0}', {1}, datetime('now', 'localtime'))
                                   """.format(item, web_site_id))
            self._logger.inform("Information stored in the database")
            connection.commit()
        except sqlite3.Error, e:
            if connection:
                connection.rollback()
            self._logger.inform("Database error: {0}".format(e.args[0]))
        finally:
            if connection:
                connection.close()

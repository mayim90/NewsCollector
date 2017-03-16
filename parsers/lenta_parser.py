from bs4 import BeautifulSoup


class LentaParser(object):
    """
    Parses lenta.ru
    """

    url = "https://lenta.ru/"
    # Web site id in database
    id = 3

    def __init__(self):
        self._html_doc = None
        self._news = []

    @property
    def news(self):
        return self._news

    def set_contents(self, contents):
        self._html_doc = BeautifulSoup(contents, "lxml")

    def find_news(self):
        if not self._html_doc:
            return
        news_div = self._html_doc.find("div", "items")
        for link in news_div.find_all("a"):
            if len(link.contents) > 1:
                self._news.append(str(link.contents[1]))

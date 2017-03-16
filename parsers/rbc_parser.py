from bs4 import BeautifulSoup


class RbcParser(object):
    """
    Parses rbc.ru
    """

    url = "http://www.rbc.ru/"
    # Web site id in database
    id = 6

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
        news_div = self._html_doc.find(
            "div", "main-feed js-main-reload-list")
        for span in news_div.find_all("span", "main-feed__item__title"):
            if span.contents:
                self._news.append(str(span.contents[0]))

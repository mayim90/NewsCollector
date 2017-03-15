from bs4 import BeautifulSoup


class YandexParser(object):
    """
    Parses yandex.ru
    """

    url = "https://www.yandex.ru/"
    # Web site id in database
    id = 2

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
            "div", "content-tabs__items content-tabs__items_active_true")
        for link in news_div.find_all("a"):
            self._news.append(str(link.contents[0]))

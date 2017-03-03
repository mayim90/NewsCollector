from bs4 import BeautifulSoup


class RamblerParser(object):
    """
    Parses rambler.ru
    """

    def __init__(self):
        self._html_doc = None
        self._url = "https://www.rambler.ru/"
        self._news = []

    @property
    def news(self):
        return self._news

    @property
    def url(self):
        return self._url

    def set_contents(self, contents):
        self._html_doc = BeautifulSoup(contents, "lxml")

    def find_news(self):
        if not self._html_doc:
            return
        news_div = self._html_doc.find("div", "mixednews_itemsline mixednews_itemsline_double-height")
        for span in news_div.find_all("span", "mixednews-item__title_text"):
            self._news.append(span.contents[0].encode("utf8"))
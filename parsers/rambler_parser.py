from bs4 import BeautifulSoup


class RamblerParser(object):
    """
    Parses rambler.ru
    """

    url = "https://www.rambler.ru/"
    # Web site id in database
    id = 1

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
            "div", "mixednews_itemsline mixednews_itemsline_double-height")
        for span in news_div.find_all("span", "mixednews-item__title_text"):
            self._news.append(span.contents[0])

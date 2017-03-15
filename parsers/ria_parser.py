from bs4 import BeautifulSoup


class RiaParser(object):
    """
    Parses ria.ru
    """

    url = "https://www.ria.ru//"
    # Web site id in database
    id = 4

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
            "div", "b-index__main-list-place")
        for span in news_div.find_all("span"):
            if span.contents and not str(span.contents[0]).endswith("</span>"):
                self._news.append(str(span.contents[0]))

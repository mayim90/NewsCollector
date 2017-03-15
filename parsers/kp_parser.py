from bs4 import BeautifulSoup


class KpParser(object):
    """
    Parses kp.ru
    """

    url = "http://www.kp.ru/"
    # Web site id in database
    id = 7

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
        news_div = self._html_doc.findfind("div", "loadSection")
        for div in news_div.find_all("div", "digestTitle"):
            print(str(div.contents[0]))

from bs4 import BeautifulSoup


class VestiParser(object):
    """
    Parses vesti.ru
    """

    url = "http://www.vesti.ru//"
    # Web site id in database
    id = 8

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
        news_headers = self._html_doc.find_all("h3", "b-item__title")
        for h in news_headers:
            a = h.find("a")
            if a.contents:
                self._news.append(str(a.contents[0]))

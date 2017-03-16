from bs4 import BeautifulSoup


class MailParser(object):
    """
    Parses mail.ru
    """

    url = "https://www.news.mail.ru/"
    # Web site id in database
    id = 5

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
            "ul", "list list_type_square list_half js-module")
        for link in news_div.find_all("a", "list__text"):
            if link.contents:
                self._news.append(str(link.contents[0]))

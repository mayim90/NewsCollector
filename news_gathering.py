from news_repository import NewsRepository
from parsers.yandex_parser import YandexParser
from parsers.rambler_parser import RamblerParser
import downloading


news_repository = NewsRepository(r"database/news.sqlite3")
parsers = [
    YandexParser(),
    RamblerParser()
]


def collect_news():
    for parser in parsers:
        downloading.download_contents_into(parser)
        parser.find_news()
        news_repository.add(parser)

if __name__ == "__main__":
    collect_news()

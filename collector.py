from newsrepo import NewsRepository
from parsers.yandex_parser import YandexParser
from parsers.rambler_parser import RamblerParser
from parsers.lenta_parser import LentaParser
from parsers.ria_parser import RiaParser
from parsers.mail_parser import MailParser
from parsers.rbc_parser import RbcParser
import downloading


news_repository = NewsRepository(r"database/news.sqlite3")
parsers = [
    YandexParser(),
    RamblerParser(),
    LentaParser(),
    RiaParser(),
    MailParser(),
    RbcParser(),
]


def collect_news():
    for parser in parsers:
        downloading.download_contents_into(parser)
        parser.find_news()
        news_repository.add(parser)

if __name__ == "__main__":
    collect_news()

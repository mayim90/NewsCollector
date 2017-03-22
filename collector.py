from newsrepo import NewsRepository
from parsers.yandex_parser import YandexParser
from parsers.rambler_parser import RamblerParser
from parsers.lenta_parser import LentaParser
from parsers.ria_parser import RiaParser
from parsers.mail_parser import MailParser
from parsers.rbc_parser import RbcParser
from parsers.kp_parser import KpParser
from parsers.vesti_parser import VestiParser
import downloading
from log import logger


news_repository = NewsRepository(r"database/news.sqlite3")
parsers = [
    YandexParser(),
    RamblerParser(),
    LentaParser(),
    RiaParser(),
    MailParser(),
    RbcParser(),
    KpParser(),
    VestiParser(),
]


def collect_news():
    total = 0
    for parser in parsers:
        downloading.download_contents_into(parser)
        parser.find_news()
        logger.inform("{0}. News downloaded: {1}".format(
            parser.url, len(parser.news)))
        news_repository.add(parser)
        total += len(parser.news)
    logger.inform("Total news: {0}".format(total))

if __name__ == "__main__":
    collect_news()

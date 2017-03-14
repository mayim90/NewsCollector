import urllib.request as request


def download_contents_into(parser):
    """
    Retrieves HTML code and
    binary files from a specific
    website
    """
    browser = request.urlopen(parser.url)
    if browser.getcode() == 200:
        parser.set_contents(browser.read())

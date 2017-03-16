from bs4 import BeautifulSoup
import urllib.request as request


browser = request.urlopen("http://www.vesti.ru/")
doc = browser.read()
soup = BeautifulSoup(doc, "lxml")
news_headers = soup.find_all("h3", "b-item__title")
for h in news_headers:
    a = h.find("a")
    if a.contents:
        print(a.contents[0])

from bs4 import BeautifulSoup
import urllib.request as request


browser = request.urlopen("http://www.kp.ru/")
doc = browser.read()
soup = BeautifulSoup(doc, "lxml")
news_div = soup.find("div", "loadSection")
for div in news_div.find_all("div", "digestTitle"):
    print(div.contents[0])

import bs4 
from bs4 import BeatifulSoup as soup
from urllib.request import urlopen

newsUrl = "https://news.google.com/news/rss"
client = urlopen(newsUrl)
xml_page = client.read()
client.close()

soupPage = soup(xml_page,"xml")
newsList = soupPage.findAll("item")

for news in newsList:
   print(news.title.text)
  print(news.link.text)
  print(news.pubDate.text)
  print("-"*60)
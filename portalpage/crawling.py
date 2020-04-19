import requests
from bs4 import BeautifulSoup
import urllib.request as req
import ssl
from bs4.builder import builder_registry

# SSL인증코드
if hasattr(ssl, '_create_unverified_context'):
  ssl._create_default_https_context = ssl._create_unverified_context

def urlparsing(base_url):
  url = base_url
  req = requests.get(url)
  html = req.content
  soup = BeautifulSoup(html, 'lxml')
  return soup

def news_searching(base_url):
  soup = urlparsing(base_url)
  items = soup.find_all('item title')

  #데이터 찾기 (title, img)
  news_item = soup.find_all('title')
  image = soup.select('description img[src]')
  link = soup.find_all('link')
  news_title = []
  news_img = []
  news_link = []
  
  for i in news_item:
    a = i.get_text()
    news_title.append(a)

  for i in image:
    a = i['src']
    news_img.append(a)

  for i in link:
    a = i.get_text()
    news_link.append(a)
    
  return news_title, news_img, news_link

def searchTrend(base_url):
  soup = urlparsing(base_url)
  
  # 데이터 찾기 (title, traffic)
  search_trend = soup.find_all('title')
  search_traffic = soup.find_all('ht:approx_traffic')
  # 배열을 만들자
  trendList = []
  trafficList = []
  for i in search_trend:
    a = i.get_text()
    trendList.append(a)
    for j in search_traffic:
      b = j.get_text()
      trafficList.append(b)
  trendList = trendList[1:11]
  trafficList = trafficList[0:10]
  merged = dict([x for x in zip(trendList, trafficList)])
  return merged


def search_news(news):
  title = news_searching(news)
  return title

# a = searchTrend('https://trends.google.com/trends/trendingsearches/daily/rss?geo=VN')
b = search_news('https://vnexpress.net/rss/tin-moi-nhat.rss')
print(b)


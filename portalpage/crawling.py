import requests
from bs4 import BeautifulSoup
import urllib.request as req
import ssl
from bs4.builder import builder_registry

# SSL인증코드
if hasattr(ssl, '_create_unverified_context'):
  ssl._create_default_https_context = ssl._create_unverified_context

# 사이트 파싱 함수
def urlparsing(base_url):
  url = base_url
  req = requests.get(url)
  html = req.content
  soup = BeautifulSoup(html, 'html.parser')
  return soup

# 뉴스 스크랩 그루핑함수
def news_merge(news_title, news_img, news_link):
  # 리스트자르기
  titleList = news_title[0:12]
  imgList = news_img[0:12]
  linkList = news_link[0:12]

  merged = dict([x for x in zip(titleList, zip(imgList, linkList))])
  return merged

def search_main():
  soup = urlparsing('https://vnexpress.net/')

  # 기사 스크랩
  title = soup.select('.item-news > .thumb-art > a')
  images = soup.select('.item-news > .thumb-art > a > picture > img')
  desc = soup.select('.item-news > .description')
  link = soup.select('.item-news > .thumb-art > a')

  # 기사 넣을 빈 리스트생성
  news_title = [news['title'] for news in title]
  news_img = [news['src'] for news in images]
  news_desc = [news.text for news in desc]
  news_link = [news['href'] for news in link]

  titleList = news_title[0:6]
  imgList = news_img[0:6]
  linkList = news_link[0:6]
  descList = news_desc[0:6]

  dic = {}
  for i in range(len(titleList)):
    dic[titleList[i]] = [imgList[i], linkList[i], descList[i]]
  
  return dic

def thegioi():
  soup = urlparsing('https://vnexpress.net/the-gioi')

  # 기사 스크랩
  title = soup.select('.item-news > .thumb-art > a')
  images = soup.select('.item-news > .thumb-art > a > picture > img')
  link = soup.select('.item-news > .thumb-art > a')

  # 기사 넣을 빈 리스트생성
  news_title = [news['title'] for news in title]
  news_img = [news['src'] for news in images]
  news_link = [news['href'] for news in link]

  # 딕셔너리화
  merged = news_merge(news_title, news_img, news_link)
  return merged

def search_trends():
  url = 'https://trends.google.com/trends/trendingsearches/daily/rss?geo=VN'
  req = requests.get(url)
  html = req.content
  soup = BeautifulSoup(html, 'lxml')
  
  # 데이터 찾기 (title, traffic)
  search_trend = soup.find_all('title')
  search_traffic = soup.find_all('ht:approx_traffic')
  # 배열 생성
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


answer = search_main()
print(answer)
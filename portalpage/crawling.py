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

  merged = dict([x for x in zip(titleList, zip(linkList, imgList))])
  return merged

def zingNews():
  soup = urlparsing('https://zingnews.vn/the-gioi.html')
  url = 'https://zingnews.vn'

  # 기사 스크랩
  news = soup.select('p.article-thumbnail > a')
  title = soup.select('p.article-title')
  images = soup.select('.article-thumbnail > a > img')
  link = soup.select('p.article-thumbnail > a')

  # 이미지가 lazy loading 인경우 해당 이미지 attr 변경
  # for i in images:
  #   if i['data-src']:
  #     i['src'] = i['data-src']
  #     del i['data-src']

  # 기사 넣을 빈 리스트생성
  news_title, news_img, news_link = [], [], []

  # 이걸로 대체하고싶지만 img부분에 url이 추가되어야함...
  # news_title = [[news.text for news in title]]
  # news_img = [news['src'] for news in image]
  # news_link = [news['href'] for news in link]

  # 각 리스트에 스크랩한 기사 추가
  for news in title:
    news_title.append(news.text)
  for news in link:
    news_link.append(url + news['href'])
  for news in images:
    news_img.append(news['src'])

  # 딕셔너리화
  merged = news_merge(news_title, news_img, news_link)
  return merged

a = zingNews()
print(a)

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

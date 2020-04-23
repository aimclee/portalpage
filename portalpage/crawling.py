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
def news_merge(main_title, main_image, main_link, sub_items):
  news_title = [main_title]
  news_img = [main_image]
  news_link = [main_link]

  for news in sub_items:
    news_title.append(news['title'])
    news_img.append('')
    news_link.append(news['href'])
  
  titleList = news_title[0:8]
  imgList = news_img[0:8]
  linkList = news_link[0:8]

  merged = dict([x for x in zip(titleList, zip(linkList, imgList))])
  return merged

# VNExpress 서칭
def vnExpress():
  url = 'https://vnexpress.net/'
  req = requests.get(url)
  html = req.content
  soup = BeautifulSoup(html, 'html.parser')

  # 첫번째 기사 스크랩
  main_title = soup.select_one(".thumb")['title']
  main_image = soup.select_one(".thumb img")['src']
  main_link = soup.select_one(".thumb")['href']
  
  # 서브 기사 스크랩
  sub_items = soup.select('h3.title-news > a')
  merged = news_merge(main_title, main_image, main_link, sub_items)
  return merged

def zingNews():
  url = 'https://zingnews.vn/'
  req = requests.get(url)
  html = req.content
  soup = BeautifulSoup(html, 'html.parser')

  # 첫번째 기사 스크랩
  main_title = soup.select_one('p.article-thumbnail > a > img')['alt']
  main_image = soup.select_one('p.article-thumbnail > a > img')['src']
  main_link = url + soup.select_one('p.article-thumbnail > a')['href']
  # 서브 기사 스크랩
  sub_items = soup.select('.article-title > a')

  news_title = [main_title]
  news_img = [main_image]
  news_link = [main_link]

  for news in sub_items:
    news_title.append(news.get_text())
    news_img.append('')
    news_link.append(url + news['href'])

  titleList = news_title[0:8]
  imgList = news_img[0:8]
  linkList = news_link[0:8]

  merged = dict([x for x in zip(titleList, zip(linkList, imgList))])
  return merged

def tuoiTre():
  url = 'https://tuoitre.vn/'
  req = requests.get(url)
  html = req.content
  soup = BeautifulSoup(html, 'html.parser')

  # 첫번째 기사 스크랩
  main_title = soup.select_one('.focus-first > a > img')['alt']
  main_image = soup.select_one('.focus-first > a > img')['src']
  main_link = url + soup.select_one('.focus-first > a')['href']
  # 서브 기사 스크랩
  sub_items = soup.select('.title-name > a')

  news_title = [main_title]
  news_img = [main_image]
  news_link = [main_link]

  for news in sub_items:
    news_title.append(news.get_text())
    news_img.append('')
    news_link.append(url + news['href'])

  titleList = news_title[0:8]
  imgList = news_img[0:8]
  linkList = news_link[0:8]

  merged = dict([x for x in zip(titleList, zip(linkList, imgList))])
  return merged

def thanhNien():
  url = 'https://thanhnien.vn/'
  req = requests.get(url)
  html = req.content
  soup = BeautifulSoup(html, 'html.parser')

  # 첫번째 기사 스크랩
  main_title = soup.select_one('.highlight > article > a')['title']
  main_image = soup.select_one('.highlight > article > a > img')['src']
  main_link = url + soup.select_one('.highlight > article > a')['href']
  # 서브 기사 스크랩
  sub_items = soup.select('.feature > article > h2 > a')

  news_title = [main_title]
  news_img = [main_image]
  news_link = [main_link]

  for news in sub_items:
    news_title.append(news.get_text())
    news_img.append('')
    news_link.append(url + news['href'])

  titleList = news_title[0:8]
  imgList = news_img[0:8]
  linkList = news_link[0:8]
  merged = dict([x for x in zip(titleList, zip(linkList, imgList))])
  return merged

def search_trends():
  url = 'https://trends.google.com/trends/trendingsearches/daily/rss?geo=VN'
  req = requests.get(url)
  html = req.content
  soup = BeautifulSoup(html, 'lxml')
  
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

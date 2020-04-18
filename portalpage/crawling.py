import requests
import feedparser
from bs4 import BeautifulSoup
import urllib.request as req
import ssl

# SSL인증코드
if hasattr(ssl, '_create_unverified_context'):
  ssl._create_default_https_context = ssl._create_unverified_context

# url 모음
vnexpress = 'https://vnexpress.net/rss/tin-moi-nhat.rss' #https://vnexpress.net/rss
thanhnien = 'https://thanhnien.vn/rss/home.rss' #https://thanhnien.vn/rss.html
tuoitre = 'https://tuoitre.vn/rss/tin-moi-nhat.rss' #https://tuoitre.vn/rss.htm
dantri = 'https://dantri.com.vn/trangchu.rss' #https://dantri.com.vn/rss.htm
nhandan = '' #https://www.nhandan.org.vn/rss

def searchTrend():
  #RSS를 lxml parser로 파싱
  base_url = 'https://trends.google.com/trends/trendingsearches/daily/rss?geo=VN'
  req = requests.get(base_url)
  html = req.content
  soup = BeautifulSoup(html, 'lxml') 
  
  #데이터 찾기 (title, traffic)
  search_trend = soup.find_all('title')
  search_traffic = soup.find_all('ht:approx_traffic')

  #배열을 만들자
  dick = {}
  for i in search_trend:
    a = i.get_text()
    for j in search_traffic:
      dick[a] = j.get_text()
  
  return dick

a = searchTrend()
print(a)


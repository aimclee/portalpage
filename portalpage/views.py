from django.shortcuts import render, redirect
import requests
from .crawling import searchTrend, search_news

# Create your views here.

# rss 모음
googletrend = 'https://trends.google.com/trends/trendingsearches/daily/rss?geo=VN'
vnexpress = 'https://vnexpress.net/rss/tin-moi-nhat.rss' #https://vnexpress.net/rss
thanhnien = 'https://thanhnien.vn/rss/home.rss' #https://thanhnien.vn/rss.html
tuoitre = 'https://tuoitre.vn/rss/tin-moi-nhat.rss' #https://tuoitre.vn/rss.htm
vtc = 'https://vtc.vn/rss/feed.rss' #https://www.nhandan.org.vn/rss
baotintuc = 'https://baotintuc.vn/tin-moi-nhat.rss'
baodautu = 'https://baodautu.vn/trang-chu.rss'
forbesvietnam = 'https://forbesvietnam.com.vn/rss/home.rss'

def home(request):
    # 구글 검색 (CSRF 오류남)
    if request.method == 'POST':
        keyword = ' ' #이부분에 뭐가 들어가야 html에서 입력한 값이 들어오나요?
        queryString = {'q': keyword}
        searchEngine = 'https://www.google.com/search'
        r = requests.get(searchEngine, params = queryString)
        return redirect(r.url)

    trends = searchTrend(googletrend)
    print(trends)
    news_vnexpress = search_news(vnexpress)
    news_thanhnien = search_news(thanhnien)
    
    return render(request, 'home.html', {'trends':trends, 'vnexpress':news_vnexpress, 'thanhnien':news_thanhnien})
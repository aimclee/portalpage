from django.shortcuts import render, redirect, get_object_or_404
import requests
from .crawling import searchTrend, news_searching
from .models import mainBanner, rollingBanner, subBanner

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

    # 배너처리
    main_banner = mainBanner.objects.all()
    rolling_banner = rollingBanner.objects.all()
    sub_banner = subBanner.objects.all()

    # 구글트렌드 반환
    # searchTrend(googletrend)는 검색어, 조회수 2가지를 반환함
    google_trends = searchTrend(googletrend)

    search_vnexpress = news_searching(vnexpress)
    search_thanhnien = news_searching(thanhnien)

    return render(request, 'home.html', {'google_trends':google_trends, 'main_banner':main_banner, 'sub_banner':sub_banner, 'search_vnexpress':search_vnexpress, 'search_thanhnien':search_thanhnien})
from django.shortcuts import render, redirect, get_object_or_404
import requests
from .crawling import search_trends, search_main, thegioi, giaitri, thethao, congnghe, doisong, suckhoe
from .models import mainBanner, rollingBanner, subBanner
from django.views.decorators.csrf import csrf_exempt


# 주소 모음
vnexpress = 'https://vnexpress.net/rss/tin-moi-nhat.rss' #https://vnexpress.net/rss
thanhnien = 'https://thanhnien.vn/rss/home.rss' #https://thanhnien.vn/rss.html
tuoitre = 'https://tuoitre.vn/rss/tin-moi-nhat.rss' #https://tuoitre.vn/rss.htm
vtc = 'https://vtc.vn/rss/feed.rss' #https://www.nhandan.org.vn/rss
baotintuc = 'https://baotintuc.vn/tin-moi-nhat.rss'
baodautu = 'https://baodautu.vn/trang-chu.rss'
forbesvietnam = 'https://forbesvietnam.com.vn/rss/home.rss'
zing = 'https://zingnews.vn/'

@csrf_exempt
def home(request):
    if request.method == 'POST':
        keyword = request.POST.get('keyword')
        queryString = {'q': keyword}
        searchEngine = 'https://www.google.com/search?'
        r = requests.get(searchEngine, params = queryString)
        return redirect(r.url)

    # 배너처리
    main_banner = mainBanner.objects.all().order_by('?')
    rolling_banner = rollingBanner.objects.all()
    sub_banner = subBanner.objects.all().order_by('?')

    # 구글트렌드 반환
    # searchTrend(googletrend)는 검색어, 조회수 2가지를 반환함
    trends = search_trends()

    # 카테고리 서치
    news_main = search_main()
    news_thegioi = thegioi()
    news_giaitri = giaitri()
    news_thethao = thethao()
    news_congnghe = congnghe()
    news_doisong = doisong()
    news_suckhoe = suckhoe()

    # 랜덤 배너 이미지 로딩
    # bannerImgs = Images.objects.order_by('?')[0]

    return render(request, 'home.html',{
        'trends':trends,
        'news_main':news_main,
        'main_banner':main_banner,
        'sub_banner':sub_banner,
        'news_thegioi':news_thegioi,
        'news_giaitri':news_giaitri,
        'news_thethao':news_thethao,
        'news_congnghe':news_congnghe,
        'news_doisong':news_doisong,
        'news_suckhoe':news_suckhoe,
        })
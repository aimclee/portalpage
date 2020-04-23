from django.shortcuts import render, redirect, get_object_or_404
import requests
from .crawling import vnExpress, search_trends, zingNews, tuoiTre, thanhNien
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
        keyword = request.POST.get('keyword') #이부분에 뭐가 들어가야 html에서 입력한 값이 들어오나요?
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
    trends = search_trends()

    # 뉴스 서치
    search_vnexpress = vnExpress()
    # 
    search_zing = zingNews()
    search_tuoitre = tuoiTre()
    search_thanhnien = thanhNien()

    return render(request, 'home.html',{
        'trends':trends,
        'main_banner':main_banner,
        'sub_banner':sub_banner,
        'search_vnexpress':search_vnexpress,
        'search_zing':search_zing,
        'search_tuoitre':search_tuoitre,
        'search_thanhnien':search_thanhnien,
        })
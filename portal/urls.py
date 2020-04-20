from django.contrib import admin
from django.urls import path
from django.conf import settings #이미지 링크 연결을 위한 settings.py 불러오기
from django.conf.urls.static import static
from portalpage import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

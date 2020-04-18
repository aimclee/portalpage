from django.shortcuts import render
from .crawling import searchTrend

# Create your views here.

def home(request):
    keyword = searchTrend()
    return render(request, 'home.html', {'keyword':keyword})
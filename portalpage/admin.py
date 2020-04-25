from django.contrib import admin
from .models import mainBanner, rollingBanner, subBanner, accessTrade

# Register your models here.
admin.site.register(mainBanner)
admin.site.register(rollingBanner)
admin.site.register(subBanner)
admin.site.register(accessTrade)
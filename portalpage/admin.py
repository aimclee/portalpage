from django.contrib import admin
from .models import mainBanner, rollingBanner, subBanner

# Register your models here.
admin.site.register(mainBanner)
admin.site.register(rollingBanner)
admin.site.register(subBanner)
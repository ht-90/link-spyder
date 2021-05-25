"""spyder app urls
"""
from django.urls import path

from spyder.views import IndexView, crawl_sitemap

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('sitemapper', crawl_sitemap, name="crawl"),
]

"""spyder app urls
"""
from django.urls import path

from spyder.views import Index, crawl_sitemap

urlpatterns = [
    path('', Index.as_view(), name="index"),
    path('sitemapper', crawl_sitemap, name="crawl"),
]

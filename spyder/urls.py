"""spyder app urls
"""
from django.urls import path, include

from spyder.views import Index

urlpatterns = [
    path('', Index.as_view(), name="index")
]

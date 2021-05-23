"""linkspyder URL Configuration

"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Spyder
    path('', include('spyder.urls'))
]

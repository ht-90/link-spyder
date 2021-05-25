from django.contrib import admin

from . import models


@admin.register(models.Sitemap)
class SitemapAdmin(admin.ModelAdmin):
    pass

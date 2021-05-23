from django.db import models


class Sitemap(models.Model):
    id = models.AutoField(
        primary_key=True,
        auto_created=True
    )
    address = models.CharField(
        max_length=500,
        null=False,
        blank=False,
        default="",
    )
    datetime_crawled = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return self.address

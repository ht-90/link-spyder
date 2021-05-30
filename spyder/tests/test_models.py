from django.test import TestCase

from .. import models


class TestSitemap(TestCase):

    def setUp(self):
        self.test_sitemap = models.Sitemap.objects.create(
            address="https://domain.com",
        )

    def test_auto_id(self):
        sitemap = models.Sitemap.objects.get(address="https://domain.com")
        self.assertEqual(sitemap.id, 1)
        self.assertEqual(sitemap.address, "https://domain.com")

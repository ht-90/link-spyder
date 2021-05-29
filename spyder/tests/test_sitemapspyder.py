from django.test import TestCase

from ..sitemapspyder import SitemapSpyder


URL = "https://test.com"

MAX_CRAWL = 5

class TestSitemapSpyder(TestCase):

    def setUp(self):
        self.crawler = SitemapSpyder(
            url=URL,
            max_crawl=MAX_CRAWL,
        )

    def test_retrieve_domain(self):
        """Test extracting domain name from url"""
        domain = self.crawler.retrieve_domain()
        self.assertEqual(domain, "test.com")


from django.test import TestCase, Client


class TestIndexView(TestCase):
    """Test index page view"""

    def test_request(self):
        client = Client()
        response = client.get("")
        self.assertEqual(response.status_code, 200)


class TestCrawlSitemap(TestCase):
    """Test crawl_sitemap api"""

    def test_post_request(self):
        client = Client()
        response = client.post("/sitemapper", {"key": "value"})
        self.assertEqual(response.status_code, 200)

    def test_get_request(self):
        """Test redirect for get request"""
        client = Client()
        response = client.get("/sitemapper")
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, "/")

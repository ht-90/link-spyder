from django.test import TestCase

from ..sitemapspyder import SitemapSpyder


URL = "https://test.com"

MAX_CRAWL = 5

SITEMAP = """
  <urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">
    <url>
      <loc>https://test.com/page1/</loc>
      <lastmod>2020-05-01T09:00:00+10:00</lastmod>
    </url>
    <url>
       <loc>https://test.com/page2/</loc>
       <lastmod>2020-05-02T14:00:00+10:00</lastmod>
     </url>
    <url>
      <loc>https://test.com/page3/</loc>
      <lastmod>2020-05-03T20:00:00+10:00</lastmod>
    </url>
  </urlset>
"""


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

    def test_parse_sitemap_loc(self):
        """Ensure all urls in sitemap are extracted"""
        locs_url = self.crawler.parse_sitemap(sitemap=SITEMAP)
        self.assertEqual(len(locs_url), 3)

    def test_parse_sitemap_strip(self):
        """Ensure '/' is stripped out from all urls in sitemap"""
        locs_url = self.crawler.parse_sitemap(sitemap=SITEMAP)
        last_letters = [url[-1] for url in locs_url]
        self.assertTrue("/" not in last_letters)

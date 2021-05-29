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

PAGE_1 = """
  <!DOCTYPE html>
  <html lang="en">
    <head>
      <meta charset="utf-8">
      <title>PAGE_1</title>
      <meta name="description" content="Page 1 Description">
    </head>
    <body>
      <div>
        <a href="https://page_2">Internal Link to Page 2</a>
        <a href="https://page_3">Internal Link to Page 3</a>
      </div>
    </body>
  </html>
"""

PAGE_2 = """
  <!DOCTYPE html>
  <html lang="en">
    <head>
      <meta charset="utf-8">
      <title>PAGE_2</title>
      <meta name="description" content="Page 2 Description">
    </head>
    <body>
      <div>
        <a href="https://page_1">Internal Link to Page 1</a>
        <a href="https://page_3">Internal Link to Page 3</a>
      </div>
    </body>
  </html>
"""

PAGE_3 = """
  <!DOCTYPE html>
  <html lang="en">
    <head>
      <meta charset="utf-8">
      <title>PAGE_3</title>
      <meta name="description" content="Page 1 Description">
    </head>
    <body>
      <div>
        <a href="https://page_1">Internal Link to Page 1</a>
        <a href="https://page_2">Internal Link to Page 2</a>
      </div>
    </body>
  </html>
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

    def test_extract_a_tags(self):
        """Ensure anchor tags and hrefs are extracted from a page"""
        soup = BeautifulSoup(PAGE_1, "html.parser")
        a_tags = self.crawler.extract_a_tags(soup=soup)
        self.assertEqual(len(a_tags), 2)
        self.assertEqual(a_tags[0].get("href"), "https://page_2")
        self.assertEqual(a_tags[1].get("href"), "https://page_3")

    def test_retrieve_a_tags(self):
        """Test retrieval of anchor tags and formation of origin page to destination pages list"""
        locs_url = self.crawler.parse_sitemap(sitemap=SITEMAP)
        pages = [
            [locs_url[0], BeautifulSoup(PAGE_1, "html.parser")],
            [locs_url[0], BeautifulSoup(PAGE_2, "html.parser")],
            [locs_url[0], BeautifulSoup(PAGE_3, "html.parser")],
        ]
        list_page_od = self.crawler.retrieve_a_tags(parsed_pages=pages)
        self.assertEqual(len(list_page_od), 3)
        self.assertEqual(len(list_page_od[0][1]), 2)
        self.assertEqual(len(list_page_od[1][1]), 2)
        self.assertEqual(len(list_page_od[2][1]), 2)

    def test_convert_to_absolute_url(self):
        """Test conversion of relative URL to absolute URL"""
        href_rel_url = "/page_1"
        abs_url = self.crawler.convert_to_absolute_url(href=href_rel_url)
        self.assertEqual(abs_url, "https://test.com/page_1")


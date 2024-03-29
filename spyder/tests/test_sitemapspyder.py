from django.test import TestCase
from bs4 import BeautifulSoup

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

    def test_normalize_url(self):
        """Test normalization of ugly URLs"""
        # Prepare ugly URLs
        url_slash = URL + "/"
        url_double_slash = URL + "//" + "page_1"
        url_param = URL + "/" + "page_1" + "/" + "?param=abc"

        # Normalize ugly URLs
        norm_url_slash = self.crawler.normalize_url(url=url_slash)
        norm_url_double_slash = self.crawler.normalize_url(url=url_double_slash)
        norm_url_param = self.crawler.normalize_url(url=url_param)

        self.assertEqual(norm_url_slash, "https://test.com")
        self.assertEqual(norm_url_double_slash, "https://test.com/page_1")
        self.assertEqual(norm_url_param, "https://test.com/page_1")

    def test_page_url_validator(self):
        """Ensure page URL validator catches invalid URL"""
        # Prepare valid URLs
        valid_url = "https://test.com/page_1/post_1"

        # Prepare invalid URLs
        invalid_url_netloc = "http://test/page_1"
        invalid_url_scheme = "test.com"
        invalid_url_localhost_1 = "http://localhost:8000"
        invalid_url_localhost_2 = "http://127.0.0.1:8000"

        # Run validator
        self.assertTrue(self.crawler._page_is_valid(url=valid_url))
        self.assertFalse(self.crawler._page_is_valid(url=invalid_url_netloc))
        self.assertFalse(self.crawler._page_is_valid(url=invalid_url_scheme))
        self.assertFalse(self.crawler._page_is_valid(url=invalid_url_localhost_1))
        self.assertFalse(self.crawler._page_is_valid(url=invalid_url_localhost_2))

    def test_extract_internal_links(self):
        """Ensure only extracting internal link URL and ignore same URL as url arg"""
        # Prepare test data
        domain = "test.com"
        hrefs = [
            "https://test.com",
            "https://test.com/page_1",
            "https://subdomain.test.com/page_1",
            "https://test.net/page_1",
        ]
        url = "https://test.com"

        # Filter internal links
        internal_links = self.crawler.extract_internal_links(hrefs=hrefs, domain_name=domain, url=url)

        # Test extraction of URL with same domain and excluding URL same as url arg
        self.assertEqual(len(internal_links), 2)
        self.assertEqual(internal_links[0], "https://subdomain.test.com/page_1")
        self.assertEqual(internal_links[1], "https://test.com/page_1")

    def test_extract_external_links(self):
        """Ensure only extracting external link URL"""
        # Prepare test data
        domain = "test.com"
        hrefs = [
            "https://test.com",
            "https://test.com/page_1",
            "https://subdomain.test.com/page_1",
            "https://test.net/page_1",
        ]
        url = "https://test.com"

        # Filter internal links
        external_links = self.crawler.extract_external_links(hrefs=hrefs, domain_name=domain, url=url)

        # Test extraction of URL with different domain from url arg
        self.assertEqual(len(external_links), 1)
        self.assertEqual(external_links[0], "https://test.net/page_1")

    def test_trim_url_scheme(self):
        """Test trimming http and https from URL"""
        url_with_http = "http://test.com/page"
        url_with_https = "https://test.com/page"
        url_without_scheme = "test.com/page"
        self.assertTrue(self.crawler.trim_url_scheme(url=url_with_http), "test.com/page")
        self.assertTrue(self.crawler.trim_url_scheme(url=url_with_https), "test.com/page")
        self.assertTrue(self.crawler.trim_url_scheme(url=url_without_scheme), "test.com/page")

    def test_create_node_categories_normalized_url(self):
        """Test extraction of parent layer of website structure for normalized URLs"""
        sitemap_urls = [
            "test.com/category/page_1",
            "test.com/category/page_2",
            "test.com/archive/2020/page_3",
            "test.com/page_4",
            "test.com",
        ]
        categories = self.crawler.create_node_categories(locs_url=sitemap_urls)

        # Ensure total number of categories extracted
        self.assertEqual(len(categories), 5)

        # Ensure "other" category is added
        self.assertTrue("other" in categories.keys())

        # Ensure categories are stored with ascending order
        self.assertEqual(categories["archive"], 0)
        self.assertEqual(categories["category"], 1)
        self.assertEqual(categories["page_4"], 2)  # anything after domain is considered category...
        self.assertEqual(categories["other"], 3)
        self.assertEqual(categories["/"], 4)

    def test_create_node_categories_ugly_url(self):
        """Test extraction of parent layer of website structure for ugly URLs"""
        sitemap_urls = [
            "test.com/",  # slash at the end
            "http://test.com/category/page_1",  # URL with scheme
            "archive/page_2",  # missing domain
        ]
        categories = self.crawler.create_node_categories(locs_url=sitemap_urls)

        # Ensure total number of categories extracted
        self.assertEqual(len(categories), 4)

        # Ensure "other" category is added
        self.assertTrue("other" in categories.keys())
        self.assertFalse("category" in categories.keys())  # category is ignored as URL contains scheme
        self.assertFalse("archive" in categories.keys())  # archive is ignored as domain is missing in URL
        self.assertEqual(categories[""], 0)  # ensure trailing "/" is trimmed before using this function

    def test_create_nodes(self):
        """Test creation of node data"""
        sitemap_urls = [
            "test.com/category/page_1",
            "test.com/category/page_2",
            "test.com/archive/2020/page_3",
            "test.com/page_4",
            "test.com",
        ]
        categories = {
            'archive': 0,
            'category': 1,
            'page_4': 2,
            'other': 3,
            '/': 4,
        }
        nodes = self.crawler.create_nodes(sitemap_locs=sitemap_urls, categories=categories)

        self.assertEqual(len(nodes), 5)
        self.assertEqual(nodes[0], {"id": sitemap_urls[0],
                                    "category": 1,
                                    "parent": "/category",
                                    "page": "/page_1",
                                    "size": 1})
        self.assertEqual(nodes[1], {"id": sitemap_urls[1],
                                    "category": 1,
                                    "parent": "/category",
                                    "page": "/page_2",
                                    "size": 1})
        self.assertEqual(nodes[2], {"id": sitemap_urls[2],
                                    "category": 0,
                                    "parent": "/archive",
                                    "page": "/page_3",
                                    "size": 1})
        self.assertEqual(nodes[3], {"id": sitemap_urls[3],
                                    "category": 2,
                                    "parent": "/page_4",  # !!! update so parent to be "/"
                                    "page": "/page_4",
                                    "size": 1})
        self.assertEqual(nodes[4], {"id": sitemap_urls[4],
                                    "category": 4,
                                    "parent": "/",
                                    "page": "/",
                                    "size": 1})

    def test_create_edges(self):
        """Test creation of edge data"""
        links = [
            {
                "source": "https://test.com/category/page_1",
                "value": 1,
                "target": ["test.com/category/page_2"]
            },
            {
                "source": "https://test.com/category/page_2",
                "value": 1,
                "target": ["test.com/category/page_1"]
            },
            {
                "source": "https://test.com/archive/page_3",
                "value": 1,
                "target": ["test.com/category/page_1", "test.com/category/page_2"]
            },
            {
                "source": "https://test.com/tag",
                "value": 1,
                "target": []
            },
        ]
        nodes = [
            {"id": "test.com/category/page_1", "category": 1, "parent": "/category", "page": "/page_1", "size": 1},
            {"id": "test.com/category/page_2", "category": 1, "parent": "/category", "page": "/page_2", "size": 1},
            {"id": "test.com/archive/page_3", "category": 0, "parent": "/archive", "page": "/page_3", "size": 1},
            {"id": "test.com/tag", "category": 2, "parent": "/tag", "page": "/tag", "size": 1},
        ]
        categories = {
            'archive': 0,
            'category': 1,
            'tag': 2,
            'other': 3,
            '/': 4,
        }
        edges = self.crawler.create_edges(links=links, nodes=nodes, categories=categories)

        self.assertEqual(len(edges), 4)
        self.assertEqual(edges[0], {'source': 'test.com/category/page_1',
                                    'source_category': 1,
                                    'target': 'test.com/category/page_2',
                                    'target_category': 1,
                                    'value': 1})
        self.assertEqual(edges[1], {'source': 'test.com/category/page_2',
                                    'source_category': 1,
                                    'target': 'test.com/category/page_1',
                                    'target_category': 1,
                                    'value': 1})
        self.assertEqual(edges[2], {'source': 'test.com/archive/page_3',
                                    'source_category': 0,
                                    'target': 'test.com/category/page_1',
                                    'target_category': 1,
                                    'value': 1})
        self.assertEqual(edges[3], {'source': 'test.com/archive/page_3',
                                    'source_category': 0,
                                    'target': 'test.com/category/page_2',
                                    'target_category': 1,
                                    'value': 1})

    def test_create_group_data(self):
        """Test creation of group data for graph visualization"""
        categories = {
            'archive': 0,
            'category': 1,
            'tag': 2,
            'other': 3,
            '/': 4,
        }
        groups = self.crawler.create_group_data(categories=categories)

        self.assertEqual(len(groups), 5)
        self.assertEqual(list(groups[0].keys()), ["category", "category_url"])
        self.assertTrue(type(groups[0]["category"]), int)
        self.assertTrue(type(groups[0]["category_url"]), str)

    def test_size_nodes(self):
        """Test updating size value of nodes"""
        links = [
            {
                'source': 'test.com/category/page_1',
                'source_category': 1,
                'target': 'test.com/category/page_2',
                'target_category': 1,
                'value': 1,
            },
            {
                'source': 'test.com/category/page_2',
                'source_category': 1,
                'target': 'test.com/category/page_1',
                'target_category': 1,
                'value': 1,
            },
            {
                'source': 'test.com/archive/page_3',
                'source_category': 0,
                'target': 'test.com/category/page_1',
                'target_category': 1,
                'value': 1,
            },
            {
                'source': 'test.com/archive/page_3',
                'source_category': 0,
                'target': 'test.com/category/page_2',
                'target_category': 1,
                'value': 1,
            },
        ]
        nodes = [
            {"id": "test.com/category/page_1", "category": 1, "parent": "/category", "page": "/page_1", "size": 1},
            {"id": "test.com/category/page_2", "category": 1, "parent": "/category", "page": "/page_2", "size": 1},
            {"id": "test.com/archive/page_3", "category": 0, "parent": "/archive", "page": "/page_3", "size": 1},
            {"id": "test.com/tag", "category": 2, "parent": "/tag", "page": "/tag", "size": 1},
        ]
        updated_nodes = self.crawler.size_nodes(links=links, nodes=nodes)

        self.assertEqual(len(updated_nodes), 4)
        self.assertEqual(updated_nodes[0]["size"], 1)
        self.assertEqual(updated_nodes[1]["size"], 1)
        self.assertEqual(updated_nodes[2]["size"], 2)
        self.assertEqual(updated_nodes[3]["size"], 0)  # !!! node size is 0 if URL page not having any internal link

    def test_generate_graph_data(self):
        """Test creation of graph visualization data"""
        nodes = [
            {"id": "test.com/category/page_1", "category": 1, "parent": "/category", "page": "/page_1", "size": 1},
            {"id": "test.com/category/page_2", "category": 1, "parent": "/category", "page": "/page_2", "size": 1},
        ]
        edges = [
            {
                'source': 'test.com/category/page_1',
                'source_category': 1,
                'target': 'test.com/category/page_2',
                'target_category': 1,
                'value': 1,
            },
            {
                'source': 'test.com/category/page_2',
                'source_category': 1,
                'target': 'test.com/category/page_1',
                'target_category': 1,
                'value': 1,
            },
        ]
        graph_data = self.crawler.generate_graph_data(nodes=nodes, edges=edges)

        self.assertEqual(list(graph_data.keys()), ["nodes", "links"])
        self.assertEqual(len(graph_data["nodes"]), 2)
        self.assertEqual(len(graph_data["links"]), 2)

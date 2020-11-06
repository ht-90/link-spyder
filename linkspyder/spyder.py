"""
spyder.py

@author: ht-90
"""


import requests
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup
from webweb import Web


class Spyder:
    """A web scraping object for a URL

    Attributes:
        url (str): a starting URL to parse content
        max_crawl (int): a number of maximum depth of crawl for internal links
        domain_name (str): a name of domain
        soup (bs4 object): html content
        internal_links (list): a list of internal link urls
        external_links (list): a list of external link urls
        scraped_link (list): an array of link urls already scraped
        edges_list (list): contains an array of an origin URL and a destinatio
                           URL

    """

    def __init__(self, url):
        """Initialise a web scraper object"""
        self.url = url
        self.max_crawl = 4
        self.domain_name = str()
        self.soup = str()
        self.internal_links = list()
        self.external_links = list()
        self.scraped_link = list()
        self.edges_list = list()
        self.edges_list_clean = list()

    def retrieve_domain(self):
        """Retrieve a domain name from the URL"""
        self.domain_name = urlparse(self.url).netloc
    
    def parse_page(self):
        """Parse the page content"""
        self.soup = BeautifulSoup(
            requests.get(self.url).content, "html.parser"
        )

    def retrieve_all_links(self, url):
        """Retrieve all href from a page"""
        for a_tag in self.soup.findAll("a"):
            href = a_tag.attrs.get("href")
            if self._href_exists(href=href):
                continue
            
            # join the URL if it's relative (not absolute link)
            href = urljoin(url, href)
            # parse href
            parsed_href = urlparse(href)
            # remove URL GET parameters, URL fragments, etc.
            href = parsed_href.scheme + "://" + parsed_href.netloc + parsed_href.path

            if not self._page_is_valid(url=href):
                # not a valid URL
                continue
            if href in self.internal_links:
                # already in the set
                continue
            if self.domain_name not in href:
                # external link
                if href not in self.external_links:
                    self.external_links.append(href)
                continue

            self.internal_links.append(href)

    def _href_exists(self, href):
        """Validate a href"""
        return href == "" or href is None

    def _page_is_valid(self, url):
        """Validate a page URL"""
        parsed = urlparse(url)
        return bool(parsed.netloc) and bool(parsed.scheme)

    def initial_crawl(self):
        """Crawl the starting URL page and extract href links

        Examples:
            >>> from linkspyder.spyder import Spyder
            >>> spyder = Spyder(url="https://abcde.com/")
            >>> spyder.initial_crawl()

        """
        # Retrieve domain of the URL
        self.retrieve_domain()
        # Scrape the URL
        self.parse_page()
        # Crawl the URL and scrape internal and external links
        self.retrieve_all_links(url=self.url)
        # Add URL to the completed URL list
        self.scraped_link.append(self.url)
        # Remove the URL from the target pages
        self.internal_links = [i_link for i_link in self.internal_links if i_link not in self.scraped_link]
        # Store scraped internal links with the page (edges)
        edges = {"name": self.url, "size": 100, "imports": self.internal_links}
        # Add the URL to internal_link edges to result list
        self.edges_list.append(edges)

    def deep_crawl(self):
        crawler = 1
        for i_URL in self.internal_links:
            if i_URL not in self.scraped_link:
                self.retrieve_all_links(url=i_URL)
                # Store scraped internal links with the page (edges) and add to result list
                edges = {"name": i_URL, "size": 100, "imports": self.internal_links}
                self.edges_list.append(edges)
                # Remove the crawled URL from the list of target pages
                self.scraped_link.append(i_URL)
                # if reached to max crawl, break
                crawler += 1
                if crawler > self.max_crawl:
                    break
                continue
            continue

        # Concatenate all list of edges_list
        self.edges_list = sum(self.edges_list, [])

    def create_web(self):
        """Create a graph from a list of edges"""
        return Web(
            adjacency=self.edges_list,
            title='Web-Viz | Link Spyder',
            display={
                # Node design
                "sizeBy": "degree",
                "radius": 10,
                "colorBy": "degree",
                "colorPalette": "Accent",
                # Node control
                "charge": 300,
                "gravity": 0.005,
                # Link design
                "linkLength": 80,
                "linkStrength": 0.2,
                "scaleLinkWidth": True,
                "scaleLinkOpacity": True,
                # Layout
                "hideMenu": True,
                "showLegend": False
            }
        ).html

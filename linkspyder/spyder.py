"""
spyder.py

@author: ht-90
"""


class Spyder:
    """A web scraping object for a URL

    Attributes:
        url (str): a starting URL to parse content
        domain_name (str): a name of domain
        soup (bs4 object): html content
        internal_links
        external_links

    """

    url = None
    domain_name = None
    soup = None
    internal_links = list()
    external_links = list()

    def __init__(self, url):
        """Initialise a web scraper object"""
        self.url = url

    def retrieve_domain(self):
        """Retrieve a domain name from the URL"""
        self.domain_name = urlparse(self.url).netloc
    
    def parse_page(self):
        """Parse the page content"""
        self.soup = BeautifulSoup(
            requests.get(self.url).content, "html.parser"
        )

    def retrieve_all_links(self):
        """Retrieve all href from a page"""
        for a_tag in self.soup.findAll("a"):
            href = a_tag.attrs.get("href")
            if self._href_exists(href=href):
                continue
            
            # join the URL if it's relative (not absolute link)
            href = urljoin(self.url, href)
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

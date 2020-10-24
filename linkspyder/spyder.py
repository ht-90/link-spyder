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
        internal_links (list): a list of internal link urls
        external_links (list): a list of external link urls

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
        edges = [[self.url, link] for link in self.internal_links]
        # Add the URL to internal_link edges to result list
        self.edges_list.append(edges)


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

    """

    url = None
    domain_name = None
    soup = None

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


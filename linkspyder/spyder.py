"""
spyder.py

@author: ht-90
"""


import requests
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup


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
        self.nodes = dict()
        self.links = dict()
        self.id_urls = dict()

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
        edges = {"source": self.url, "value": 1, "target": self.internal_links}
        # Add the URL to internal_link edges to result list
        self.edges_list.append(edges)

    def deep_crawl(self):
        crawler = 1
        for i_URL in self.internal_links:
            if i_URL not in self.scraped_link:
                self.retrieve_all_links(url=i_URL)
                # Store scraped internal links with the page (edges) and add to result list
                edges = {"source": i_URL, "value": 1, "target": self.internal_links}
                self.edges_list.append(edges)
                # Remove the crawled URL from the list of target pages
                self.scraped_link.append(i_URL)
                # if reached to max crawl, break
                crawler += 1
                if crawler > self.max_crawl:
                    break
                continue
            continue

        # # Concatenate all list of edges_list
        # self.edges_list = sum(self.edges_list, [])

    def generate_nodes_links(self):
        links_array = []
        nodes_array = []
        nodes_reg = []
        for item in self.edges_list:
            # Clean up scraped URL
            source_clean = (
                item['source']
                .replace("https://", "")
                .replace("http://", "")
                .replace("www.", "")
                .replace(".html", "")
                .strip("/")
            )
            # Remove duplicated URLs in the internal_link array
            target_clean = [
                tgt
                .replace("https://", "")
                .replace("http://", "")
                .replace("www.", "")
                .replace(".html", "")
                .strip("/") for tgt in sorted(item['target'])
            ]
            target_clean = [tgt for tgt in target_clean if tgt != source_clean] # remove self-link
            target_clean = list(set(target_clean)) # remove duplicated URLs
            # Append link in a required format
            for tgt in target_clean:
                link = {
                    "source": source_clean,
                    "target": tgt,
                    "value": 1,
                }
                node = {
                    "id": tgt,
                    "category": 1
                }
                # Register link
                links_array.append(link)
                # Register target URL as node (avoid duplicates)
                if tgt not in nodes_reg:
                    nodes_array.append(node)
                nodes_reg.append(tgt)

            # Add cleaned links data
            self.links = {"links": links_array}
            # Register source URL as node
            if source_clean not in nodes_reg:
                nodes_array.append({
                    "id": source_clean,
                    "category": 1
                })

        # Add cleaned nodes data
        self.nodes = {"nodes": nodes_array}

    def categorise_nodes(self):
        """Update category value and strip parent URL of node"""
        cat_urls = []
        id_num = 0
        for i_node, node in enumerate(self.nodes["nodes"]):
            # Find the last index of "/" as URL category
            i_last_slash = node['id'].rfind("/")
            # Get category URL category URL of source and target URL of edge
            if i_last_slash >= 0:
                cat_url = node['id'][:i_last_slash]
                page_name = node['id'][i_last_slash:]
            else:
                cat_url = page_name = node['id']
            # If URL already found, use relevant id number, otherwise assign new id number and update "category" value in the edge data
            if cat_url not in self.id_urls.keys():
                self.id_urls.update({cat_url: id_num})
                self.nodes["nodes"][i_node]["category"] = id_num
                self.nodes["nodes"][i_node]["id"] = page_name
                id_num += 1
            else:
                self.nodes["nodes"][i_node]["category"] = self.id_urls[cat_url]
                self.nodes["nodes"][i_node]["id"] = page_name

    def categorise_links(self):
        cat_urls = []
        id_num = 0

        for i_link, link in enumerate(self.links["links"]):
            i_src_last_slash = link["source"].rfind("/")
            i_tgt_last_slash = link["target"].rfind("/")

            if i_src_last_slash >= 0:
                cat_src_url = link['source'][:i_src_last_slash]
                src_page_name = link['source'][i_src_last_slash:]
            else:
                cat_src_url = src_page_name = link['source']
            if i_tgt_last_slash >= 0:
                cat_tgt_url = link['target'][:i_tgt_last_slash]
                tgt_page_name = link['target'][i_tgt_last_slash:]
            else:
                cat_tgt_url = tgt_page_name = link['target']
            
            self.links["links"][i_link]["source_category"] = self.id_urls[cat_src_url]
            self.links["links"][i_link]["source"] = src_page_name
            self.links["links"][i_link]["target_category"] = self.id_urls[cat_tgt_url]
            self.links["links"][i_link]["target"] = tgt_page_name

    def generate_graph_data(self):
        graph_data = {}
        graph_data.update(self.nodes)
        graph_data.update(self.links)

        return graph_data

from bs4 import BeautifulSoup
import requests
from urllib.parse import urlparse, urljoin
from concurrent.futures import ThreadPoolExecutor, as_completed


class SitemapSpyder:
    def __init__(self, url, max_crawl):
        self.url = url
        self.max_crawl = max_crawl

    def retrieve_domain(self):
        """Retrieve a domain name from the URL"""
        domain_name = urlparse(self.url).netloc
        return domain_name

    def parse_sitemap_xml(self):
        """Parse sitemap xml data as text"""
        if "sitemap.xml" in self.url:
            return requests.get(self.url).text
        else:
            print("Error reading a sitemap URL!!!")
            return False

    @staticmethod
    def parse_sitemap(sitemap):
        """Parse sitemap xml data to extract all page urls"""
        soup = BeautifulSoup(sitemap, features="lxml")
        if len(soup.find_all("loc")) > 0:
            locs = soup.find_all("loc")
            locs_url = sorted(list(set(
                [loc.contents[0].strip("/") for loc in locs]
            )))
            return locs_url
        else:
            print("No <loc> tag found in a sitemap!!!")
            return False

    # PARSE URL AND EXTRACT a tags
    def parse_page(self, url):
        """Parse the page content

        Args:
            url (str): URL of a page extracted from sitemap

        Returns:
            An array containing a normalized page URL and soup.

        """
        soup = BeautifulSoup(requests.get(url).content, "html.parser")
        return [self.normalize_url(url), soup]

    def parse_page_threading(self, urls):
        """
        Return:
            Returns a list of lists containing parsed url and html pages in a
            list

        Example:
            [
                ["https://domain.com": "parsed html as str"],
                ["https://domain.com/page1": "parsed html as str"],
                ["https://domain.com/page2": "parsed html as str"],
            ]
        """
        urls = urls[:self.max_crawl]
        MAX_THREADS = 30
        threads = min(MAX_THREADS, len(urls))
        parsed_pages = []
        with ThreadPoolExecutor(max_workers=threads) as executor:
            futures = []
            for url in urls:
                futures.append(executor.submit(self.parse_page, url))
            for future in as_completed(futures):
                parsed_pages.append(future.result())
        return parsed_pages

    @staticmethod
    def extract_a_tags(soup):
        # !!! UPDATE THIS TO EXTRACT FROM BLOG CONTENT AND OTHER
        # FOCUS ANALYSIS ON INTERNAL LINKS WITHIN CONTENT
        a_tags = soup.findAll("a")
        return a_tags

    def retrieve_a_tags(self, parsed_pages):
        """Retrieve all a tags from each parsed pages
        Args:
            parsed_pages (list): a list of parsed page html soups
        Return:
            a list of page url and a list of a tags
        Example:
            [
                [
                    "https:domain.com", [
                        <a href="https://domain.com/page1">page1</a>,
                        <a href="https://domain.com/page2">page2</a>,
                        <a href="https://domain.com/page3">page3</a>,
                    ]
                ],
                [
                    "https:domain.com/page1", [
                        <a href="https://domain.com/page1">page1</a>,
                        <a href="https://domain.com/page2">page2</a>,
                        <a href="https://domain.com/page3">page3</a>,
                    ]
                ],
            ]
        """
        return [
            [page[0], self.extract_a_tags(soup=page[1])]
            for page in parsed_pages
        ]

    # PARSE AND NORMALIZE href
    def convert_to_absolute_url(self, href):
        # join the URL if it's relative (not absolute link)
        return urljoin(self.url, href)

    @staticmethod
    def normalize_url(url):
        """Parse url components and normalize it
        scheme: http, https
        netloc: domain
        path: path after domain
        params: url params
        query
        fragment
        """
        parsed_url = urlparse(url)
        # remove URL GET parameters, URL fragments, etc.
        norm_url = (
            parsed_url.scheme
            + "://"
            + parsed_url.netloc
            + parsed_url.path.replace("//", "/")
        )
        norm_url = norm_url.strip("/")
        return norm_url

    # VALIDATE href
    @staticmethod
    def _page_is_valid(url):
        """Validate a page URL"""
        parsed = urlparse(url)
        return (
            bool(parsed.netloc) and bool(parsed.scheme)  # domain and sheme not empty
        ) and (
            (parsed.scheme == "http") or (parsed.scheme == "https")
        ) and (
            ("localhost:" not in parsed.netloc) and ("127.0.0.1:" not in parsed.netloc)
        ) and (
            "." in parsed.netloc
        )

    @staticmethod
    def _page_is_in_sitemap(url, sitemap_locs):
        """Check if url is included in sitemap"""
        return url in sitemap_locs

    # EXTRACT INTERNAL AND EXTERNAL LINKS (href)
    @staticmethod
    def extract_internal_links(hrefs, domain_name, url):
        """Extract only URLs containing the same domain name from a list of URLs"""
        return sorted(
            list(set(
                [
                    href for href in hrefs
                    if (domain_name in href) and (href != url)
                ]
            ))
        )

    @staticmethod
    def extract_external_links(hrefs, domain_name, url):
        return sorted(
            list(set(
                [
                    href
                    for href in hrefs
                    if (domain_name not in href) and (href != url)
                ]
            ))
        )

    @staticmethod
    def trim_url_scheme(url):
        """Trim http:// and https:// from URL"""
        return urlparse(url).netloc + urlparse(url).path

    # CREATE NODES AND EDGES
    @staticmethod
    def create_node_categories(locs_url):
        """Extract parent layer names of website structure

        Args:
            locs_url (list): a list of URLs without scheme (http:// or https://)

        Returns:
            A dict with layer names as keys and id number for them as values. Keys and values are stored in ascending
            order.

        Example:
            {'': 0, 'archive': 1, 'category': 2, 'contact': 3, 'other': 4, '/': 6}
        """
        # !!! Extract parent layer names assuming that parent layer is directly after domain
        cats = [loc.split("/")[1] for loc in locs_url if "/" in loc]
        cats = sorted(list(set(cats)))
        cats = {
            cat: cat_num for cat, cat_num in zip(cats, range(0, len(cats)))
        }
        # Append "other" layer and top-level layer with id values
        cats.update({"other": len(cats)})
        cats.update({"/": len(cats)})

        return cats

    @staticmethod
    def create_nodes(sitemap_locs, categories):
        """Create node data for graph visualization"""
        nodes = []
        for loc in sitemap_locs:
            if "/" not in loc:
                # Top page
                cat_id = categories["/"]
                parent = "/"
                page = "/"
            else:
                # Not top page - any depth
                cat_id = categories[loc.split("/")[1]]
                parent = "/" + loc.split("/")[1]
                page = "/" + loc.split("/")[-1]

            nodes.append(
                {
                    "id": loc,
                    "category": cat_id,
                    "parent": parent,
                    "page": page,
                    "size": 1,
                }
            )
        return nodes

    @staticmethod
    def create_edges(links, nodes, categories):
        """Create edges list and add source and target categories

        Example:
            [
                {
                    'source': 'domain.com/category_1/page_1',
                    'source_category': 1,
                    'target': 'domain.com/category_2/page_2',
                    'target_category': 2,
                    'value': 1
                },
                ...
            ]
        """
        edges_int = []
        nodes = [n["id"] for n in nodes]

        for link in links:
            src = urlparse(link["source"]).netloc\
                + urlparse(link["source"]).path

            if "/" in src:
                src_cat = categories[src.split("/")[1]]
            else:
                # Top page
                src_cat = categories["/"]

            for tgt in link["target"]:
                tgt = urlparse(tgt).netloc + urlparse(tgt).path
                # ignore if target url not in nodes (avoid error in d3)
                if tgt in nodes:
                    if ("/" in tgt) and (
                        urlparse(tgt).path.split("/")[1] in categories.keys()
                    ):
                        # Category exists on sitemap
                        tgt_cat = categories[urlparse(tgt).path.split("/")[1]]
                    elif (
                        ("/" in tgt) and
                        (
                            urlparse(tgt).path.split("/")[1]
                            not in categories.keys()
                        )
                    ):
                        # Not top page but category not on sitemap
                        tgt_cat = categories["other"]
                    else:
                        # Top page
                        tgt_cat = categories["/"]

                    edges_int.append(
                        {
                            "source": src,
                            "source_category": src_cat,
                            "target": tgt,
                            "target_category": tgt_cat,
                            "value": link["value"],
                        }
                    )

        return edges_int

    @staticmethod
    def create_group_data(categories):
        return [
            {"category": cat_num, "category_url": cat}
            for cat, cat_num in categories.items()
        ]

    @staticmethod
    def size_nodes(links, nodes):
        """Add number of target links per node as size"""
        link_src = [src["source"] for src in links]
        for i_node, node in enumerate(nodes):
            size = link_src.count(node["id"])
            nodes[i_node].update({"size": size})
        return nodes

    # CREATE GRAPH DATA
    @staticmethod
    def generate_graph_data(nodes, edges):
        graph_data = {}
        graph_data.update({"nodes": nodes})
        graph_data.update({"links": edges})

        return graph_data

from bs4 import BeautifulSoup
import requests
from urllib.parse import urlparse, urljoin
from concurrent.futures import ThreadPoolExecutor, as_completed


class SitemapSpyder:
    def __init__(self, url):
        self.url = url
        self.max_crawl = 4

    # PARSE SITEMAP AND DOMAIN NAME
    def parse_sitemap(self, url):
        # !!! MAKE IT WORK IF USER ENTER NON-TOP PAGE URL
        sitemap = urljoin(url, "sitemap.xml")
        xml_sitemap = requests.get(sitemap).text
        soup = BeautifulSoup(xml_sitemap, features="lxml")
        locs = soup.find_all("loc")
        locs_url = sorted(list(set([loc.contents[0].strip("/") for loc in locs])))
        return locs_url

    def retrieve_domain(self, url):
        """Retrieve a domain name from the URL"""
        domain_name = urlparse(url).netloc
        return domain_name

    # PARSE URL AND EXTRACT a tags
    def parse_page(self, url):
        """Parse the page content"""
        soup = BeautifulSoup(requests.get(url).content, "html.parser")
        return [self.normalize_url(url), soup]

    def parse_page_threading(self, urls):
        """
        Return:
            Returns a list of lists containing parsed url and html pages in a list
        Example:
            [
                ["https://domain.com": "parsed html as str"],
                ["https://domain.com/page1": "parsed html as str"],
                ["https://domain.com/page2": "parsed html as str"],
            ]
        """
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

    def extract_a_tags(self, soup):
        # !!! UPDATE THIS TO EXTRACT FROM BLOG CONTENT AND OTHER - FOCUS ANALYSIS ON INTERNAL LINKS WITHIN CONTENT
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
        return [[page[0], self.extract_a_tags(soup=page[1])] for page in parsed_pages]

    # PARSE AND NORMALIZE href
    def convert_to_absolute_url(self, url, href):
        # join the URL if it's relative (not absolute link)
        return urljoin(url, href)

    def normalize_url(self, url):
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
    def _page_is_valid(self, url):
        """Validate a page URL"""
        parsed = urlparse(url)
        return (bool(parsed.netloc) and bool(parsed.scheme)) and (
            (parsed.scheme == "http") or (parsed.scheme == "https")
        )

    def _page_is_in_sitemap(self, url, sitemap_locs):
        """Check if url is included in sitemap"""
        return url in sitemap_locs

    # EXTRACT INTERNAL AND EXTERNAL LINKS (href)
    def extract_internal_links(self, hrefs, domain_name, url):
        return sorted(
            list(
                set([href for href in hrefs if (domain_name in href) and (href != url)])
            )
        )

    def extract_external_links(self, hrefs, domain_name, url):
        return sorted(
            list(
                set(
                    [
                        href
                        for href in hrefs
                        if (domain_name not in href) and (href != url)
                    ]
                )
            )
        )

    def trim_url_scheme(self, url):
        return urlparse(url).netloc + urlparse(url).path

    # CREATE NODES AND EDGES
    def create_node_categories(self, locs_url):
        cats = [loc.split("/")[1] for loc in locs_url if "/" in loc]
        cats = sorted(list(set(cats)))
        cats = {cat: cat_num for cat, cat_num in zip(cats, range(0, len(cats)))}
        cats.update({"other": len(cats)})
        cats.update({"/": len(cats) + 1})
        return cats

    def create_nodes(self, sitemap_locs, categories, url):
        """
        url (str): user input url
        """
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

    def create_edges(self, links, nodes, categories):
        """Create edges list and add source and target categories"""
        edges_int = []
        nodes = [n["id"] for n in nodes]

        for l in links:
            src = urlparse(l["source"]).netloc + urlparse(l["source"]).path
            print(src)
            if "/" in src:
                src_cat = categories[src.split("/")[1]]
            else:
                # Top page
                src_cat = categories["/"]

            for tgt in l["target"]:
                tgt = urlparse(tgt).netloc + urlparse(tgt).path
                # ignore if target url not in nodes (avoid error in d3)
                if tgt in nodes:
                    if ("/" in tgt) and (
                        urlparse(tgt).path.split("/")[1] in categories.keys()
                    ):
                        # Category exists on sitemap
                        tgt_cat = categories[urlparse(tgt).path.split("/")[1]]
                    elif ("/" in tgt) and (
                        urlparse(tgt).path.split("/")[1] not in categories.keys()
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
                            "value": l["value"],
                        }
                    )

        return edges_int

    def create_group_data(self, domain_name, categories):
        return [
            {"category": cat_num, "category_url": cat}
            for cat, cat_num in categories.items()
        ]

    def size_nodes(self, links, nodes):
        """Add number of target links per node as size"""
        link_src = [src["source"] for src in links]
        for i_node, node in enumerate(nodes):
            size = link_src.count(node["id"])
            nodes[i_node].update({"size": size})
        return nodes

    # CREATE GRAPH DATA
    def generate_graph_data(self, nodes, edges):
        graph_data = {}
        graph_data.update({"nodes": nodes})
        graph_data.update({"links": edges})

        return graph_data

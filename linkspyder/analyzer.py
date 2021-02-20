"""
analyzer.py

@author: ht-90
"""


import numpy as np
from urllib.parse import urlparse


class Analyzer:
    """Analyze web crawl statistics

    Attributes:
        url (str): URL of a website
        graph_data (dict): crawl data for graph visualisation
        category_data (dict): crawl data for URL categories

    """

    def __init__(self, url, graph, cat):
        self.url = url
        self.graph_data = graph
        self.category_data = cat

    def _top_pages(self):
        """Return top level page urls"""
        return [
            cat for cat in self.category_data
            if "/" not in cat["category_url"]
        ]

    def _top_pages_sitemap(self):
        """Return top level page urls"""
        return urlparse(self.url).netloc

    def _pages_found(self):
        """Number of pages identified"""
        return len(self.graph_data["nodes"])

    def _links_found(self):
        """Number of internal links identified"""
        return len(self.graph_data["links"])

    def _crawled_pages(self):
        """Crawled pages"""
        return np.unique(
            [link["source"] for link in self.graph_data["links"]]
        ).tolist()

    def _target_pages(self):
        """Target pages"""
        return np.unique(
            [link["target"] for link in self.graph_data["links"]]
        ).tolist()

    def top_outgoing_pages(self, pages=5):
        """Top 5 pages with outgoing links"""
        top_outgoing = []
        for p in self._crawled_pages():
            src_pages = [
                link["source"] for link in self.graph_data["links"]
                if link["source"] == p
            ]
            top_outgoing.append([p, len(src_pages)])
        # Sort and extract result
        top_outgoing = np.array(top_outgoing)
        sort_top_og = top_outgoing[np.argsort(top_outgoing[:, 1])]
        filt_top_og = sort_top_og[::-1][:pages]

        return filt_top_og.tolist()

    def top_incoming_pages(self):
        """Top 5 pages with incoming links"""
        top_incoming = []
        for p in self._target_pages():
            tgt_pages = [
                link["target"] for link in self.graph_data["links"]
                if link["target"] == p
            ]
            top_incoming.append([p, len(tgt_pages)])
        # Sort and extract results
        top_incoming = np.array(top_incoming)
        sort_top_ic = top_incoming[np.argsort(top_incoming[:, 1])]
        filt_top_ic = sort_top_ic[::-1][:5]

        return filt_top_ic.tolist()

    def generate_stats(self):
        """Execute analyses and generate statistics"""
        return {
            "top_pages": self._top_pages(),
            "pages_found": self._pages_found(),
            "links_found": self._links_found(),
            "crawled_pages": self._crawled_pages(),
            "target_pages": self._target_pages(),
            "top_outgoing_pages": self.top_outgoing_pages(),
            "top_incoming_pages": self.top_incoming_pages(),
        }

    def generate_stats_sitemap(self):
        """Execute analyses and generate statistics"""
        return {
            "top_pages": self._top_pages_sitemap(),
            "pages_found": self._pages_found(),
            "links_found": self._links_found(),
            "crawled_pages": self._crawled_pages(),
            "target_pages": self._target_pages(),
            "top_outgoing_pages": self.top_outgoing_pages(),
            "top_incoming_pages": self.top_incoming_pages(),
        }

"""
analyzer.py

@author: ht-90
"""


import numpy as np


class Analyzer:
    """"""
    def __init__(self, url, graph, cat):
        self.url = url
        self.graph_data = graph
        self.category_data = cat

    def _top_pages(self):
        """Return top level page urls"""
        return [cat for cat in self.category_data if "/" not in cat["category_url"]]

    def _pages_found(self):
        """Number of pages identified"""
        return len(self.graph_data["nodes"])

    def _links_found(self):
        """Number of internal links identified"""
        return len(self.graph_data["links"])

    def _crawled_pages(self):
        """Crawled pages"""
        return np.unique([l["source"] for l in self.graph_data["links"]]).tolist()

    def _target_pages(self):
        """Target pages"""
        return np.unique([l["target"] for l in self.graph_data["links"]]).tolist()

    def top_outgoing_pages(self, pages=5):
        """Top 5 pages with outgoing links"""
        top_outgoing = []
        for p in self._crawled_pages():
            top_outgoing.append([p, len([l["source"] for l in self.graph_data["links"] if l["source"] == p])])
        top_outgoing = np.array(top_outgoing)
        return top_outgoing[np.argsort(top_outgoing[:, 1])][::-1][:pages].tolist()

    def top_incoming_pages(self):
        """Top 5 pages with incoming links"""
        top_incoming = []
        for p in self._target_pages():
            top_incoming.append([p, len([l["target"] for l in self.graph_data["links"] if l["target"] == p])])
        top_incoming = np.array(top_incoming)
        return top_incoming[np.argsort(top_incoming[:, 1])][::-1][:5].tolist()

    def generate_stats(self):
        """Execute analyses and generate statistics"""
        return {
            "top_pages": self._top_pages(),
            "pages_found": self._pages_found(),
            "links_found": self._links_found(),
            "crawled_pages": self._crawled_pages(),
            "target_pages": self._target_pages(),
            "top_outgoing_pages": self.top_outgoing_pages(),
            "top_incoming_pages": self.top_incoming_pages()
        }

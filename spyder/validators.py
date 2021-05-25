"""
validation.py

@author: ht-90
"""

import re


class SitemapURLValidator:
    address = str()
    regex = re.compile(
        r"^(?:http|ftp)s?://"  # http:// or https://
        r"(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|"  # domain...
        r"localhost|"  # localhost...
        r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"  # ...or ip
        r"(?::\d+)?"  # optional port
        r"(?:/?|[/?]\S+)$",
        re.IGNORECASE,
    )

    def __init__(self, address, verify_exists=False):
        self.address = address
        self.verify_exists = verify_exists

    def __call__(self):
        return re.match(self.regex, self.address) is not None

"""
validation.py

@author: ht-90
"""


import re
from urllib.parse import urlparse, urljoin


# Django URL validator
class URLValidator:
    url = str()
    regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

    def __init__(self, url, verify_exists=False):
        self.url = url
        self.verify_exists = verify_exists
    
    def __call__(self):
        return (re.match(self.regex, self.url) is not None)

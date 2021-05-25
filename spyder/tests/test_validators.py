from django.test import TestCase

from .. import validators


class TestValidator(TestCase):

    def test_URLValidator_with_https(self):
        test_url = "https://domain.com"
        is_url_valid = validators.SitemapURLValidator(address=test_url)
        self.assertTrue(is_url_valid())

    def test_URLValidator_with_http(self):
        test_url = "http://domain.com"
        is_url_valid = validators.SitemapURLValidator(address=test_url)
        self.assertTrue(is_url_valid())

    def test_URLValidator_without_scheme(self):
        test_url = "domain.com"
        is_url_valid = validators.SitemapURLValidator(address=test_url)
        self.assertFalse(is_url_valid())

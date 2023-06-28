import pytest
from data.demo.demo_data import DemoData
from pages.demo.demo_pages import DemoPages
from testcases.base_test import BaseTest
from utils.data_sets import Methods


class TestDemo(BaseTest):
    def setup_class(self):
        super().setup_class(self)
        self.page = DemoPages(self.web)
        self.data = DemoData()

    def test_01_get_access_token(self):
        """Define the case that belong to the module"""
        result = self.page.http_methods(Methods.post, self.data.url)

        self.page.assert_json_response(result, self.data.want_data, "$..headers..User-Agent")

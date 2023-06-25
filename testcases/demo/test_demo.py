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
        params = {"corpid": self.data.corpid, "corpsecret": self.data.corpsecret}
        result = self.page.http_methods(Methods.get, self.data.url, params=params)

        self.page.assert_status_code(result, self.data.e_status)
        self.page.assert_key_in_json(result, self.data.want_data)

from data.demo.demo_data import DemoData
from pages.demo.demo_pages import DemoPages
from testcases.base_test import BaseTest
from utils.data_sets import Methods


class TestDemo(BaseTest):
    def setup_class(self):
        super().setup_class(self)
        self.page = DemoPages(self.web)
        self.data = DemoData()

    def test_01(self):
        """Define the case that belong to the module"""
        params = {"status": "available"}

        result = self.page.http_methods(Methods.get, self.data.url, params=params)

        self.page.assert_json(result, self.data.want_data, "id", 9223372036854252693)

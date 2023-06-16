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
        params = {"params": "wangyun"}

        result = self.page.http_methods(Methods.post, "https://httpbin.ceshiren.com/post", json_params=params)
        self.page.assert_status_code(result, 200)

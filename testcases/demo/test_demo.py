import pytest

from data.demo.demo_data import DemoData
from pages.demo.demo_pages import DemoPages
from testcases.base_test import BaseTest
from utils.decorator import exception_capture


class TestDemo(BaseTest):
    def setup_class(self):
        super().setup_class(self)
        self.page = DemoPages(self.web)
        self.data = DemoData()

    @exception_capture
    @pytest.mark.parametrize()
    def test_01_get_list(self):
        self.page.navigate(self.data.url())

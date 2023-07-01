"""
企业微信的接口测试案例
接口文档: https://developer.work.weixin.qq.com/document/path/90664
建议终端执行, 执行命令: python -m pytest testcases/qi_weixin/test_qi_weixin.py -vs --suite=requests --web=None
"""

from data.qi_weixin.qi_weixin_data import QiWeixinData
from pages.qi_weixin.qi_weixin_pages import QiWeixinPages
from testcases.base_test import BaseTest


class TestQiWeixin(BaseTest):
    def setup_class(self):
        super().setup_class(self)
        self.page = QiWeixinPages(self.web)
        self.data = QiWeixinData()

    def test_01_create_department(self):
        # 创建部门
        self.page.create_department(self.data.department)

"""
霍格沃滋测试开发学社宠物商店的接口测试案例
接口文档: https://petstore.swagger.io/
建议终端执行, 执行命令: python -m pytest testcases/pet_store/test_pet_store.py -vs --suite=requests --web=None
"""

from data.pet_store.pet_store_data import PetStoreData
from pages.pet_store.pet_store_pages import PetStorePages
from testcases.base_test import BaseTest


class TestDemo(BaseTest):
    def setup_class(self):
        super().setup_class(self)
        self.page = PetStorePages(self.web)
        self.data = PetStoreData()

    def test_01_pet_hot(self):
        # 增加宠物 -> 查看新增宠物
        self.page.pet_add(self.data.pet)
        self.page.pet_find(self.data.pet)

        # 更改宠物信息 -> 查看更改后宠物信息
        self.page.pet_update(self.data.pet_update)
        self.page.pet_find(self.data.pet_update)

        # 删除宠物信息 -> 查看被删除的宠物信息
        self.page.pet_delete(self.data.pet_update)
        self.page.pet_find(self.data.pet_update, has_no=True)

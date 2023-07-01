import inspect
from data.qi_weixin import Department
from data.qi_weixin.qi_weixin_data import QiWeixinData
from pages.pet_store import BASE
from utils.data_sets import Methods


class QiWeixinPages(BASE):
    def __init__(self, driver):
        super().__init__(driver)
        self.data = QiWeixinData()

    def _get_access_token(self):
        r = self.http_methods(Methods.get, self.data.getttoken_url, params=self.data.getttoken_params)
        self.get_token(r, "$.access_token")

    def create_department(self, department: Department):
        self._get_access_token()
        r = self.http_methods(
            Methods.post, self.data.create_department_url, params={"access_token": self.token}, json_params=department
        )

        self.assert_status_code(r)
        self.assert_json_response(r, want=department.id, expr="$.id")

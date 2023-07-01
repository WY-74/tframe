import os
from dataclasses import dataclass, field
from typing import Dict
from data.qi_weixin import Token, Department


@dataclass
class QiWeixinData:
    base_url = "https://qyapi.weixin.qq.com/cgi-bin"
    getttoken_url = f"{base_url}/gettoken"
    create_department_url = f"{base_url}/department/create"

    getttoken_params = Token().__dict__
    department = Department(name="230701_3", id=7)

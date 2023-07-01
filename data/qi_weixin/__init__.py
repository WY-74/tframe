import os
from dataclasses import dataclass


@dataclass
class Token:
    corpid: str = os.getenv("corpid")
    corpsecret: str = os.getenv("corpsecret")


@dataclass
class Department:
    name: str = ""
    parentid: int = 1
    order: int = 1
    id: int = 1

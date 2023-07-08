from dataclasses import dataclass


@dataclass
class Methods:
    get: str = "get"
    post: str = "post"
    put: str = "put"
    delete: str = "delete"


@dataclass
class TimeOut:
    fast: int = 3
    normal: int = 10


@dataclass
class AssertMethods:
    complete_match = "complete_match"
    include = "include"
    non_match = "non_match"
    non_include = "non_include"

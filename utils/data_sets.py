from dataclasses import dataclass


@dataclass
class Methods:
    get: str = "get"
    post: str = "post"
    put: str = "put"
    delete: str = "delete"

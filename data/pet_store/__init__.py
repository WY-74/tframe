from dataclasses import dataclass, field
from typing import List, Dict


@dataclass
class Category:
    id: int = 0
    name: str = "string"


@dataclass
class Tags:
    id: int = 0
    name: str = "string"


@dataclass
class Status:
    avaliable: str = "avaliable"
    pending: str = "pending"
    sold: str = "sold"


@dataclass
class Pet:
    id: int = 0
    category: Category = field(default_factory=lambda: Category().__dict__)
    name: str = "string"
    photoUrls: List[str] = field(default_factory=lambda: ["string"])
    tags: List[Tags] = field(default_factory=lambda: [Tags().__dict__])
    status: Status = Status.avaliable

from dataclasses import dataclass


@dataclass
class DemoData:
    url: str = "https://petstore.swagger.io/v2/pet/findByStatus"
    want_data = {
        "id": 9223372036854252693,
        "category": {"id": 0, "name": "string"},
        "name": "fish",
        "photoUrls": ["string"],
        "tags": [{"id": 0, "name": "string"}],
        "status": "available",
    }

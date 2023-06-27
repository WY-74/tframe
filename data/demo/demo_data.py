from dataclasses import dataclass


@dataclass
class DemoData:
    url: str = "https://www.nasa.gov/rss/dyn/lg_image_of_the_day.rss"
    e_status: str = 200
    corpid: str = "wwb316419364456d42"
    corpsecret: str = "72H_JVRwStrmaK-3aG-fRblVMS1OC-q_yrlQovUXWhQ"
    want_data = "dasdsd"
    # want_data = {
    #     "id": 9223372036854252693,
    #     "category": {"id": 0, "name": "string"},
    #     "name": "fish",
    #     "photoUrls": ["string"],
    #     "tags": [{"id": 0, "name": "string"}],
    #     "status": "available",
    # }

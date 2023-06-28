from dataclasses import dataclass


@dataclass
class DemoData:
    url: str = "https://httpbin.ceshiren.com/post"
    e_status: str = 200
    corpid: str = "wwb316419364456d42"
    corpsecret: str = "72H_JVRwStrmaK-3aG-fRblVMS1OC-q_yrlQovUXWhQ"
    want_data = "python-requests/2.31.0"

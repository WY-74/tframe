import os
from dataclasses import dataclass

@ dataclass
class ENV:
    CHROME_DEBUG: int = os.getenv("CHROME_DEBUG")
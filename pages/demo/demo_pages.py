import time
import importlib
from typing import Dict

from conftest import ENV
from pages.base_pages import SeleniumBasePages, PlaywrightBasePage


Base = SeleniumBasePages if ENV["suite"] == "selenium" else PlaywrightBasePage


class DemoPages(Base):
    def navigate(self, url: str):
        self.open(url)

    def get_list(self, actions: list):
        self.action_flow(actions)

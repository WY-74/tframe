from conftest import ENV
from pages import base_pages

BASE = getattr(base_pages, f"{ENV['suite'].title()}BasePages")


class DemoPages(BASE):
    """Define the actions that belong to the module"""

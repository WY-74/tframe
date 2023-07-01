from conftest import ENV
from pages import base_pages


if ENV["suite"] == "requests":
    BASE = base_pages.RequestsBase
else:
    BASE = getattr(base_pages, f"{ENV['suite'].title()}BasePages")

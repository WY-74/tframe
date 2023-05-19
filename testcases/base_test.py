from conftest import ENV
from utils.instantiate_driver import instantiate_driver


class BaseTest:
    def setup_class(self):
        self.web = instantiate_driver()

    def teardown_class(self):
        self.web.quit() if ENV["suite"] == "selenium" else self.web.close()

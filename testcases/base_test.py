from utils.instantiate_driver import instantiate_driver


class BaseTest:
    def setup_class(self):
        self.driver = instantiate_driver()

    def teardown_class(self):
        self.driver.quit()

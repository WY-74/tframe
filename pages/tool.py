from typing import Dict
from selenium.webdriver.common.by import By


class Tool:
    def __init__(self, driver):
        self.driver = driver
        self.split_symbol = "@"

    def open(self, url: str):
        self.driver.get(url)

    def _refresh(self):
        self.driver.refresh()

    def _back(self):
        self.driver.back()

    def _click(self, locator: str):
        self.driver.find_element(By.CSS_SELECTOR, locator).click()

    def action_flow(self, actions: Dict[str, str]):
        for action in actions:
            if "input" in action:
                locator, text = actions[action].split(self.split_symbol)
                self.driver.find_element(By.CSS_SELECTOR, locator).send_keys(text)
            if "click" in action:
                self.driver.find_element(By.CSS_SELECTOR, actions[action]).click()

    def get_attributes(self, data: str):
        locator, attr = data.split(self.split_symbol)
        elements = self.driver.find_elements(By.CSS_SELECTOR, locator)
        if attr == "text":
            return [e.text for e in elements]
        else:
            return [e.get_attribute(attr) for e in elements]

    # def get_all_attributes(self, locators: List[Tuple[str, str]] | str) -> List:
    #     attr_list = []
    #     for locator in locators:
    #         element = self.driver.find_element(By.CSS_SELECTOR, locator[0])
    #         if (attr := locator[1]) == "text":
    #             attr_list.append(element.text)
    #         else:
    #             attr_list.append(element.get_attribute(attr))
    #     return attr_list

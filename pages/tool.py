from typing import Dict
from dataclasses import dataclass
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains, Keys

@dataclass
class TimeOut:
    normal: int = 10


class Tool:
    def __init__(self, driver):
        self.driver = driver
        self.split_symbol = "@"
    
    def _click_and_confirm(self, click_locator: str, target_locator):
        def _inner(driver):
            self.driver.find_element(By.CSS_SELECTOR, click_locator).click()
            return self.driver.find_element(By.CSS_SELECTOR, target_locator)
        return _inner
    
    def cilck_until(self, locators: tuple[str, str], time_out:int = TimeOut.normal):
        elem = WebDriverWait(self.driver, time_out).until(self._click_and_confirm(*locators), message="并未通过点击找到期望元素")
        return elem

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
        
    def keyboard_enter(self, actions: Dict[str, str]):
        self.action_flow(actions=actions)
        ActionChains(self.driver).key_down(Keys.ENTER).perform()

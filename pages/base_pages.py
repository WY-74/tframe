from typing import Dict, List, Union
from dataclasses import dataclass

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains, Keys


@dataclass
class TimeOut:
    normal: int = 10


class BasePages:
    def __init__(self, driver):
        self.driver = driver
        self.split_symbol = "@"

    def _click_and_confirm(self, button_locator: str, target_locator: str):
        def _click(driver):
            driver.find_element(By.CSS_SELECTOR, button_locator).click()
            return self.driver.find_element(By.CSS_SELECTOR, target_locator)

        return _click

    def _get_element(self, locator: str):
        def _get(driver):
            return driver.find_element(By.CSS_SELECTOR, locator)

        return _get

    def _status_hack(self, *args) -> WebElement | List[WebElement]:
        arg = args[0]
        if isinstance(arg, str):
            self.must_get_element(arg)
            return self.driver.find_elements(By.CSS_SELECTOR, arg)
        elif isinstance(arg, WebElement):
            return [arg]
        elif isinstance(arg, list):
            return arg
        else:
            raise Exception("[Err]: missing valid locator or elements")

    def open(self, url: str):
        self.driver.get(url)

    def must_get_element(self, locator: str, time_out: int = TimeOut.normal) -> WebElement:
        return WebDriverWait(self.driver, timeout=time_out).until(
            self._get_element(locator), message=f"[Err]: expected element not found: {locator}"
        )

    def must_after_cilck(self, button_locator: str, target_locator: str, time_out: int = TimeOut.normal) -> WebElement:
        return WebDriverWait(self.driver, time_out).until(
            self._click_and_confirm(button_locator, target_locator),
            message=f"[Err]: the button or expected element is not found: {target_locator}",
        )

    def click_element(self, web: str | WebElement) -> None:
        element = self._status_hack(web)[0]
        element.click()

    def get_element_by_text(self, locator: str, text: str) -> WebElement:
        elements = self._status_hack(locator)
        attrs = self.get_attributes("text", elements)

        for i, attr in enumerate(attrs):
            if attr == text:
                return elements[i]

    def get_attributes(self, attr: str, web: str | List[WebElement]) -> List[str]:
        elements = self._status_hack(web)
        attr_list = [e.text for e in elements] if attr == "text" else [e.get_attribute(attr) for e in elements]

        return attr_list

    def select_dropdown(self, box_locator: str, menu_locator: str, item: str) -> None:
        drop_items_locator = "a"

        self.click_element(box_locator)
        self.must_get_element(menu_locator)
        self.click_element(self.get_element_by_text(locator=f"{menu_locator} {drop_items_locator}", text=item))

    def action_flow(self, actions: Dict[str, str]):
        for do in actions:
            action = do.split("_")[-1]
            if action == "input":
                locator, text = actions[do].split(self.split_symbol)
                element = self.must_get_element(locator)
                element.send_keys(text)
            elif action == "click":
                self.click_element(actions[do])
            elif action == "dropdown":
                box, menu, item = actions[do].split(self.split_symbol)
                self.select_dropdown(box, menu, item)

    def keyboard_enter(self, actions: Dict[str, str]) -> None:
        self.action_flow(actions=actions)
        ActionChains(self.driver).key_down(Keys.ENTER).perform()

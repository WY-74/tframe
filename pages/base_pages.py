import requests
from requests import Response
from typing import Dict, List
from dataclasses import dataclass
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains, Keys

from utils import data_sets
from utils.decorator import avoid_popups


@dataclass
class TimeOut:
    normal: int = 10


class SeleniumBasePages:
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

    def _scroll_to_element(self, element: WebElement):
        element_location = element.location['y'] - 130
        element_location = 0 if element_location < 0 else element_location
        self.driver.execute_script(f"window.scrollTo(0, {str(element_location)})")

    def _status_hack(
        self, eol: str | WebElement | List[WebElement], index: int = None
    ) -> WebElement | List[WebElement]:
        if isinstance(eol, str):
            self.must_get_element(eol)
            elements = self.driver.find_elements(By.CSS_SELECTOR, eol)
            if index != None:
                element = elements[index]
                self._scroll_to_element(element)
                return element
            return elements
        elif isinstance(eol, WebElement):
            self._scroll_to_element(eol)
            return eol
        elif isinstance(eol, list):
            return eol
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

    @avoid_popups
    def scroll_and_click(self, eol: str | WebElement) -> None:
        element = self._status_hack(eol, 0)
        element.click()

    def get_element_by_text(self, locator: str, text: str) -> WebElement:
        elements = self._status_hack(locator)
        attrs = self.get_attributes("text", elements)

        for i, attr in enumerate(attrs):
            if attr == text:
                return elements[i]

    def get_element_by_childtext(
        self, locator: str, child_locator: str, text: str, complete: bool = True
    ) -> WebElement | None:
        roots = self._status_hack(locator)
        for root in roots:
            _text = root.find_element(By.CSS_SELECTOR, child_locator).text
            if compile and _text == text:
                return root
            if not compile and text in _text:
                return root
        return None

    def get_attributes(self, attr: str, eol: str | List[WebElement]) -> List[str]:
        elements = self._status_hack(eol)
        attr_list = [e.text for e in elements] if attr == "text" else [e.get_attribute(attr) for e in elements]

        return attr_list

    def select_dropdown(self, box_locator: str, menu_locator: str, item: str) -> None:
        drop_items_locator = "a"

        self.scroll_and_click(box_locator)
        self.must_get_element(menu_locator)
        self.scroll_and_click(self.get_element_by_text(locator=f"{menu_locator} {drop_items_locator}", text=item))

    def action_flow(self, actions: Dict[str, str]):
        for do in actions:
            action = do.split("_")[-1]
            if action == "input":
                locator, text = actions[do].split(self.split_symbol)
                element = self.must_get_element(locator)
                element.send_keys(text)
            elif action == "click":
                self.scroll_and_click(actions[do])
            elif action == "dropdown":
                box, menu, item = actions[do].split(self.split_symbol)
                self.select_dropdown(box, menu, item)

    def keyboard_enter(self, actions: Dict[str, str]) -> None:
        self.action_flow(actions=actions)
        ActionChains(self.driver).key_down(Keys.ENTER).perform()


class PlaywrightBasePages:
    def __init__(self, playwright):
        self.playwright = playwright
        self.split_symbol = "@"

    def open(self, url: str):
        self.playwright.goto(url)


class AppiumBasePages:
    def __init__(self, driver):
        self.driver = driver
        self.split_symbol = "@"


class RequestsBase:
    def __init__(self, driver: None):
        self.methods = data_sets.Methods()

    def http_methods(
        self,
        method: data_sets.Methods(),
        url: str,
        params: Dict[str, str | int] | None = None,
        headers: Dict[str, str | int] | None = None,
        json_params: Dict[str, str | int] | None = None,
    ) -> Response:
        return requests.request(method, url, params=params, headers=headers, json=json_params)

    def assert_status_code(self, response: Response, e_status: int):
        assert response.status_code == e_status

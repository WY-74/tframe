import requests
import jsonpath
from requests import Response
from xml.etree import ElementTree
from typing import Dict, List, Any
from dataclasses import dataclass
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains, Keys
from utils.data_sets import TimeOut, Methods, AssertMethods
from utils.decorator import avoid_popups
from utils.jsonschema_util.jsonschema_util import JsonSchemaUtil
from utils.db_util.mysql_util import MySqlUtil
from utils.assert_util.assert_util import AssertUtil
from conftest import LOGGER


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
        self.token = ""
        self.cookies = {}

    def _get_items_by_jsonpath(self, obj, expr: str) -> list | bool:
        return jsonpath.jsonpath(obj, expr)

    def http_methods(
        self,
        method: Methods,
        url: str,
        params: Dict[str, str | int] | None = None,
        headers: Dict[str, str | int] | None = None,
        json_params: Any = None,
        data_params: Dict[str, str | int] | None = None,
        cookies: Dict[str, str | int] | None = None,
        timeout: TimeOut = TimeOut.fast,
    ) -> Response:
        # Most of the time our data structures are not passed in as dict
        # So we need to do a data type conversion
        if json_params and not isinstance(json_params, dict):
            json_params = json_params.__dict__

        return requests.request(
            method,
            url,
            params=params,
            headers=headers,
            json=json_params,
            data=data_params,
            cookies=cookies,
            timeout=timeout,
        )

    def http_with_proxy(
        self, method: Methods, url: str, http: str = "127.0.0.1:8888", https: str | None = None, **kwargs
    ) -> Response:
        https = http if https == None else https
        proxies = {"http": f"http://{http}", "https": f"http://{https}"}
        LOGGER.info(f"Proxy port information: {proxies}")
        return requests.request(method, url, proxies=proxies, verify=False, **kwargs)

    def http_with_file(self, url: str, path: str, name: str = "name by tframe", filename: str = ""):
        files = {name: open(path, "rb")} if not filename else {name: (filename, open(path, "rb"))}
        return requests.request(Methods.post, url, files=files)

    def assert_status_code(self, response: Response, e_status: int = 200):
        status = response.status_code
        LOGGER.info(f"status: {e_status}")
        AssertUtil.assert_with_log(status, e_status)

    def assert_json_response(
        self, response: Response, want: Any, expr: str = "$", overall: bool = False, has_no: bool = False
    ):
        root = response.json()
        LOGGER.info(root)

        if overall:
            try:
                # Most of the time our data structures are not passed in as dict
                # So we need to do a data type conversion
                want = want.__dict__
                assert want == root
            except Exception:
                LOGGER.warning(f"{want} != {root}")
            return

        items = self._get_items_by_jsonpath(root, expr)
        if not items:
            LOGGER.warning("JsonPath did not match the content")

        LOGGER.info(f"get items after jsonpath: {items}")
        if has_no:
            try:
                assert want not in items
            except Exception:
                LOGGER.warning(f"{want} still present in {items}")
            return

        try:
            assert want in items
        except Exception:
            LOGGER.warning(f"{want} not in {items}")

    def assert_xml_response(self, response: Response, xpath: str, want: str):
        root = ElementTree.fromstring(response.text)
        items = root.findall(f".{xpath}")
        items = [item.text for item in items]
        try:
            assert want in items
        except Exception:
            LOGGER.warning(f"The expected value '{want}' is not in {items}")

    def assert_by_jsonschema(self, response: Response, generate: bool = True, file_path: str | None = None):
        response = response.json()
        if generate:
            schema = JsonSchemaUtil.generate_jsonschema(response, file_path)
        assert JsonSchemaUtil.validate_jsonschema(response, schema, file_path)

    def assert_from_db(self, sql: str, want: str = None, complete_match: bool = False):
        if complete_match and want == None:
            LOGGER.warning("[assert_from_db]: We need to pass in the 'want' or change the 'assert_mothod' to False!")

        result = MySqlUtil.execute_sql(sql)
        AssertUtil.assert_with_log(want, result) if complete_match else AssertUtil.assert_with_log(
            None, result, AssertMethods.non_match
        )

    def get_token(self, response: Response, expr: str):
        root = response.json()
        items = self._get_items_by_jsonpath(root, expr)
        if not items:
            LOGGER.warning("Get token JsonPath did not match the content")

        self.token = items[0]
        LOGGER.info(f"tonken: {self.token}")

    def get_cookies(self, response: Response):
        cookies = response.cookies
        for cookie in cookies:
            self.cookies[cookie.name] = cookie.value
        LOGGER.info(f"cookies: {self.token}")

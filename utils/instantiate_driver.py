from selenium import webdriver as sw
from selenium.webdriver.remote.webdriver import WebDriver
from playwright.sync_api import sync_playwright
from appium import webdriver as aw

from conftest import ENV
from utils.capabilities import SELENIUM_CAPS, APPIUM_ANDROID_CAPS, APPIUM_IOS_CAPS


def instantiate_driver():
    if ENV["suite"] == "selenium":
        web = instantiate_selenium()
    elif ENV["suite"] == "playwright":
        web = instantiate_playwright()
    elif ENV["suite"] == "appium":
        web = instantiate_appium()
    else:
        raise Exception("[Err]: Please set up 'selenium', 'playwriht' or 'appium' via --suite")

    return web


def instantiate_selenium() -> WebDriver:
    _web = ENV["web"]
    if _web != "Chrome" and _web != "Firefox":
        raise Exception("[Err]: In selenium environment, please set up 'Chrome' or 'Firefox' via --web")
    headless = bool(ENV["headless"])
    if not ENV["remote"]:
        options = getattr(sw, f"{_web}Options")()
        options.page_load_strategy = 'eager'
        if headless:
            options.add_argument('--headless')
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')
        if ENV["debugger"]:
            options.debugger_address = "localhost:9000"
        web = getattr(sw, _web)(options=options)
        web.maximize_window()
        web.implicitly_wait(3)
        return web
    hogwarts_grid_url = "https://selenium-node.hogwarts.ceshiren.com/wd/hub"  # 这是一个暂时的节点终端

    return sw.Remote(command_executor=hogwarts_grid_url, desired_capabilities=SELENIUM_CAPS)


def instantiate_playwright():
    if ENV["web"] != "Chrome":
        raise Exception("[Err]: In playwright environment, please set up 'Chrome' via --web")
    headless = bool(ENV["headless"])

    return sync_playwright().start().chromium.launch(headless=headless).new_page()


def instantiate_appium():
    _web = ENV["web"]
    if _web != "Android" and _web != "Ios":
        raise Exception("[Err]: In appium environment, please set up 'Android' or 'Ios' via --web")
    _caps = APPIUM_ANDROID_CAPS if _web == "Android" else APPIUM_IOS_CAPS

    return aw.Remote("http://localhost:4723/wd/hub", _caps)
